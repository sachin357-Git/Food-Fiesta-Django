from django.db import models

# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    message=models.TextField(null=True)

class tblgalerry(models.Model):
    title=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to="static/picture/",null=True)

class Booking(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    guests = models.IntegerField()

    date = models.DateField()

    time = models.TimeField()

    message = models.TextField()

    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )


    def __str__(self):
        return self.name

class Feedback(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    rating = models.CharField(max_length=20)

    message = models.TextField()


    def __str__(self):
        return self.name

class Dish(models.Model):

    CATEGORY_CHOICES = (
        ("Fast Food", "Fast Food"),
        ("Main Course", "Main Course"),
        ("Desserts", "Desserts"),
        ("Drinks", "Drinks"),
    )

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(
        upload_to="static/dishes/",
        null=True
    )


    def __str__(self):
        return self.name