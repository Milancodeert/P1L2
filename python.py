def naam_en_leeftijd():
    input("wat is je naam?")
    input("Wat is jouw leeftijd?")
    print("Jouw naam is", naam, "en jouw leeftijd is", leeftijd)
    
naam_en_leeftijd()
def vraag_input(onderwerp):
    input("geef me een onderwerp:")
    return input("geef me een" + onderwerp + ": ")
