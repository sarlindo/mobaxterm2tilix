import ConfigParser
import json
import ntpath

Config = ConfigParser.ConfigParser()
Config.read("MobaXterm.ini")

items = dict(Config.items("Bookmarks_1"))

sessionlist = []
for key, value in items.iteritems() :
    if (key != 'subrep' and key != 'imgnum'):

       pkname = ntpath.basename(value.split("%")[14])

       if (pkname != ""):
          parm = "-i ~/.ssh/" + pkname.replace('.ppk','.pem')

       d = {
         'command': "",
         'host': value.split("%")[1],
         'name': key,
         'params': parm,
         'port': int(value.split("%")[2]),
         'protocolType': "SSH",
         'type': "REMOTE",
         'user': value.split("%")[3]
       }  
       sessionlist.append(d)


with open('bookmarks.json', 'w') as fp:
    json.dump({'list':[{'list': sessionlist,'name': "Mobaxterm",'type': "FOLDER"}],'name': "Root",'type': "FOLDER"}, fp, sort_keys=True, indent=4)
