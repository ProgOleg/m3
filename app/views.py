from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from django.template import loader, Context
from app.models import *
from app.forms import *
# from app.utils import *
from django.conf import settings
from django.db.models import Prefetch, F


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
            data.save()
            resp = 200
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
