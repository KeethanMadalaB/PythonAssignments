str_x = "Emma is a good developer, Emma is a writer, Emmaaa and Emma".split(" ")
count=0

for i in str_x:
    if i == "Emma": count+=1

print("Emma appeared",count,"times")
print("Emma" in str_x)