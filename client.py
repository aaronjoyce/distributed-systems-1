import socket
import urllib
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--h", "--host", dest="HOST", 
                  help="Specify the host to connect to; for example, localhost")
parser.add_option("-p", "--port", dest="PORT",
                  help="Specify the port to connect to")

parser.add_option("-m", "--message", dest="MESSAGE",
                  help="Specify the message to send to the echo server")


options, args = parser.parse_args()
host = options.HOST
port = int(options.PORT)
message = options.MESSAGE
print(port)


# constants 
BUFFER_SIZE = 1024
DEFAULT_PORT = 8000
CRLF = "\r\n\r\n"

# create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port specified via the CLI


CRLF = "\r\n\r\n"
print(s.connect((host, port)))
s.send("GET /echo.php?message=%s HTTP/1.0%s" % (urllib.quote_plus(message), CRLF))

while True:
  	received = s.recv(BUFFER_SIZE)
 	if not received:
 		break
   	else:
   		print received
s.close()
