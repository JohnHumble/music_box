from synthesizer import Player, Synthesizer, Waveform
from Notes import Notes

import random


def digitalChime ():
    player = Player()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=0.1, use_osc2=False)
    player.open_stream()

    #find base note
    base = random.randint(1,6)
    time = random.randint(1,4)*0.25

    octive = 1
    sig = 3

    #play this many notes
    for i in range(0,400):
        next = random.randint(1,6)

        print('|  ',end='')


        if i % sig == 0:
            base = random.randint(1,6)
            if base == 1:
                base = Notes['C4']
                print('Cv ',end='♪ ')
            elif base == 2:
                base = Notes['D4']
                print('Dv ',end='♪ ')
            elif base == 3:
                base = Notes['F4']
                print('Fv ',end='♪ ')
            elif base == 4:
                base = Notes['G4']
                print('Gv ',end='♪ ')
            elif base == 5:
                base = Notes['A4']
                print('Av ',end='♪ ')
            else:
                base = Notes['C5']
                print('C  ',end='♪ ')
            base = (base / 2) * octive
        else:
            print('"  ',end='♫ ')

        if next == 1:
            next = Notes['C4']
            print('C  ',end='')
        elif next == 2:
            next = Notes['D4']
            print('D  ',end='')
        elif next == 3:
            next = Notes['F4']
            print('F  ',end='')
        elif next == 4:
            next = Notes['G4']
            print('G  ',end='')
        elif next == 5:
            next = Notes['A4']
            print('A  ',end='')
        else:
            next = Notes['C5']
            print('C^ ',end='')

        if i % (int)(20 / time) == 0:
            print(' | ',end='♫ ')
            sig = random.randint(2,8)
            time = random.randint(2,10)*0.125
            octive = random.randint(0,2)
            if octive == 0:
                octive = 0.5
            elif octive < 0:
                octive = 0.25
            print(octive * 4,end=' ♪ ')
            print(time,end=' ♪\n')
        else:
            print(' |')

        next *= octive
        chord = [next,base]

        #print(octive)
        #print(time)

        player.play_wave(synthesizer.generate_chord(chord,time))
        # player.play_wave(synthesizer.generate_constant_wave(next,0.5))

if __name__ == "__main__": digitalChime()