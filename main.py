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


def main():
    char1, char2, r = generate_character_pair(10, -0.10)
    print(char1)
    print(char2)
    print(r)


if __name__ == '__main__':
    main()
