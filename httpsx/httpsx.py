import sys
import argparse
import random

parser = argparse.ArgumentParser(description="[*] For bug bounty hunter!!!", usage="%(prog)s -f file -o output", epilog="[*] %(prog)s -f file.txt -o output.txt")

parser.add_argument("-u", "--url",
                    metavar="url",
                    help="submit url",
                    dest="arg_url",
                    nargs="+"
)

parser.add_argument("-f", "--file",
                    metavar="file",
                    help="submit input url file",
                    dest="arg_file"
)

parser.add_argument("-o", "--output",
                    metavar="output",
                    help="set output file name",
                    dest="arg_output"
)

args = parser.parse_args()
arg_url = args.arg_url
arg_file = args.arg_file
arg_output = args.arg_output
lst, https_url_lst, http_url_lst = [], [], []

def banner():
    banner1 = """
    __    __  __            _  __
   / /_  / /_/ /_____  ____| |/ /
  / __ \/ __/ __/ __ \/ ___/   / 
 / / / / /_/ /_/ /_/ (__  )   |  
/_/ /_/\__/\__/ .___/____/_/|_|  
             /_/                 
    """
    banner2 = """
.__     __    __                        
|  |___/  |__/  |_______  _________  ___
|  |  \   __\   __\____ \/  ___/\  \/  /
|   Y  \  |  |  | |  |_> >___ \  >    < 
|___|  /__|  |__| |   __/____  >/__/\_ """+"""\"""
     \/           |__|       \/       \/
    """
    banner3 = """
    __    __  __                 
   / /_  / /_/ /_____  ______  __
  / __ \/ __/ __/ __ \/ ___/ |/_/
 / / / / /_/ /_/ /_/ (__  )>  <  
/_/ /_/\__/\__/ .___/____/_/|_|  
             /_/                 
    """

    banner4 = """
    
.__     __    __               ____  ___
|  |___/  |__/  |_______  _____\   \/  /
|  |  \   __\   __\____ \/  ___/\     / 
|   Y  \  |  |  | |  |_> >___ \ /     \ 
|___|  /__|  |__| |   __/____  >___/\  """+"""\"""
     \/           |__|       \/      \_/
    """

    banners = [banner1, banner2, banner3, banner4]
    print(random.choice(banners))
    print("[*] Created by Adarsh Addee!!!")
    print("[*] Make any link full accessible!!!")
    print("[*] You can use a file to create URL and save output!!!")
    print()

def make_url(make_url):
    r_https = "https://"+make_url
    r_http = "http://"+make_url
    print(r_https)
    print(r_http)
    https_url_lst.append(r_https)
    http_url_lst.append(r_http)
    

def handle_url(*url_entry):
    for var in url_entry:
        for l in var:
            if len(l) > 1:
                lst.append(l)
    
    try:
        if len(lst) > 1:
            for arg_tuple in url_entry:
                for url in arg_tuple:
                    make_url(url)

        if len(lst) <= 1:
            for url in url_entry:
                make_url(url)
        

    except Exception as e:
       print("[X] Try to Add Two URLs!!!")
       print("[X] Kindly Add Two URLs!!!")


def handle_file():
    if arg_file:
        with open(arg_file) as file:
            for line in file:
                line = line.strip("\n")
                handle_url(line)

def handle_output():
    if arg_output:
        with open(arg_output, "a") as output_file:
            output_file.write("All https links are:")
            output_file.write("\n")
            for htps_url in https_url_lst:
                output_file.write(htps_url)
                output_file.write("\n")
            
            output_file.write("\n\n")

            output_file.write("All http links are:")
            output_file.write("\n")
            for htp_url in http_url_lst:
                output_file.write(htp_url)
                output_file.write("\n")

            output_file.write("\n")
            

if __name__ == "__main__":
    if len(sys.argv) == 1:
        banner()
        parser.print_help(sys.stderr)
        sys.exit(1)

    if arg_file:
        handle_file()

    if arg_url:
        handle_url(arg_url)

    if arg_output:
        handle_output()

    print()


