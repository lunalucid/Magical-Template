init offset = -1

## Say screen ##################################################################
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who underline True id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')




## Input screen ################################################################
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"




## Choice screen ###############################################################
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    default i = 0
    style_prefix "choice"
    add "gui/screens/overlay.png"
    showif True:
        add "gui/screens/main_menu/crystal_ball.png" at crystal_ball_float
    add "twinkle" pos(470,200)


    text "Choose Wisely" xalign 0.5 ypos 100 color "#fff" size 50
    vbox:
        xalign 0.5
        ypos 330
        spacing 30
        hbox:
            xalign 0.5
            textbutton "<<" action [If(i == 0, SetScreenVariable("i", len(items)-1), SetScreenVariable("i", i - 1))] text_size 30
            textbutton "{}/{}".format(i+1, len(items)) text_size 30 text_hover_color "#000" action NullAction()
            textbutton ">>" action [If(i == len(items)-1, SetScreenVariable("i", 0), SetScreenVariable("i", i + 1))] text_size 30
        hbox:
            xalign 0.5
            textbutton items[i].caption action items[i].action

define config.narrator_menu = True

## Quick Menu screen ###########################################################

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

## Navigation screen ###########################################################

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

## Main Menu screen ############################################################

screen main_menu():
    default ball_active = False
    default twink = False
    tag menu

    if ball_active:
        add "gui/screens/main_menu/background2.png"
    else:
        add "gui/screens/main_menu/background.png"

    showif ball_active:
        add "gui/screens/main_menu/crystal_ball.png" at crystal_ball_stop
    else:
        add "gui/screens/main_menu/crystal_ball.png" at crystal_ball_float
        add "ball_shadow_animation"

    if gui.show_name:

        vbox:
            xalign 0.5
            ypos 50
            text "[config.name!t]":
                style "main_menu_title"

            #text "[config.version]":
                #style "main_menu_version"
    vbox:
        xalign 0.5
        ypos 320
        imagebutton:
            idle "gui/screens/main_menu/buttons/start_idle.png"
            hover "gui/screens/main_menu/buttons/start_hover.png"
            hovered [SetScreenVariable("ball_active", True), SetScreenVariable("twink", True)]
            unhovered [SetScreenVariable("ball_active", False), SetScreenVariable("twink", False)]
            action Start()
        imagebutton:
            idle "gui/screens/main_menu/buttons/load_idle.png"
            hover "gui/screens/main_menu/buttons/load_hover.png"
            hovered [SetScreenVariable("ball_active", True), SetScreenVariable("twink", True)]
            unhovered [SetScreenVariable("ball_active", False), SetScreenVariable("twink", False)]
            action ShowMenu('load')
        imagebutton:
            idle "gui/screens/main_menu/buttons/prefs_idle.png"
            hover "gui/screens/main_menu/buttons/prefs_hover.png"
            hovered [SetScreenVariable("ball_active", True), SetScreenVariable("twink", True)]
            unhovered [SetScreenVariable("ball_active", False), SetScreenVariable("twink", False)]
            action ShowMenu('preferences')
        imagebutton:
            idle "gui/screens/main_menu/buttons/about_idle.png"
            hover "gui/screens/main_menu/buttons/about_hover.png"
            hovered [SetScreenVariable("ball_active", True), SetScreenVariable("twink", True)]
            unhovered [SetScreenVariable("ball_active", False), SetScreenVariable("twink", False)]
            action ShowMenu('about')
        imagebutton:
            idle "gui/screens/main_menu/buttons/quit_idle.png"
            hover "gui/screens/main_menu/buttons/quit_hover.png"
            hovered [SetScreenVariable("ball_active", True), SetScreenVariable("twink", True)]
            unhovered [SetScreenVariable("ball_active", False), SetScreenVariable("twink", False)]
            action Quit()

        at transform:
            alpha 0.0
            linear 2.0 alpha 1.0
    if twink:
        add "twinkle" pos(470,200)





### bar

screen game_bar():

    hbox:
        yalign 0.01
        xalign 0.99
        frame:
            hbox:
                add "gui/money.png"
                text "{}".format(money)




## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")





## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu
    add "gui/screens/history/scroll.png" xalign 0.5 yalign 0.5
    ## Avoid predicting this screen, as it can be very large.
    predict False
    style_prefix "about"
    vbox:
        xalign 0.5
        ypos 200
        viewport id "vpgrid":
            yinitial 1.0
            #draggable True
            mousewheel True
            xmaximum 500
            ymaximum 620
            yfill True
            vbox:
                label "[config.name!t]"
                text _("Version [config.version!t]\n")

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
    use back_button


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""





## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load


screen save():

    tag menu

    use file_slots

screen load():

    tag menu

    use file_slots


