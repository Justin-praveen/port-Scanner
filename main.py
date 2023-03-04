import click
import pyfiglet
import socket
import sys

#figle for Banner
Banner = pyfiglet.figlet_format("JUSTIN PRAVEEN")
print(Banner)

def new (name):
    return socket.gethostbyname(name)

print("...................................................................")
print("IP is {}".format(a))
print("...................................................................")

try :
   
   for port in range(1,63535):
    
    # setup for connections
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # connect to the ports

    connection = soc.connect_ex((a,port))

    if connection == 0: print(" Open : {}".format(port))
    soc.close()

except KeyboardInterrupt :
   print("Please Try someTimes")
   sys.exit()
except socket.gaierror:
   print("Please Try someTimes")
   sys.exit()
except socket.error:
   print("Please Try someTimes")
   sys.exit()



#it will be executes first

if __name__ == "__main__":
   a = new(input("Enter hostname :"))
   

   

