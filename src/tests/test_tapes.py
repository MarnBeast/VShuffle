from gk.tapes.atmosfear import *
from moviepy.editor import VideoFileClip, CompositeVideoClip

CROSSFADE_SEC = 1

tape = create_atmosfear_the_harbingers_tape()

for_test_div_time = 2   # make everything this many times shorter
timeline_sec = 0

source_dict = {}
for gksource in tape._m_sources:
    source_dict[gksource] = VideoFileClip(gksource._m_path)

clips = []
for gkclip in tape._m_clips:
    if "Gatekeeper" in gkclip._m_labels:
        source = source_dict[gkclip._m_source]
        clip = source.subclip(gkclip._m_start_sec, gkclip._m_start_sec + (gkclip._m_end_sec-gkclip._m_start_sec)/for_test_div_time)
        print("timeline_sec " + str(timeline_sec))
        if(len(clips) > 0):
            print("NEXT")
            clip = clip.set_start(timeline_sec/for_test_div_time - CROSSFADE_SEC) \
                .crossfadein(CROSSFADE_SEC)
            timeline_sec += clip.duration - CROSSFADE_SEC
        else:
            timeline_sec += clip.duration
        clip = clip.crossfadeout(CROSSFADE_SEC)
        clips.append(clip)

final = CompositeVideoClip(clips)
final.audio.fps = final.fps

final.preview()
#final.write_videofile("testfile.mp4")