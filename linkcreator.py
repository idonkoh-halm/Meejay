import sys
import urllib2

class Text_Output:
    '''
    from a bunch of user defined links, this will attempt to take those links
    and add them line by line to create a m3u file.
    '''
    def ___init___(self,filename):
        self.f = file(filename,'w')
    def new_text (self, txt):
        self.f.write(txt+'\n') #creates a new line
    def output_list(self, url_list):
        txt=''
        for itm in data_list:
            txt+= str(itm)+'\n'
            
    
    def finish(self):
        self.f.close()

def generate_m3u(m3u_name,songs):
    "Takes what is generated from make html, and generates an .m3u"
# Hinkle's reworking of above..
    def make_html (song_path, directory): #="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/"):
        '''
        argument "song_path" is wrapped around the root directory in order to create a proper path name.
        Example: takes word "tank", and changes it to "http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/tank"
        '''
        newlink=directory+urllib2.quote(song_path)+".mp3"
        return newlink
        text_output=Text_Output()
        text_output.new_text(newlink)
    playlistname=m3u_name+".m3u"
    pla = open(playlistname, "wb")

    print "Name of the file: ", pla.name
    for song in songs:
        pla.write(str(make_html(song,"/Users/programmer/Documents/Meejay/Music Directory/%s/"%m3u_name)))
        pla.write('\n')
    pla.close()


song_data = {
    'Rock':['The Toadies - Possum Kingdom','Queen - Another One Bites the Dust',],
    'Rap' : ['01 Ultralight Beam','Lupe Fiasco - SNDCLSH in Vegas'],
    'Jazz' : ['Vince Guaraldi Trio - Pebble Beach'],
    }
for genre,songs in song_data.items():
    generate_m3u(genre,songs)
#def texttohtml():
#    directory="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/JetSetRadio/"
#    text=raw_input('Enter normie text here')
#    newlink=directory+urllib2.quote(text)+".mp3"
#    print newlink



#DEPRECATED CODE
#def get_url_from_user ():
#    print texttohtml(raw_input('Enter normie text here'))
#texttohtml("touch and go")
#get_url_from_user()
#m3u_generator('playlist.txt')