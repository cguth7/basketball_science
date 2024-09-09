import pandas as pd
from nba_api.stats.endpoints import leagueleaders
import os

def calculate_trueshooting(row: pd.Series) -> float:
    if row['FGA'] == 0:
        print("hi")
        return None
    else:
        return row['PTS'] / (2 * (row['FGA'] + 0.44 * row['FTA']))
    

def calculate_fgadd(row, league_average: float) -> float:
    #true shoot add is the players true shooting multiplied by possesions, I don't quite know the difference. 
    if row['TS%'] == None:
        return None
    else:
        return (row['TS%']-league_average) * (row['FGA'] * 2 + row['FTA'])
    

def get_league_leaders(season) -> pd.DataFrame:
    df = leagueleaders.LeagueLeaders(season=season).get_data_frames()[0]
    return df


# # Get the list of files in the data league leaders folder
# folder_path = "data/league_leaders"
# file_list = os.listdir(folder_path)

# # Iterate over each file
# for file_name in file_list:
#     # Extract the year from the file name
#     year = file_name.split(".")[0]
    
#     # Read the file as a data frame
#     file_path = os.path.join(folder_path, file_name)
#     df_year = pd.read_csv(file_path)
    
#     # Add the season column to the data frame
#     df_year["Season"] = year
    
#     # save over the file
#     df_year.to_csv(file_path, index=False)
