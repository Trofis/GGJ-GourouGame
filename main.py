import gs
import gs.plus.render as render
import gs.plus.input as input

x =["@data/place_desert.png", '@data/place_espace.png', '@data/place_montagne.png','@data/chat.jpg','@data/phoque.jpg','@data/phoque2.jpg' ]
y =['Il fait chaud !', 'Ohh il fait beau', 'On va faire du ski ?', 'Ohh le chattt', 'Trop mignon le phoque', 'ohh je préfère celui-ci']

gs.LoadPlugins(gs.get_default_plugins_path())
class main(object):
    def __init__(self, images, phrases):
        self.listeImage = images
        self.phrases = phrases
        self.ImgPhr = []
        self.phase = 0
        self.listeImageAffich = []
        render.init(1920, 1080, "pkg.core")
        gs.MountFileDriver(gs.StdFileDriver("assets"),'@data')

    # def distriImages(self):
    #     for i in range(3):
    #         self.listeImageAffich = getImages() [(self.phase*3)+i]

    def getImages(self):
        return self.listeImage

    def getCommentaire(self):
        return self.phrases

    def AssocieImgPhr(self):
        for i in range(3):
            print((self.phase*3)+i)
            j = self.phase*3 + i
            self.ImgPhr.append({'img': self.getImages()[j], 'phrase': self.getCommentaire()[j]})

    def getImgPhr(self):
        return self.ImgPhr

    def afficheTexte(self):
        render.text2(400, 540, "Cest rigolo python")


    def afficheImage(self, x, y ,i, echelle):
        render.image2d(x,y,echelle,self.getImgPhr() [i] ['img'])


if __name__ == "__main__":
    o = main(x,y)
    o.AssocieImgPhr()
    indexDecor = -1
    indexEntrer = -1
    entrer = False
    o.phase = 0
    while not input.key_press(gs.InputDevice.KeyEscape):
        render.clear()
        if input.key_press(gs.InputDevice.KeyLeft):
            indexDecor-=1

        if input.key_press(gs.InputDevice.KeyRight):
            indexDecor +=1
        if indexDecor >= 0 and indexDecor < len(o.getImgPhr()):
            o.afficheImage(1000,300, indexDecor, 0.5)

        if input.key_press(gs.InputDevice.KeyEnter):
            entrer = True
            indexEntrer = indexDecor
        if entrer:
            o.phase += 1
            for i in range (o.phase+1):
                o.afficheImage(300,200, indexEntrer, 1)

            o.ImgPhr = []
            o.AssocieImgPhr()
            entrer = False
        render.flip()
