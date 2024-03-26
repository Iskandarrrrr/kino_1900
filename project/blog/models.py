from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Name category')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Name movie')
    content = models.TextField(verbose_name='About movie')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Photo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update date')
    publish = models.BooleanField(default=True, verbose_name='Status public')
    views = models.IntegerField(default=0, verbose_name='Views')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category movie')
    video = models.CharField(max_length=500, verbose_name='Link video', blank=True, null=True)

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://previews.123rf.com/images/lobo71/lobo711804/lobo71180400088/100042388-no-movie-camera-reflective-sign.jpg'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
