import math

def Query():
    print("Enter Three Numbers And This Program Will Determine If It Is A Valid Pythagorean Tripple")
    print("                     Please Type Q To Escape Or S To Start")
    response = input("Input Q Or S: ")
    if response in "QqQuitquit":
        return
    elif response in "SsStartstart":
        GatherInputs()
    else: 
        print("Invalid Input, Try Again.");
        Query();

def GatherInputs():
    print("")
    coords = []
    x = input("Enter Side X: ")
    coords.append(int(x))
    y = input("Enter Side Y: ")
    coords.append(int(y))
    z = input("Enter Side Z: ")
    coords.append(int(z))
    hypot = 0;
    sides = []
    for i in range(len(coords)):
        if(coords[i]>hypot):
            hypot=coords[i]
    for coord in coords:
        if coord!=hypot:
            sides.append(coord)
    CheckTripple(hypot,sides)

def CheckTripple(hypotenous, sides):
    if(math.pow(sides[0],2)+math.pow(sides[1],2)==math.pow(hypotenous,2))and hypotenous%1==0:
        print();
        print("This Is A Pythagorean Triple, Congrats For Finding One!")
        print();
        Query()
    else:
        print();
        print("This Is Not A Pythagorean Triple.")
        print()
        Query()

def main():
    Query();

if __name__=="__main__":
    main()