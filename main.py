import gs
import gs.plus.geometry as geometry
import gs.plus.render as render
import gs.plus.input as input
import gs.plus.audio as audio
import gs.plus.clock as clock
from gs.plus import *
import random


SCREEN_W = 1920
SCREEN_H = 1080

dt_text_scroll = 0.0

phases = [
        [[{'img': '@data/montagne.png', 'phrase': 'sous la neige'},
         {'img': '@data/foret.png', 'phrase': "sous les chênes"},
         {'img': "@data/mer.png", 'phrase': ' sous les cocos '}]
           ],
        [  [ {'img': '@data/montagne_plus_groupedanimaux.png', 'phrase': 'chat'},
            {'img': '@data/montagne_plus_halucination.png', 'phrase': 'phoque'},
            {'img': '@data/montagne_plus_groupedhumains.png', 'phrase': 'phoque'}],
            [{'img': '@data/foret_plus_groupedanimaux.png', 'phrase': 'phoque'},
            {'img': '@data/foret_plus_hallucination.png', 'phrase': 'phoque'},
            {'img': '@data/foret_plus_groupedhumains.png', 'phrase': 'phoque'}],
            [{'img': '@data/mer_plus_groupedanimaux.png', 'phrase': 'phoque'},
            {'img': '@data/mer_plus_hallucination.png', 'phrase': 'phoque'},
            {'img': '@data/mer_plus_groupedhumains.png', 'phrase': 'phoque'}]],
        [[{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
         [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
         [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
         [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
         [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
         [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
        [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
        [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
        [{'img': '@data/soleil.jpg', 'phrase': 'ce beau soleil'},
         {'img': '@data/Pluie.jpg', 'phrase': 'celle belle averse'},
         {'img': '@data/arcEnCiel.jpg', 'phrase': 'ce beau arc-en-ciel'}],
    ]]

gs.LoadPlugins(gs.get_default_plugins_path())
render.init(SCREEN_W, SCREEN_H, "pkg.core")
gs.MountFileDriver(gs.StdFileDriver("assets"), '@data')
gs.MountFileDriver(gs.StdFileDriver("pkg.core"), "@core")

def musique():
    global sound
    audio.init()
    sound = audio.get_mixer().Stream("@data/haters.ogg")


def joue_sfx_selection():
    audio.get_mixer().Stream("@data/sfx_select_" + str(random.randint(0,5)) + ".wav")

def joue_sfx_phase():
    audio.get_mixer().Stream("@data/sfx_phase_" + str(random.randint(0,4)) + ".wav")

def main ():
    global cube, angle
    musique()
    intro()
    angle = 0
    cube = render.create_geometry(geometry.create_cone(subdiv_x=4))
    gourou = selection()
    generation(gourou)
    audio.get_mixer().Stop(sound)
    final()


# Cette fonction peut être appelée de partout
# Elle utilise une variable globale (paaas bien)
# A appeler juste après le render clear.
def dessine_fond_qui_scroll():
    global dt_text_scroll
    dt_text_scroll += clock.update()
    dt_text_scroll %= 1.0
    for i in range(20):
        j = i + dt_text_scroll
        afficheTexte(j * -10.0, j * 50, '~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ~   ', 0.15)


def intro():
    text_blink = 0.0
    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear(gs.Color.White)
        text_blink += clock.update()
        if text_blink > 1.0:
            text_blink = 0.0

        # Effet de background animé à la "Street Fighter" (hem)
        # dessine_fond_qui_scroll()

        afficheTexte(500, 400, 'Quel est ton gourou ?', size = 2)
        afficheTexte(500, 365, 'Choisis le sens de ta vie ~~~~~~~~~~~~~~')
        afficheTexte(500, 325, '...et appuie sur [enter]', text_blink)
        render.flip()


    while input.key_press(gs.InputDevice.KeyEnter):
        render.clear()
        render.flip()

def getImgParPha(phases):
    return len(phases[0] [0])


def getImg(phases, phase,jeuCarte, phrase_courante):
    return phases[phase] [jeuCarte] [phrase_courante]['img']


def getTxt(phases, phase,jeuCarte, phrase_courante):
    return phases[phase] [jeuCarte] [phrase_courante]['phrase']


def selection():
    global indexImg
    Gourou = []
    indexDecor = 0
    indexEntrer = -1
    amplitude = 1
    indexImg = {}
    for phase in range(len(phases)):

        joue_sfx_phase()
        entrer = False
        angle = 0

        while not entrer:
            render.clear(gs.Color.White)
            # dessine_fond_qui_scroll()

            if input.key_press(gs.InputDevice.KeyLeft) and indexDecor > 0:
                indexDecor = (indexDecor - 1)%getImgParPha(phases)
                joue_sfx_selection()
                amplitude = 1

            if input.key_press(gs.InputDevice.KeyRight) and indexDecor < getImgParPha(phases)-1:
                indexDecor = (indexDecor + 1)%getImgParPha(phases)
                joue_sfx_selection()
                amplitude = 1

            if indexDecor >= 0:
                # render.geometry2d(100, 100, cube, angle, angle * 2, 0, 100)
                amplitude *= 0.95

            yOffSet = [0,0,0]*3**phase

            print(indexDecor)
            render.set_blend_mode2d(1)
            afficheImageNot(430, 165 + 25,  1, '@data/ornement_gauche.png')
            afficheImageNot(1090, 165 + 25,  1, '@data/ornement_droite.png')
            render.set_blend_mode2d(0)
            if phase == 0:
                yOffSet [indexDecor] = random.randint(-5,5)
                afficheImage((SCREEN_W-1050)/2, 285+random.randint(-25,25)*amplitude, phase, 1.0, indexDecor, 0)
                afficheTexte(800, 220 + 25, 'OÙ VEUX TU TE RETIRER ?', size=0.85)
                render.set_blend_mode2d(1)
                afficheImageNot(600, 50,  1, '@data/choix_paysage.png')
                render.set_blend_mode2d(0)
                afficheTexte(600, 25+yOffSet[0], getTxt(phases, phase,0, 0))
                afficheTexte(830, 25+yOffSet[1], getTxt(phases, phase,0, 1))
                afficheTexte(1100, 25+yOffSet[2], getTxt(phases, phase,0, 2))

            elif phase == 1:
                yOffSet [indexDecor*indexImg[phase-1]] = random.randint(-5,5)
                afficheImage((SCREEN_W-1050)/2, 285+random.randint(-25,25)*amplitude, phase, 1.0, indexDecor,indexImg[phase-1] )
                afficheTexte(750, 220 + 25, 'CHOISIS UNE AMBIANCE MYSTIQUE', size=0.85)
                render.set_blend_mode2d(1)
                afficheImageNot(600, 50,  1, '@data/choix_ambiance.png')
                render.set_blend_mode2d(0)
                print(indexImg)
                afficheTexte(670, 25+yOffSet[0+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1], indexDecor))
                afficheTexte(900, 25+yOffSet[1+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1],indexDecor))
                afficheTexte(1180, 25+yOffSet[2+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1], indexDecor))

            else:
                yOffSet [indexDecor*indexImg[phase-1]] = random.randint(-5,5)
                afficheImage((SCREEN_W-1050)/2, 285+random.randint(-25,25)*amplitude, phase, 1.0, indexDecor, indexImg[phase-1])
                afficheTexte(700, 220 + 25, 'CHOISIS UN TRUC A OBSERVER', size=0.85)
                render.set_blend_mode2d(1)
                afficheImageNot(600, 50,  1, '@data/choix_paysage.png')
                render.set_blend_mode2d(0)
                afficheTexte(670, 25+yOffSet[0+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1], indexDecor))
                afficheTexte(900, 25+yOffSet[1+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1],indexDecor))
                afficheTexte(1180, 25+yOffSet[2+(indexImg[phase-1])*3], getTxt(phases, phase, indexImg[phase-1], indexDecor))
            angle += 0.01
            if input.key_press(gs.InputDevice.KeyEnter):

                entrer = True
                indexEntrer = indexDecor
                if phase ==0:
                    Gourou.append(getTxt(phases, phase, 0, indexDecor))
                else:
                    Gourou.append(getTxt(phases, phase, indexImg[phase-1], indexDecor))

            if entrer:
                indexImg[phase] = indexEntrer


            # if phase > 0:
            #     for index in range(len(indexImg)):
            #         if index != 2:
            #             render.set_blend_mode2d(1)
            #             afficheImage(100+(600*(index)), 400, index , 0.6, indexImg[index])
            #             render.set_blend_mode2d(0)
            #         else:
            #             render.set_blend_mode2d(1)
            #             afficheImage(450, 100, index , 0.6, indexImg[index])
            #             render.set_blend_mode2d(0)

            render.flip()
        render.flip()

        # prochaine phase, on joue un son de "selection"
        joue_sfx_selection()

    return Gourou

def afficheTexte(x, y, texte, transparence = 1.0, size = 1.0):
    # Ugly patch, waiting for a fix of the font kerning ^__^;
    for c in texte:
        if c == ' ':
            x += 5 * size
        else:
            render.text2d(x, y, c, 30 * size, gs.Color(35/255, 40/255, 114/255, 1.0), '@data/monof55.ttf')
            x += 15 * size


def afficheImage(x, y ,phase, echelle, phraseCourante, jeuCarte):
    render.image2d(x,y,echelle,getImg(phases, phase,jeuCarte, phraseCourante) )

def afficheImageNot(x, y, echelle, lien):
    render.image2d(x,y,echelle,lien )


def generation(gourou):
    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear(gs.Color.White)
        # dessine_fond_qui_scroll()

        afficheTexte(800, 500, 'Voyons désormais quel est votre Gourou ....')
        render.image2d(200,250,0.7,'@data/Guru.jpg' )
        render.flip()
    render.flip()

    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear(gs.Color.White)
        # dessine_fond_qui_scroll()
        afficheTexte(1000, 500, 'Il était un fois dans'+str(getTxt(phases,0,0 ,indexImg[0])))
        afficheTexte(1050, 400, 'Un petit '+str(getTxt(phases,1,indexImg[0],indexImg[1])))
        afficheTexte(1100, 300, 'Qui regarda '+str(getTxt(phases,2,indexImg[1], indexImg[2] )))
        render.image2d(200,250,0.7,'@data/Guru.jpg' )
        render.flip()
    render.flip()


def final():

    while not input.key_press(gs.InputDevice.KeyEnter):
        render.clear()


        # initialize graphic and audio systems

        movie = gs.WebMMovie()
        movie.Open("@data/thriftShop.webm")

        video_format = movie.GetVideoData().GetFormat()

        # create the frame textures and frame object
        gpu = render.get_renderer()
        y_tex = gpu.NewTexture()
        gpu.CreateTexture(y_tex, video_format.width, video_format.height, gs.GpuTexture.R8, gs.GpuTexture.NoAA, gs.GpuTexture.UsageDefault, False)
        u_tex = gpu.NewTexture()
        gpu.CreateTexture(u_tex, video_format.width // 2, video_format.height // 2, gs.GpuTexture.R8, gs.GpuTexture.NoAA, gs.GpuTexture.UsageDefault, False)
        v_tex = gpu.NewTexture()
        gpu.CreateTexture(v_tex, video_format.width // 2, video_format.height // 2, gs.GpuTexture.R8, gs.GpuTexture.NoAA, gs.GpuTexture.UsageDefault, False)

        frame = gs.VideoFrame()
        video_format.ClearFrame(frame)
        video_timestamp = gs.time(0)  # assume first frame time stamp is 0

        # load the YV12 to RGB shader and setup drawing states
        shader = gpu.LoadShader("@data/yv12.isl")

        gpu.EnableDepthTest(False)  # disable depth testing so that we don't even need to clear the z-buffer

        # start streaming the movie audio data
        channel = audio.get_mixer().StreamData(movie.GetAudioData())

        # play until movie ends
        while not movie.IsEOF():
            render.clear()
            # fit the while output window
            screen_size = gpu.GetCurrentOutputWindow().GetSize()
            gpu.SetViewport(gs.fRect(0, 0, screen_size.x, screen_size.y))
            gpu.Set2DMatrices()  # update the 2d matrix

            # fetch the next video frame once audio gets past video
            audio_timestamp = audio.get_mixer().GetChannelPosition(channel)  # audio timestamp as reported by the mixer

            if audio_timestamp >= video_timestamp:
                movie.GetVideoData().GetFrame(frame)
                video_timestamp = frame.GetTimestamp()
                gpu.BlitTexture(y_tex, frame.GetPlaneData(gs.VideoFrame.Y), video_format.width, video_format.height)
                gpu.BlitTexture(u_tex, frame.GetPlaneData(gs.VideoFrame.U), video_format.width // 2, video_format.height // 2)
                gpu.BlitTexture(v_tex, frame.GetPlaneData(gs.VideoFrame.V), video_format.width // 2, video_format.height // 2)

                # draw the current video frame to screen
                vtxs = [gs.Vector3(0, 0, 0.5), gs.Vector3(0, screen_size.y, 0.5), gs.Vector3(screen_size.x, screen_size.y, 0.5), gs.Vector3(0, 0, 0.5), gs.Vector3(screen_size.x, screen_size.y, 0.5), gs.Vector3(screen_size.x, 0, 0.5)]
                uvs = [gs.Vector2(0, 1), gs.Vector2(0, 0), gs.Vector2(1, 0), gs.Vector2(0, 1), gs.Vector2(1, 0), gs.Vector2(1, 1)]
            render_system = render.get_render_system()
            gpu.SetShader(shader)
            gs.SetShaderEngineValues(render_system)
            gpu.SetShaderTexture("y_tex", y_tex)
            gpu.SetShaderTexture("u_tex", u_tex)
            gpu.SetShaderTexture("v_tex", v_tex)
            render_system.DrawTriangleUV(2, vtxs, uvs)
            render.flip()
        render.flip()
    render.flip()


main()
