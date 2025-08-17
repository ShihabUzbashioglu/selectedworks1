from scrapy.all import *

interface = "wlan0"
probeRegs = []

def SelfPropare(p):
    if p.hasLayer(DotilProbeReg)
    netName = getlayer(DotilProbeReg).info
    if netName not in probeRegs:
        probeRegs.append(netName)
        print('[+]  Detected New Probe Request ' + netName)

sniff( face = interface , gen =sniffproves)
