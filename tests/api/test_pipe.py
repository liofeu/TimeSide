# -*- coding: utf-8 -*-
from timeside.tests.api import examples
from timeside.core import *
from timeside.api import *
from sys import stdout

import os.path
source = os.path.join(os.path.dirname(__file__),  "../samples/guitar.wav")

print "Normalizing %s" % source
decoder  = examples.FileDecoder(source)
maxlevel = examples.MaxLevel()
duration = examples.Duration()

(decoder | maxlevel | duration).run()

gain = 1
if maxlevel.result() > 0:
    gain = 0.9 / maxlevel.result()

print "input maxlevel: %f" % maxlevel.result()
print "gain: %f" % gain
print "duration: %f %s" % (duration.result(), duration.unit())

gain     = examples.Gain(gain)
encoder  = examples.WavEncoder("normalized.wav")
fixed    = examples.FixedInputProcessor()

subpipe  = gain | fixed | maxlevel

(decoder | subpipe | encoder).run()

print "output maxlevel: %f" % maxlevel.result()

