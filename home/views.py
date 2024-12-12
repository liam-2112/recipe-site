from django.views.generic import TemplateView

# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'home/index.html'
