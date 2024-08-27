# from .models import Cart

# def cart_item_count(request):
#     cart = Cart.objects.filter(user=request.user).first()
#     item_count = cart.product.count() if cart else 0
#     return {'cart_item_count': item_count}