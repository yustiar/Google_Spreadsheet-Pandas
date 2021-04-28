from django.contrib import admin

from .models import Post
# Register your models here.


class BaseAdmin(admin.ModelAdmin):
	list_display = ('namakk','alamat','jumlahart','nomorhp')
	search_fields = ('namakk', 'alamat',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Post, BaseAdmin);