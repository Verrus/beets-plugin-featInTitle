# This file is part of beets.

"""puts featuring artists in the title instead of the artist field"""

from beets.plugins import BeetsPlugin
from beets import library
from beets import ui
import re


class ftInTitle(BeetsPlugin):
    def commands(self):
        cmd = ui.Subcommand('ftintitle', help='puts featuring artists in the title instead of the artist field')
        def func(lib, config, opts, args):
	  for track in lib.items():
	    artistfield  = track.__getattr__("artist")
	    regxRes = re.split('[fF]t\.|[fF]eaturing|[fF]eat\.', artistfield)
	    if len(regxRes)>1:
	      titleField = track.__getattr__("title")
	      featInTitle = re.search('[fF]t\.|[fF]eaturing|[fF]eat\.', titleField)
	      if featInTitle==None:
		print track.__getattr__("path")
		track.__setattr__("artist", regxRes[0])
		track.__setattr__("title", titleField + " feat." + regxRes[1])
		track.write()
	      else:
		track.__setattr__("artist", regxRes[0])	      
		track.write()
	  ui.print_("A Manual 'beet update' run is recommended. ")
        cmd.func = func
        
        return [cmd]
        