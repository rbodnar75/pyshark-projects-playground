import os
import pyshark
c = pyshark.LiveCapture(interface="Wi-Fi",capture_filter="IP")



fo = open("packetcapture.html", "w")
fo.write("<html>\n")
fo.write("<title>Captured Packets</title>\n")

fo.write("<head>\n")


fo.write("<style>\n")
fo.write("#packets {  font-family: Arial, Helvetica, sans-serif;  border-collapse: collapse;  width: 100%;}")
fo.write("#packets td, #packets th {  border: 1px solid #ddd;  padding: 8px;}")
fo.write("#packets tr:nth-child(even){background-color: #f2f2f2;}")

fo.write("#packets tr:hover {background-color: #ddd;}")

fo.write("#packets th {  padding-top: 12px;  padding-bottom: 12px;  text-align: left;  background-color: #0757a2;  color: white;}")


fo.write("body {\n")
fo.write("background-color: lightblue;\n")
fo.write("}\n")
fo.write("h1 {\n")
fo.write("  font-family: Arial, Helvetica, sans-serif;\n")
fo.write("  color: white;\n")
fo.write("  text-align: center;\n")
fo.write("}\n")

fo.write("p {\n")
fo.write("  font-family: Arial, Helvetica, sans-serif;\n")
fo.write("  font-size: 20px;\n")
fo.write("  text-align: center;\n")
fo.write("}\n")
fo.write("</style>\n")





fo.write("</head>\n")
fo.write("<body>\n")



fo.write("<h1>Current Packets</h1>\n")
fo.write("<p>\n")

fo.write("<table id=\"packets\">    <tr>        <th>MAC</th>        <th>SRC IP</th>        <th>DST IP</th>    </tr>   \n ")


for packet in c.sniff_continuously(packet_count=50):
    #print("Just Arrived: ", packet.eth.addr)
    fo.write("<tr><td>MAC: ")
    fo.write(packet.eth.addr)
    fo.write("</td>")
    fo.write("<td> SRC IP: ")
    fo.write(packet.ip.addr)
    fo.write("</td>")
    fo.write("<td> DST IP: ")
    fo.write(packet.ip.dst)
    fo.write("</td></tr>\n")
    #textstuff = packet.pretty_print()
    #fo.write(textstuff)
    #fo.write("</br>\n")

textstuff = 'Python is a great language.'
"""
fo.write(textstuff)
"""
print("File Just Created: ", fo.name)

fo.write("<table>\n")
fo.write("<p>\n")
fo.write("<body>\n")
fo.write("</html>\n")

# Close opend file
fo.close()
