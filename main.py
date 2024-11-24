import pandas as pd
from collections import defaultdict

import group
from player import Player


if __name__ == "__main__":
    ACCOUNT_END_COLUMN = input("What is the last account column? ")
    CHARACTERS_PER_ACCOUNT = int(input("How many characters per account? "))
    FILE_NAME = input("What is the excel file name? ")
    SHEET_NAME = input("What is the sheet name? ")
    MAX_CHARACTER_PER_GROUP = int(input("How many character do we assign per group? "))
    VALID_TASKS = [x for x in input("Enter valid tasks separated by spaces: ").split()]
    VALID_PAIRS = []
    pair_count = int(input("How many valid pairs are there? "))
    if pair_count > 0:
        for i in range(pair_count):
            a, b = input(f"Enter pair {i+1}: ").split()
            VALID_PAIRS.append((a, b))

    # ACCOUNT_END_COLUMN = "traicay8"
    # CHARACTERS_PER_ACCOUNT = 5
    # SHEET_NAME = "Sheet1"
    # FILE_NAME = "input.xlsx"
    # MAX_CHARACTER_PER_GROUP = 5
    # VALID_TASKS = ["I", "II", "III", "IV", "V"]
    # VALID_PAIRS = [("I", "IV"), ("II", "III")]

    # Load the Excel file
    file_path = FILE_NAME
    df = pd.read_excel(file_path, sheet_name=SHEET_NAME)

    # Mark empty task
    no_task_assigned = ""
    df = df.fillna(no_task_assigned)

    # skip first column
    accs = df.columns.tolist()[1:]

    player_per_single_task = defaultdict(list)
    for row_index, row in df.iterrows():
        if row_index == CHARACTERS_PER_ACCOUNT:
            break
        for acc in accs:
            task = row[acc]
            if task == no_task_assigned:
                continue
            player_per_single_task[task].append(Player(acc, row_index+1))
    

    grouper = group.Grouper(MAX_CHARACTER_PER_GROUP)
    # group 1 are group of players group per task and not collocate in same accounts
    group1, leftover_players_per_task = grouper.group(player_per_single_task)

    # group2 are group of players group per pair i.e.
    # I + IV
    # II + III
    player_per_grouped_task = {x: [] for x in VALID_PAIRS}  

    # There could be players not being a part of any grouped task i.e. V 
    # we would want to flag those tasks
    unsatisfiable_players_per_task = defaultdict(list)
    for task, players in leftover_players_per_task.items():
        could_not_packed = True
        # See if this tasks match any pair members of any VALID_PAIRS
        for pair in VALID_PAIRS:
            if task == pair[0] or task == pair[1]:
                could_not_packed = False
        if could_not_packed:
            unsatisfiable_players_per_task[task].extend(players)

    for pair in VALID_PAIRS:
        # Example pair (II, III)
        # Taking player from task II is pair[0]
        player_per_grouped_task[pair].extend(leftover_players_per_task[pair[0]])
        # Taking player from task III is pair[1]
        player_per_grouped_task[pair].extend(leftover_players_per_task[pair[1]])
    group2, leftover_players_per_grouped_task = grouper.group(player_per_grouped_task)

    # sanity check
    count_left_over_players_from_single_group = sum((len(x) for x in leftover_players_per_task.values()))
    count_grouped_tasks_players = sum(len(x) for x in player_per_grouped_task.values())
    count_unstatisfiable_players = sum(len(x) for x in unsatisfiable_players_per_task)
    assert count_left_over_players_from_single_group == (count_grouped_tasks_players + count_unstatisfiable_players)

    # Display result
    for g in [group1, group2]:
        for task, players in g.items():
            print("TASK", task, end=": ")
            for p in players:
                print(p, end=' ')
            print()
    
    # Unsatisfiable players
    print("\nWARNING: these players could not be processed:")
    for task, players in unsatisfiable_players_per_task.items():
        for p in players:
            print(f"{p} | Task {task}")
        print()