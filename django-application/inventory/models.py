import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name=models.CharField(max_length=20, null=False)
    selling_price=models.DecimalField(decimal_places=2,max_digits=10, null=False)
    buying_price=models.DecimalField(decimal_places=2, max_digits=10, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural="Products"