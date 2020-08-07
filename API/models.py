from django.db import models

# customer model
class customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# csv_product model
class csv_product(models.Model):
    title = models.CharField(max_length=500)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    customer_id = models.ForeignKey(customer,related_name='products',on_delete=models.PROTECT)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('customer_id', 'title','price')
        ordering = ('-uploaded_date',)
    def __str__(self):
        return self.title

class file_uploads(models.Model):
    uploaded_by = models.ForeignKey(customer,to_field='id', on_delete=models.CASCADE)
    file= models.FileField(blank=True)
    def __str__(self):
        return self.uploaded_by