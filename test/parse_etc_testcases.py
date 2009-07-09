from __future__ import division
"""Utility functions to work with ETC-style test files.
Not intended for release."""

import os
from pysynphot import etc

def execute_cline(cline,rpath='.'):
    """execute the command, return the results"""
    cparts=cline.split('&')
    task=(cparts[0].split()[-1]).strip("'")
    fname=cparts[3].split('output=')[-1]
    cmd=cline.replace(os.path.dirname(fname),
                      rpath)
    cparts=cmd.split('&')
    return factory(task,cparts[1:])

def factory(taskname, *args, **kwargs):
    """This method encapsulates the ETC dependency.
    Eventually, pysynphot servers that support more than just the
    ETC functionality might be desired, and we could probably
    refactor and make specialized subclasses."""
    return str(apply(etc.tasks[taskname], args, kwargs))

def parse_cline(cline):
    """Return command, spectrum, & instrument strings"""
    cparts=cline.split('&')
    #Part one is the command itself. Take the last word,excluding the quote
    task=(cparts[0].split()[-1]).strip("'")
    #Part two is the spectrum specification
    spstring=(cparts[1].split('spectrum=')[-1]).strip('"')
    #Part three is the obsmode
    omode=(cparts[2].split('instrument=')[-1]).strip('"')
    #Part four is the filename
    fname=cparts[3].split('output=')[-1]
    return task, spstring,omode,fname

def parse_rline(rline):
    """Return just the numeric part of the response"""
    
    ans=rline.split(';')[0]
    return float(ans.strip("'"))

def parse_line(line):
    if line.startswith('[PysynphotRunner.doRun] command'):
        return parse_line(cline)
    elif line.startswith('[PysynphotRunner.doRun] response'):
        return parse_line(rline)

def runfile(fname,accuracy=1.0e-7):
    f=open(fname)
    cline="Hello world"
    while cline != '':
        try:
            cline=f.readline()
            rline=f.readline()
            tline=execute_cline(cline)
            tvalue=parse_rline(tline)
            ref=parse_rline(rline.split("response is '")[1])
            result=(tvalue-ref)/ref
            if ( result > accuracy):
                print "Failed: %s...",cline[30:70]
                print "Failed: tvalue %f, ref %f: %f"%(tvalue,ref,result)
            else:
                print "ok"


        except (IOError),e:
            if cline != '':
                print "%s ... Proceeding"%str(e)
            else:
                break
    f.close()

def parsefile(fname,outname):
    f=open(fname)
    cline="Hello world"
    counter=1
    out=open(outname,'w')
    while cline != '':
        try:
            cdummy=f.readline()
            cline=f.readline()
            rdummy=f.readline()
            rline=f.readline()
            sepdummy=f.readline()
            task, spstring,omode,fname = parse_cline(cline)
            ans=parse_rline(rline)

            out.write("class C%d(ETCTestCase):\n"%counter)
            out.write("    def setparms(self):\n")
            out.write("        self.sp=parse_spec('%s')\n"%spstring)
            out.write("        self.bp=ObsBandpass('%s')\n"%omode)
            out.write("        self.ref_rate=%g\n"%float(ans))
            out.write("        self.cmd='%s'\n"%task)
            out.write("        self.fname='%s'\n"%os.path.basename(fname))
            out.write("\n\n")
            out.flush()
            counter+=1
                      
        except (IndexError),e:
            if cline != '':
                print "%s ... Proceeding"%str(e)
            else:
                break
    f.close()
    out.close()
                                                    
