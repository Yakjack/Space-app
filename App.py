


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