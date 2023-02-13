wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print('1: Wizard')
    print("2: Elf")
    print("3: Human")
    charater = input("Choose your character:")
    if charater == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif charater == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif charater == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        character = "Unknown character"
    print("Unknown Character")

print("You chose {}" .format(character))
print("Your HP is: {}" .format(my_hp))
print("Your damage is {}" .format(my_damage))

while True:
    dragon_hp -= my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp} \n")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp -= dragon_damage
    print(f"The Dragon strikes back at {character}!")
    print(f"The {character} hitpoints are now: {my_hp}\n")
    if my_hp <= 0:
        print(f"The {character} has lost the battle")
        break
