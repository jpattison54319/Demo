label cornmaze:
    $ userOrder = []
    $ counter = 0
    scene cornmaze
    "You go deeper into the cornfield and suddenly get lost. You dont remember how to get out."
    "It almost seems like some parts of the maze might have shuffled."
    "You hear an ominous voice speaking words as if whispering in your ear."
    "Telling break of day, A barrelled, hairy gun barks, in spite of the bird"

    label cornmazeMain:
        menu:
            e "Where should I go to get out?"

            "Go NORTH":
                e "Imma try going north!"
                $ userOrder.append("NORTH")
                $ counter+=1
            "Go EAST":
                e "Imma try going east!"
                $ userOrder.append("EAST")
                $ counter+=1
            "Go SOUTH":
                e "Imma try going south!"
                $ userOrder.append("SOUTH")
                $ counter+=1
            "Go WEST":
                e "Imma try going west!"
                $ userOrder.append("WEST")
                $ counter+=1
            "Remember Haiku":
                "Telling break of day.
                A barrelled, hairy gun barks.
                in spite of the bird"
                jump cornmazeMain
            "Listen for sounds":
                "You hear a rooster's loud and piercing cock-a-doodle-do coming from the NORTH,
                deep growls and earth-shattering popping noises from the EAST, loud engine noises to your WEST, and whispers to your WEST"
                jump cornmazeMain
            "Start fresh":
                "You succumb to the maze, reappearing back in the center, clean slate."
                $ userOrder.clear()
                $ counter = 0
                jump cornmazeMain

        jump cornmaze2

    label cornmaze2:
        menu:
            e "Where should I go to get out?"

            "Go NORTH":
                e "Imma try going north!"
                $ userOrder.append("NORTH")
                $ counter+=1
            "Go EAST":
                e "Imma try going east!"
                $ userOrder.append("EAST")
                $ counter+=1
            "Go SOUTH":
                e "Imma try going south!"
                $ userOrder.append("SOUTH")
                $ counter+=1
            "Go WEST":
                e "Imma try going west!"
                $ userOrder.append("WEST")
                $ counter+=1
            "Remember Haiku":
                "Telling break of day.
                A barrelled, hairy gun barks.
                in spite of the bird"
                jump cornmaze2
            "Listen for sounds":
                "You hear loud deep growls and earth-shattering popping noises from the NORTH,
                beautiful birds singing to the EAST, frogs croaking vicuously to your WEST, and high pitch screaming to your WEST"
                jump cornmaze2
            "Start fresh":
                "You succumb to the maze, reappearing back in the center, clean slate."
                $ userOrder.clear()
                $ counter = 0
                jump cornmazeMain

        jump cornmaze3

    label cornmaze3:
        menu:
            e "Where should I go to get out?"

            "Go NORTH":
                e "Imma try going north!"
                $ userOrder.append("NORTH")
                $ counter+=1
            "Go EAST":
                e "Imma try going east!"
                $ userOrder.append("EAST")
                $ counter+=1
            "Go SOUTH":
                e "Imma try going south!"
                $ userOrder.append("SOUTH")
                $ counter+=1
            "Go WEST":
                e "Imma try going west!"
                $ userOrder.append("WEST")
                $ counter+=1
            "Remember Haiku":
                "Telling break of day.
                A barrelled, hairy gun barks.
                in spite of the bird"
                jump cornmaze3
            "Listen for sounds":
                "You hear loud deep growls and earth-shattering popping noises from the NORTH,
                thumping engine noises to the EAST, frogs croaking vicuously to your WEST, and beautiful, melodious chirping to your WEST"
                jump cornmaze3
            "Start fresh":
                "You succumb to the maze, reappearing back in the center, clean slate."
                $ userOrder.clear()
                $ counter = 0
                jump cornmazeMain
        if userOrder == cornfieldOrder:
            "You have successfully exited the maze, returning back to the entrance to the cornfield"
            e "Sick! I can finally get to work now that I found my way out."
            jump cornfieldChoices
        else:
            "You suddenly fade into nothingness, as if you drifted away in the wind to only find yourself
            back in the center of the maze a few moments later."
            $ userOrder.clear()
            $ counter = 0
            jump cornmazeMain
    return