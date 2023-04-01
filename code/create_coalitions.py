import pydub
import os
import itertools

STEM_DIR = "E:/OneDrive/uni_work/programming/data_science/music_xai_stemming/music/stems/"
COALITION_DIR = "E:/OneDrive/uni_work/programming/data_science/music_xai_stemming/music/coalitions/"

file_names = os.listdir(STEM_DIR)

# Infer unique tracks from files
track_names = list(set([track_name.split("_")[0] for track_name in file_names]))

# Retrieve sources for all tracks
track_sources = {t:[] for t in track_names}
for file_name in file_names:
    t = file_name.split("_")[0]
    s = file_name.split("_")[-1].split(".")[0]
    track_sources[t].append(s)
    
# Generate all possible coalitions (in list form) for each track
track_coalitions = {t:[] for t in track_names}
for track_name, sources in track_sources.items():
    for i in range(1, len(sources) + 1):
        for combination in itertools.combinations(sources, i):
            track_coalitions[track_name].append(combination)

# Transform each coalition to an audio file and export it
for track_name, coalitions in track_coalitions.items():
    
    for coalition in coalitions:
        coalition_name = f"{track_name}_{coalition[0]}"
        base_audio = pydub.AudioSegment.from_mp3(f"{STEM_DIR}{track_name}_{coalition[0]}.mp3")
        if len(coalition) > 1:
            for source in list(coalition)[1:]:
                additional_audio = pydub.AudioSegment.from_mp3(f"{STEM_DIR}{track_name}_{source}.mp3")
                base_audio = base_audio.overlay(additional_audio)
                coalition_name += f"_{source}"
        coalition_name += ".mp3"
        base_audio.export(COALITION_DIR+coalition_name)
    
