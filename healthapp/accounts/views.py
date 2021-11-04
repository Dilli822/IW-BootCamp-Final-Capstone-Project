from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        # LoginForm will capture the request.POST all data
        form = LoginForm(request.POST)
        if form.is_valid():
            user= authenticate(username = form.cleaned_data['username'],
                               password=form.cleaned_data['password'])
            if user:
                print("A user is found--->", user)
                login(request, user)
                return redirect('/accounts/profile/')
            else:
                print("ERROR---> Auth Credentials donot match")
            
            print(form.cleaned_data)

    elif request.method == 'GET':    
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# protecting this view for only authenticated user
def profile_view(request):
    if request.user.is_authenticated:
        #ok passed
        pass
    else:
        #throw error for not authenticated person
        pass
    return render(request, 'accounts/profile.html')
