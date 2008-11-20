"""This script *replaces* the processlog.csh shell script. It has
more sophisticated logic to add the etc test name to the pysynphot
command as another keyword-value pair."""

import sys,re

def run(fname):
    log=open(fname)
    out=open(fname.replace('.txt','_parsed.txt'),'w')

    line='unopened'
    while len(line)>0:
        line = log.readline().strip()
        if "] starting" in line or "] running" in line:
            x=re.search("'(?P<name>.*)'",line)
            testname=x.group('name')
        elif 'command is' in line:
            prefix,value=line.lstrip().split('command is')
            cmd='%s&etcid="%s"\n'%(value[0:-2],
                                   testname)
            out.write(cmd)

    log.close()
    out.close()
            
if __name__ == '__main__':
    run(sys.argv[1])
