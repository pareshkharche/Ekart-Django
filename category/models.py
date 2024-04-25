from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name= models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank=True)
    
    
    #this code will change the model name inside the admin page which give plural form like categorys this is worng spelling so to changes to make correct spelling is categories that's why this coode.
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
        
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])
        
    def __str__(self):
        return self.category_name