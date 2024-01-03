import random

def parse_input(num):
    possible_values = ['1', '2', '3', '4', '5', '6']
    if num.strip() in possible_values:
        return int(num)
    else:
        print('Please enter an integer from 1 to 6')
        raise SystemExit(1)
    
def roll_dice(num):
    result = []
    for i in range(num):
        result.append(random.randint(1,6))

    return result

# dice.py
import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def generate_dice_visuals(results):
    dice_to_display = [DICE_ART[num] for num in results]
    
    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    row_5 = []
    for dice in dice_to_display:
        row_1.append(dice[0])
        row_2.append(dice[1])
        row_3.append(dice[2])
        row_4.append(dice[3])
        row_5.append(dice[4])

    entire_visual = [row_1, row_2, row_3, row_4, row_5]
    entire_visual_str = [' '.join(row) for row in entire_visual]

    width = len(entire_visual_str[0])
    print()
    print('RESULTS'.center(width,'*'))
    for row in entire_visual_str:
        print(row)
        
        
def main():

    num = input('How many dice would you like to roll? [1-6]: ')
    checked_num = parse_input(num)
    results = roll_dice(checked_num)

    generate_dice_visuals(results)

main()