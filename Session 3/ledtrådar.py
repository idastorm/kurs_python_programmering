# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:53:25 2020

@author: Ida Storm
"""
class Utmaning_löner:

    def ledtråd1():
        print("Förslagsvis skapar du en ny lista och lägger till ett värde varje gång du loopar över en lön")
        
    def ledtråd2():
        print("Varje nytt värde ska vara 5% av lönen, lön*0.05 i loopen får fram detta värdet")
        
    def ledtråd3():
        print("sum() är en inbyggd funktion som ger det totala värdet av alla tal i en lista")
        
    def lösning():
        print("bonusar=[]\nfor lön in löner:\n   bonus=lön*0.05\n   bonusar.append(bonus)\nprint(sum(bonusar)")

class Utmaning_index:
    
    def ledtråd1():
        print("Kom ihåg att indexering i programmeringsspråk börjar på 0")

    def ledtråd2():
        print("Om det första elementet elementet i en lista är list[0] kan det sista elementet fås genom att indexera 'bakåt'")

    def ledtråd3():
        print("Om det sista elementet är list[-1], och man kan indexera bakåt, vad är då elementet för det? Tänk årtal f. Kr.")
        
class Utmaning_namn:
    
    def ledtråd1():
        print("Ett dubbelnamn har antingen ett mellanrum ( ) eller ett bindesteck (-) i namnet. Använd det i din if-sats. (if ' ' in namn)")
    
    def ledtråd2():
        print("För att undersöka om namnet har ett mellanrum ELLER ett bindestreck, använd or i din if-sats.")
        
    def lösning():
        print("for namn in mest_populära_killnamn_2014:\n    if '-' in namn or ' ' in namn:\n        print(namn)")
              
