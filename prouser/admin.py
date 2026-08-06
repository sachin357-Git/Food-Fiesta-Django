from django.contrib import admin
from .models import *


# Contact Admin
@admin.register(tblcontact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "message"
    )

    search_fields = (
        "name",
        "email"
    )


# Gallery Admin
@admin.register(tblgalerry)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "picture"
    )



# Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "guests",
        "date",
        "time",
        "status"
    )

    search_fields = (
        "name",
        "email",
        "phone"
    )

    list_filter = (
        "date",
        "time",
        "status"
    )



# Feedback Admin
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "rating",
        "message"
    )

    search_fields = (
        "name",
        "email"
    )

    list_filter = (
        "rating",
    )

# Admin Panel Branding

admin.site.site_header = "Food Fiesta Admin Panel"

admin.site.site_title = "Food Fiesta Admin"

admin.site.index_title = "Restaurant Management Dashboard"

# Dish Admin
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price"
    )

    search_fields = (
        "name",
        "category"
    )

    list_filter = (
        "category",
    )