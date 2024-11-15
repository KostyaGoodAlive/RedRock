from django.shortcuts import render, get_object_or_404
from .models import NewsCard
from .models import ClubsCard
from .models import Photo
from .models import LocationsCard
from .models import CarouselImage, Team08_09


def location(request):
    return render(request, 'location.html')


def eight_nine(request):
    carousel_images = CarouselImage.objects.all()
    team = Team08_09.objects.all()
    context = {
        'carousel_images': carousel_images,
        'team':team,
    }
    return render(request, '08-09.html', context)


def ten_eleven(request):
    return render(request, '10-11.html')


def girls_u12(request):
    return render(request, 'girls_u12.html')


def girls_u11(request):
    return render(request, 'girls_10-11.html')


def girls_u14(request):
    return render(request, 'girls_u14.html')


def twelve_thirteen(request):
    return render(request, '12-13.html')


def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'galery.html', {'photos': photos})


def fourteen_sixteen(request):
    return render(request, '14-16.html')


def about_us(request):
    return render(request, 'about_us.html')


def improve_us(request):
    return render(request, 'improve_us.html')


def teams(request):
    return render(request, 'teams.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def clubs_list(request):
    clubs_cards = ClubsCard.objects.all()
    return render(request, 'club.html', {'clubs_cards': clubs_cards})


def locations_list(request):
    locations_cards = LocationsCard.objects.all()
    return render(request, 'location.html', {'locations_cards': locations_cards})


def location_detail(request, location_id):
    location = get_object_or_404(LocationsCard, id=location_id)
    return render(request, 'about_location.html', {
        'location': location,
    })


def news_list(request):
    news_cards = NewsCard.objects.all()
    return render(request, 'news.html', {'news_cards': news_cards})
