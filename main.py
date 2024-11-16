import pandas as pd
import cryptpandas as crp

decrypted_df = crp.read_encrypted(path='encrypted_data/release_3675.crypt', password='PSI9bPh4aM3iQMuE')

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

# #dump into csv
# decrypted_df.to_csv('csv_data/release_3675.csv', index=False)