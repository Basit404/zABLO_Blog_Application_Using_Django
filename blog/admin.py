from django.contrib import admin
from blog.models import Blog, Feedback

# Register your models here.

# for configuration BlogAdmin
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "s_no")
    search_fields = ("title",)
    list_per_page = 10

# for configuration FeedbackAdmin
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "s_no", "email")
    search_fields = ("name",)
    list_per_page = 10

admin.site.register(Blog, BlogAdmin)
admin.site.register(Feedback, FeedbackAdmin)