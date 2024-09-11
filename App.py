


#--------------------
#Manage data with python ditionarier 
#Task: Analyze the solar system. 
#task: Analys the number of moons on different planets in the solar system 
#Task: you want to display the information to the user 

#create dictionary 
planets ={
    'name': 'earth', 
    'moons': 1, 
}

#read dictionary 
print(planets.get('name'))
#another way to read dictionary 
print(planets['name'])

#modify key value 
planets.update({'name': 'Makemake'})

planets.update({

    'name':'hej',
    'moons': '4'

})
print(planets['name'])

#add and remove key 
planets['orbital period'] = 4333

#Remove the key 
planets.pop('orbital period')

#add adress, nested dictionary 
planets['diameter (km)'] = {

    'polar':33556,
    'Equatorial': 34522

}

#retreive data from nested dictionary 
print(f'{planets["name"]} polar diameter: {planets["diameter (km)"]['polar']}')

#lista = List_namn{}
#hämta något från listan = ['value']
#hämta en kategori i listan {List_name['name på subkategori']['namn_på_det jag vill hämta']}

#exercise
planets = {
    'name':'Mars',
    'moons': 2
}
#display data 
print(planets['name'])
print(f'planet {planets['name'] } has {planets['moons']}')

planets['circumference (km)'] = {
    'polar': 6757,
    'equatorial': 6792

}
print(f'{planets['name']} has a polar circumference  of {planets['circumference (km)']["polar"]}')

#dynamic programming with dictionaries 
#dictionary storing data about rainy days 
#keys() iterate over a list in 

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
#display list 
for key in rainfall.keys(): #för varje nyckel i tabell rainfall(nyckel)
    print(f'{key}: {rainfall[key]} cm') #skriv ut nyckel 

#determine if key exist in dictionary 
#om order ' december ' finns i listan rainfall kör kod nedanför 
if 'december' in rainfall: 
    # i listan rainfall värder 'december vill vi öka med 1(+1)
    rainfall['december'] = rainfall['december'] + 1 
else:
    #om inte december finns skapar vi den med värdet 1 
    rainfall['december'] = 1


#retrrive all values
# total rainfall at al 
total_rainfall = 0 
#get all values in the list 
for value in rainfall.values(): 
    #lägg till värdet från varje rad i listan till totalen
    total_rainfall = total_rainfall + value

#skriv ut listan
print(f'if there was any rainfall {total_rainfall} cm in the last quarter')

#dynamic programming with 
#task -  you will calculate both the total number of moons in the solar system and the average number of moons a planet has. 

planets_moon = {
    'mercury': 0,
    'venus':0,
    'earth':1,
    'mars':2,
    'jupyter':79,
    'saturn':82,
    'uranus':27,
    'neptune':14,
    'pluto':5,
    'haumea':2,
    'makemake':1,
    'eris':1

}

#all value of the list planet_moon stores in moons
moons = planets_moon.values()

#obtain the total number of plantes and store the value in a valriable total planet 
total_planets = len(planets_moon.keys())
#calculate avg

#Start by creating a variable named total_moons
total_moons = 0
#Then add a for loop to loop through the list of moons, adding each value to total_moons
for moon in moons: 
    total_moons = total_moons + moon 


average = total_moons / total_planets

print(f'Each planet have an average of {average} moons')

#Learnings
#Acess all key values .key()
#use . get{} to retrive all values + keys in a list. 
#--------------------------------------------------------

#python functions  - Organise data about a rocket 
#create function , empty() mean no argument needed
def rocket_parts():
    print("payload", "propellant", "structure")
    return 
#call function 
rocket_parts()

def rocket_part():
    return "payload", "propellant", "structure"
output = rocket_parts()
output

#any(True)
#str()

#function to calculate the distance insice the spacecraft 
def disance_from_earth(destination):
    if destination  == 'Moon':
        return "238,455"
    else:
        return "unable to comput that destination"
disance_from_earth("Moon") 

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
print(distance_from_earth("Moon"))

#calculate how many days it take 
#Let's create a function that can calculate how many days it takes to reach a destination, given distance and a constant speed:

#multiple arguments 
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24
days_to_complete(238855, 75)
print(days_to_complete(238855, 75))

#avrunda det 
total_days = days_to_complete(238855, 75)
round(total_days)
print(total_days)

#Task: fuel report: throughout the rocket ship
#Task: display the amount of fuel in each tank

def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)
generate_report(80, 70, 75)

#use keywords argument in python 
#Let's create a function that returns the estimated time of arrival by using the same value as the Apollo 11 mission as the default:
from datetime import timedelta, datetime

def arrival_time(hours=0):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

#Anoth example for key argument 
#animal 
def animal_classifications(animal): 
    #animal dictionary 
    animal_dictionary = {
        "Dog": "Mammal",
        "Eagle": "Bird",
        "Shark": "Fish",
        "Frog": "Amphibian",
        "Cobra": "Reptile"
    }
    
    return animal_dictionary.get(animal, "Unknown classification")

print(animal_classifications("Dog"))
print(animal_classifications("Eagle")) 
print(animal_classifications("Tiger"))

#user variable arguments 
def variable_length(*arg):
    print(arg)

#variable length function that can calulate how many minutes until launch, give you how mich time each step is going to take:
def sequence_time(*arg):
    total_minutes = sum(arg)
    if total_minutes < 60:
        return f"total time to launch is {total_minutes} minutes"
    else: 
        return f"total time to launch {total_minutes/ 60} hours"
    
print(sequence_time(4, 14, 18))

#example two with Exersice duration time 
def total_exercise_time(*durations):
    total_time = sum(durations)
    if total_time < 60:
        return f"Total minutes exercised today:  {total_time}"
    else:
        return f"Total hourse exersices today:{total_time}"

print(total_exercise_time( 1, 15, 1))

#kwargs -----------
def variable_length(**kwargs): #kwargs allow to pass any number of name arguments to a function
    print(kwargs)
    
#collect all the arguments in a function
variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

#report the astronauts assigned to the mission
def assigned_austronauts(**kwargs):
    print(kwargs)

assigned_austronauts(austronatus= 10, mission ="pluto", pilots=3) 
{'austronatus': 10, "mission": "pluto", 'pilots': 3}

#crewmemebers 
def crew_members(**kwargs):
    print(f"{len(kwargs)} austronauts assigned for this mission")
    for title, name in kwargs.items(): 
        print(f"{title}:{name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

#create an updated fuel report -----------
#1.Create an updated fuel report function
def fuel_report(**fuel_tank):
    for name, value in fuel_tank.items():
        print(f"{name}:{value}")

fuel_report(main="50", exteral="100", emergency="60")
              