# ------------------------- Creating Dictionaries -------------------------
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# ------------------------- Accessing Items -------------------------
print(band["vocals"])
print(band.get("guitar"))

# ------------------------- Listing Keys and Values -------------------------
print(band.keys())
print(band.values())

# As Tuples
print(band.items())

# Verify Key Existence
print("guitar" in band)
print("instu" in band)

# ------------------------- Changing Values -------------------------
band["vocals"] = "Coverdale"
band.update({"base": "JPG", "vocals": "Plants"})
print(band)

# ------------------------- Removing Items -------------------------
print(band.pop("base"))
print(band)

print(band.popitem())  # Removes last added item
print(band)

# ------------------------- Delete and Clear -------------------------
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

# del band2  # Uncommenting this would delete the variable

# ------------------------- Copying Dictionaries -------------------------
# Wrong way: band2 = band  (Both refer to same object)
band2 = band.copy()
print(band)
print(band2)

# ------------------------- Nested Dictionaries -------------------------
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band3 = {
    "mem1": member1,
    "mem2": member2
}
print(band3)
print(band3["mem1"]["name"])

# ------------------------- Sets -------------------------
nums = {1, 2, 3, 4}
nums2 = set((2, 4, 6, 8))
print(nums)
print(nums2)
print(len(nums2))
print(type(nums))

nums3 = {1, 2, 3, 4, 4}
print(nums3)  # No duplicates

# True is 1, False is 0 (so duplicates are removed)
nums4 = {True, 2, 3, False, 0}
print(nums4)

nums5 = {1, True, 2, 3, 0, False}
print(nums5)

# ------------------------- Set Operations -------------------------
print(2 in nums5)

# Add new element
nums.add(8)
print(nums)

# Add values from another iterable
nums.update(nums4)
print(nums)

# Merge sets into a new one
one = {1, 2, 3}
two = {5, 6, 7}
newset = one.union(two)
print(newset)

# Keep only duplicates (intersection)
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# Keep elements except duplicates (symmetric difference)
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
