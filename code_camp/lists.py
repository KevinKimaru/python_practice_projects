#to access lists from the end use negative numbers,,:note// the last in the list is -1

#list slicing
#my_list[start:end] //end is excluded while start is included
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[0:6]
upstairs = areas[6:10]
print(downstairs)
print(upstairs)

# length of a list, max, sort
print(len(areas))
x = [1,5,89,90,45]
print(max(x))
print(sorted(x, reverse=True))
print(sorted(x, reverse=True))

downstairs = areas[:6]
upstairs = areas[6:]
print(downstairs)
print(upstairs)

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
print(x[2][0])
print(x[-1][:2])

# to dlete from alist
del (areas[1])
print(areas)

#to explicitely copy a list
areas_copy = areas[:]
areas_copy2 = list(areas)

#methods for a string
room = "pool"
print(room.upper())
print(room.count("o"))
print(areas.append("KING"))

#methods for a list
print(areas.index("kitchen"))
print(areas.count("kitchen"))
areas.append("sittingroom")#to add to a list
print(areas)
areas.remove("kitchen")#removes the first occurrence
print(areas)
areas.reverse()#reverse
print(areas)

