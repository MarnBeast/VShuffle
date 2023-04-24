from gk.tape import *

def create_atmosfear_the_harbingers_tape():
    tape = GkTape().addLabel("TAPE: Atmosfear")
    src = tape.createSource(r'C:\Users\marti\Videos\20220204_Atmosfear： The Harbingers (4K).mp4') \
        .addLabel("SRC: The Harbingers")
    src.createClip(0, 14*60 + 50) \
        .addLabel("Instructions")
    src.createClip(14*60 + 50, 15*60 + 41) \
        .addLabel("Countdown")
    src.createClip(15*60 + 41, 15*60 + 55) \
        .addLabel("On your marks")
    src.createClip(15*60 + 55, 16*60 + 53) \
        .addLabel("Filler")
    src.createClip(16*60 + 53, 17*60 + 10) \
        .addLabel("Gatekeeper") \
        .addLabel("Cruel") \
        .addLabel("Return to start")
    src.createClip(17*60 + 10, 18*60 + 5) \
        .addLabel("Filler")
    src.createClip(18*60 + 5, 18*60 + 26) \
        .addLabel("Gatekeeper") \
        .addLabel("Generous") \
        .addLabel("Free Turns") \
        .addLabel("Cutthroat") \
        .addLabel("Interplay") \
        .addLabel("Return to start")
    src.createClip(18*60 + 26, 19*60 + 24) \
        .addLabel("Filler")
    src.createClip(19*60 + 24, 19*60 + 46) \
        .addLabel("Gatekeeper") \
        .addLabel("Cruel") \
        .addLabel("Miss a turn")
    src.createClip(19*60 + 46, 20*60 + 47) \
        .addLabel("Filler")
    
    return tape