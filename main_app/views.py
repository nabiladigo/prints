from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View 
from .models import Print, Card, Mug, Photo, Puzzle




class Home(TemplateView):
    template_name = "home.html"

    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     context["giftsets"] = GiftSet.objects.all()
    #     return context

class About(TemplateView):
    template_name = "about.html"

class PrintList(TemplateView):
    template_name = "print_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["prints"] = Print.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["prints"] = Print.objects.all()
            context["header"] = "Trending Prints"
        return context

class PrintCreate(CreateView):
    model = Print
    fields = ['name', 'image', 'price']
    template_name = "print_create.html"

    def get_success_url(self):
        return reverse('print_detail', kwargs={'pk': self.object.pk})

class PrintDetail(DetailView):
    model = Print
    template_name = "print_detail.html"

class PrintUpdate(UpdateView):
    model = Print
    fields = ['name', 'image', 'price', 'verified_print']
    template_name = "print_update.html"

    def get_success_url(self):
        return reverse('print_detail', kwargs={'pk': self.object.pk})

class PrintDelete(DeleteView):
    model = Print
    template_name = "print_delete_confirmation.html"
    success_url = "/prints/"


class CardCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        price = request.POST.get("price")
        print = Print.objects.get(pk=pk)
        Card.objects.create(name=name, image=image, price = price , print=print)
        return redirect('print_detail', pk=pk)

class MugCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        price = request.POST.get("price")
        print = Print.objects.get(pk=pk)
        Mug.objects.create(name=name, image=image, price = price , print=print)
        return redirect('print_detail', pk=pk)

class PhotoCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        price = request.POST.get("price")
        print = Print.objects.get(pk=pk)
        Photo.objects.create(name=name, image=image, price = price , print=print)
        return redirect('print_detail', pk=pk)

class PuzzleCreate(View):
    
    def post(self, request, pk):
        name = request.POST.get("name")
        image = request.POST.get("image")
        price = request.POST.get("price")
        print = Print.objects.get(pk=pk)
        Puzzle.objects.create(name=name, image=image, price = price , print=print)
        return redirect('print_detail', pk=pk)