import xml.etree.ElementTree as etree
from datetime import datetime
from urllib2 import Request, urlopen, URLError
from smtplib import SMTP                  #standard SMTP protocol (port 25, no encryption)
from email.MIMEText import MIMEText
import sys

sys.path.append('NZGoalDtree') 

import NZGoalDtree.secrets as secret

def auditLds(dtree_ldsids ,date_from, date_to, email):
    feed = '{http://www.w3.org/2005/Atom}'
    status = 200
    page = 1
    lds_datasets = {}
    
    while status == 200:
        req = Request('http://data.linz.govt.nz/feeds/layers?page={}'.format(page))
        try: 
            response = urlopen(req)
            status = response.getcode()
            data = response.read()
            tree = etree.fromstring(data)
            entries = tree.findall(feed+'entry') 
            for e in entries:
                data_set_date = e.find(feed+'published').text.rsplit('T')[0]
                data_set_date = datetime.strptime(data_set_date, "%Y-%m-%d").date()
                if data_set_date >= date_from and data_set_date <= date_to:
                    id = e.find(feed+'id').text
                    ldsid = id[id.rfind(':')+1:] #<id>tag:data.linz.govt.nz,2016-09:layers:3452</id>
                    lds_datasets[ldsid] = e .find(feed+'title').text
        except URLError, e:
            status = e.getcode()
        response.close()
        page += 1
    
    missing_ids = {}
    registered_ids = {}
    for id, tilte in lds_datasets.iteritems():
        if id not in dtree_ldsids:
            missing_ids[id]=tilte
        else:
            registered_ids[id]=tilte
            
    sendEmail(email, date_from, date_to, missing_ids, registered_ids)

def sendEmail(email, date_from, date_to, missing_ids, registered_ids):
    server = secret.mailServer()
    sender = 'no-reply@linz.govt.nz'
    recipients = [email]
    #extrarecipients = ['splanzer@linz.govt.nz']
    content = report(date_from, date_to, missing_ids, registered_ids)
    
    try:
        msg = MIMEText(content, 'plain')
        msg['Subject'] = 'NZGOAL LDS Decisions Audit'
        msg['From'] = sender
        
        conn = SMTP(server) 
        conn.set_debuglevel(False)
        #conn.login(*creds())
        try:
            conn.sendmail(sender, recipients, msg.as_string())
        finally:
            conn.close()
    
    except Exception as exc:
        sys.exit( 'Email sending failed; {0}'.format(exc))
    
def report(date_from, date_to, missing_ids, registered_ids):
    results = ''
    datasetCount = len(missing_ids) + len(registered_ids)
    time = datetime.now()
    if len(missing_ids) > 0: 
        results = '''The below datasets have been published via the LDS but have not been registered
        as having gone through the NZGOAL Decision making process\n\n'''
        
        for k, v in missing_ids.iteritems():
                results += '    lds_id: {0}| Dataset Name: {1}\n'.format(k, v)
    
    else:
        results = '''\nAll lds datasets have been regisered as having gone through the NZGOAL Decision making process'''
    
    
    return  ''' 
    
    {0}
    
    This is a system generated report from the lds/nzgoal desicion making framework website.
    You are receiving this as the your email had been provided for the latest audit 
     
     
    REPORT: >>
            
        {1} LDS datasets published between {2} and {3} have been evaluate to ensure
        prior to publishing the NZGOAL Framework has been considered 
        
        
    {4}
        
        
    << REPORT END
    
    For more information please visit https://www.wikipedia.org/
    '''.format(time, datasetCount, date_from, date_to,results)

