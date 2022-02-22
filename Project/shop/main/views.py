from .forms import ReviewForm
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Product


def index(request):
    return render(request, 'main/index.html')


class ProductDetailView(DetailView, FormMixin):
    model = Product
    template_name = 'main/product.html'
    context_object_name = 'get_product'
    form_class = ReviewForm
    success_msg = 'Комментарий успешно создан'

    def get_success_url(self, **kwargs):
        return reverse_lazy('product', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.product_review = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/shop.html', context)