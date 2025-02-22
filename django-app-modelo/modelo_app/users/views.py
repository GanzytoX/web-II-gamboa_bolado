from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Users
from django.shortcuts import render, get_object_or_404, redirect

def indexUsers(request):
    users = Users.objects.all()
    data = {
        "users": users,
        "titulo": "Lista de clientes",
    }
    return render(request, 'users/index.html', data)

def createUser(request):
    data = {}

    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            age = request.POST.get('age')
            rfc = request.POST.get('rfc')
            photo = request.POST.get('photo') 

            user = Users(name=name, email=email, age=age, rfc=rfc, photo=photo)
            user.save()

            data["user"] = user
            data["message"] = "Usuario creado correctamente"
            data["status"] = "success"

            

        except Exception as e:
            data["message"] = str(e)
            data["status"] = "error"

    return render(request, 'users/create.html', data)

def userDetail(request, id):
    user = get_object_or_404(Users, id=id)

    if request.method == "POST":
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.rfc = request.POST.get('rfc')

        user.save()

        return redirect('userDetail', id=user.id)

    return render(request, 'users/detail.html', {"user": user})



    

