import pandas as pd
import cryptpandas as crp
import strategy as strat
import submission_checker as sc
from submission_checker import get_positions

decrypted_df = crp.read_encrypted(path='encrypted_data/release_3867.crypt', password='mXTi0PZ5oL731Zqx')

print(decrypted_df)

# dump into csv
decrypted_df.to_csv('csv_data/release_3867.csv', index=False)

strategy = strat.strategy(4507)

strategy = sc.get_submission_dict(strategy)
print(strategy)

#add team name and passcode
form_name = 'https://docs.google.com/forms/d/e/1FAIpQLSeUYMkI5ce18RL2aF5C8I7mPxF7haH23VEVz7PQrvz0Do0NrQ/formResponse'
