# Кнопка карти 
init:
    $ map_mark = 0

# Відбувається перевірка на те чи відкрити чи закрита карта, карта сама зроблена слоями
# zorder відповідає за слої, оскільки карта на слой більша, отже вона відображається поверх фону

screen map_button:
    zorder 12
    if map_mark == 0:
        frame:
            textbutton "Відкрити мапу":
                action SetVariable('map_mark',1),Show('map') 
    else:
        frame:
            textbutton "Закрити мапу":
                action SetVariable('map_mark',0),Hide('map')
 
#Екран мапи
screen map:
    zorder 11
    modal True
    add '/images/map1.png' align (0.5, 0.5)

    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.6, 0.5):
        action NullAction() 



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