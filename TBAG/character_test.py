from character import Enemy

wolf = Enemy("Wolf", "A wild, peculiar creature with eerie, blue eyes.")
wolf.describe()

wolf.set_conversation("Howl!")
wolf.talk()

wolf.set_weakness("silver sword")
print("What will you fight with?")
fight_with = input().lower()
wolf.fight(fight_with)
