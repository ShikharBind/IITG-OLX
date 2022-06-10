from urllib import request
from django.shortcuts import render,get_object_or_404, redirect
from posts_app.models import Product
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from user_profile import models
import user_profile
from user_profile.models import UserProfileInfo
from user_profile.forms import UserProfileInfoForm,UserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ProfileDetailView(LoginRequiredMixin,DetailView):
    # login_url = '/profile/login/?next=/profile/'
    login_url = '/microsoft/to-auth-redirect/?next=/profile/'
    # redirect_field_name = 'user_profile/user_detail.html'

    template_name = 'user_profile/user_detail.html'
    context_object_name = 'user_data'
    model = UserProfileInfo

    
    

class CreateProfileView(LoginRequiredMixin,CreateView):
    login_url = '/microsoft/to-auth-redirect/?next=/profile/new/'

    model = UserProfileInfo
    fields = ('profile_pic','program','department','contact')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # make change at the object
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    login_url = '/microsoft/to-auth-redirect/'

    model = UserProfileInfo
    fields = ('profile_pic','program','department','contact')

# class ProfileDeleteView(DeleteView):
#     model = UserProfileInfo
#     success_url = reverse_lazy('posts_app:index')





@login_required
def product_add_to_wishlist(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if product:
        request.user.detail.add_to_wishlist(product)
    return HttpResponseRedirect(reverse("posts_app:product_detail",kwargs={'pk':pk}))
    # return redirect('posts_app:product_detail',pk=pk)


@login_required
def product_remove_from_wishlist(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if product:
        request.user.detail.remove_from_wishlist(product)
    return HttpResponseRedirect(reverse("posts_app:product_detail",kwargs={'pk':pk}))
    # return redirect('posts_app:product_detail',pk=pk)