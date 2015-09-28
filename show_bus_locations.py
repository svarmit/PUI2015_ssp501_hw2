import json
import urllib2
import sys

if __name__=='__main__':
    url = (('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s')%(sys.argv[1],sys.argv[2]))
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    busInfo = (data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'])
    count_var = 0
    for b in busInfo:
        vehActivity = b['VehicleActivity']
        print 'Bus Line : ',vehActivity[0]['MonitoredVehicleJourney']['PublishedLineName']    
        print 'Number of Active Buses : ',len(vehActivity)
        for i in vehActivity:
            count_var +=1
            vehJourney = i['MonitoredVehicleJourney']
            print 'Bus %s is at latitude %10s and longitude %10s '%(count_var,vehJourney['VehicleLocation']['Latitude'],vehJourney['VehicleLocation']['Longitude'])

