from django.contrib import admin
from .models import *
from .foreign_keys import *


# Models
admin.site.register(About)
admin.site.register(ContactDetail)
admin.site.register(Project)

# Foreign Key models
admin.site.register(Media)
