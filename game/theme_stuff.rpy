init offset = -1

transform crystal_ball_float:
    subpixel True
    xalign 0.5
    ypos 225
    on appear, show:
        linear 1.0 ypos 210
        block:
            linear 2.0 ypos 240
            linear 2.0 ypos 210
            repeat
    on hide:
        easein_expo 0.5 ypos 225

transform crystal_ball_stop:
    subpixel True
    xalign 0.5
    ypos 225
    alpha 0.0
    on show:
        time 0.5
        alpha 1.0
    on hide:
        alpha 0.0

image ball_shadow_animation:
    subpixel True
    xalign 0.5
    ypos 950
    zoom 1.1
    "gui/screens/main_menu/ball_shadow.png"
    on appear, show:
        linear 1.0 zoom 1.0
        block:
            linear 2.0 zoom 1.2
            linear 2.0 zoom 1.0
            repeat
image star:
    subpixel True
    choice:
        "gui/s_star1.png"
    choice:
        "gui/b_star1.png"
    choice:
        "gui/b_star2.png"
    choice:
        "gui/s_star1.png"
    choice:
        "gui/s_star2.png"
    choice:
        "gui/s_star1.png"
    xanchor 0.5
    yanchor 0.5
    alpha 0.0
    rotate 0
    pause renpy.random.randint(0, 15)
    linear 2.0 alpha 1.0 rotate 180
    linear 2.0 alpha 0.0 rotate 360
    repeat
image star_choice:
    subpixel True
    "gui/s_star1.png"
    xoffset -10
    yoffset 25
    alpha 0.5
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.5
    repeat

image twinkle = Composite(
    (1028, 731),
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star",
    (renpy.random.randint(0,1028), renpy.random.randint(0, 731)),"star"
    )

image random_vial_picker:
    choice:
        "gui/bar/green_vial.png"
    choice:
        "gui/bar/purple_vial.png"
    choice:
        "gui/bar/yellow_vial.png"
    choice:
        "gui/bar/blue_vial.png"
    choice:
        "gui/bar/red_vial.png"
    choice:
        "gui/bar/indigo_vial.png"
    choice:
        "gui/bar/turquoise_vial.png"
    choice:
        "gui/bar/pink_vial.png"
    alpha 0.5
    linear 1.0 alpha 1.0
    pause renpy.random.randint(5, 10)
    linear 1.0 alpha 0.5
    repeat

image bubbles:
    animation
    subpixel True

    choice:
        "gui/bubble_3.png"
    choice:
        "gui/bubble_3.png"
    choice:
        "gui/bubble_4.png"
    choice:
        "gui/bubble_4.png"
    choice:
        "gui/bubble_4.png"
    choice:
        "gui/bubble_4.png"
    xanchor 0.0
    yanchor 0.0
    zoom 1
    xoffset 0
    yoffset 0
    alpha 0.0
    pause renpy.random.randint(0, 15)

    linear 4.0 alpha 1.0 yoffset -200 xoffset renpy.random.randint(0, 10) zoom 1.8 rotate 180
    linear 4.0 alpha 0.0 yoffset -350 xoffset -renpy.random.randint(0, 5) rotate 360
    repeat
image shimmers:
    subpixel True
    choice:
        "gui/shimmer_2.png"
    choice:
        "gui/shimmer_3.png"
    choice:
        "gui/shimmer_3.png"
    choice:
        "gui/shimmer_4.png"
    choice:
        "gui/shimmer_4.png"
    xanchor 0.0
    yanchor 0.0
    alpha 0.0
    rotate 0
    pause renpy.random.randint(0, 30)
    linear 1.0 alpha 1.0 rotate 180 zoom 1.2
    linear 1.0 alpha 0.0 rotate 360 zoom 1.4
    repeat
image shimmers2:
    subpixel True
    choice:
        "gui/shimmer_2.png"
    choice:
        "gui/shimmer_3.png"
    choice:
        "gui/shimmer_3.png"
    choice:
        "gui/shimmer_4.png"
    choice:
        "gui/shimmer_4.png"
    xanchor 0.0
    yanchor 0.0
    alpha 0.0
    rotate 0
    pause renpy.random.randint(0, 10)
    linear 1.0 alpha 1.0 rotate 90 zoom 1.2
    linear 1.0 alpha 0.0 rotate 180 zoom 1.4
    repeat

define random_vial_x1 = 45
define random_vial_x2 = 65
define random_vial_y1 = 350
define random_vial_y2 = 440

define random_vial_x3 = 40
define random_vial_x4 = 70
define random_vial_y3 = 15
define random_vial_y4 = 400

define vial_factor = 1.7
define vial_xsize = 143
define vial_ysize = 473



image empty_vial = Composite(
    (vial_xsize, vial_ysize),
    (0, 0), Transform("gui/bar/empty_vial.png", zoom=vial_factor)
    )
image vial = Composite(
    (vial_xsize, vial_ysize),
    (0, 0), Transform("random_vial_picker", zoom=vial_factor),
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x1, random_vial_x2), renpy.random.randint(random_vial_y1,random_vial_y2)), "bubbles",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers",
    (0, 0), Transform("gui/bar/empty_vial.png", zoom=vial_factor),
)

image vial_hover = Composite(
    (vial_xsize, vial_ysize),
    (0, 0), Transform("gui/bar/hover_full_vial.png", zoom=vial_factor),
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
    (renpy.random.randint(random_vial_x3, random_vial_x4), renpy.random.randint(random_vial_y3,random_vial_y4)), "shimmers2",
)
image empty_vial_hover = Transform("gui/bar/empty_vial.png", zoom=vial_factor)
