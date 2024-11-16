import pandas as pd
import cryptpandas as crp

decrypted_df = crp.read_encrypted(path='release_3547.crypt', password='oUFtGMsMEEyPCCP6')

print(decrypted_df)

#dump into csv
decrypted_df.to_csv('release_3547.csv', index=False)