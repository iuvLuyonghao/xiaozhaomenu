#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.utils.notice import Notice

@csrf_exempt
def choose_food(request):
    """
    小赵点餐
    :param request:
    :return:
    """
    if request.method == 'POST':
        food=request.POST.get('food')
        request={"code":200,"data":{"text":"小赵点餐啦，菜品为%s" %food},"message":"None"}
        print(request)
        Notice().email(message='小赵点餐啦，菜品为%s' %food,subject='小赵已经点餐啦')
        return JsonResponse(request,json_dumps_params={'ensure_ascii':False})
    else:
        return HttpResponse('must post!!!')
