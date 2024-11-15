from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.locations_list, name='locations_list'),
    path('location/<int:location_id>/', views.location_detail, name='location_detail'),
    path('teams/', views.teams, name='teams'),
    path('08-09/', views.eight_nine, name='eight_nine'),
    path('10-11/', views.ten_eleven, name='ten_eleven'),
    path('12-13/', views.twelve_thirteen, name='twelve_thirteen'),
    path('14-16/', views.fourteen_sixteen, name='fourteen_sixteen'),
    path('', views.about_us, name='about_us'),
    path('club/', views.clubs_list, name='clubs_list'),
    path('news/', views.news_list, name='news_list'),
    path('improve_us/', views.improve_us, name='improve_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('gallery/', views.gallery, name='gallery'),
    path('girls_u12/', views.girls_u12, name='girls_u12'),
    path('girls_10-11/', views.girls_u11, name='girls_u11'),
    path('girls_u14/', views.girls_u14, name='girls_u14'),
]


urlpatterns += staticfiles_urlpatterns()