__author__ = 'hecxac0d3@gmail.com'

class alert():
    def sms(self,admin,msg):
        self.mobile = admin
        self.sms = msg
        # call service/protocol/type send sms

    def msg(self,email,msg):
        self.email = email
        self.msg = msg
        # call service/prot send email