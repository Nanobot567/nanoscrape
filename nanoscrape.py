# nanoscrape 1.4
# by nanobot567
# started work on april 7, 2021


try:
    print("Importing assets...")
    import requests
    print("Done!\n")
except:
    print("Import failed, downloading required assets from pip...")
    try:
        try:
            from pip._internal import main as _pip_main
        except ImportError:
            from pip import main as _pip_main

        _pip_main(["install", "requests"])
    except:
        print("You do not have pip installed! Please download it before you run this program.")
        quit()



ans = ""




def menu():
    print("""

1. Download from a discord link (insert extension)
2. Download from a discord link (detect extension)
3. Download from a direct download link
4. Show this menu
5. Quit 


""")


def disLinkExt():
    x = ""
    x = input("Please paste the link here or type 'cancel' to cancel: ")
    if "https://" in x:
        
        url = x
        try:
            r = requests.get(url)
            m = input("What is the file extension (.zip, .exe, etc.)? ")
            if "." in m:
                ext = m
                l = input("Where would you like this to be stored (please put double backslashes like C:\\\\ if you are on windows)? ")
                path = l
                s = input("What is this file going to be called (without extension)? ")
                name = s
                print("Alright, downloading...")
                try:
                    with open(f'{path}{name}{ext}', 'wb') as f:
                        f.write(r.content)

                    print(f"status_code: {r.status_code}")
                    print(f"type: {r.headers['content-type']}")
                    print(f"encoding: {r.encoding}")
                except Exception as e:
                    print(f"Something went wrong! Please try again. (Error: {str(e)})")
        except Exception as e:
            print(f"Something went wrong! Please try again. (Error: {str(e)})")
    elif x == "cancel":
        pass
    else:
        print("That is not a valid url! Please try again.")



def direct():
    x = ""
    x = input("Please paste the link here or type 'cancel' to cancel: ")
    if "https://" or "http://" in x:
        
        url = x
        print("Please wait while I check if the link is valid... (this could take several minutes)")
        try:
            r = requests.get(url)
            m = input("What is the file extension (.zip, .exe, etc.)? ")
        
            if "." in m:
                ext = m
                l = input("Where would you like this to be stored (please put double backslashes like C:\\\\ if you are on windows)? ")
                path = l
                s = input("What is this file going to be called (without extension)? ")
                name = s
                print("Alright, downloading...")
                try:
                    with open(f'{path}{name}{ext}', 'wb') as f:
                        f.write(r.content)

                    print(f"status_code: {r.status_code}")
                    print(f"type: {r.headers['content-type']}")
                    print(f"encoding: {r.encoding}")
                except Exception as e:
                    print(f"Something went wrong! Please try again. (Error: {str(e)})")

        except Exception as e:
            print(f"Something went wrong! Please try again. (Error: {str(e)})")
    elif x == "cancel":
        pass
    else:
        print("That is not a valid url! Please try again.")
            
        


def disLinkFind():
    x = ""
    x = input("Please paste the link here or type 'cancel' to cancel: ")
    if "https://" in x:
        
        url = x
        try:
            r = requests.get(url)
            print("Detecting extension...")

            ext = url.split(".",3)[3]

            print(f"I detected that the extension was .{ext}.")
            
            l = input("Where would you like this to be stored (please put double backslashes like C:\\\\ if you are on windows)? ")
            path = l
            s = input("What is this file going to be called (without extension)? ")
            name = s
            print("Alright, downloading...")
            try:
                with open(f'{path}{name}.{ext}', 'wb') as f:
                    f.write(r.content)

                print(f"status_code: {r.status_code}")
                print(f"type: {r.headers['content-type']}")
                print(f"encoding: {r.encoding}")
                print("Done!")
            except Exception as e:
                print(f"Something went wrong! Please try again. (Error: {str(e)})")

        except Exception as e:
            print(f"Something went wrong! Please try again. (Error: {str(e)})")
    elif x == "cancel":
        pass
    else:
        print("That is not a valid url! Please try again.")



print('Welcome to...')
print("""

        nanoscrape.py
         version 1.0
        

""")

print("Please select an option.")

menu()

while ans != "4" or ans != "quit":
    ans = input("NSCRAPE > ")

    if ans == "1":
        disLinkExt()
    elif ans == "2":
        disLinkFind()
    elif ans == "3":
        direct()
    elif ans == "4" or ans == "menu":
        menu()
    elif ans == "5" or ans == "quit":
        print("Quitting...")
        break
    else:
        print("Sorry, there is no option for that.")


