import cryptpandas as crp

#create a list of all the encrypted data file names it updates by 64 every time and there are 77 files in total
encrypted_data_files = ["3547", "3611", "3675", "3739", "3803", "3867", "3931", "3995", "4059", "4123", "4187", "4251", "4315", "4379", "4443", "4507", "4571", "4635", "4699", "4763", "4827", "4891", "4955", "5019", "5083", "5147", "5211", "5275", "5339", "5403", "5467", "5531", "5595", "5659", "5723", "5787", "5851", "5915", "5979", "6043", "6107", "6171", "6235", "6299", "6363", "6427", "6491", "6555", "6619", "6683", "6747", "6811", "6875", "6939", "7003", "7067", "7131", "7195", "7259", "7323", "7387", "7451", "7515", "7579", "7643", "7707", "7771", "7835", "7899", "7963", "8027", "8091", "8155", "8219", "8283", "8347", "8411", "8475"]

#fetch data from slack

# decrypt all the files
file = "3547"
password = "1vA9LaAZDTEKPePs"
decrypted_df = crp.read_encrypted(path=f'encrypted_data/release_{file}.crypt', password=f'{password}')
decrypted_df.to_csv(f'csv_data/release_{file}.csv', index=False)
