grades={
    ("John","Math"):5,
    ("Alice", "Biology"):4,
    ("Bob", "Physics"):3.5,
    ("Eve", "Music"):5,
    ("John", "English"):4
}
#John's grade in math
print(grades["John", "Math"])
#add a grade to bob in math
grades[("Bob", "Math")]=3
print(grades)

#how to get all of the students names
keys=list(grades.keys())
print(keys)
