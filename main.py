subject = input("Enter the subject: ")
hours = input("Enter studied hours: ")
with open("data.txt", "a") as file:
  file.write(subject + "," + hours + "\n")
print("Saved successfully")
total = 0
with open("data.txt", "r") as file:
  for line in file:
    parts = line.strip().split(",")
    if len(parts) == 2:
      subject, hours = parts
      try:
          total += float(hours)
      except ValueError:
       continue 
print("Total hours studied: ", total)






























