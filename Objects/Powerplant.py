from abc import ABC, abstractmethod

class Powerplant(ABC):
    def __init__(self, name, type, efficiency, pmin, pmax, fuels):
        self.name = name
        self.type = type
        self.efficiency = efficiency
        self.pmin = pmin
        self.pmax = pmax
        self.fuels = self.convert_fuels(fuels)

    #Convert fuel key names into easier keys
    def convert_fuels(self, fuels):
        res = {}
        replacement_values = {
            "gas(euro/MWh)": "gas",
            "kerosine(euro/MWh)": "kerosine",
            "co2(euro/ton)": "co2",
            "wind(%)": "wind"
        }
        for key in fuels.keys():
            res[replacement_values[key]] = fuels[key]

        return res

    #Define the cost for a single unit of power
    @abstractmethod
    def cost_per_MWh(self):
        pass

    #Calculate the cost given a certain load (in euro/MWh)
    @abstractmethod
    def calculate_cost(self):
        pass

class Gas(Powerplant):
    def __init__(self, name, type, efficiency, pmin, pmax, fuels):
        super().__init__(name, type, efficiency, pmin, pmax, fuels)
        #Cost per unit of energy
        self.cost = self.fuels['gas'] / efficiency
    
    def cost_per_MWh(self):
        return self.cost

    def calculate_cost(self, load):
        return load * self.cost


class Turbojet(Powerplant):
    def __init__(self, name, type, efficiency, pmin, pmax, fuels):
        super().__init__(name, type, efficiency, pmin, pmax, fuels)
        #Cost per unit of energy
        self.cost = self.fuels['kerosine'] / efficiency

    def cost_per_MWh(self):
        return self.cost

    def calculate_cost(self, load):
        return load * self.cost

class Wind(Powerplant):
    def __init__(self, name, type, efficiency, pmin, pmax, fuels):
        super().__init__(name, type, efficiency, pmin, pmax, fuels)
        self.pactual = pmax * (self.fuels['wind'] / 100)
    
    #Wind turbines don't have a cost
    def cost_per_MWh(self):
        return 0

    def calculate_cost(self, load):
        return 0