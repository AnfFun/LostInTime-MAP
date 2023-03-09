# Кнопка карти 
init:
    $ map_mark = 0

# Відбувається перевірка на те чи відкрити чи закрита карта, карта сама зроблена слоями
# zorder відповідає за слої, оскільки карта на слой більша, отже вона відображається поверх фону

screen map_button:
    zorder 12
    if map_mark == 0:
        frame:
            imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.5, 0.5):
                action SetVariable('map_mark',1),Show('map') 
    else:
        frame:
            imagebutton auto '/images/map_icon_%s.png'  align (0.5, 0.5):
                action SetVariable('map_mark',0),Hide('map')  
 
# Екран мапи
screen map:
    zorder 11
    modal True
    add '/images/map.png' align (0.5, 0.5)

# Іконки переміщення
    
    #Тенсей
    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.70, 0.73):
        action Jump ("tensei")
    # Імеяма
    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.61, 0.33):
        action Jump("imeyama")
    # Коханаши
    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.77, 0.16):
        action Jump ("kohanashi")
    # Ліс
    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.28, 0.75):
        action Jump("hiroki")
    # Моніморі
    imagebutton auto '/images/map_icon_%s.png' focus_mask(True) align (0.28, 0.25):
        action Jump ("monimori")

#   Стартовий Лейбл

label start:
    "Мапа світу"
    show screen map_button 
    scene black with dissolve 
    pause
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

# Хайдимо скріни аби гра не зупинялась

label map_tp:
    hide screen imeyama
    hide screen hiroki
    hide screen kohanashi
    hide screen monimori
    hide screen tensei
    return

# Лейбли переміщень (не використовувати для прописання історії) лейбли переміщення окремо
# А лейбли історії окремо

label imeyama:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen imeyama with dissolve
    window hide
    pause

label hiroki:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen hiroki with dissolve
    pause

label kaiyo:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen kaiyo with dissolve
    pause

label kohanashi:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen kohanashi with dissolve
    pause

label monimori:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen monimori with dissolve
    pause

label tensei:
    call map_tp
    $ map_mark = 0
    hide screen map
    show screen tensei with dissolve
    pause