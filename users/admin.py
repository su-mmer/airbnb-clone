from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# 장고에 모델이 나타나게 하는 두가지 방법
# @admin.register(models.User)
# admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # 내장된 UserAdmin.fieldsets과 Custom한 fieldsets를 합쳐주어야 함
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
