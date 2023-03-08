#Екран мапи
screen map:
    modal True
    add 'images/map.png'

label start:
    "Мапа світу"
    jump imeyama
    return



#Опис екранів для лейблів

screen imeyama:
    modal True
    add 'images/imeyama.jpg'
    

screen hiroki:
    modal True
    add 'images/hiroki.jpg'
    

screen kohanashi:
    modal True
    add 'images/kohanashi.jpg'
    

screen kaiyo:
    modal True
    add 'images/kaiyo.jpg'
    

screen monimori:
    modal True
    add 'images/monimori.jpg'
    

screen tensei:
    modal True
    add 'images/tensei.jpg'
    

# Лейбли переміщень (не використовувати для прописання історії) лейбли переміщення окремо
# А лейбли історії окремо

label imeyama:
    show screen imeyama with fade
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