from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Models,Cars

def main(request: WSGIRequest):
    cars = Cars.objects.all()
    models = Models.objects.all()
    context ={
        'cars':cars,
        'models':models}

    return render(request,'index.html',context=context)

def cars_by_models (request :WSGIRequest,model_id):
    models = Models.objects.all()
    car = Cars.objects.filter(model_id=model_id)
    context ={
        "model":models,
        'cars':car
    }
    return render(request,'index.html',context)


def car_detail(request :WSGIRequest,pk):
    cars = Cars.objects.get(pk=pk)
    models = Models
    context = {
        "car":cars,
        "model":models
    }
    return render(request,'Detail.html',context)


def carmodels(request: WSGIRequest):
    models = Models.objects.all()
    context = {
        'models':models
    }
    return render(request,'models.html',context=context)

def cars(request:WSGIRequest):
    cars = Cars.objects.all()
    context = {
        'cars':cars
    }
    return render(request,'cars.html',context=context)