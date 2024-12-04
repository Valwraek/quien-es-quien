import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.text("Bardia", color_scheme="tomato"),
        rx.link(
            "Gabriel",
            href="https://gabrielgsd.developer.li/",
            color_scheme="cyan"
            ),
        class_name="footer"
    )