import pandas as pd
import cryptpandas as crp

decrypted_df = crp.read_encrypted(path='encrypted_data/release_3867.crypt', password='mXTi0PZ5oL731Zqx')

print(decrypted_df)

# dump into csv
decrypted_df.to_csv('csv_data/release_3867.csv', index=False)

def strategy():
    return 0

strategy = strategy()

#add team name and passcode
form_value = {}