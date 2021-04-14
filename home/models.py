from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class Post(models.Model):
    IS_ACTIVE = (
        ('T', 'Visible'),
        ('F', 'Not Visible'),
    )
    title = models.CharField(max_length=254)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    description = models.TextField()
    is_visible = models.CharField(max_length=1, choices=IS_ACTIVE)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name
    