from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Car


class CarListView(ListView):
    template_name = "cars/car_list.html"
    model = Car


class CarDetailView(DetailView):
    template_name = "cars/car_detail.html"
    model = Car


class CarCreateView(CreateView):
    template_name = "cars/car_create.html"
    model = Car
    fields = ['name', 'desc', 'purchaser']


class CarUpdateView(UpdateView):
    template_name = "cars/car_update.html"
    model = Car
    fields = ['name', 'desc', 'purchaser']


class CarDeleteView(DeleteView):
    template_name = "cars/car_delete.html"
    model = Car
    success_url = reverse_lazy("car_list")