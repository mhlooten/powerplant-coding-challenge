from Objects.Powerplant import Powerplant
import math

#Greedy solver
def solve_greedy(powerplants, total_load):
    #Sort powerplants on cost per Mwh energy produced
    powerplants.sort(key=lambda x: x.cost_per_MWh())

    final_list = [] # List of all the powerplants with their respective power generation
    current_load = 0 # Variable with current load, should always be smaller or equal to total load
    load_list = [] # List with all the power usages in relation to the powerplants
    diff_list = [] # List with all the power differences between the current power usage and the pmin of each gasfired plant. Used to tune the power usage down and allow new power plants to be added
    diff_indexes = [] # List with the indexes of the plants with a power difference > 0, used for quick lookup in the diff_list
    diff_total = 0 # Total difference that can be tuned

    #Strategy:
    # - Check each element in the sorted list
    # - Each element with a pmax that fits the remaining load, is entirely added
    # - Each element (not wind) which has a pmin smaller than the remaining load but a greater pmax, is scaled towards the remaining load
    # - Each element (not wind) which has a pmin greater than the remaining load, will be attempted to scaled by taking some load off other elements if possible
    # - If there's not enough load to take off from other elements, the element is skipped
    # - This process continues until all elements are considered or when the total load has been reached

    for i, el in enumerate(powerplants):
        p = 0 #Load for this powerplant
        if current_load == total_load:
            pass
        elif el.type == "windturbine":
            pactual = round_down(el.pactual)
            if current_load + pactual <= total_load: #Wind turbine can be turned on
                p = pactual
                diff_list.append(0)       
        elif el.type == "gasfired":
            if current_load + el.pmin <= total_load: #Gas can be turned on, which means the minimum usage load can be added
                p = round_down(min(total_load - current_load, el.pmax))
                diff = p - el.pmin
                diff_list.append(diff) 
                if diff > 0:
                    diff_indexes.append(i)
                diff_total += diff
            elif diff_total > (current_load + el.pmin) - total_load: #Take some load off the other powerplants in order to fit if possible
                load_value = (current_load + el.pmin) - total_load #Value to be taken off the other powerplants
                to_load = load_value
                while to_load > 0: #Iterate over the tunable power and subtract it where necessary to achieve the pmin to start another power plant
                    current_index = diff_indexes[0]
                    diff = diff_list[current_index]
                    if to_load < diff:
                        diff_list[current_index] = diff - to_load
                        load_list[current_index] = load_list[current_index] - to_load
                        to_load = 0
                        diff_total -= diff
                    else: #Since the tunable power has reached 0 (power = pmin), the power plant is removed from the indexes list
                        diff_list[current_index] = 0
                        load_list[current_index] = load_list[current_index] - diff
                        diff_indexes.pop()
                        to_load = to_load - diff
                        diff_total -= diff
                p = el.pmin
                total_load += load_value

                
                
        elif el.type == "turbojet": #Turbo can always be turned on, since it does not have a minimum usage load
            p = round_down(min(total_load - current_load, el.pmax))

        current_load += p
        load_list.append(p)

    for i, el in enumerate(powerplants):
        final_list.append({"name": el.name, "p": load_list[i]})

    return final_list, current_load, total_load
            
def round_down(number):
    return math.floor(number * 10) / 10

    