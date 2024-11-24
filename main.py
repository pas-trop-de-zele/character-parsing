import pandas as pd
from collections import defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Player:
    acc: str
    char: str

    def __str__(self):
        return f"{self.acc}-{self.char+1}"

ACCOUNT_END_COLUMN = input("What is the last account column? ")
CHARACTERS_PER_ACCOUNT = int(input("How many characters per account? "))
FILE_NAME = input("What is the excel file name? ")
SHEET_NAME = input("What is the sheet name? ")
MAX_CHARACTER_PER_GROUP = int(input("How many character do we assign per group? "))

# ACCOUNT_END_COLUMN = "traicay8"
# CHARACTERS_PER_ACCOUNT = 5
# SHEET_NAME = "Sheet1"
# FILE_NAME = "input.xlsx"
# MAX_CHARACTER_PER_GROUP = 5

# Load the Excel file
file_path = FILE_NAME
df = pd.read_excel(file_path, sheet_name=SHEET_NAME)

# Mark empty task
no_task_assigned = ""
df = df.fillna(no_task_assigned)

player_per_task = defaultdict(list)

# skip first column
accs = df.columns.tolist()[1:]

for row_index, row in df.iterrows():
    if row_index == CHARACTERS_PER_ACCOUNT:
        break
    for acc in accs:
        task = row[acc]
        if task == no_task_assigned:
            continue
        player_per_task[task].append(Player(acc, row_index+1))

# Here we need to make sure no character in the same account do the same task
ret = defaultdict(list)
for task, players in player_per_task.items():
    remaining_players = set(players)
    group_key_index = 0
    while len(remaining_players) > 0:
        group_key = "{0}-{1}".format(task, group_key_index+1)
        assert group_key not in ret
        
        # We need to group players per acc
        players_per_acc = defaultdict(list)
        for p in remaining_players:
            players_per_acc[p.acc].append(p)

        # These are the group of players from the same account
        incompatible_groups = [v for v in players_per_acc.values()]
        # We need to sort the group of players so that the group
        # with the most player will always get considered first
        incompatible_groups.sort(key=lambda x : len(x), reverse=True)

        to_drop = set()
        for group in incompatible_groups:
            ret[group_key].append(group[0])
            to_drop.add(group[0])
            if len(ret[group_key]) == MAX_CHARACTER_PER_GROUP:
                break
        remaining_players = [x for x in remaining_players if x not in to_drop]
        group_key_index += 1

for task, players in ret.items():
    print("TASK", task, end=": ")
    for p in players:
        print(p, end=' ')
    print()