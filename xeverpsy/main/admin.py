from django.contrib import admin

@admin.register(PostVideo)
class PostVideoAdmin(admin.ModelAdmin):
     list_display = ['title', 'filename', 'id']
     search_fields = ['title']
     fields = ['title', 'video_file']

