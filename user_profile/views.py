from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from user_profile import models
import user_profile
from user_profile.models import UserProfileInfo
from user_profile.forms import UserProfileInfoForm,UserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def user_login(request):
    redirect_address = '../../microsoft/to-auth-redirect/'#?next=/profile/register'
    return HttpResponseRedirect(redirect_address)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts_app:index'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_getID(request):
    current_user = request.user
    if hasattr(current_user,'detail'):
        pk = current_user.detail.pk
        pk = str(pk)
        # return HttpResponse(pk)
        return HttpResponseRedirect(pk)
    else:
        return HttpResponseRedirect(reverse('user_profile:create_data'))

class ProfileDetailView(DetailView):
    template_name = 'user_profile/user_detail.html'
    context_object_name = 'user_data'
    model = UserProfileInfo

class CreateProfileView(CreateView):
    model = UserProfileInfo
    fields = ('profile_pic','program','department','contact')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # make change at the object
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




class UpdateProfileView(UpdateView):
    model = UserProfileInfo
    fields = ('profile_pic','program','department','contact')

class ProfileDeleteView(DeleteView):
    model = UserProfileInfo
    success_url = reverse_lazy('posts_app:index')