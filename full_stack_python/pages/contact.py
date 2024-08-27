
import reflex as rx

from ..ui.base import base_page
from .. import navigation

class ContactState(rx.State):

    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        print(form_data)


@rx.page(route=navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form =  rx.form(
            rx.vstack(
                rx.input(
                    name="first_name",
                    placeholder="First Name",
                    type='text',
                    required=True
                ),
                rx.input(
                    name="last_name",
                    placeholder="Last Name",
                    type='text',
                ),
                rx.input(
                    name='email',
                    placeholder='example@email.com',
                    type='email'
                ),
                rx.text_area(
                    name='message',
                    placeholder="your message",
                    required=True

                ),
                # rx.hstack(
                #     rx.checkbox("Checked", name="check"),
                #     rx.switch("Switched", name="switch"),
                # ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )

    my_child = rx.vstack(
            rx.heading('Contact us', size='9'),
            my_form,
            spacing='5',
            justify='center',
            min_height='85vh',
            align='center',
            id='my-child'
        )

    return base_page(my_child)
