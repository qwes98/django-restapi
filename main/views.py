from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

import json

@csrf_exempt
def profile_list(request):
    result = {
            'status': 200,
            'msg': 'success',
            'data': {}
    }

    if request.method == 'GET':
        qs = Profile.objects.all()
        data = [{'name': inst.name, 'age': inst.age} for inst in qs]
        result['data'] = data
        return JsonResponse(result)
    elif request.method == 'POST':
        data = json.loads(request.body)
        Profile.objects.create(name=data['name'], age=data['age'])
        return JsonResponse(result)
    else:
        result['status'] = 404
        result['msg'] = 'Unsupported method request'
        return JsonResponse(result)

@csrf_exempt
def profile_detail(request, pk):
    result = {
            'status': 200,
            'msg': 'success',
            'data': {}
    }

    def get_profile_or_fail(pk):
        try:
            profile = Profile.objects.get(id=pk)
            return profile
        except:
            result['status'] = 404
            result['msg'] = 'Cannot get data for this pk'
            return None

    if request.method == 'GET':
        profile = get_profile_or_fail(pk=pk)
        if profile:
            data = {'name': profile.name, 'age': profile.age}
            result['data'] = data
        return JsonResponse(result)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        profile = get_profile_or_fail(pk=pk)
        if profile:
            profile.name = data['name']
            profile.age = data['age']
            profile.save()
        return JsonResponse(result)
    elif request.method == 'DELETE':
        profile = get_profile_or_fail(pk=pk)
        if profile:
            profile.delete()
        return JsonResponse(result)
    else:
        result['status'] = 404
        result['msg'] = 'Unsupported method request'
        return JsonResponse(result)