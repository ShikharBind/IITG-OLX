from time import timezone
from urllib import request
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from posts_app.models import Product, BuyRequest
from posts_app.forms import ProductForm, BuyRequestForm, SearchForm

# Create your views here.

class IndexView(ListView):
    template_name = 'posts_app/index.html'
    model = Product
    searchform = SearchForm()


    extra_context={'form': searchform}

    def get_queryset(self):

        search = self.request.GET.get('search', None)
        min_p = self.request.GET.get('minimum_price', None)
        max_p = self.request.GET.get('maximum_price', None)

        query =  Product.objects.filter(published_date__lte=timezone.now(),is_sold=False).order_by('-published_date')
        
        if search:
            lookups = Q(product_title__icontains=search)| Q(product_details__icontains=search)
            query = query.filter(lookups).distinct()
        
        if min_p:
            query = query.filter(price__gte=min_p)
            
        if max_p:
            query = query.filter(price__lte=max_p)

        return query



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

    
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('posts_app:index')

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.requests.all().delete()
        return super().delete(request, *args, **kwargs)



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


class BuyRequestsListView(LoginRequiredMixin,ListView):
    login_url = '/microsoft/to-auth-redirect/'
    
    template_name = 'posts_app/buy_requests_list.html'
    model = BuyRequest



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