screen file_slots():
    add "gui/screens/save_load/idle.png"
    imagemap:
        idle "gui/screens/save_load/idle.png"
        hover "gui/screens/save_load/hover.png"

        hotspot(207, 60, 370, 407) action FileAction(1):
            use load_save_slot(number=1)
        hotspot(774, 60, 370, 407) action FileAction(2):
            use load_save_slot(number=2)
        hotspot(1341, 60, 370, 407) action FileAction(3):
            use load_save_slot(number=3)
        hotspot(207, 531, 370, 407) action FileAction(4):
            use load_save_slot(number=4)
        hotspot(774, 531, 370, 407) action FileAction(5):
            use load_save_slot(number=5)
        hotspot(1341, 531, 370, 407) action FileAction(6):
            use load_save_slot(number=6)
    hbox:
        style_prefix "page"

        xalign 0.5
        yalign 0.0

        spacing gui.page_spacing

        textbutton _("<") action FilePagePrevious()

        if config.has_autosave:
            textbutton _("{#auto_page}A") action FilePage("auto")

        if config.has_quicksave:
            textbutton _("{#quick_page}Q") action FilePage("quick")

        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, 4):
            textbutton "[page]" action FilePage(page)

        textbutton _(">") action FilePageNext()

    use back_button


screen load_save_slot:
    $ file_text = "{} {}".format(
                        FileTime(number, format=_("{#file_time}%b %d %Y, %I:%M")),
                        FileSaveName(number))
    button:
        background AlphaMask(FileScreenshot(number),"gui/screens/save_load/alpha_globe.png") xalign 0.5 yalign 0.5
        add "gui/screens/save_load/frame.png" xalign 0.5 yalign 0.5
        text file_text text_align 0.5 ypos 250 xpos 65
    hbox:
        xalign 0.5
        yalign 0.85

        imagebutton:
            idle "gui/screens/save_load/delete.png"
            insensitive "gui/screens/save_load/delete_false.png"
            hover "gui/screens/save_load/delete_hover.png"
            action FileDelete(number)


screen back_button():
    textbutton "Return" action Return() xalign 0.5 yalign 0.97 text_size 40 text_color "#B4A9C2" text_hover_color "#fff"

screen preferences():
    add "gui/screens/main_menu/background.png"
    tag menu
    style_prefix "thepref"

    if renpy.variant("pc") or renpy.variant("web"):
        vbox:
            yalign 0.1
            hbox:
                if config.has_music:
                    vbox:
                        fixed:
                            fit_first True
                            add "gui/screens/poof.png"
                            textbutton _("Music Volume") action ToggleMute("music")
                        vbar value Preference("music volume")
                if config.has_sound:
                    vbox:
                        fixed:
                            fit_first True
                            add "gui/screens/poof.png"
                            textbutton _("Sound Volume") action ToggleMute("sfx")
                        vbar value Preference("sound volume")
                if config.has_voice:
                    vbox:
                        fixed:
                            fit_first True
                            add "gui/screens/poof.png"
                            textbutton _("Voice Volume") action ToggleMute("voice")
                        vbar value Preference("voice volume")
                vbox:
                    fixed:
                        fit_first True
                        add "gui/screens/poof.png"
                        text _("Auto-Forward Time")
                    vbar value Preference("auto-forward time")
                vbox:
                    fixed:
                        fit_first True
                        add "gui/screens/poof.png"
                        text "Text Speed"
                    vbar value Preference("text speed")

            vbox:
                style_prefix "prefradio"
                hbox:
                    label _("Display")
                    add "gui/divider.png"
                    hbox:
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                hbox:
                    label _("Skip")
                    add "gui/divider.png"
                    hbox:
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                hbox:
                    label _("Rollback Side")
                    add "gui/divider.png"
                    hbox:
                        textbutton _("Disable") action Preference("rollback side", "disable")
                        textbutton _("Left") action Preference("rollback side", "left")
                        textbutton _("Right") action Preference("rollback side", "right")

        use back_button








## History screen ##############################################################
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    add "gui/screens/history/scroll.png" xalign 0.5 yalign 0.5
    ## Avoid predicting this screen, as it can be very large.
    predict False
    style_prefix "history"
    vbox:
        xalign 0.5
        ypos 200
        viewport id "vpgrid":
            yinitial 1.0
            #draggable True
            mousewheel True
            xmaximum 500
            ymaximum 620
            yfill True
            vbox:

                for h in _history_list:

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

                    if h.who:
                        text "- " + h.who xalign 1.0 text_align 1.0
                    add "gui/screens/history/divider.png" xalign 0.5
                if not _history_list:
                    label _("The dialogue history is empty.")

    use back_button

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()





## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()






################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 20

            label _(message):
                style "confirm_prompt"
                xalign 0.5
            add "gui/screens/history/divider.png" xalign 0.5
            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action





## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat





## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0





## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length





################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
