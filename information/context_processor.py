from .models import AboutUs

def about_us(request):
    about=AboutUs.objects.last()
    return {'about':about}