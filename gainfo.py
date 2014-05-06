#!/usr/bin/env python
# Copyright (c) 2013-2014, Matthew W. Moskewicz <moskewcz@alumni.princeton.edu>; see LICENSE
import os,sys,re
join = os.path.join
import wave
import contextlib

class scan_t( object ):
    def __init__( self, top_dir ):
        self.num_fns = 0
        self.tot_dur = 0.0
        for root, dirs, fns in os.walk( top_dir ):
            for fn in fns:
                self.proc_fn( join(root,fn) )
        print( "num=%s tot_dur=%.0fs (%.1fh) avg_dur=%.3fs" % 
               ( self.num_fns, self.tot_dur, self.tot_dur / 60.0 / 60.0, self.tot_dur / self.num_fns ) )

    def proc_fn( self, fn ):
        with contextlib.closing(wave.open(fn,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            dur = frames / float(rate)
            #print( fn, dur )
            self.num_fns += 1
            self.tot_dur += dur

if __name__ == "__main__":
    scan_t( sys.argv[1] )
