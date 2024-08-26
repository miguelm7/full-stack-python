import reflex as rx

from .nav import navbar

def base_page(child: rx.Component,hide_navbar=False, *args, **kwargs) -> rx.Component:
    
    # print( [type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading('This is not a valid child element')

    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position='bottom-left'),
        )

    return rx.fragment( # rx.fragment -> renders nothing
        navbar(),
        rx.box(
            child,
            id='my-child-content',
            # bg=rx.color('accent', 3),
            padding='1em',
            width='100%',
        ),
        rx.logo(),
        rx.color_mode.button(position='bottom-left',id='my-light-mode-btn'),
        id='my-base-container'
    )