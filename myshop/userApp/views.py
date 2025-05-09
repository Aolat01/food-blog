from django.shortcuts import render, get_object_or_404 , redirect 
from .forms import SignUpForm, ProfileForm, UserForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Profile



class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = 'registration/signup.html'

def ProfileView(request):
    userInfo = User.objects.get(id = request.user.id)
    profileInfo = Profile.objects.get(user_id=request.user.id)


    return render(request, 'profile.html', {'userInfo': userInfo, 'profileInfo': profileInfo})

def editProfile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.method == 'POST':
        userForm = UserForm(request.POST, instance=user)
        profileForm = ProfileForm(request.POST, request.FILES, instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
        else:
            print(userForm.errors, profileForm.errors)
        
        return redirect('profile')
    
    else:
        userForm = UserForm(instance=user)
        profileForm = ProfileForm(instance=profile)
        return render(request, 'edit_profile.html', {'userForm': userForm, 'profileForm': profileForm})