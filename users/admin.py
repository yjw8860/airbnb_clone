from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User) #admin pannel에서 user를 보여줄거다. user를 컨트롤하는 class는 CustomUserAdmin이다
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (("Custom Profile",{'fields':("avatar","gender","bio","birthdate","language","currency","superhost")}),)

    list_filter = UserAdmin.list_filter +  (
        'superhost',
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'language',
        'currency',
        'superhost',
        'is_staff',
        'is_superuser',
    )