import django_tables2 as tables
from .models import Load
import itertools

class Load(tables.Table):
    class Meta:
        template_name = "home.html"
        origin = tables.Column("origin")
        destination = tables.Column("destination")
        rate = tables.Column("urls")
        urtotal_km = tables.Column("urls")
        email = tables.Column("urls")
        urphone_number = tables.Column("urls")