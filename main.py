import random
from typing import List, Dict


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


def main():
    for i in range(2):
        character = generate_character(10)
        print(character)


if __name__ == '__main__':
    main()
