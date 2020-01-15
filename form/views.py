from django.shortcuts import render
from django.views.generic import View

class HelloView(View):
    def get(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        return render(request, 'index.html' , context={})

class showFormView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'form.html' ,context={})
