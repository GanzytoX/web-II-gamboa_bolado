from django.shortcuts import render
from .models import Users, UserAddress

def usersIndex(request):
    users = Users.objects.all()
    data = {
        "users": users,
        "titulo": "Index de users por variable",
        "total_users": users.count(),
        "total_addresses": UserAddress.objects.count(),
        "users_list": [
            {
                "id": 1, "age": 100, "name": "Carlos Eduardo",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 2, "age": 200, "name": "Maria Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            },
            {
                "id": 3, "age": 300, "name": "Juan Carlos",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 4, "age": 400, "name": "Luisa Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            },
                        {
                "id": 1, "age": 100, "name": "Carlos Eduardo",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 2, "age": 200, "name": "Maria Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            },
            {
                "id": 3, "age": 300, "name": "Juan Carlos",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 4, "age": 400, "name": "Luisa Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            },
                        {
                "id": 1, "age": 100, "name": "Carlos Eduardo",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 2, "age": 200, "name": "Maria Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            },
            {
                "id": 3, "age": 300, "name": "Juan Carlos",
                "image": "https://media.istockphoto.com/id/2161765195/photo/a-smiling-man-working-over-the-laptop-at-the-office.jpg?s=1024x1024&w=is&k=20&c=JNz97YVBteawk9cn5WgFrVPeI2ks0BvMTRtCBQHIEVg="
            },
            {
                "id": 4, "age": 400, "name": "Luisa Fernanda",
                "image": "https://media.istockphoto.com/id/2073254261/photo/an-adult-man-is-using-his-smartphone.jpg?s=1024x1024&w=is&k=20&c=xNIjvUR3J7C1fFcCbjq_syI3rDb0loJ_xyvDkZx7PCU="
            }
        ]
    }
    return render(request, 'users/index.html', data)

def addressesByUser(request):
    addresses = UserAddress.objects.all()
    data = {
        "addresses": addresses,
        "titulo": "Direcciones de usuarios",
        "total_addresses": addresses.count()
    }
    return render(request, 'users/addresses.html', data)
