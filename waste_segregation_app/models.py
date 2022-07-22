from django.db import models

bins = { 
    'yellow': ['plastic', 'carton of milk', 'carton of juice', 'tin', 'bottle cap', 'metal'],
    'blue' : ['newspaper', 'book', 'paper', 'cardboard'],
    'green' : ['glass'],
    'black' : ['sponge', 'cloth', 'meat', 'fish', 'poo', 'oil', 'dust', 'china', 'diaper', 'sanitary towel', 'cotton wool', 'leather', 'tea bag', 'hair'],
    'pharmacy' : ['medicinie', 'drug', 'pill'],
    'brown' : ['grass', 'flowers']
}

# Create your models here.
class Trash(models.Model):
    trash_description = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = 'trash'
    
    def __str__(self):
        return self.trash_description
    
    def check_bin(self):
        trash_description = self.trash_description.lower()
        for bin in bins:
            if trash_description in bins.get(bin): 
                    return bin
            for trash in trash_description.split(): 
                if trash in bins.get(bin):
                    return bin
        return 'Unknown'
    