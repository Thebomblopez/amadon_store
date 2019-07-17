from django.shortcuts import render, redirect 
from .models import Order, Product

# Dictionary for product prices mathed up with there Product ID
prices = {
    1: 25.99,
    2: 35.99,
    3: 59.99
}

# Homepage with products
def index(request):
    context = {
        "all_products": Product.objects.all(),
    }
    return render(request, "store/index.html", context)

#Info from picking product and quantity processed.
def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = prices[int(request.POST["price"])]
    print(price_from_form)
    total_charge = quantity_from_form * price_from_form
    # print(f"Charging credit card {total_charge}")
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(f"view_order/{new_order.id}")

#Helper function to get sum of all orders made.
def total_cost(arr):
    sum = 0
    for order in arr:
        sum += order.total_price
    return sum 

# Info on the order the user just made
def view_order(request, order_id):
    print(order_id)
    selected_order = Order.objects.get(id=order_id)
    print(selected_order.total_price)
    sum_all_orders = total_cost(Order.objects.all())
    context = {
        "total_price": selected_order.total_price,
        "quantity": selected_order.quantity_ordered,
        "sum_all_orders": sum_all_orders 
    }
    
    return render(request, "store/checkout.html", context)