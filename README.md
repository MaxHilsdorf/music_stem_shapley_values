# Music Shapley Values through Source Separation
This repository provides the code used to write the Medium article: "Making AI Music-Tagging Explainable through Source Separation".

The code in this repository cannot be used to reproduce the entire project, as the source separation and music tagging were done in a semi-manual process. This repo features all the code to
* build the coalitions from stems
* compute shapley values based on stem coalitions
* create the visualizations used in the article

The implementations of the algorithm used in this repository are inefficient and hardly reusable, as they were developed solely for the blog post. If, however, you do find something useful, that's even better.

The excel file with the analysis results for each coalition can be found in ```analysis_results/```. Here's what the code in ```code/``` does:
* ```create_coalitions.py``` uses a local file system path to combine all stems into coalitions.
* ```music_shapley.py``` implements the music stem shapley value as a simple class.
* ```compute_shapley_values.py``` can be used to get a quick shapley value analysis for one of the three example tracks.
* ```create_visualizations.py``` generates the visualizations used in the blog post.
