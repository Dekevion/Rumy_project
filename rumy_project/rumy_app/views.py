from django.shortcuts import render

# Create your views here.
from json import loads

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import UserModel
from .serializers import UserSerializer


def client_to_server(request):
    # print('test' + str(request.body))
    client_body = loads(request.body)
    client_username = client_body['username']
    client_password = client_body['password']
    print(client_username + client_password)
    user_verify = UserModel.objects.filter(username=client_username)
    # print(user_verify[0]);
    if user_verify:
        if user_verify[0].password == client_password:
            # TODO: Check into building json in a better way
            return JsonResponse(
                {
                    "logged_in": True,
                    "username": user_verify[0].username,
                    "password": user_verify[0].password,
                    "id": user_verify[0].id,
                    "bio": user_verify[0].bio,
                    "age": user_verify[0].age,
                }

            )
            # return HttpResponse(user_verify[0].id)
        else:
            # return HttpResponse(False)
            return JsonResponse(
                {
                    "logged_in": False
                }
            )
    else:
        # return HttpResponse(False)
        return JsonResponse(
            {
                "logged_in": False
            }
        )