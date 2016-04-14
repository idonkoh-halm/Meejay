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

def generate_m3u():
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
    pla = open("mar17.m3u", "wb")
    print "Name of the file: ", pla.name
    pla.write(str(make_html('idk',"http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/")))
    pla.close()

song_data = {
    'Rock':['Possum Kingdom','Another one Bites the Dust',],
    'Rap' : ['Ultralight Beam','SNDLSCH in Vegas'],
    'Jazz' : ['Pebble Beach'],
    }

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




