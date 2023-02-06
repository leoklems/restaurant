from admin_site.models import *
from reservation.forms import *


def layout_variable(request):
    site_info = SiteInfoModel.objects.first()
    reservation_form = ReservationForm

    return {
        'site_info': site_info,
        'reservation_form': reservation_form

        }



