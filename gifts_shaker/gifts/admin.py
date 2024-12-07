from django.contrib import admin

# Register your models here.
from gifts.models import Invitation, Shaker, Gift, Pairs

admin.site.register(Invitation)
admin.site.register(Shaker)
admin.site.register(Gift)
admin.site.register(Pairs)
