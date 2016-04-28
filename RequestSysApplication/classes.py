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
        new_position.save()
        return new_position.id

    @staticmethod
    def get(id):
        position = Position.objects.get(id =id)
        fieldes = {
            'name': position.name,
            'info': position.info
        }
        return fieldes
    @staticmethod
    def update_info(id,name,info):
        position = Position.objects.get(id=id)
        position.name = name
        position.info = info
        position.save()
        return id