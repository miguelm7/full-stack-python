
import reflex as rx
from ..ui.base import base_page

from .. import navigation

@rx.page(route=navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    # Welcome Page (Index)
    # return base_page('abc')

    my_child = rx.vstack(
            rx.heading('Contact', size='9'),
            rx.text(
                'Contact us!'
            ),
            spacing='5',
            justify='center',
            min_height='85vh',
            align='center',
            id='my-child'
        )

    return base_page(my_child)
