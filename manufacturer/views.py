from django.views import generic

from manufacturer.models import Manufacturer


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "shop/manufacturer_list.html"
