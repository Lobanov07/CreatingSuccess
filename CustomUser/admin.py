from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.empty_value_display = "Не задано"


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "bio",
                    "date_of_birth",
                    "profile_picture",
                    "phone_number",
                )
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "bio",
                    "date_of_birth",
                    "profile_picture",
                    "phone_number",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
