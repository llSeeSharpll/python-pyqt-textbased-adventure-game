sword = 0
flower = 0


#The story is broken into sections, starting with "intro"
class Intro():
  intro = "After a drunken night out with friends.\nyou awaken the\
  next morning in a thick, dank forest.\nHead spinning and\
  fighting the urge to vomit.\nyou stand and marvel at your new,\
  unfamiliar setting.\nThe peace quickly fades when you hear a\
  grotesque sound\nemitting behind you.A slobbering orc is\
  running towards you.\nYou will:"

  choiceA = " Grab a nearby rock and throw it at the orc"
  choiceB = " Lie down and wait to be mauled"
  choiceC =" Run"

#Option rock
class Option_Rock():
  option_Rock="The orc is stunned, but regains control.\nHe begins\
  running towards you again.\nWill you:"
  choiceA = " Run"
  choiceB = " Throw another rock"
  choiceC = " Run towards a nearby cave"


#Option Run
class Option_Run():
  option_Run = "You run as quickly as possible, but the orc's speed is too great.\nYou will:"
  option_Run_cave = ""
  choiceA = " Hide behind boulder"
  choiceB = " Trapped, so you fight"
  choiceC = " Run towards an abandoned town"


class Option_Cave():
  option_Cave = "You were hesitant, since the cave was dark and ominous.\nBefore you fully enter, you notice a shiny sword on the ground.\nDo you pick up a sword?"
  choiceY = "Yes"
  choiceN = "No"

class Option_Cave_2():
  option_Cave_2 = "What do you do next?"

  choiceA = " Hide in silence"
  choiceB = " Fight"
  choiceC = "Run"

class Option_Town():
  option_Town = "While frantically running, you notice a rusted sword lying in the mud.\n\
    You quickly reach down and grab it,but miss.\n\
    You try to calm your heavy breathing as you hide behind a delapitated building,\n\
    waiting for the orc to come charging around the corner.\n\
    You notice a purple flower near your foot.\n\
    Do you pick it up?"
  
  choiceY = "Yes"
  choiceN = "No"

class Option_Town_2():
  option_Town_2 = "You hear its heavy footsteps and ready yourself for the impending orc."
  choiceA = "Give the orc a flower"
  choiceB = "Hide in abandant building"
  choiceC = "No where to run. Prepare to fight"
