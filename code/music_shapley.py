import pandas as pd
import numpy as np

class MusicShapley:
    
    def __init__(self, df: pd.DataFrame, track_name: str, track_column: str, coalition_column: str, score_column: str, stem_names: list):
        
        self.df = df
        self.track_name = track_name
        self.track_column = track_column
        self.coalition_column = coalition_column
        self.score_column = score_column
        self.stem_names = stem_names
        
        self.df_sub = df[df[track_column] == track_name]
        self.df_score = self.get_score_df()
        
    def get_score_df(self):
        """
		Returns a DataFrame that contains the scores and coalition membership
		for each stem in the given track.
		"""
        
        score_dict = {self.score_column: [], **{stem:[] for stem in self.stem_names}}
        
        for i, row in self.df_sub.iterrows():
            score_dict[self.score_column].append(row[self.score_column])
            for stem in self.stem_names:
                score_dict[stem].append(int(stem in row[self.coalition_column]))
        
        df_score = pd.DataFrame(score_dict)
        return df_score
    
    
    def get_shapley_val(self, stem_name):
        """
		Calculates the Shapley value for a given stem in the track.

		Args:
		stem_name (str): The name of the stem for which to calculate the Shapley value.

		Returns:
		shapley_val (float): The Shapley value for the given stem.
		"""

        # Get duplicate indices
        df_reduced = self.df_score.drop(columns=[self.score_column]+[stem_name])
        duplicates = df_reduced.duplicated(keep=False)
        
        index_pairs = []
        for i in range(len(df_reduced)):
            for j in range(i+1, len(df_reduced)):
                # if the rows are duplicates, add the pair of indices to the list
                if duplicates[i] and duplicates[j] and all(df_reduced.iloc[i] == df_reduced.iloc[j]):
                		index_pairs.append((i, j))
                  
        # Compare coalitions with/without stem
        diffs = []
        for (a, b) in index_pairs:
            
            with_idx = a if self.df_score[stem_name][a] == 1 else b
            without_idx = a if with_idx == b else b
            
            with_score = self.df_score.loc[with_idx][self.score_column]
            without_score = self.df_score.loc[without_idx][self.score_column]
            diffs.append(with_score - without_score)
            
        # The shapley value is the average diff
        return np.mean(diffs)
            
            
            
    
    
        
        
        