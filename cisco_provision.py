import sys,os

print ""

# Read the last_config.ini file
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read('last_cisco_provision.ini')

mac = ""
if len(sys.argv) > 1 and len(sys.argv[1]) >= 12: 
	mac = sys.argv[1]
else:
	while(len(mac) < 12): mac = raw_input("MAC?: ")

mac = mac.replace("-","").replace(".","").replace(" ","").replace("/","")

# Set the ip pbx address
ippbx = config.get('last_config', 'IPPBX')
tmp = raw_input("PBX? (" + ippbx + ") (blank for same): ")
if tmp != "" and ippbx != tmp: ippbx = tmp

# Set the ip pbx sip port
sport = config.get('last_config', 'SPORT')
tmp = raw_input("SIP? (" + sport + ") (blank for same): ")
if tmp != "" and sport != tmp: sport = tmp

# Set the user account
exten = config.get('last_config', 'EXTEN')
tmp = raw_input("EXT? (" + exten + ") (blank for same): ")
if tmp != "" and exten != tmp: exten = tmp

# Set the password account
passw = "Abcd" + str(exten)
tmp = raw_input("PWD? (" + passw + ") (blank for same): ")
if tmp != "" and passw != tmp: passw = tmp

# Set the VM extension
vmail = config.get('last_config', 'VMAIL')
tmp = raw_input("VoM? (" + vmail + ") (blank for same): ")
if tmp != "" and vmail != tmp: vmail = tmp

# Set the firmware to upgrade
firmw = "SIP69xx.9-4-1-3"
tmp = raw_input("FRW? (" + firmw + ") (Y/N): ")
if tmp == "N" or tmp == "": firmw = ""

# advanced config
# rtpst = 10000
# rtpen = 20000
rtpst = config.getint('last_config', 'RTPST')
rtpen = config.getint('last_config', 'RTPEN')

tmp = raw_input("Advance config? (N) (Y/N): ")
if tmp == "Y":
	# Set the rtp media ports
	tmp = raw_input("RTP? (" + str(rtpst) + "-" + str(rtpen) + ") (blank for same): ")
	if tmp != "": 
		rtpst = int(tmp.split("-")[0])
		rtpen = int(tmp.split("-")[1])
		
		if not(rtpst > 0 and rtpen > 0 and rtpen > rtpst):
			rtpst = 10000
			rtpen = 20000


# file name with mac
file_name = "SEP" + mac 

itl_file = "ITL" + file_name + ".tlv"
cnf = file(itl_file, "w")
cnf.write("")
cnf.close()

ctl_file = "CTL" + file_name + ".tlv"
cnf = file(ctl_file, "w")
cnf.write("")
cnf.close()

# Read in the file
with open('SEP_base_.cnf.xml', 'r') as file:
	filedata = file.read()

# Replace the target string
filedata = filedata.replace('_IPPBX_', ippbx)
filedata = filedata.replace('_SPORT_', sport)
filedata = filedata.replace('_EXTEN_', exten)
filedata = filedata.replace('_PASSW_', passw)
filedata = filedata.replace('_VMAIL_', vmail)
filedata = filedata.replace('_FIRMW_', firmw)
filedata = filedata.replace('_RTPST_', str(rtpst))
filedata = filedata.replace('_RTPEN_', str(rtpen))

# Write the file out again
with open(file_name + '.cnf.xml', 'w') as file:
	file.write(filedata)

# all good!
print ""
print "File " + file_name + ".cnf.xml has been created."

# Write last_constants.ini file
file = open("last_cisco_provision.ini","w")
file.write("[last_config]\n")
file.write("IPPBX = " + ippbx		+ "\n")
file.write("SPORT = " + sport		+ "\n")
file.write("EXTEN = " + exten		+ "\n")
file.write("VMAIL = " + vmail		+ "\n")
file.write("FIRMW = " + firmw		+ "\n")
file.write("RTPST = " + str(rtpst)	+ "\n")
file.write("RTPEN = " + str(rtpen)	+ "\n")
file.close()