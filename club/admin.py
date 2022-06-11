from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)

class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email',)
    list_display_links = ('email',)


admin.site.register(User, UserAdmin)