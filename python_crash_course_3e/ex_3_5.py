guest_list=['Tendulkar','Kohli','Ganguly']
print(f"I would like to invite {guest_list[0]} to dinner in Mumbai")
print(f"I would like to invite {guest_list[1]} to dinner in Delhi")
print(f"I would like to invite {guest_list[2]} to dinner in Kolkata")

print(f"Uh oh {guest_list[0]} cant make it, changing to Laxman")
guest_list.remove('Tendulkar')
guest_list.insert(0,'Laxman')
print(f"I would like to invite {guest_list[0]} to dinner in Hyderabad")
print(f"I would like to invite {guest_list[1]} to dinner in Delhi")
print(f"I would like to invite {guest_list[2]} to dinner in Kolkata")
