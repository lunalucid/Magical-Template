## Magical Template
<span style="color:red">FREE VERSION</span>
[![Creative Commons Attribution Non-Commercial](https://i.creativecommons.org/l/by-nc/4.0/88x31.png "CC BY-NC License")](https://creativecommons.org/licenses/by-nc/4.0/)


This is a fully coded GUI template for Ren'Py.  
- If you use this template as a base for your game or borrow any GUI elements or code, please give attribution to [LunaLucid](https://lunalucid.itch.io/).
- Please refer to further licensing information regarding additional assets inside the folder. If you keep any fonts, art, or music included in this package, please follow licensing requirements for each.
- You may not redistribute or resell this template.


Animations/theme elements are located in **theme_stuff.rpy**

#### Menu Choices
![Choice Menu](https://img.itch.zone/aW1hZ2UvNTA5Nzg5LzI2NDYwMDQucG5n/347x500/BbaiTn.png)  
If you'd like to use images in your menu choices similar to the game's example, you can link the image inside the choice string:
```python
image image_1 = "images/example_1.png"
image image_2 = "images/example_2.png"
```

```python
menu:
    "Option 1{image=image_1}":
        # do something
    "Option 2{image=image_2}":
        # do something
```

#### Applying Existing Animations
You can place the animations for the menus in other areas as you build more of your game.
###### References:
- **twinkle** - *composite of random twinkling, rotating stars*
- **vial** - *random color changing potion vial with bubbles and sparkles*
- **vial_hover** - *vial with black potion and sparkles*
- **empty_vial** - *an empty vial*
- **star_choice** - *a single twinkling star used as a bullet point*
- **floating_crystal_ball** - *crystal ball that goes up and down*
- **ball_shadow_animation** - *oval shadow shape that grows and shrinks to match the floating crystal ball*

###### In screens
```python
add "twinkle"
```
###### In dialogue
```python
show twinkle
```
