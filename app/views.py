from django.views.generic import View
from django.shortcuts import render # redirect
from django.http import HttpResponse # JsonResponse, HttpResponseRedirect, FileResponse
# from django.template import loader, Context
from app.models import *
from app.forms import *
# from app.utils import *
# from django.conf import settings
# from django.db.models import Prefetch, F
import requests
from m3 import settings
import datetime


class IndexPage(View):

    def get(self, request):
        products = Products.objects.filter(is_active=True)
        comments = Comments.objects.filter(is_active=True)
        regions = Region.objects.all().values("descripton", "is_active")
        ports = Port.objects.all().values("address", "phone", "region", "is_active", "map_link")
        stocks = Stock.objects.all().values("address", "phone", "region", "is_active", "map_link")

        regions_accum = {}
        for el in regions:
            descripton = el.get("descripton")
            regions_accum.update({descripton: el.get("is_active")})

        port_accum = {}
        for el in ports:
            region = el.pop("region")
            if port_accum.get(region):
                port_accum[region].append(el)
            else:
                port_accum.update({region: [el]})

        stock_accum = {}
        for el in stocks:
            region = el.pop("region")
            if stock_accum.get(region):
                stock_accum[region].append(el)
            else:
                stock_accum.update({region: [el]})

        context = {
            "products": products,
            "comments": comments,
            "regions": regions_accum,
            "ports": port_accum,
            "stock": stock_accum
        }

        return render(request, 'app/index.html', context)


def oder_approval(request):
    resp = 400
    if request.is_ajax() and request.method == "POST":
        data = OrdersForm(request.POST)
        if data.is_valid():
            data = data.save()
            resp = 200
            date = data.date_created
            date = date + datetime.timedelta(hours=3)
            date = date.strftime("%Y-%m-%d %H:%M")
            url = f"https://api.telegram.org/bot{settings.T_BOT_TOKEN}/sendMessage"
            headers = {'Content-Type': 'application/json'}
            text = f"""
Заявка №-{data.id}
Имя: {data.name}
Телефон: {data.t_number}
Дата создания: {date}
"""
            json_ = {"text": text, "chat_id": settings.T_ADMIN_CHAT_ID}
            requests.post(url, headers=headers, json=json_)
    return HttpResponse(status=resp)


def comments_approval(request):
    resp = 400
    if request.is_ajax() and request.method == "POST":
        data = CommentsForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            resp = 200
    return HttpResponse(status=resp)


def subscribe(request):
    resp = 400
    if request.is_ajax() and request.method == "POST":
        data = SubscribeForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            resp = 200
    return HttpResponse(status=resp)
