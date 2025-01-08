import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.link("Bardia", href="https://www.filtershecan.com/", is_external=True, color_scheme="tomato"),
        rx.link(
            "Gabriel",
            href="https://gabrielgsd.developer.li/",
            color_scheme="cyan"
            ),
        class_name="footer"
    )