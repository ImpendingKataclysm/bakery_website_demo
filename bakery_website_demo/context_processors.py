from main_site.models import Location


def location_data(request):
    """
    Define a keyword to reference the bakery location throughout the
    site.
    :param request:
    :return:
    """
    context = {
        'location': Location.objects.first()
    }

    return context
