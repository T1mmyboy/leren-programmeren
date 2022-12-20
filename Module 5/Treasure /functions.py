from calendar import week
from cmath import cos
from decimal import ROUND_DOWN
from math import ceil, trunc
from tempfile import TemporaryDirectory
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS,COST_FOOD_HORSE_COPPER_PER_DAY,COST_FOOD_HUMAN_COPPER_PER_DAY
from data import mainCharacter
from data import COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HORSE_COPPER_PER_NIGHT, COST_INN_HUMAN_SILVER_PER_NIGHT

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    
    return amount/10

def silver2gold(amount:int) -> float:
    
    return amount/5

def copper2gold(amount:int) -> float:
    
    return amount/50

def platinum2gold(amount:int) -> float:
    
    return amount*25

def getPersonCashInGold(personCash:dict) -> float:
    return copper2gold(personCash.get("copper"))+silver2gold(personCash.get("silver"))+personCash.get("gold")+platinum2gold(personCash.get("platinum"))

##################### M04.D02.O4 #####################s

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return copper2gold((COST_FOOD_HUMAN_COPPER_PER_DAY*people+COST_FOOD_HORSE_COPPER_PER_DAY*horses)*JOURNEY_IN_DAYS)
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    dict = []
    for x in range(len(list)):
        if list[x][key] == value:
            dict.append(list[x])
    return dict
def getAdventuringPeople(people:list) -> list:
    
    return getFromListByKeyIs(people, "adventuring", True)
def getShareWithFriends(friends:list) -> list:
    
    return getFromListByKeyIs(friends, "shareWith", True)
def getAdventuringFriends(friends:list) -> list:
    buddies = []
    adventur = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)
    for x in range(len(adventur)):
        if share[x] in adventur:
            buddies.append(share[x])
    return buddies
    



##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    if (people % 2) == 0:
        return people/2
    else:
        return (people/2)+0.5

def getNumberOfTentsNeeded(people:int) -> int:
    if (people % 3) == 0:
        return people/3
    else:
        return ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    price_horses = JOURNEY_IN_DAYS*(COST_HORSE_SILVER_PER_DAY*horses)
    price_horses=silver2gold(price_horses)
    price_tents = (ceil(JOURNEY_IN_DAYS/7))*(COST_TENT_GOLD_PER_WEEK*tents)
    price_total = price_tents+price_horses
    return price_total
##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    if len(items) == 1:
        old = str(items[0]["amount"])+items[0]["unit"]+" "+items[0]["name"]
    else:
        old = str(items[0]["amount"])+items[0]["unit"]+" "+items[0]["name"]+", "
    for x in range(1, len(items)):
        if x == len(items)-1:
            old = old+str(items[x]["amount"])+items[x]["unit"]+" "+items[x]["name"]
            break
        if x<len(items):
            old = old+str(items[x]["amount"])+items[x]["unit"]+" "+items[x]["name"]+", "
    return old

def getItemsValueInGold(items:list) -> float:
    total = 0
    for x in range(len(items)):
        cost = items[x]["price"]["amount"] *items[x]["amount"]
        if items[x]["price"]["type"] == "copper":
            total = total+copper2gold(cost)
        elif items[x]["price"]["type"] == "silver":
            total = total+silver2gold(cost)
        elif items[x]["price"]["type"] == "gold":
            total = total+cost
        elif items[x]["price"]["type"] == "platinum":
            total = total+platinum2gold(cost)
    return total

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    partyCash = 0
    for x in range(len(people)):
        partyCash+=copper2gold(people[x]["cash"]["copper"])
        partyCash+=silver2gold(people[x]["cash"]["silver"])
        partyCash+= people[x]["cash"]["gold"]
        partyCash+=platinum2gold(people[x]["cash"]["platinum"])
        partyCash=round(partyCash,2)
    return partyCash
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    Interesting = []
    for x in range(len(investors)):
        if investors[x]["profitReturn"] <10:
            Interesting.append(investors[x])
    return Interesting
def getAdventuringInvestors(investors:list) -> list:
    Adventurers = []
    interesting =getInterestingInvestors(investors)
    for x in range(len(interesting)):
        if interesting[x]["adventuring"] == True:
            Adventurers.append(interesting[x])
    return Adventurers


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    important_people =getAdventuringInvestors(investors)
    foodcosts = getJourneyFoodCostsInGold(len(important_people),len(important_people))
    tent_horse_costs = getTotalRentalCost(len(important_people),len(important_people))
    item_costs = getItemsValueInGold(gear)*len(important_people)
    return foodcosts+tent_horse_costs+item_costs
##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    Human = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT*people)
    Horse = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT*horses)
    total_costs = Human+Horse
    total_days = trunc(leftoverGold/total_costs)
    return total_days


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    Human_costs = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)*people
    Horse_costs = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)*horses
    totalCostsPerNight = Horse_costs+Human_costs
    return round(totalCostsPerNight*nightsInInn,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    AmountOfGold = []
    
    investors = getInterestingInvestors(investors)
    for x in range(len(investors)):
        print(round(profitGold/100*investors[x]["profitReturn"],2))
        AmountOfGold.append(round((profitGold/100)*investors[x]["profitReturn"],2))
    return AmountOfGold

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()