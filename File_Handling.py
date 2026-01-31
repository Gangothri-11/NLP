f = open("demo.txt", "r")
print(f.read())

with open("demo.txt") as f:
  print(f.read())

f = open("demo.txt")
print(f.readline())
f.close()

with open("demo.txt") as f:
  print(f.read(5))

with open("demo.txt", "a") as f:
  f.write("Now the file has more content!")
with open("demo.txt") as f:
  print(f.read())
