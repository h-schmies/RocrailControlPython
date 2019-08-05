from socket import *
 
# Function, to send a message to the Server
def sendMsg( s, xmlType, xmlMsg ):
  s.send("<xmlh><xml size=\"%d\" name=\"%s\"/></xmlh>%s" %(len(xmlMsg), xmlType, xmlMsg))
 
# Creating a connection to the local Rocrail-Server
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8051))
 
# The command "PowerON" is stored ind the variable "rrMsg" 
rrMsg = "<sys cmd=\"go\"/>"
sendMsg( s, "sys", rrMsg )
 
# Die Verbindung zum Server wird geschlossen
s.close()