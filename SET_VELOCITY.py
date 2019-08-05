from socket import *
 
# Function, to send a message to the Server
def sendMsg( s, xmlType, xmlMsg ):
  s.send("<xmlh><xml size=\"%d\" name=\"%s\"/></xmlh>%s" %(len(xmlMsg), xmlType, xmlMsg))
 
# Creating a connection to the local Rocrail-Server
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8051))
 
# The command "SetVelocity" is stored ind the variable "rrMsg" in an xml-command and is then pushed to the Rocrail-Server via the sendMsg function
rrMsg = "<lc  id=\"Reichsbahn\" cmd=\"velocity\" V=\"100\"/>"
sendMsg( s, "sys", rrMsg )
 
# The connection to the server is closed
s.close()