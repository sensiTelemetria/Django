from django.shortcuts import render,HttpResponse, redirect
from App_Django.accounts.forms import UserForm
from    django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from    django.contrib.auth.forms import PasswordChangeForm
from    django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def add_User(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            login(request, user)
            return redirect("/")
        #"/accounts/login-usuario"
    else:
        User = UserForm()
       # print("aquiiiiiiiiiiiiiiiiiii")
    return render(request, 'accounts/index.html', {'User': User})
    #return HttpResponse("criado com sucesso")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(password)
        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request,"Usuário ou senha inválidos")



    return render(request,"accounts/user_login_bootstrap.html")

def user_logout(request):
    logout(request)
    return redirect("/accounts/login-usuario")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/change-password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})