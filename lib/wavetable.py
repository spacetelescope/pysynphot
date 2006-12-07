import re
import locations

wavetable = {}

fs = open(locations.wavecat+'data/wavecat.dat', mode='r')
lines = fs.readlines()
fs.close()

regx = re.compile(r'\S+', re.IGNORECASE)
for line in lines:
    try:
        [obm,coeff] = regx.findall(line)
        wavetable[obm] = coeff
    except ValueError:
        pass
