import gs
import gs.plus.render as render
import gs.plus.input as input
import gs.plus.audio as audio
from gs.plus import *


phases = [
        [{'img': "@data/place_desert.png", 'phrase': 'Il fait chaud !'},
           {'img': '@data/place_espace.png', 'phrase': 'Ohh il fait beau'},
           {'img': '@data/place_montagne.png', 'phrase': 'On va faire du ski ?'}],
        [{'img': '@data/chat.jpg', 'phrase': 'Ohh le chattt'},
             {'img': '@data/phoque.jpg', 'phrase': 'Trop mignon le phoque'},
             {'img': '@data/phoque2.jpg', 'phrase': 'ohh je préfère celui-ci'}],
        [{'img': '@data/soleil.jpg', 'phrase': 'Il fait beau'},
         {'img': '@data/Pluie.jpg', 'phrase': 'Ohh mince il pleut'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'Après la pluie le beau temps'}]
    ]

gs.LoadPlugins(gs.get_default_plugins_path())
render.init(1920, 1080, "pkg.core")
gs.MountFileDriver(gs.StdFileDriver("assets"), '@data')

audio.init()
sound = audio.get_mixer().Stream("@data/haters.ogg")

def main ():
    intro()
    gourou = selection()
    generation(gourou)


def intro():
    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear()
        afficheTexte(500, 400,'Quel est ton gourou')
        afficheTexte(500, 300,'Choisis le sens de ta vie')
        render.flip()
    # render.flip()

    while input.key_press(gs.InputDevice.KeyEnter):
        render.clear()
        render.flip()

def getImgParPha(phases):
    return len(phases[0])


def getImg(phases, phase, phrase_courante):
    return phases[phase][phrase_courante]['img']


def getTxt(phases, phase, phrase_courante):
    return phases[phase][phrase_courante]['phrase']


def selection():
    Gourou = []
    indexDecor = 0
    indexEntrer = -1
    entrer = False
    indexImg = {}
    for phase in range(len(phases)):

        while not input.key_press(gs.InputDevice.KeyEnter):
            render.clear()
            if input.key_press(gs.InputDevice.KeyLeft) and indexDecor > 0:
                indexDecor = (indexDecor - 1)%getImgParPha(phases)

            if input.key_press(gs.InputDevice.KeyRight) and indexDecor < getImgParPha(phases)-1:
                indexDecor = (indexDecor + 1)%getImgParPha(phases)

            if indexDecor >= 0:
                afficheImage(1200, 300, phase, 0.5, indexDecor)
                afficheTexte(1200, 200, getTxt(phases, phase, indexDecor))

            if input.key_press(gs.InputDevice.KeyEnter):
                entrer = True
                indexEntrer = indexDecor
                Gourou.append(getTxt(phases, phase, indexDecor))
            if entrer:
                indexImg[phase] = indexEntrer
                entrer = False

            if phase > 0:
                for index in range(len(indexImg)):
                    if index != 2:
                        afficheImage(100+(600*(index)), 400, index , 0.6, indexImg[index])
                    else:
                        afficheImage(450, 100, index , 0.6, indexImg[index])

            render.flip()
        render.flip()

    return Gourou

def afficheTexte(x, y, texte):
    # Ugly patch, waiting for a fix of the font kerning ^__^;
    for c in texte:
        render.text2d(x, y, c, 30, gs.Color.White, '@data/monof55.ttf')
        if c == ' ':
            x += 5
        else:
            x += 15


def afficheImage(x, y ,phase, echelle, phraseCourante):
        render.image2d(x,y,echelle,getImg(phases, phase, phraseCourante) )


def generation(gourou):
    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear()
        afficheTexte(1000, 500, 'Voyons désormais quel est votre Gourou ....')
        render.image2d(200,250,0.7,'@data/Guru.jpg' )
        render.flip()
    # render.flip()

    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear()
        afficheTexte(1000, 500, 'lol')
        render.image2d(200,250,0.7,'@data/Guru.jpg' )
        render.flip()
    # render.flip()

main()
