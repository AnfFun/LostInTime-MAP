# Кнопка карти 
init:
    $ map_mark = 0

screen map_button:
    zorder 12
    if map_mark == 0:
        textbutton "Відкрити мапу" action SetVariable('map_mark',1),Show('map')
    else:
        textbutton "Закрити мапу" action SetVariable('map_mark',0),Hide('map')
 
#Екран мапи
screen map:
    zorder 11
    modal True
    add '/images/map.png'



label start:
    "Мапа світу"
    show screen map_button
    jump imeyama
    return



#Опис екранів для лейблів

screen imeyama:
    zorder 10
    modal True
    add '/images/imeyama.jpg'
    

screen hiroki:
    zorder 10
    modal True
    add '/images/hiroki.jpg'
    

screen kohanashi:
    zorder 10
    modal True
    add '/images/kohanashi.jpg'
    

screen kaiyo:
    zorder 10
    modal True
    add '/images/kaiyo.jpg'
    

screen monimori:
    zorder 10
    modal True
    add '/images/monimori.jpg'
    

screen tensei:
    zorder 10
    modal True
    add '/images/tensei.jpg'
    

# Лейбли переміщень (не використовувати для прописання історії) лейбли переміщення окремо
# А лейбли історії окремо

label imeyama:
    show screen imeyama 
    window hide
    pause

label hiroki:
    show screen hiroki with fade
    pause

label kaiyo:
    show screen kaiyo with fade
    pause

label kohanashi:
    show screen kohanashi with fade
    pause

label monimori:
    show screen monimori with fade
    pause

label tensei:
    show screen tensei with fade
    pause