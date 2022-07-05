from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    mail = models.EmailField(max_length=50, blank=False, null=False)
    
    def full_name(self):
        return f'{ self.last_name } { self.first_name }'
    
    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{ self.caption }'

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts") # related_name is important for inverse querying
    title = models.CharField(max_length=100, unique=True)
    excerpt = models.CharField(max_length=300)
    img_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.CharField(max_length=150, unique=True, db_index=True) # SlugField is indexed automatically
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)    
    
    def save(self):
        super().save()
        self.slug = slugify(self.title)
    
    def __str__(self):
        return f'{ self.title }, { self.date }, { self.author }'
    
    
