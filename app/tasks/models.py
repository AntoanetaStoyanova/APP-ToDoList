from django.db import models  # models contains classes and functions that allow us to define data models for the Django app
from django.utils.text import slugify
# uses the Django framework to define data models 

# Create your models here.
class Collection(models.Model): # Collection (data model) inherits from the models.Model and it benefits from amma the basic Django functionality for managing database data  
    name = models.CharField(max_length=60) # text field (string), 60 characters, store the name of a collection 
    slug = models.SlugField() # slug (url) store URL strings 

    @classmethod
    def get_default_collection(cls) -> 'Collection':
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

class Task(models.Model):
    description = models.CharField(max_length=300) # store the description of the task
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE) # ForeignKey field establishes a relationship between Task and Collections. if a collection is deleted, all tasks associated with that collection will also be deleted   

    def __str__(self):
        return self.description