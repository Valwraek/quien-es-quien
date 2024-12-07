import reflex as rx

class estilos():

    shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
    chat_margin = "20%"
    
    caja_input = dict(
        width="100%",
        box_sizing="border-box",
    )
    input_style = dict(
        border_width="1px",
        padding="0.5em",
        box_shadow=shadow,
        width="100%",
        color= "white",
        background_color="#111113",
        justify_content="center",
        align_items="center",
        transform="translateX(10px)",
    )
    message_style = dict(
        padding="1em",
        border_radius="5px",
        margin_y="0.5em",
        box_shadow=shadow,
        max_width="30em",
        display="inline-block",
        transform="translateX(26px)",      
    )
    question_style = message_style | dict(
        margin_left=chat_margin,
        background_color=rx.color("gray", 4),
        transform="translateX(0px)",        
    )
    answer_style = message_style | dict(
        margin_right=chat_margin,
        background_color=rx.color("accent", 8),
        transform="translateX(0px)",     
    )