﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    call variables from _call_variables 
    call characters from _call_characters

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    e "Man what a night I had last night, cant believe I have to start this new job being a nightly janitor for this elementary school"

    e "Im just happy I get a decent paycheck that will put food on the table, and beer in my belly"

    label parking_lot:
        scene parkinglot
        e "Hmmm, so I just arrived, should I get straight to work?"
        e "I am currently standing in the parking lot. I see a playground on the left side of the school and a cornfield to the right."
        e "I also see a parked car in this parking lot, I thought I was suppose to be the only one here?"
        label parkingLotChoices:
            scene parkinglot
            menu:
                e "What should I do?"

                "Explore Playground":
                    e "Looks like I am gonna have some fun on the playground before my shift"
                    jump playground

                "Explore cornfield":
                    e "I wish I grew up on a farm"
                    jump cornfield

                "Explore parked car":
                    e "I really should be the only one here, lets take a look at this parked car!"
                    jump parkedCar

                "Explore schools front entrance":
                    e "Playtime can be done later, I have lots of work to do if I want to keep this job!"
                    jump schoolFrontDoor

    label playground:
        scene playground
        e "Alright, im at the playground, but why? I really need to get to work."
        e "Hmmm there seems to be some dumpsters behind the school, or maybe I should just head inside the school without smelling like trash"

        label playgroundChoices:
            menu:
                e "What should I do?"

                "Slide down the slide":
                    if not slidDownSlide:
                        e "Weeee, damn that was fun! Made me feel like a kid again."
                        e "I could have sworn I felt something fall out of that slide."
                    else:
                        e " Weee, never gets old!"
                    $ roomItems["playground"].append(playgroundItem)
                    $ slidDownSlide = True
                    jump playgroundChoices

                "Pick up item off the floor that fell from the slide" if (slidDownSlide and playgroundItem in roomItems["playground"]):
                    e "Oh sick, im not really a smoker but I wont turn down free matches."
                    menu:
                        "Keep [playgroundItem]": 
                            e "Im going to put these in my pocket to keep them for later."
                            $ inventory.append(playgroundItem)
                            $ roomItems["playground"].remove(playgroundItem)
                            jump playgroundChoices
                        "Discard [playgroundItem]":
                            e "On second thought, these would just be junk anyways."
                            jump playgroundChoices
                "Go back to parking lot":
                    jump parkingLotChoices
                "Explore behind the school":
                    jump behindSchool

            return
    
    label cornfield:
        scene cornfield
        e "This is a nice cornfield, but probably shouldn't go in too deep, things a maze!"
        label cornfieldChoices:
            menu:
                "What should you do?"

                "Go deeper in the cornfield":
                    e "I really shouldn't go deeper but I can't resist the urge."
                    call cornmaze from _call_cornmaze
                    jump cornfieldChoices

                
                "Explore behind the school":
                    jump behindSchool
                
                "Explore parking lot":
                    jump parkingLotChoices
        return

    label parkedCar:
        scene car
        e "Hmm, this car is empty."
        e "Maybe there is another janitor inside I wasnt told about?"
        label parkedCarChoices:
            menu:
                e "What should I do?"

                "Try to open car door":
                    e "Im not getting in, its locked."
                    jump parkedCarChoices
                "Break window" if not carWindowBroke:
                    $ carWindowBroke = True
                    e "Im not a bad person, just curious"
                    "You hit the window at the bottom left corner and it shatters into a thousand pieces."
                    e "Shit, my hand is bleeding, But nothing major."
                    jump parkedCarChoices

                "Search the inside of the car" if carWindowBroke:
                    e "Well, since I broke the window I might as well see whats inside."
                    label insideCar:
                        menu:
                            "Check glove box":
                                e "Doesn't seem to be anything in the glove box."
                                jump insideCar
                            "Check center console":
                                e "Doesn't seem to be anything in the center console."
                                jump insideCar
                            "Look under seats":
                                if insideCarItem not in inventory:
                                    e "Just an empty plastic water bottle."
                                    menu:
                                        "Take water bottle":
                                            e "Might come in handy later, if I get thirsty I guess."
                                            $ inventory.append(insideCarItem)
                                            $ roomItems["insideCar"].remove(insideCarItem)
                                            jump insideCar
                                        "Leave water bottle":
                                            e "This man needs to clean his car, Im not going to do it for him"
                                            jump insideCar
                                else:
                                    e "Just an empty plastic water bottle."
                                    jump insideCar

                        jump parkedCarChoices
                            
                "Walk away from car":
                    jump parkingLotChoices
        return

    label schoolFrontDoor:
        "Time for work, I should probably open the door now!"
        menu:
            "What should I do?"

            "Go inside":
                jump mainEntrance

            "Go back to parking lot":
                jump parkingLotChoices
        

    label behindSchool:
        scene dumpsters
        "You see dumpsters in front of you, and the playground / baseball field on either side of the school"
        e "Smells like trash!"

        label dumpsterChoices:
            menu:
                e "What should I do?"

                "Look under dumpster":
                    e "Well, not sure what im really looking for but theres nothing under here."
                    jump dumpsterChoices
                "Look inside dumpster":
                    e "As far as dumpsters go, this is definitely one of the cleanest ones ive seen"
                    if dumpsterItem in roomItems["dumpster"]:
                        menu:
                            "There is a single clove of garlic inside the dumpster"

                            "Take garlic":
                                e "Come to think of it, I did forget my lunch!"
                                $ inventory.append(dumpsterItem)
                                $ roomItems["dumpster"].remove(dumpsterItem)
                                jump dumpsterChoices
                            
                            "Leave garlic":
                                e "Probably for the best I dont smell like garlic."
                                jump dumpsterChoices
                    else: 
                        "Dumpster is empty"
                        jump dumpsterChoices
                    
                "Explore cornfield":
                    e "Lets go harvest some corn!"
                    jump cornfield
                "Explore playground":
                    jump playground

        return

    # This ends the game.

    return
