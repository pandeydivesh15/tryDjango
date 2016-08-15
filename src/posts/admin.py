from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	"""docstring for PostModelAdmin"""
	class Meta:
		model = Post
	list_display=["title", "timestamp", "updated"]
	list_display_links=["title"]
	list_filter= ["timestamp","updated"]
	search_fields =["title","content"]

admin.site.register(Post, PostModelAdmin)