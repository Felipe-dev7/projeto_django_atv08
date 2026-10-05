from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
  myusers = User.objects.all().values()
  template = loader.get_template('all_users.html')
  context = {
    'myusers': myusers
  }

  return HttpResponse(template.render(context, request))



def details(request, id):
  myusers = User.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myusers': myusers
  }

  return HttpResponse(template.render(context, request))



def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())






def teste(request):
  template = loader.get_template('template.html')
  context = {
    'carros': ['Uno', 'Uno com escada', 'Uno sem placa']
  }

  return HttpResponse(template.render(context, request))

