from xml.etree import ElementTree
from sys import argv
from os.path import expanduser
from pyDes import *
from Tkinter import *
import ttk
import tkFileDialog

class HandleXML:

    def __init__(self):
        self.username = ""
        self.score = 0
        self.lastcompleted = ""
        self.lastcompletedtime = ""

    def parseXML(self, fn, key):

        k = des(key, padmode=PAD_PKCS5)
        f = open(fn, 'rb')
        data = f.read()
        root = ElementTree.fromstring(k.decrypt(data))
        for node in root:
            if "name" == node.tag:
                self.username = node.text
            elif "score" == node.tag:
                self.score = int (node.text)
            elif "progress" == node.tag:
                for exercise in node:
                    if exercise.get('completed'):
                        self.lastcompleted = exercise.get('id')
                        self.lastcompletedtime = exercise.get('completed')
        f.close

    def getUsername(self):
        return self.username

    def getScore(self):
        return self.score

    def getLastCompleted(self):
        return self.lastcompleted

    def getCompletedTime(self):
        return self.lastcompletedtime


class LatidoFilereader:

    def loadCallback(self):
        print "load button"
        print tkFileDialog.askdirectory(mustexist=True,
            title='Select Your Folder of Latido User Files.',
            initialdir = expanduser('~'))

    def saveCallback(self):
        print "save button"
        print tkFileDialog.asksaveasfile(title='Choose Location to Save Your Progress Report.',
            initialdir = expanduser('~'))

    def __init__(self, root):
        self.root = root
        self.root.option_add('*tearOff', False)
        self.root.resizable(True, True)
        self.root.title ("Latido Progress File Reader")
        self.buttonbar_frame = ttk.Frame(root)
        self.buttonbar_frame.pack()
        self.text = Text(root, height=40, width=100)
        self.text.pack()

        ttk.Label(self.buttonbar_frame, text="Library Key (8 chars):").grid(column = 0, row = 0)
        self.loadbutton = ttk.Button(self.buttonbar_frame,
            text = 'Select Folder of Latido Progress Files',
            command = self.loadCallback)
        self.keyval = StringVar()
        self.keyentry = ttk.Entry(self.buttonbar_frame,
            textvariable = self.keyval)
        self.keyval.set("eyesears")
        self.savebutton = ttk.Button(self.buttonbar_frame,
            text = 'Save Progress Report',
            command = self.saveCallback)

        self.keyentry.grid (column = 1, row = 0)
        self.loadbutton.grid (column = 2, row = 0)
        self.savebutton.grid (column = 3, row = 0)

def main():
    root = Tk()
    gui = LatidoFilereader (root)
    root.mainloop()

if __name__ == "__main__": main()

