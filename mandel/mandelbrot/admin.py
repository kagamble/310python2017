# admin.py
# Register your models here.
from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin

from django.contrib.auth.models import User
from mandelbrot.models          import Profile

#replace the registered admin model with a custom UserAdmin to display user profile

class ProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'
    max_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]
    #override default list_display to include color
    list_display = ('username','email','first_name','last_name','is_staff','get_color')
    list_select_related = ('profile', )

    def get_color(self, instance):
      return instance.profile.color
    get_color.short_description = 'Color'              #table heading

#unregister the default admin model
admin.site.unregister(User)

#register the custom admin model
admin.site.register(User, CustomUserAdmin)

