from socket import *

# Funktion, um Message an Server zu senden
def sendMsg( s, xmlType, xmlMsg ):
  s.send("<xmlh><xml size=\"%d\" name=\"%s\"/></xmlh>%s" %(len(xmlMsg), xmlType, xmlMsg))
 
# Herstellung einer Verbindung zum Rocrail-Server
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8051))
 print("Die Lok Reichsbahn wurde zum rest-block geschickt.")
# Command "Velocity" wird in der Variable "rrMsg" als XML-Befehl gespeichert und mit der Funktion sendMsg and den Server übertragen
rrMsg = "<<lc id=\"Reichsbahn\" cmd=\"gotoblock\" blockid=\"block\"/>>"
sendMsg( s, "sys", rrMsg )
 
# Die Verbindung zum Server wird geschlossen
s.close()