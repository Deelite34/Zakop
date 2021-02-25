from django.contrib import admin

# Register your models here.

from zakop_app.models import FindingRating, Tag
from zakop_app.models import Finding, Comment
from zakop_app.models import CommentsRating, ZakopUser

admin.site.register(FindingRating)
admin.site.register(Finding)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(CommentsRating)
admin.site.register(ZakopUser)
