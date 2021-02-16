import random
from typing import List, Dict
from scipy.stats import pearsonr


def generate_character(target_points: int) -> Dict[str, int]:
    stats: List[str] = ['str', 'dex', 'con', 'int', 'per', 'wil']
    point_cost_to_score: Dict[int, int] = {
        0: 0,
        1: 1,
        2: 2,
        4: 3,
        6: 4
    }
    character = {}
    total_point_cost = 0
    while True:
        for stat in stats:
            point_cost = random.choice(list(point_cost_to_score.keys()))
            score = point_cost_to_score[point_cost]
            character[stat] = score
            total_point_cost += point_cost
        if total_point_cost == target_points:
            break
        total_point_cost = 0
    return character


def generate_character_pair(target_points: int, max_correlation_coeff: float):
    char1 = generate_character(target_points)
    while True:
        char2 = generate_character(target_points)
        r, _ = pearsonr([char1[x] for x in char1], [char2[x] for x in char2])
        if r <= max_correlation_coeff:
            return char1, char2, r

def get_char_generator_stats():
    n_char1_has_four = 0
    n_char2_has_four = 0
    n_both_has_four = 0
    n = 10000
    for i in range(n):
        char1, char2, r = generate_character_pair(10, -0.1)
        char1_has_four = False
        char2_has_four = False
        for stat in char1:
            if char1[stat] == 4:
                char1_has_four = True
                break
        for stat in char2:
            if char2[stat] == 4:
                char2_has_four = True
                break
        if char1_has_four:
            n_char1_has_four += 1
        if char2_has_four:
            n_char2_has_four += 1
        if char1_has_four and char2_has_four:
            n_both_has_four += 1
    p_char1_has_four = n_char1_has_four / n
    p_char2_has_four = n_char2_has_four / n
    print('Proportion Char 1 has a four:', p_char1_has_four)
    print('Proportion Char 2 has a four:', p_char2_has_four)
    print('Proportion both have a four', n_both_has_four / n, 'expected', p_char1_has_four * p_char2_has_four)


def main():
    # char1, char2, r = generate_character_pair(10, -0.10)
    # print(char1)
    # print(char2)
    # print(r)
    get_char_generator_stats()


if __name__ == '__main__':
    main()
