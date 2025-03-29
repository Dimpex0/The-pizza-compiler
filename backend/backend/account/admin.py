from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class ClientAdmin(UserAdmin):
    list_display = ['id', 'email', 'is_staff', 'is_superuser']
    readonly_fields = ['date_joined', 'password']
    ordering = ['-id']
    search_fields = ['email', 'id']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'password1', 'password2'),
        }),
    )