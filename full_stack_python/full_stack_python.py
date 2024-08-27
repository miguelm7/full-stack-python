'''Welcome to Reflex! This file outlines the steps to create a basic app.'''

import reflex as rx

from rxconfig import config
from .ui.base import base_page
# from .pages.about import about_page

from . import pages
from . import navigation


class State(rx.State):
    '''The app state.'''
    label : str = 'Welcome to Reflex!'

    def handle_title_input_change(self, val: str):
        self.label = val

    def did_click(self):
        print('hello world, did click')

@rx.page(route=navigation.routes.HOME_ROUTE)
def index() -> rx.Component:
    # Welcome Page (Index)
    # return base_page('abc')

    my_child = rx.vstack(
            rx.heading(State.label, size='9'),
            rx.text(
                'Get started by editing ',
                rx.code(f'{config.app_name}/{config.app_name}.py'),
                size='5',
            ),
            
            rx.input(
                default_value=State.label,
                on_click=State.did_click,
                on_change=State.handle_title_input_change
            ),
            # rx.button("About us",on_click=rx.redirect("/about")),
            rx.link( # esta forma es mejor que el on click, permite copiar el enlace, etc...
                rx.button("About us"),
                href=navigation.routes.ABOUT_US_ROUTE,
            ),
            spacing='5',
            justify='center',
            min_height='85vh',
            # text_align='center',
            align='center',
            id='my-child'
        )

    return base_page(my_child)


app = rx.App()
# app.add_page(index) # using the page decorator instead of add_page
# app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
# app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
# app.add_page(pages.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
