import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from music_shapley import MusicShapley

# Read data
df = pd.read_excel("../analysis_results/classifier_outputs.xlsx", dtype={"track": str})

# Plot settings
bar_width=0.5
plt.style.use("my_style.mplstyle")


## ROCK TRACK ##


track_name = "010055"
stem_names = ["vocals", "eguitar", "drums", "bass"]

# Get scores

RockShapGenre1 = MusicShapley(df, track_name, "track", "coalition", "genre1_score", stem_names)
RockShapGenre2 = MusicShapley(df, track_name, "track", "coalition", "genre2_score", stem_names)
RockShapMood1 = MusicShapley(df, track_name, "track", "coalition", "mood1_score", stem_names)
RockShapMood2 = MusicShapley(df, track_name, "track", "coalition", "mood2_score", stem_names)

scores_genre = {
	"rock": [RockShapGenre1.get_shapley_val(stem) for stem in stem_names],
	"metal": [RockShapGenre2.get_shapley_val(stem) for stem in stem_names]
}

scores_mood = {
	"energetic": [RockShapMood1.get_shapley_val(stem) for stem in stem_names],
	"aggressive": [RockShapMood2.get_shapley_val(stem) for stem in stem_names]
}

# Plot

fig, axs = plt.subplots(1,2, figsize=(7,4))

y = np.arange(0, len(stem_names)*1.3, 1.3)

axs[0].barh(y=y, width=scores_genre["rock"], height=bar_width, label="rock", zorder=2)
axs[0].barh(y=y+0.5, width=scores_genre["metal"], height=bar_width, label="metal", zorder=2)
axs[0].set_yticks(y+0.25)
axs[0].set_yticklabels(stem_names)
axs[0].set_xlim(-0.6,0.6)
axs[0].set_ylim(y[0]-1, y[-1]+1.5)
axs[0].set_xlabel("Shapley Value")
axs[0].set_title("Genre", size=12)
axs[0].legend(ncol=1, loc="upper left", fontsize=7)
axs[0].invert_yaxis()

axs[1].barh(y=y, width=scores_mood["energetic"], height=bar_width, label="energetic", zorder=2)
axs[1].barh(y=y+0.5, width=scores_mood["aggressive"], height=bar_width, label="aggressive", zorder=2)
axs[1].set_yticks(y+0.25)
axs[1].set_yticklabels([])
axs[1].set_xlim(-0.6,0.6)
axs[1].set_ylim(y[0]-1, y[-1]+1.5)
axs[1].set_xlabel("Shapley Value")
axs[1].set_title("Mood", size=12)
axs[1].legend(ncol=1, loc="upper left", fontsize=7)
axs[1].invert_yaxis()

plt.savefig("fig/rock_track_stem_analysis.png", dpi=500)


## JAZZ TRACK ##


track_name = "064570"
stem_names = ["piano", "drums", "eguitar", "bass"]

# Get scores

JazzShapGenre1 = MusicShapley(df, track_name, "track", "coalition", "genre1_score", stem_names)
JazzShapMood1 = MusicShapley(df, track_name, "track", "coalition", "mood1_score", stem_names)
JazzShapMood2 = MusicShapley(df, track_name, "track", "coalition", "mood2_score", stem_names)

scores_genre = {
	"jazz": [JazzShapGenre1.get_shapley_val(stem) for stem in stem_names],
}

scores_mood = {
	"happy": [JazzShapMood1.get_shapley_val(stem) for stem in stem_names],
	"chill": [JazzShapMood2.get_shapley_val(stem) for stem in stem_names]
}

# Plot

fig, axs = plt.subplots(1,2, figsize=(7,4))

y = np.arange(0, len(stem_names)*1.3, 1.3)

axs[0].barh(y=y+0.25, width=scores_genre["jazz"], height=bar_width, label="jazz", zorder=2)
axs[0].set_yticks(y+0.25)
axs[0].set_yticklabels(stem_names)
axs[0].set_xlim(-0.6,0.6)
axs[0].set_ylim(y[0]-1, y[-1]+1.5)
axs[0].set_xlabel("Shapley Value")
axs[0].set_title("Genre", size=12)
axs[0].legend(ncol=1, loc="upper left", fontsize=7)
axs[0].invert_yaxis()

axs[1].barh(y=y, width=scores_mood["happy"], height=bar_width, label="happy", zorder=2)
axs[1].barh(y=y+0.5, width=scores_mood["chill"], height=bar_width, label="chill", zorder=2)
axs[1].set_yticks(y+0.25)
axs[1].set_yticklabels([])
axs[1].set_xlim(-0.6,0.6)
axs[1].set_ylim(y[0]-1, y[-1]+1.5)
axs[1].set_xlabel("Shapley Value")
axs[1].set_title("Mood", size=12)
axs[1].legend(ncol=1, loc="upper left", fontsize=7)
axs[1].invert_yaxis()

plt.savefig("fig/jazz_track_stem_analysis.png", dpi=500)


## MIXED TRACK ##


track_name = "027223"
stem_names = ["vocals", "drums", "piano", "eguitar", "bass"]

# Get scores

MixedShapGenre1 = MusicShapley(df, track_name, "track", "coalition", "genre1_score", stem_names)
MixedShapGenre2 = MusicShapley(df, track_name, "track", "coalition", "genre2_score", stem_names)
MixedShapMood1 = MusicShapley(df, track_name, "track", "coalition", "mood1_score", stem_names)
MixedShapMood2 = MusicShapley(df, track_name, "track", "coalition", "mood2_score", stem_names)

scores_genre = {
	"rock": [MixedShapGenre1.get_shapley_val(stem) for stem in stem_names],
	"jazz": [MixedShapGenre2.get_shapley_val(stem) for stem in stem_names]
}

scores_mood = {
	"happy": [MixedShapMood1.get_shapley_val(stem) for stem in stem_names],
	"chill": [MixedShapMood2.get_shapley_val(stem) for stem in stem_names]
}

# Plot

fig, axs = plt.subplots(1,2, figsize=(7,4))

y = np.arange(0, len(stem_names)*1.3, 1.3)

axs[0].barh(y=y, width=scores_genre["rock"], height=bar_width, label="rock", zorder=2)
axs[0].barh(y=y+0.5, width=scores_genre["jazz"], height=bar_width, label="jazz", zorder=2)
axs[0].set_yticks(y+0.25)
axs[0].set_yticklabels(stem_names)
axs[0].set_xlim(-0.6,0.6)
axs[0].set_ylim(y[0]-1, y[-1]+1.5)
axs[0].set_xlabel("Shapley Value")
axs[0].set_title("Genre", size=12)
axs[0].legend(ncol=1, loc="upper left", fontsize=7)
axs[0].invert_yaxis()

axs[1].barh(y=y, width=scores_mood["happy"], height=bar_width, label="happy", zorder=2)
axs[1].barh(y=y+0.5, width=scores_mood["chill"], height=bar_width, label="chill", zorder=2)
axs[1].set_yticks(y+0.25)
axs[1].set_yticklabels([])
axs[1].set_xlim(-0.6,0.6)
axs[1].set_ylim(y[0]-1, y[-1]+1.5)
axs[1].set_xlabel("Shapley Value")
axs[1].set_title("Mood", size=12)
axs[1].legend(ncol=1, loc="upper left", fontsize=7)
axs[1].invert_yaxis()

plt.savefig("fig/mixed_track_stem_analysis.png", dpi=500)
