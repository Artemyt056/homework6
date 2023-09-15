cities = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч".replace(',', ' ').replace('.', ' ').title().split()


for city in cities:
    print(f"Я\U00002764_{city}_")
