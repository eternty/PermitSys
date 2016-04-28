from RequestSysApplication.models import MyRequest, Position


class RequestServiceLayer(object):                 #SERVICE LAYER
    @staticmethod
    def parse(choice, reqobject,pk):
        if choice == u'delete':
            MyRequest.deletion(pk)                 #DOMAIN
        else:
            reqobject.request_proceed(choice)      #DOMAIN
        return
class PositionGateWay(object):                         #GATEWAY
    @staticmethod
    def create(name, info):
        new_position = Position()
        new_position.name = name
        new_position.info = info
        return new_position