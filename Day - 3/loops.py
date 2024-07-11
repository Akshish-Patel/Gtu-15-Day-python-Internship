#  While Loop

print("\n\nWhile Loop")
i = 0
while (i < 5): 
	print(i)
	i+=1


# for Loop
print("\n\nFor loop")
for i in range(5): # here range function is gives the list of 0-4 values
    print(i)

l = ["ram", "shyam", "om"]
for i in l:
    print(i)

# Nested Loops

print("\n\nNested Loops")
for i in range(1, 5):
	for j in range(i):
		print(i, end=' ')
	print()


# Loop Control Statements

# break (break statement is use to stop the flow of the loops generaly it is used in the infinite loops)
print("\n\nBreak statement")

i=0
while True:
	print(i)
	if(i == 5):
		print("brake statement execute")
		break
	i+=1
	
# continue (continue statement is use to skip the further statement for that iteration)
print("\n\nBreak statement")
i = 0
while(i <= 5):
	if(i == 3):
		print("continue statement execute")
		i+=1
		continue
	print(i)
	i+=1