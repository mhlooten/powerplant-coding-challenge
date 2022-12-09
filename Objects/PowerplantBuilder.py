from Objects.Powerplant import Powerplant, Gas, Turbojet, Wind

#Builder for powerplants depending on type
class PowerplantBuilder():
    
    @staticmethod
    def build_powerplant(name, type, efficiency, pmin, pmax, fuels):
        if type == "gasfired":
            return Gas(name, type, efficiency, pmin, pmax, fuels)
        if type == "turbojet":
            return Turbojet(name, type, efficiency, pmin, pmax, fuels)
        if type == "windturbine":
            return Wind(name, type, efficiency, pmin, pmax, fuels)