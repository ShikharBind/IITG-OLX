from time import timezone
from urllib import request
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseRedirect
from posts_app.models import Product, BuyRequest
from posts_app.forms import ProductForm, BuyRequestForm

# Create your views here.

class IndexView(ListView):
    template_name = 'posts_app/index.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(published_date__lte=timezone.now(),is_sold=False).order_by('-published_date')



class ProductDetailView(LoginRequiredMixin,DetailView):
    login_url = '/microsoft/to-auth-redirect/'

    template_name = 'posts_app/product_detail.html'
    context_object_name = 'product_data'
    model = Product

    # extra_context={'users': YourModel.objects.all()}

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        product = context['product_data']
        current_user = self.request.user
        buyrequest = product.requests.all().filter(buyer=current_user)
        context['buyrequest'] = buyrequest
        return context


    

class ProductCreateView(LoginRequiredMixin,CreateView):
    login_url = '/microsoft/to-auth-redirect/'

    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # make change at the object
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/microsoft/to-auth-redirect/'

    model = Product
    form_class = ProductForm

class DraftsListView(LoginRequiredMixin,ListView):
    login_url = '/microsoft/to-auth-redirect/'
    
    template_name = 'posts_app/drafts_list.html'
    model = Product

    def get_queryset(self):
        current_user = self.request.user
        query = Product.objects.filter(owner=current_user,published_date__isnull=True).order_by('-created_date')
        return query




class BuyRequestCreateView(LoginRequiredMixin,CreateView):
    login_url = '/microsoft/to-auth-redirect/'

    model = BuyRequest
    form_class = BuyRequestForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # make change at the object
        self.object.buyer = self.request.user
        product = get_object_or_404(Product,pk=self.kwargs['pk'])
        self.object.product = product
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class BuyRequestUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/microsoft/to-auth-redirect/'

    model = BuyRequest
    form_class = BuyRequestForm

    
class BuyRequestDeleteView(DeleteView):
    model = BuyRequest
    success_url = reverse_lazy('posts_app:index')



####################################################################################
####################################################################################







@login_required
def product_publish(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if product.owner == request.user:
        product.publish()
    return HttpResponseRedirect(reverse("posts_app:product_detail",kwargs={'pk':product.pk}))
    # return redirect('posts_app:product_detail',pk=pk)



@login_required
def product_sell(request,pk):
    buyrequest = get_object_or_404(BuyRequest,pk=pk)
    product = buyrequest.product
    if product.owner == request.user:
        if buyrequest.price_negotiating:
            product.price = buyrequest.price_negotiating
        product.sell(buyrequest)
    return HttpResponseRedirect(reverse("posts_app:product_detail",kwargs={'pk':product.pk}))
