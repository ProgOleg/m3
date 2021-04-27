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
        context = {
            "products": products,
            "comments": comments
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
