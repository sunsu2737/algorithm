import datetime
def solution(a, b):
    d=datetime.date(2016,a,b)
    
    
    return  d.strftime('%a').upper()