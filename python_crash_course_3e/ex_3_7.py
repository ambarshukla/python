guest_list=['Tendulkar','Kohli','Ganguly']

print("List initially is ", end="")
print(guest_list)

print(f"I would like to invite {guest_list[0]} to dinner in Mumbai")
print(f"I would like to invite {guest_list[1]} to dinner in Delhi")
print(f"I would like to invite {guest_list[2]} to dinner in Kolkata")

print(f"Uh oh {guest_list[0]} cant make it, changing to Laxman")
guest_list.remove('Tendulkar')
guest_list.insert(0,'Laxman')
print("List now is ", end="")
print(guest_list)
print(f"I would like to invite {guest_list[0]} to dinner in Hyderabad")
print(f"I would like to invite {guest_list[1]} to dinner in Delhi")
print(f"I would like to invite {guest_list[2]} to dinner in Kolkata")

print("Players from other countries joining also... Chaminda at start, Lara in middle, Pietersen at end")
guest_list.insert(0,'Chaminda')
guest_list.insert(3,'Lara')
guest_list.append('Pietersen')
print("Final list is ", end="")
print(guest_list)


last_name = guest_list.pop()
print(f"Sorry {last_name} you cannot come to dinner")
last_name = guest_list.pop()
print(f"Sorry {last_name} you cannot come to dinner")
last_name = guest_list.pop()
print(f"Sorry {last_name} you cannot come to dinner")
last_name = guest_list.pop()
print(f"Sorry {last_name} you cannot come to dinner")

print("\n\n")
print("Final 2 guests are ", end="")
print(guest_list)

print("\n\n")
print("Uh oh removing the last 2 also...")
del guest_list[0]
del guest_list[0]
print("Final list is (should be empty) -->    ", end="")
print(guest_list)
