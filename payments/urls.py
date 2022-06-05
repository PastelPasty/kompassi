from django.conf.urls import include

from payments.views import (
    payments_checkout_success_view,
    payments_checkout_cancel_view,
    payments_checkout_success_callback,
    payments_checkout_cancel_callback,
)
from django.urls import re_path


urlpatterns = [
    re_path(
        r"payments/checkout/success/?$",
        payments_checkout_success_view,
        name="payments_checkout_success_view",
    ),
    re_path(
        r"payments/checkout/cancel/?$",
        payments_checkout_cancel_view,
        name="payments_checkout_cancel_view",
    ),
    re_path(
        r"payments/checkout/callbacks/success/?$",
        payments_checkout_success_callback,
        name="payments_checkout_success_callback",
    ),
    re_path(
        r"payments/checkout/callbacks/cancel/?$",
        payments_checkout_cancel_callback,
        name="payments_checkout_cancel_callback",
    ),
]
