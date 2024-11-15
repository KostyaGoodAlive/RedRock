from django.db import models


class CarouselImage(models.Model):
    image = models.ImageField()
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_text = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0) 

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption_title or "Carousel Image"

class Team08_09(models.Model):
    full_name = models.CharField(max_length=255)
    trainer = models.CharField(max_length=255)
    ppg = models.FloatField()

    def __str__(self):
        return self.full_name
class NewsCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class LocationsCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    image5 = models.ImageField()
    time = models.TextField()

    def __str__(self):
        return self.title    


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description or 'Без опису'


class ClubsCard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
