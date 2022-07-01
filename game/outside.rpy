# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    call variables from _call_variables
    call characters from _call_characters

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    e "Man what a night I had last night, cant believe I have to start this new job being a nightly janitor for this elementary school"

    e "Im just happy I get a decent paycheck that will put food on the table, and beer in my belly"

    e "Hmmm, so I just arrived, should I get straight to work?"

    label parking_lot:
        e "I am currently standing in the parking lot. I see a playground on the left side of the school, baseball field to the right."
        e "I also see a parked car in this parking lot, I thought I was suppose to be the only one here?"
        label parkingLotChoices:
            menu:
                e "What should I do?"

                "Explore Playground":
                    e "Looks like I am gonna have some fun on the playground before my shift"
                    jump playground

                "Explore baseball field":
                    $ drank_tea = True
                    e "Looks like i am gonna have some fun on the baseball field before my shift"
                    jump baseballField

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
                    $ slidDownSlide = True
                    e "Weeee, damn that was fun! Made me feel like a kid again."
                    e "I could have sworn I felt something fall out of that slide."
                    $ roomItems["playground"].append(playgroundItem)
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
    
    label baseballField:
        "This is a nice baseball field"
        return

    label parkedCar:
        e "Hmm, this car is empty."
        return

    label schoolFrontDoor:
        "Time for work, I should probably open the door now!"
        return
    label behindSchool:
        scene dumpsters
        e "Smells like trash!"
        
        return

    # This ends the game.

    return
