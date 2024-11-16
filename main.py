import pandas as pd
import cryptpandas as crp

decrypted_df = crp.read_encrypted(path='encrypted_data/release_3739.crypt', password='1vA9LaAZDTEKPePs')

print(decrypted_df)

def get_positions():
    #TODO
    return 0

#write the function to get the submission dictionary
def get_submission_dict(pos_dict, your_team_name: str = "2.5 Asians", your_team_passcode: str =
"tate"):
    return {
        **get_positions().to_dict(),
        **{
            "team_name": your_team_name,
            "passcode": your_team_passcode,
        },
    }

# {'strat_12': 0.1, 'strat_6': -0.1, 'strat_8': 0.1, 'strat_5': 0.1, 'strat_21': 0.1, 'strat_2': -0.1, 'strat_18': -0.1, 'strat_20': -0.1, 'strat_1': -0.1, 'strat_22': 0.1, 'team_name': '2.5 Asians', 'passcode': 'tate'}

# dump into csv
decrypted_df.to_csv('csv_data/release_3739.csv', index=False)