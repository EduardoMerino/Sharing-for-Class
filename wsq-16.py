txt=open("93cars.dat.txt","r") # mode 'r' the file will only be read
cgm=0 #gas mileage in city
hgm=0 #gas mileage on highway
price=0 #price of the car
l=1 #this is a control for reading the lines
cars=0 #amount of cars
for line in txt: #divides the file by lines
    if l%2==1: #reads every other line (the one with the data)
        cgm=cgm+float(line[52:54])#place in text where the city milage is
        hgm=hgm+float(line[55:57])
        price=price+float(line[42:46])
        cars=cars+1
    l=l+1
ac=round(cgm/cars,5) #avarage city
ah=round(hgm/cars,5) #avarage highway
ap=round(price/cars,5)#avarage price7

#code:
print("there are ",cars," different cars")
print("the average gas mileage in city is: " ,ac)
print("the average gas mileage on highway is: " ,ah)
print("the average midrange price of the vehicles in the set is: " ,ap)
