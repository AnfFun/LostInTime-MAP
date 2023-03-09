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