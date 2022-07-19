label mainEntrance:
    $ checkedSurr = False
    scene mainEntrance
    "You open the door and walk inside. Immediately then door slams shut behind you. You suddenly feel a cool shiver down your spine."
    label mainEntranceChoices:
        menu:
            "What should I do?"

            "Check front doors behind you":
                return

            "Investigate your surroundings":
                #TODO Skinny fills in surrounding description
                ""
                $ checkedSurr = True
                jump mainEntranceChoices
            
            "Go WEST to Principle's Office" if checkedSurr:
                if keyCheck():
                    jump principlesOffice
                e "[doorLocked]"
                jump mainEntranceChoices
            
            "Go EAST to 2nd floor staircase" if checkedSurr:
                "You're standing in front of the stairs."
                "You notice a door that leads to a room under the steps with a sign saying \"mainenance\""
                menu:
                    "What should I do?"

                    "Go up the stairs":
                        jump staircaseTo2

                    "Go into the maintenance room":
                        jump maintenance
            
            "Go NORTH, proceed down main hallway" if checkedSurr:
                if keyCheck():
                    jump mainHall1
                e "[doorLocked]"
                jump mainEntranceChoices

label mainHall1:

label principlesOffice:

label staircaseTo2:

label maintenance:
    "You enter a dark musty room that looks like it hadn't been organized or cleaned for years. 
    The room is dead silent, except for the eerie persistant  “drip drip drip” falling from one of the pipes that mazed the ceiling. 
    Rusty tools and supplies litter the tall metal shelves that line the wall in front of you. 
    To your left is a abnormally large desk luminated by the soft glow from a lamp that turned out to be the only light source in the room. "

    menu:
        "What should I do?"

        "Investigate desk":
            "The metal desk stood in front of you cluttered with crinkled papers, crumbs, and wrappers."
            e "It looks like this is the office and cafeteria to me"
            "On the center of the desk lies a coffee stained note on top of all the usless clutter."
            menu:
                "Take and read note":
                    return
                "Leave and do not read note":
                    return


            

        "Investigate metal shelves":
            return
    return



            

