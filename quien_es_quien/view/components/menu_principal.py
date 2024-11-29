import reflex as rx

def menu_principal() -> rx.Component:
    return rx.box(
        rx.heading("¿Quién es Quién?",class_name="encabezado"),
        rx.box(
            rx.link(
                "1 jugador", 
                href="/un_jugador",
                target="_blank",
                class_name="caja_individual",  

            ),
            rx.link(
                "Próximamente Jugador vs Jugador", 
                href="",
                class_name="caja_individual_proximamente",
            ),
            rx.link(
                "Reglas", 
                href="/reglas",
                target="_blank",
                class_name="caja_individual",                                   

            ),
            class_name="caja_padre",

        ),
        class_name="caja_principal"
    )
