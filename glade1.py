#!/usr/bin/env python

import os
import pygtk
pygtk.require('2.0')

import gtk

class Buglump:

  def on_window1_destroy(self, object, data=None):
    print "quit with cancel"
    gtk.main_quit()

  def on_gtk_quit_activate(self, menuitem, data=None):
    print "quit from menu"
    gtk.main_quit()

  def hamdi(self, object):
    #dialog = gtk.FileChooserDialog("Open..",
    #                           None,
    #                           gtk.FILE_CHOOSER_ACTION_OPEN,
    #                           (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
    #                            gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    #dialog.set_default_response(gtk.RESPONSE_OK)
    #response = dialog.run()
    #if response == gtk.RESPONSE_OK:
    print object.get_filename(), 'selected'
    #elif response == gtk.RESPONSE_CANCEL:
    #print 'Closed, no files selected'
    #dialog.destroy()

  def __init__(self):
    self.gladefile = os.path.join(os.path.dirname(__file__), 'glade1.glade')
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.builder.connect_signals(self)
    self.window = self.builder.get_object("window1")
    self.window.show()
    


if __name__ == "__main__":
  main = Buglump()
  gtk.main()

