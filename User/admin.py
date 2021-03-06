from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
                                        'is_staff',
                                        'is_superuser',
                                        'groups',
                                        'user_permissions',
                                        'image',
                                        'created',
                                        'is_owner',
                                        'is_advisor',
                                        'number',
                                        'code_agency',
                                    )
admin.site.register(User, UserAdmin)