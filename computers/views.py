from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Computer, OS, Producer


# Create your views here.
class ComputerList(LoginRequiredMixin, ListView):
    model = Computer


class ComputerCreate(CreateView):
    model = Computer
    model2 = OS
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('computers_app:computer_list')


class ComputerUpdate(UpdateView):
    model = Computer
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('computers_app:computer_list')


class ComputerDelete(DeleteView):
    model = Computer
    success_url = reverse_lazy('computers_app:computer_list')
