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

def m3u_generator(filename='playlist.txt'):
    def texttohtml():
        directory="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/JetSetRadio/"
        text=raw_input('Enter normie text here')
        newlink= directory+urllib2.quote(text)+".mp3"
        print newlink
        return newlink
    text_output=Text_Output(filename)
    text_output.new_text(newlink)

#m3u_generator()

song_data = {
    'Rock':['paradise city','bad company',],
    'Pop' : ['Love love love you','Ooooooh babe'],
    'Rap' : ['Some rap song'],
    }

#def texttohtml():
#    directory="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/JetSetRadio/"
#    text=raw_input('Enter normie text here')
#    newlink=directory+urllib2.quote(text)+".mp3"
#    print newlink


# Hinkle's reworking of above..
def texttohtml (text, directory="http://googledrive.com/host/0B_QRZ8n8sCFLdkJTMU1Ed0k3VVk/music/"):
    newlink=directory+urllib2.quote(text)+".mp3"
    return newlink

def get_url_from_user ():
    print texttohtml(raw_input('Enter normie text here'))




texttohtml("touch and go")
get_url_from_user()


#texttohtml()

