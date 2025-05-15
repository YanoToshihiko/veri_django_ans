from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class CreateEmployeeView(LoginRequiredMixin, CreateView):
    template_name = "employeelist/create.html"
    model = Employee
    fields = ["no", "name", "salary"]
    success_url = reverse_lazy("list-employee")


class ListEmployeeView(LoginRequiredMixin, ListView):
    template_name = "employeelist/list.html"
    model = Employee
    paginate_by = 3


class DetailEmployeeView(LoginRequiredMixin, DetailView):
    template_name = "employeelist/detail.html"
    model = Employee


class UpdateEmployeeView(LoginRequiredMixin, UpdateView):
    template_name = "employeelist/edit.html"
    model = Employee
    fields = ["no", "name", "salary"]
    success_url = reverse_lazy("list-employee")


class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    template_name = "employeelist/delete_confirm.html"
    model = Employee
    success_url = reverse_lazy("list-employee")


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
    else:
        form = ContactForm()
    return render(request, 'employeelist/contact.html', {'form': form}) 
