from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Banner
from scheduling.models import Service, ServiceType
from django.db.models import Q

def index(request):
    featured_products = Product.objects.filter(is_featured=True)
    categories = Category.objects.all()
    banners = Banner.objects.filter(is_active=True)
    service_types = ServiceType.objects.all()
    return render(request, 'store/index.html', {
        'featured_products': featured_products, 
        'categories': categories, 
        'banners': banners, 
        'service_types': service_types
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products_by_category.html', {'category': category, 'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('store:view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('store:view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    cart_product_ids = list(cart.keys())

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })
        total_price += item_total

    suggested_products = []
    if cart_product_ids:
        # Find categories of products in the cart
        products_in_cart = Product.objects.filter(id__in=cart_product_ids)
        category_ids = products_in_cart.values_list('category_id', flat=True).distinct()

        # Find other products in the same categories, excluding those already in the cart
        suggested_products = Product.objects.filter(category_id__in=category_ids) \
                                            .exclude(id__in=cart_product_ids) \
                                            .distinct() \
                                            .order_by('?')[:4]

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'suggested_products': suggested_products
    })

def search_results(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()
    return render(request, 'store/search_results.html', {'products': products, 'query': query})