letterA = {"A", "B", "C", "D", "D"}
letterB = {"E", "E", "F", "G", "B"}
letterC = ["A", "B", "C", "D", "D"]
letterD = ["Z", "S", "W", "L"]

union = letterA | letterB
intersection = letterA & letterB

unionList = set(letterC) | set(letterD)
intersectionList = set(letterC) & set(letterD)

differenceA = letterA - letterB
differenceB = letterB - letterA
print(f"Union from set is {union}") # Union
print(f"Intersection from set is {intersection}") # Intersection

print(f"Union from List [] is {unionList}") #Union
print(f"Intersection from List [] is {intersectionList}") #Intersection
print(f"DifferenceA from set {differenceA}") #Difference
print(f"DifferenceB from set {differenceB}") #Difference