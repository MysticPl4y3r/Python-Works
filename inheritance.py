class vehicle(object):
    #protected
    _name=None
    _color=None
    _speed=None
    
    #public
    def __init__(self,name,color,tspeed):
        self._name=name
        self._color=color
        self._speed=tspeed
    def getspeed(self):
        return self._speed

class car(vehicle):
    #private
    __type=None
    __owner=None
    
    #public
    def __init__(self,name,color,tspeed,ownr):
        vehicle.__init__(self,name,color,tspeed)
        self.__type="Car"
        self.__owner=ownr
        
    def vehtype(self):
        return self.__type
    
    def vehowns(self):
        return self.__owner
    
class aeroplane(vehicle):
    #private
    __type=None
    __owner=None
    
    #public
    def __init__(self,name,color,tspeed,ownr):
        vehicle.__init__(self,name,color,tspeed)
        self.__type="Aircraft"
        self.__owner=ownr
        
    def vehtype(self):
        return self.__type
    
    def vehowns(self):
        return self.__owner
    

Car1=car("Koenigsegg One:1","white",447,"The Stig")
Car2=car("McLaren Senna GTR","blue",340,"Richard Miller")

Plane1=aeroplane("CFA-44 Nosferatu","Strigon Livery",2000,"Lt. Pasternak")
Plane2=aeroplane("Boeing 737","Red",1800,"SpiceJet")

Car1.getspeed()