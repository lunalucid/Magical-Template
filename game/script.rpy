image white_background = Solid("#fff")

default bag = []
default money = 200

default mayo_emotion = "normal"
default hana_emotion = "neutral"
image mayo = "images/sprites/mayonaise/mayonaise_[mayo_emotion].png"
image hana = "images/sprites/hana/hana_[hana_emotion].png"

define m = Character("Mayonaise")
define h = Character("Hana")

image green_potion:
    "images/items/Bottle-Green2.png"
    zoom .8
image book:
    "images/items/book1.png"
    zoom .5
image rose:
    "images/items/rose.png"
    zoom .8



label start:
    show screen game_bar
    jump tutorial

label tutorial:
    scene white_background
    $ renpy.music.stop(fadeout=3.0)
    $ renpy.music.set_volume(0.5, delay=3, channel="music")
    queue music "audio/eric_matyas/RPG-Map-Music_Looping.mp3"
    m "I've been expecting you."
    scene fantasy with dissolve
    show mayo at left
    $ mayo_emotion = "happy"
    m "Luna sends her gratitude for choosing her magical template."
    $ mayo_emotion = "smile"
    m "If you couldn't already tell, this template is already fully functioning."
    m "From here, you can add or change anything to your liking."
    $ mayo_emotion = "happy"
    show hana at right with moveinright
    $ mayo_emotion = "normal"
    h "Hello, developer. If you ever run into any trouble with this template, please ask {a=https://lemmasoft.renai.us/forums/memberlist.php?mode=viewprofile&u=29301}Luna{/a} for help."
    $ hana_emotion = "serious"
    h "You can't go out there empty handed."
    $ mayo_emotion = "happy"
    m "We have some great things for sale here."
    $ mayo_emotion = "normal"
    $ hana_emotion = "neutral"
    h "If you wish to add an image to a choice like this one coming up, just use the image tag in your menu item {{image=image_name}"
    h "You may need to resize images to fit on the choice screen correctly. Check script.rpy for examples."
    menu:
        with dissolve
        "Buy the potion. ($86){image=green_potion}":
            $ money -= 86
            $ bag.append("Green potion")
            h "Good choice. It's effects are unknown but you might need it one day."
        "Buy the book. ($55){image=book}":
            $ money -= 55
            $ bag.append("Book")
            m "There might be some helpful spells in there."
        "Buy the rose. ($19){image=rose}":
            $ money -= 19
            $ bag.append("Rose")
            $ hana_emotion = "disappointed"
            h "It seems we have a romantic."

    $ mayo_emotion = "happy"
    $ hana_emotion = "smile"
    m "Thanks, come again!"
    "I hope you enjoy this template :)"
    return
