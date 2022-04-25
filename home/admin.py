from django.contrib import admin
from .models import accounts,docaccounts,msgs
# Register your models here.
admin.site.register(accounts)
admin.site.register(docaccounts)
admin.site.register(msgs)
