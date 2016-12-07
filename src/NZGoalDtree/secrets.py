import os 

def secretKey():
    '''
    The django web site key assign to the
    env var as per the read me
    '''
    
    return os.environ['dj_dtree_key']


def mailServer():
    '''
    The django web site key assign to the
    env var as per the read me
    '''
    
    return os.environ['dj_dtree_mail_serv']
