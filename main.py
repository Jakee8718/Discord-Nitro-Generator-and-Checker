from discord_webhook import DiscordWebhook
import requests
import random
import string
import time
import os
import colorama
from colorama import Fore
from colorama import init as colorama_init

class NitroGen: # Initialise the class
    def __init__(self): # The initaliseaiton function
        self.fileName = "Nitro Codes.txt" # Set the file name the codes are stored in

    def main(self): # The main function contains the most important code
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen

        print(Fore.LIGHTBLUE_EX + """

███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝ 
                                                        """ + Fore.RESET) 
        print(Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + 'Made by: daddy m') # me!
        print()
        print(Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + 'Nitro is very rare to get btw')
    
        print() 
        self.slowType(Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + 'Input How Many Codes to Generate and Check: ', .02, newLine = False) 

        num = int(input('')) # the amount of nitro codes u want

        
        self.slowType(Fore.RESET + Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + 'Do you want to use a discord webhook?', .02, newLine = True)
        self.slowType(Fore.RESET + Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + 'If so type it here or press enter if you not using a webhook: ', .02, newLine = False)
        url = input('') # if they put the webhook
        webhook = url if url != "" else None # If the url is empty make it be None insted

        print() # skip

        valid = [] # Keep track of valid codes
        invalid = 0 # Keep track of how many invalid codes was detected

        for i in range(num): # Loop over the amount of codes to check
            code = "".join(random.choices( # Generate the id for the gift
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))
            url = f"https://discord.gift/{code}" # generate it so u can nitro duh

            result = self.quickChecker(url, webhook) # checks it to make sure valid 

            if result: # If the code was valid
                valid.append(url) # Add that code to the list of found codes
            else: # If the code was not valid
                invalid += 1 # Increase the invalid counter by one

            if result and webhook is None: # check for webhook and if no webhook then brak the script
                break # End the script


        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") # Give stats
        input(Fore.RESET + Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX + "Succesfully Genertated Nitro Codes! Press Enter 5 times to close the program. Or Refresh The Page to use the gen again" + Fore.RESET) # Tell the user the program finished
        [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


    def slowType(self, text, speed, newLine = True): 
        for i in text: # Loop over the message
            print(i, end = "", flush = True) 
            time.sleep(speed)
        if newLine: 
            print() # skip

    def generator(self, amount): # stores the codes
        with open(self.fileName, "w", encoding="utf-8") as file: # load
            print("Wait, Generating for you") # ITS GENERATING OMGG

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) # Generate the code id so u can get nitro!
                file.write(f"https://discord.gift/{code}\n") # Write the code

            # Tell the user its done generating and how long tome it took
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): # Function used to check nitro codes from a file
        valid = [] # A list of the valid codes
        invalid = 0 # The amount of invalid codes detected
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

                # Create the requests url for later use
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( # sends a msg to the discord webhook saying U FOUND DAMN NITRO
                            url = notify,
                            content = f"Nitro code generated! Made by daddy m#8718 @everyone   \n{nitro}"
                        ).execute()
                    else: # if no webhook then stop
                        break 

                else: # errors
                    print(f"  Not valid | {nitro} ") # tested and invalid or valid idk
                    invalid += 1 # Increase the invalid counter by one

        return {"valid" : valid, "invaild" : invalid} # stat again

    def quickChecker(self, nitro, notify = None): # check 1 code at a time aka slow
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Valid | {nitro} ") # Notify the user the code was valid

            if notify is not None: # If a webhook has been added
                DiscordWebhook( # send a msg to the discord webhook cuz Yuh Babe
                    url = notify,
                    content = f"Nitro code generated! Made by daddy m#8718 @everyone \n{nitro}"
                ).execute()

            return True 

        else: # more errors
            print(Fore.RESET + Fore.LIGHTGREEN_EX + '[ + ] ' + Fore.RESET + Fore.LIGHTBLUE_EX +  f" Invalid | {nitro} "+Fore.RESET) 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() # Run the main code
