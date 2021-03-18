def roll_dice(number_of_nobles, noble_loyalty_range, loyalty_needed, current_combination, combination_list):
    """Rolls dice, because each noble removes 20-35 loyalty from a village, which makes them a 16 sided dice"""
    if number_of_nobles <= 0:
        if current_combination >= loyalty_needed:
            combination_list.append(current_combination)
        return combination_list

    for side in range(1, noble_loyalty_range + 1):
        roll_dice(number_of_nobles - 1, noble_loyalty_range, loyalty_needed, current_combination + side, combination_list)
    return combination_list


if __name__ == '__main__':
    num_of_nob = int(input("How many nobles are you sending?"))
    bonus = int(input("How big is your bonus per noble?"))
    nob_loy_ran = 16
    loy_needed = 100 - num_of_nob * (19 + bonus)
    comb_list = roll_dice(num_of_nob, nob_loy_ran, loy_needed, 0, [])
    percent_chance = len(comb_list) / nob_loy_ran ** num_of_nob * 100
    print(f"The chance of capturing the village is {percent_chance:.2f}%")
