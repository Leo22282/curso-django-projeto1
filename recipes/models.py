from django.db import models
from django.contrib.auth.models import User #Traz um model de usuario
# Create your models here.

# A classe é a tabela e os atributos são as colunas

class Category(models.Model):
    name = models.CharField(max_length=65)
    
    # Este campo é para que os nomes dos registros no admin db django tenham o nome do item
    def __str__(self): 
        return self.name
        
        

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/') #Salva na pasta do ano depois do mes e depois do dia.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # Quando a categoria for apagada, ele deixa o campo nulo aqui.
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self): 
        return self.title