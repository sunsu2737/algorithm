from requests import Request,Session

s=Session()

BASE='https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'



def base_api(method,url,auth_key,body={}):
    header={
        'Authorization':auth_key,
        'Content-Type': 'application/json'
    }
    if method=='GET':
        req=Request(method,BASE+url,headers=header)
    else:
        req=Request(method,BASE+url,json=body,headers=header)
    prepped = req.prepare()
    return s.send(prepped)



def start_api(problem):
    header={
    'X-Auth-Token':'cf04482ab7bd18ed2ca4f32b5329dde5',
    'Content-Type': 'application/json'
    }
    body={
        'problem':problem
    }
    req=Request('POST',BASE+'/start',params=body,headers=header)
    prepped = req.prepare()
    return s.send(prepped).json()



def location_api(auth_key):
    return base_api('GET','/locations',auth_key).json()

def truck_api(auth_key):
    return base_api('GET','/trucks',auth_key).json()


def simulate_api(commands,auth_key):
    body={
        'commands':commands
    }
    return base_api('PUT','/simulate',auth_key,body)

def score_api(auth_key):
    return base_api('GET','/score',auth_key).json()

    

    