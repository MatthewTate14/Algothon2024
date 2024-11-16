import pandas as pd
import cryptpandas as crp

decrypted_df = crp.read_encrypted(path='encrypted_data/release_3611.crypt', password='GMJVDf4WWzsV1hfL')

print(decrypted_df)

#dump into csv
decrypted_df.to_csv('csv_data/release_3611.csv', index=False)