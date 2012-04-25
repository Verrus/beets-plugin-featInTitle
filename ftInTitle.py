#Copyright (c) <2012>, <github.com/Verrus/beets-plugin-featInTitle>
#All rights reserved.
## New BSD License:
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
    #* Redistributions of source code must retain the above copyright
      #notice, this list of conditions and the following disclaimer.
    #* Redistributions in binary form must reproduce the above copyright
      #notice, this list of conditions and the following disclaimer in the
      #documentation and/or other materials provided with the distribution.
    #* Neither the name of the <organization> nor the
      #names of its contributors may be used to endorse or promote products
      #derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This file is a plugin on beets.

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
	    regxRes = re.split('[fF]t\.|[fF]eaturing|[fF]eat\.|[wW]ith', artistfield)
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
	  print "A Manual 'beet update' run is recommended. "
        cmd.func = func
        
        return [cmd]
        
