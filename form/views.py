from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm

class HelloView(View):
    def get(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        return render(request, 'index.html' , context={})

class showFormView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'form.html' ,context={})


def personalformRender(request):
    form = MyForm()
    first_name = request.POST.get("first_name","-")
    last_name = request.POST.get("last_name","-")
    gender = request.POST.get("gender","-")
    date_of_birth = request.POST.get("date_of_birth","-")
    title = "-"
    if gender=='M':
        title = "Mr."
    elif gender=="F":
        title = "Mrs."
    table =  {
                'title':title,
                'first_name':first_name,
                'last_name':last_name,
                'date_of_birth':date_of_birth
            }
    return render(request, 'form.html', {'form':form, 'table':table});
