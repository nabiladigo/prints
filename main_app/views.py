from django.shortcuts import redirect, render
from django.views import View 
from django.views.generic.base import TemplateView
from .models import Print, Card, Mug, Photo, Puzzle,  GiftSet
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["giftsets"] = GiftSet.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"


@method_decorator(login_required, name='dispatch')

class PrintList(TemplateView):
    template_name = "print_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["prints"] = Print.objects.filter(user=self.request.user, name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["prints"] = Print.objects.filter(user=self.request.user)
            context["header"] = "The Perfect Gift for Loved One."
        return context


    

class PrintCreate(CreateView):
    model = Print
    fields = ['name', 'image', 'price']
    template_name = "print_create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PrintCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('print_detail', kwargs={'pk': self.object.pk})


class PrintDetail(DetailView):
    model = Print
    template_name = "print_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["giftset"] = GiftSet.objects.all()
        return context

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

class GiftSetCardAssoc(View):
    def get(self, request, pk, card_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            GiftSet.objects.get(pk=pk).cards.remove(card_pk)
        if assoc == "add":
            GiftSet.objects.get(pk=pk).cards.add(card_pk)
        return redirect('home')

class GiftSetMugAssoc(View):
    def get(self, request, pk, card_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            GiftSet.objects.get(pk=pk).cards.remove(card_pk)
        if assoc == "add":
            GiftSet.objects.get(pk=pk).cards.add(card_pk)
        return redirect('home')

class GiftSetPhotoAssoc(View):
    def get(self, request, pk, card_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            GiftSet.objects.get(pk=pk).cards.remove(card_pk)
        if assoc == "add":
            GiftSet.objects.get(pk=pk).cards.add(card_pk)
        return redirect('home')

class GiftSetPuzzleAssoc(View):
    def get(self, request, pk, card_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            GiftSet.objects.get(pk=pk).cards.remove(card_pk)
        if assoc == "add":
            GiftSet.objects.get(pk=pk).cards.add(card_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect("print_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)




# class GiftSet(DetailView):
#     model = GiftSet
#     template_name = "giftset_detail.html"        