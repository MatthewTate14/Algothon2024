import cryptpandas as crp

#create a list of all the encrypted data file names it updates by 64 every time and there are 77 files in total
encrypted_data_files = ["3547", "3611", "3675", "3739", "3803", "3867", "3931", "3995", "4059", "4123", "4187", "4251", "4315", "4379", "4443", "4507", "4571", "4635", "4699", "4763", "4827", "4891", "4955", "5019", "5083", "5147", "5211", "5275", "5339", "5403", "5467", "5531", "5595", "5659", "5723", "5787", "5851", "5915", "5979", "6043", "6107", "6171", "6235", "6299", "6363", "6427", "6491", "6555", "6619", "6683", "6747", "6811", "6875", "6939", "7003", "7067", "7131", "7195", "7259", "7323", "7387", "7451", "7515", "7579", "7643", "7707", "7771", "7835", "7899", "7963", "8027", "8091", "8155", "8219", "8283", "8347", "8411", "8475"]

import requests
import schedule
import time
import logging

def fetch_messages():
    # Store conversation history
    conversation_history = []
    # ID of the channel you want to send the message to
    channel_id = "C080P6M4DKL"
    #user Joe: U080GCRATP1
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    # write code to get converstaion history

    # Get the URL
    url = f"https://slack.com/api/conversations.history?channel=C080P6M4DKL&pretty=1"
    # Set the headers
    headers = {
    }
    # Make the request
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Get the JSON response
        data = response.json()
        # Get the messages
        messages = data["messages"]
        # Store the messages in the conversation_history list
        conversation_history.extend(messages)
        # find messages by joe and print the most recent message with passcode
        for message in conversation_history:
            if message.get("user") == "U080GCRATP1":
                text = message.get("text")
                if "passcode" in text:
                    passcode_line = text
                    break
        print(passcode_line)
        # Output: Data has just been released 'release_4187.crypt' the passcode is 'InhVD4qy1Vmbpl5c'. Please make a forecast. [Internal Check: 2024-11-16 14:12]
        # extract passcode from this
        passcode = passcode_line.split("is ")[1].split(".")[0][1:-1]
        #extract the file name
        file = passcode_line.split("release_")[1].split(".")[0]
        print(passcode, file)
        decrypted_df = crp.read_encrypted(path=f'encrypted_data/release_{file}.crypt', password=f'{passcode}')
        decrypted_df.to_csv(f'csv_data/release_{file}.csv', index=False)

    else:
        # Log the error
        logging.error(f"Failed to fetch messages: {response.text}")


# Schedule the task every 19 minutes run it once before the first 19 minutes
fetch_messages()
schedule.every(19).minutes.do(fetch_messages)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
