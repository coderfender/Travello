
import time
import json
import urllib2
# from __future__ import unicode_literals


def train_status(train_no):
    

    apikey = 89321

    try:

        if( 00116 < int(train_no) < 84370):
            d= time.strftime('%Y%m%d')
            url = 'http://api.railwayapi.com/live/train/%s/doj/%s/apikey/10270'%(train_no,d)
        
            json_data= urllib2.urlopen(url)
            #json_data2= urllib2.urlopen(url2)
            data = json.load(json_data)
            return data
            # op2= [(str(data['route'][i]['station']),str(data['route'][i]['status']),str(data['route'][i]['actarr'])) for i in range(0,len(data['route']))]
            # # return "<br>".join(["%s: %s" % (str(key), ('%('+str(key)+')s') % op2) for key in op2]
            # res =  str([str(item)[2:-2].strip('()')+"<br>" for item in op2])
            # return str([str(item)[2:-2].strip('()')+"<br>" for item in op2])

        else:
            return "  The train number entered is invalid"

    except ValueError:
        return ("  Invalid entry! Please try again")

    except KeyError:
        return "  Maximum hits reached!Try after 24 hrs!"
    except KeyboardInterrupt:
        return "  Thanks asshole!Get the fuck outta here!"
    except Exception,e:
        return str(e)