from cmath import cos
import time
from termcolor import colored
from data import JOURNEY_IN_DAYS,COST_FOOD_HORSE_COPPER_PER_DAY,COST_FOOD_HUMAN_COPPER_PER_DAY
from data import mainCharacter

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
    total_copper = (COST_FOOD_HUMAN_COPPER_PER_DAY*people+COST_FOOD_HORSE_COPPER_PER_DAY*horses)*JOURNEY_IN_DAYS
    return copper2gold(total_copper)
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
    my_list = []
    adventur = getAdventuringPeople(friends)
    share = getShareWithFriends(friends)
    combo = adventur+share
    for x in friends:
        if x not in my_list:
            my_list.append(x)
    return my_list


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

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