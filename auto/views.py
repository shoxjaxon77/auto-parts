from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from .models import Kategoriyalar,Brands,ExtiyotQismlar, Transportlar,Xaridlar
from .forms import ExtiyotQismForm,XaridlarForm,TransportlarForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .utils import Excel

class AdminCheck(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class HomeView(View):
    def get(self,request):
        kategoriyalar = Kategoriyalar.objects.all().order_by('nomi')
        brand = Brands.objects.all()
        extiyotqismlar = ExtiyotQismlar.objects.all()
        cars = Transportlar.objects.all().order_by('nomi')
        return render(request,'home.html',{'cars':cars,'brands':brand,'extiyotqismlar':extiyotqismlar})


class MahsulotView(View):
    def get(self, request):
        
        cars = Transportlar.objects.all().order_by('-id')
        kategoriya = Kategoriyalar.objects.all()

        # search_query = request.GET.get('q', '')
        # if search_query:
        #     extiyotqismlar = ExtiyotQismlar.objects.filter(nomi__icontains=search_query)
        #     extiyotqismlar = ExtiyotQismlar.objects.filter(nomi__contains=search_query)

        return render(request, 'mahsulotlar.html', {'cars': cars, 'kategoriya': kategoriya})



class CarDetailView(View):
    def get(self, request, id):
        car = get_object_or_404(Transportlar, id=id)
        extiyot_qism = ExtiyotQismlar.objects.filter(avto_id=id)
        kategoriya = Kategoriyalar.objects.all()
        categorized_spares = {}
        for cat in kategoriya:
            categorized_spares[cat.nomi] = extiyot_qism.filter(kategoriya_id=cat)
        return render(request, 'car_detail.html', {
            "car": car,
            "categorized_spares": categorized_spares,
            'kategoriya': kategoriya
        })
    
    
class AvtoQushishView(AdminCheck,View):
    def get(self,request):
        form = TransportlarForm()
        cars = Transportlar.objects.all()
        return render(request,'addcar.html',{'form':form,'cars':cars})
    
    def post(self,request):
        form = TransportlarForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mahsulot')
        else:
            return render(request,'addcar.html',{'form':form})





class AvtoEditView(AdminCheck,View):
        def get(self,request,id):
            car = Transportlar.objects.get(id=id)
            form = TransportlarForm(instance=car)
            return render(request, "editcar.html", {"form":form})

        def post(self,request,id):
            car = Transportlar.objects.get(id=id)
            form = TransportlarForm(data=request.POST,instance=car,files=request.FILES)

            if form.is_valid(): 
                form.save()
                return redirect("mahsulot")
            return render(request, "editcar.html", {"form":form})



class AvtoDeleteView(AdminCheck,View):
    def get(self, request, id):
        car = Transportlar.objects.get(id=id)
        car.delete()
        return redirect("mahsulot")



class ExtiyotQismQushishView(AdminCheck, View):
    def get(self, request):
        form = ExtiyotQismForm()
        extiyotqismlar = ExtiyotQismlar.objects.all()
        return render(request, 'ExtiyotQismQushish.html', {'form': form, 'extiyotqismlar': extiyotqismlar})
    
    def post(self, request):
        form = ExtiyotQismForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            extiyotqism = form.save()
            return redirect(reverse("car-detail", kwargs={'id': extiyotqism.avto.id}))
        else:
            extiyotqismlar = ExtiyotQismlar.objects.all()
            return render(request, 'ExtiyotQismQushish.html', {'form': form, 'extiyotqismlar': extiyotqismlar})

        

class DownloadToExcel(View):
    def get(self, request):
        data = ExtiyotQismlar.objects.all() 
        excel = Excel()

        for item in data:
            excel.add(item.id, item.nomi, item.narxi, item.malumot, item.miqdori, item.keltirilgan_sana, item.kategoriya_id, item.picture)

        file_path = excel.save()

        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="mahsulotlar.xlsx"'

        return response

# class XaridQushishView(AdminCheck,View):
#     def get(self,request):
#             form = XaridlarForm()
#             xarid = Xaridlar.objects.all()
#             return render(request,'xaridlar.html',{'form':form,'xaridlar':xarid})
    
#     def post(self,request):
#         form = XaridlarForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('addxarid')
#         else:
#             return render(request,'xaridlar.html',{'form':form})



        
# class CategoryNameView(View):
#     def get(self, request, id):
#         extiyotqismlar = ExtiyotQismlar.objects.filter(kategoriya_id=id).order_by('nomi')
#         kategoriya = Kategoriyalar.objects.all()

#         search_query = request.GET.get('q', '')
#         if search_query:
#             extiyotqismlar = ExtiyotQismlar.objects.filter(nomi__icontains=search_query)
            
#         return render(request, 'mahsulotlar.html', {'extiyotqismlar': extiyotqismlar, 'kategoriya': kategoriya,'poisk':search_query})
    


class QismEditView(AdminCheck,View):
        def get(self,request,id):
            extiyotqism = ExtiyotQismlar.objects.get(id=id)
            form = ExtiyotQismForm(instance=extiyotqism)
            return render(request, "QismEdit.html", {"form":form})

        def post(self,request,id):
            extiyotqism = ExtiyotQismlar.objects.get(id=id)
            form = ExtiyotQismForm(data=request.POST,instance=extiyotqism,files=request.FILES)

            if form.is_valid(): 
                form.save()
                return redirect(reverse("car-detail",kwargs={'id':extiyotqism.avto.id}))
            return render(request, "QismEdit.html", {"form":form})
    
class QismDeleteView(View):
    def get(self, request, id):
        # Correctly capture the 'id' parameter
        extiyotqism = get_object_or_404(ExtiyotQismlar, id=id)
        extiyotqism.delete()
        return redirect(reverse("car-detail",kwargs={'id':extiyotqism.avto.id}))
    
    


    





