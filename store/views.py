from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, CartItem


def get_cart_count(request):
    """Get the number of items in the cart"""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    return CartItem.objects.filter(session_key=session_key).count()


def home(request):
    """Home page with product listings and search/filter functionality"""
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Category filter
    category_id = request.GET.get('category', '')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Price filter
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'min_price': min_price,
        'max_price': max_price,
        'cart_count': get_cart_count(request),
    }
    return render(request, 'store/home.html', context)


def product_detail(request, product_id):
    """Product detail page"""
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
        'cart_count': get_cart_count(request),
    }
    return render(request, 'store/product_detail.html', context)


def cart(request):
    """Shopping cart page"""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    cart_items = CartItem.objects.filter(session_key=session_key).select_related('product')
    total = sum(item.total_price for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': len(cart_items),
    }
    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    """Add a product to the cart"""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    product = get_object_or_404(Product, id=product_id)
    
    # Check if item already in cart
    cart_item, created = CartItem.objects.get_or_create(
        session_key=session_key,
        product=product,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Updated {product.name} quantity in cart!')
    else:
        messages.success(request, f'Added {product.name} to cart!')
    
    # Redirect back to the page the user came from
    next_url = request.GET.get('next', 'home')
    return redirect(next_url)


def update_cart(request, item_id):
    """Update cart item quantity"""
    cart_item = get_object_or_404(CartItem, id=item_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated!')
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart!')
    
    return redirect('cart')


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart_item = get_object_or_404(CartItem, id=item_id)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'Removed {product_name} from cart!')
    return redirect('cart')


def checkout(request):
    """Checkout page"""
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key
    
    cart_items = CartItem.objects.filter(session_key=session_key).select_related('product')
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('home')
    
    total = sum(item.total_price for item in cart_items)
    
    if request.method == 'POST':
        # Process checkout (simplified - just clear the cart)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        
        if name and email:
            # Clear the cart after successful checkout
            cart_items.delete()
            messages.success(request, f'Thank you {name}! Your order has been placed successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': len(cart_items),
    }
    return render(request, 'store/checkout.html', context)
