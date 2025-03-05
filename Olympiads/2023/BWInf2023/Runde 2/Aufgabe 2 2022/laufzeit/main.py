import random
lst=["Python", "Java", "C++", "CSS"]
for n in range(10):
    s=random.choices(lst,cum_weights=(3,6,9,12),k=3)
    print("In iteration",n,"Weighted Random is:", s)
