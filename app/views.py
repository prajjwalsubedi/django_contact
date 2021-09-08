from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView, DetailView, edit
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
# def home(request):
#     context = {
#     'contacts': models.Contact.objects.all()
#     }
#     return render(request,'index.html', context)

# def detail(request, id):
#     context = {
#     'contact': get_object_or_404(models.Contact,pk=id)
#     }
#     return render(request,'detail.html', context)

class HomePageView(LoginRequiredMixin, ListView):
    model = models.Contact
    template_name = "index.html"
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager=self.request.user)

class ContactDetailView(LoginRequiredMixin, DetailView):
    model = models.Contact
    template_name = "detail.html"
    context_object_name = 'contact'

@login_required()
def Search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = models.Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(phone__iexact=search_term) |
            Q(info__icontains=search_term)


            )
        context = {
            'search_term' : search_term,
            'contacts' : search_results.filter(manager=request.user)
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')

class ContactCreateView(LoginRequiredMixin, edit.CreateView):
    template_name = 'create.html'
    model = models.Contact
    fields = ['name', 'gender', 'email', 'info', 'phone','image']
    success_url = '/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        messages.success(self.request, "Your contact has been successfully created!")
        return redirect('home')
    
class ContactUpdateView(LoginRequiredMixin, edit.UpdateView):
    template_name = 'update.html'
    model = models.Contact
    fields = ['name', 'gender', 'email', 'info', 'phone','image']
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Your contact has been successfully Updated!")
        return redirect('detail', instance.pk)

class ContactDeleteView(LoginRequiredMixin, edit.DeleteView):
    template_name = 'delete.html'
    model = models.Contact
    fields = ['name', 'gender', 'email', 'info', 'phone','image']
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your contact has been successfully Deleted!")
        return super().delete(self, request, *args, **kwargs)
    


#user creation
class SignUpView(edit.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('home')


