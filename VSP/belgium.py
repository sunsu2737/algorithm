import re

class NationalRegisterNumber:

    def __init__(self,Number):
        self.Number=re.sub('[^0-9]','',Number)
    def __str__(self):
        N=self.Number
        return '{}.{}.{}-{}.{}'.format(N[0:2],N[2:4],N[4:6],N[6:9],N[9:11])
    def gender(self):
        if int(self.Number[6:9])%2==1:
            return 'male'
        else:
            return 'female'
    def checksum(self,y2k=False):
        if y2k:
            N='2'+self.Number[0:9]
            print(N)
            return 97-(int(N)%97)
        else:
            N=self.Number[0:9]
            return 97-(int(N)%97)
a=NationalRegisterNumber('09082428248')
print(a.checksum(False))
