responses = {"cześć": "Witaj, młody wędrowcze!", "gdzie jestem?": "Jesteś w magicznej krainie" }

def talk(player_input):
    return responses.get(player_input.lower(), "Nie rozumiem")
