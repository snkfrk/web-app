from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import SignupForm,LoginForm
from django.contrib.auth.decorators import login_required

# アカウントの登録
def accounts_signup(request):
    print("★accounts_signup★")
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request,user)
                return redirect('user')
    else:
        form = SignupForm
    params = {
        'form':form,
    }
    return render(request,'accounts_app/signup.html',params)

# ログイン
def accounts_login(request):
    print("★accounts_login★")
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request,user)
                return redirect('user')
    else:
        form = LoginForm
    params = {
        'form':form
    }
    return render(request,'accounts_app/login.html',params)

# ログアウト
@login_required
def accounts_logout(request):
    print("★accounts_logout★")
    logout(request)
    return render(request,'accounts_app/logout.html')
