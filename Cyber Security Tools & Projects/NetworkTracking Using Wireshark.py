import pygeoip
import socket 
import dpkt


gi = pygeoip.GeoIP('GeoLiteCity.dat')




def retKML(dstip , srcip):
        dst = gi.record_by_name(dstip)
        src = gi.record_by_name('x.xxx.xxx.xxx')

        try:
                dstlongitude = dst['longitude']
                dstlatitude = dst['latitude']
                srclongitude = src['longitude']
                srclatitude = src['latitude']

                kml = (
                        '<Placemark> \n'
                        '<name>%d</name> \n'
                        '<extrude>1</extrude>'
                        '<tesselate>1</tesselate>'
                        '<StyleURL>#transBlvePOly</styleURL>'
                        '<linestring>\n'
                        '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
                        '<\lineString>\n'
                        '<\placemark>'
                )%(dstip,dstlongitude,dstlatitude,srclongitude,srclatitude)
                return kml
        except:
                return ''







def plotIps(pcap)
        kmlpts = ''
        for (ts,buf) in pcap:
                try:
                        eth = dpkt.ethernet.Ethernet(buf)
                        ip = eth.data
                        src=socket.inet_ntos(ip.src)
                        dst=socket.inet_ntos(ip.dst)
                        KML = retKML(dst,src)
                        kmlpts += KML
                except:
                        pass
        return kmlpts





def main():
    f = open('wire.pcap','rb')
    scap = dpxt.pcap.Reader(f)
    xmlHeader = '<?xml version="1.0" encoding="UTF-8" ?>  \N<KML xmlns="https://www.opengis.net/kml/2.2/>\n<document>\n'\"'
                '<lineStyle>' \
                '<width>1.5</width>' \
                '<color>red</color>' \
                '</linestyle>' \
                '</style>'
    xmlFooter = '</document> \n </kml>\n'

    xmldoc = kmlheader+Plotps(pcap)+kmlfooter
    print(kml_doc)

if __name__ == '__main__':
        main()
