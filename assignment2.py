import random
#Question1
L = [10, 20, 30, 40, 50, 60, 70, 80]
L.append(200)
L.append(300)
L.remove(10)
L.remove(30)
L.sort()#ascending
L.sort(reverse=True)#descending

#Question2
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
max_score = scores.index(max(scores))
print(max_score)
min_score = min(scores)
print(min_score)
print(f'Count of min score in list is: {scores.count(min_score)}')
print(f"reversed list is: {list(reversed(scores))}")
x = int(input("Enter number:"))
if x in scores:
    print(scores.index(x))
else:
    print("Key not present")

#Question3
l = []
for i in range(0, 100):
    l.append(random.randint(100, 900))
odd = [x for x in l if x % 2 != 0]
even = [x for x in l if x % 2 == 0]
prime = []
print(f'Odd numbers count: {len(odd)}')
print(odd)
print(f'Even number count: {len(even)}')
print(even)

#Question4
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
unique_scores = A.union(B)
common_scores = A.intersection(B)
exclusive_scores = A.symmetric_difference(B)
count = 0
for score in A:
    if score in B:
        count += 1

if count == len(B):
    print("A is subset of B")

score = int(input("Enter score:"))
if score in A:
    A.discard(score)
else:
    print("Score not in A")

#Question5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York",
}
sample_dict.update({"location": sample_dict.pop("city")})
print(sample_dict)
