from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from super_market.models import Product, Order, OrderItem
from django.views.decorators.csrf import csrf_exempt


def login_view(request):
    if request.POST:
        print("\n\n", "1", "\n\n")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:

            # Return an 'invalid login' error message.
            return redirect("login")

    return render(request, "login/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def index(request):
    return render(request, "page/index.html")


@login_required
def search_item(request):
    q = False
    if request.POST:

        query = request.POST["q"]
        print("\n\n", query, "\n\n")
        if Product.objects.filter(barcode=query).exists():
            q = Product.objects.filter(barcode=query)[0]

    return render(request, "page/search.html", {"query": q})


@login_required
def sell(request):
    """
    create order object
    send request with bar code that serach in product table and get the product the respose is prodect name and sell price (API call)
    if post create
    send request with id of prodect and qeantaty and ,sell price total (sell price * qeantay) --> that create order itam object
    if delete send delete method that delete item order
    sell option  = true
    if sell option -->
    """
    if request.POST:
        pass
    return render(request, "page/sell.html")


import json
from django.db import transaction


@transaction.atomic
@login_required
@csrf_exempt
def get_data_about_prodeuct(request):
    data = None
    if request.method == "POST":
        # print("\n\n", "post body", request.body, "\n\n")
        if request.body == b"[]":
            pass
        else:
            try:
                d = json.loads(request.body)

                # print("the d is \n\n", d.pop(), "\n")
                oreder = Order.objects.create(total_oreders=d[-1]["totalGrand"])
                d.pop()

                for i in d:
                    try:
                        prodect = Product.objects.get(name=i["name"])
                        prodect.Quantity -= i["quantity"]
                        OrderItem.objects.create(
                            order=oreder,
                            product=prodect,
                            quantity=i["quantity"],
                            price=i["price"],
                        )
                        prodect.save()
                    except Exception as e:
                        transaction.set_rollback(True)
                        return JsonResponse({"error": str(e)}, status=400)
            except Exception as e:
                transaction.set_rollback(True)
                return JsonResponse({"error": str(e)}, status=400)

            return redirect("bell")
        return redirect("bell")

    if request.GET:

        q = request.GET["q"]

        if Product.objects.filter(barcode=q).exists():

            q = Product.objects.get(barcode=q)
            data = {
                "barcode": q.barcode,
                "name": q.name,
                "price": q.sell_price,
                "quantity": 1,
                # Add more fields as needed
            }
            print(data)

    return JsonResponse(data, safe=False)


@login_required
def bell(request):
    return render(request, "page/bell.html")


@login_required
def return_item(request):
    code = None
    order_data = None
    if request.method == "POST":
        pk = request.POST["pk"]
        order = OrderItem.objects.get(pk=pk)
        order.product.Quantity += order.quantity
        order.product.save()
        order.order.total_oreders -= order.total_cost
        order.order.save()
        order.save()
        order.delete()
        if order.order.total_oreders == 0:
            order.order.delete()
    if request.GET:
        code = request.GET["code"]
        print(code)
        if Order.objects.filter(pk=code).exists():
            order = Order.objects.get(pk=code)
            print(order)
            order_data = OrderItem.objects.filter(order=order)
            for r in order_data:
                print(r.product.name, "  ", r.quantity, r.total_cost, order.pk)
    return render(request, "page/return.html", {"order_data": order_data})


@login_required
def add_page(request):

    return render(request, "page/add.html")
