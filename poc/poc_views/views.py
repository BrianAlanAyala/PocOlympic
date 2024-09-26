from django.http import HttpResponse


def contacto(request):
    nombre = request.GET.get('nombre', 'desconocido')
    return HttpResponse(f"Hola {nombre}, bienvenido a Hola mundo!!!")
