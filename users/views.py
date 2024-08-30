from django.shortcuts import render,redirect,get_object_or_404
from .models import User
from .forms import UserForm
# Create your views here.
from django.template import loader
from django.http import HttpResponse,HttpResponseBadRequest

def user_list(request):
    users = User.objects.all()
    template = loader.get_template('user_list.html')
    context = {
    'users': users,
  }
    return HttpResponse(template.render(context,request))

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    else:
        form = UserForm()
        template = loader.get_template('create_user.html')
        context ={'form': form,}
        return HttpResponse(template.render(context,request))
    
    return render(request, 'create_user.html', {'form': form})
def user_edit(request,pk):
    user = User.objects.get(pk=pk)
    template = loader.get_template('user_edit.html')
    context = {
    'user': user,
  }
    return HttpResponse(template.render(context,request))



def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        x=request.POST['id']
        y=request.POST['username']
        z=request.POST['password']
        value = request.POST.get('active')
        boolean_value = value in ['true', '1', 'yes', 'on','false','0']
        user.id=x
        user.username=y
        user.password=z
        user.active=boolean_value
        user.save()
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()    
            return redirect('/users')
           # return HttpResponse("Successfull")
        #else:
           # return HttpResponse(user)
    else:
            #template = loader.get_template('user_edit.html')
           # context = {
           # 'user': user,}
           # return HttpResponse(template.render(context,request))
           return HttpResponseBadRequest('User ID is invalid')
def user_delete(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('/users')

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
