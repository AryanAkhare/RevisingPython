# #Creating dictionaries
band={
    "vocals":"Plant",
    "guitar":"Page"
}
band2=dict(vocals="Plant", guitar="Page")
print(band)
print(band2)
print(type(band))
print(len(band))
 
#Accessing items
print(band["vocals"])
print(band.get("guitar"))

#list all keys and values
print(band.keys())
print(band.values())

#as tuples
print(band.items())

#verify key exist
print("guitar" in band)
print("instu" in band)

#change values
band["vocals"]="Coverdale"
band.update({"base":"JPG","vocals":"Plants"})
print(band)

#remove items
print(band.pop("base"))
print(band)

print(band.popitem()) #removes last item added
print(band)

#delete and clear
band["drums"]="Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2
#copying dicts

#wrong way , both var refers saem thing
#band2=band 

#correct way
band2=band.copy()
print(band)
print(band2)


#nested dictionaries
member1={
    "name":"Plant",
    "instrument":"vocals"
}
member2={
    "name":"Page",
    "instrument":"guitar"
}
band3={
    "mem1":member1,
    "mem2":member2
 }
print(band3)
print(band3["mem1"]["name"])

# #SETS -- no duplicates
nums={
    1,2,3,4
}
nums2=set((2,4,6,8))
print(nums)
print(nums2)
print(len(nums2))
print(type(nums))

nums3={1,2,3,4,4}
print(nums3)
#True is 1 , false is 0 so considers duplicates
#if 1 is first , true is duplicate and removes true , and vice versa

nums4={True,2,3,False,0}
print(nums4)
nums5={1,True,2,3,0,False}
print(nums5)

print(2 in nums5) #cant be refferd value by index or key

#adding new element into set
nums.add(8)
print(nums)

#add sets into another --can be used by dic,list,tuple
nums.update(nums4)
print(nums)

#merging two sets to create new set
one={1,2,3}
two={5,6,7}
newset=one.union(two)
print(newset)

#keep only duplicates of two sets
one={1,2,3}
two={2,3,4}
one.intersection_update(two)
print(newset)
#keep except duplicates of two sets
one={1,2,3}
two={2,3,4}
one.symmetric_difference_update(two)
print(newset)