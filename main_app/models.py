from django.db import models



class Print(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.TextField(max_length=500)
    verified_print = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Card(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    print = models.ForeignKey(Print, on_delete= models.CASCADE, related_name= "cards")
    
    def __str__(self):
        return self.name
     
class Mug(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    print = models.ForeignKey(Print, on_delete= models.CASCADE, related_name= "mugs")
    
    def __str__(self):
        return self.name
     
class Photo(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    print = models.ForeignKey(Print, on_delete= models.CASCADE, related_name= "photos")
    
    def __str__(self):
        return self.name
     
class Puzzle(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    print = models.ForeignKey(Print, on_delete= models.CASCADE, related_name= "puzzles")
    
    def __str__(self):
        return self.name



class GiftSet(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    cards = models.ManyToManyField(Card)
    mugs = models.ManyToManyField(Mug)
    photos = models.ManyToManyField(Photo)
    puzzles = models.ManyToManyField(Puzzle)

     
    def __str__(self):
        return self.title