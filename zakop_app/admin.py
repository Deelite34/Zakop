from django.contrib import admin

# Register your models here.

from zakop_app.models import findings_rating, tag
from zakop_app.models import finding, comment
from zakop_app.models import comments_rating, user

admin.site.register(findings_rating)
admin.site.register(finding)
admin.site.register(comment)
admin.site.register(tag)
admin.site.register(comments_rating)
admin.site.register(user)
