from collections import defaultdict


class Grouper():

    def __init__(self, max_character_per_group):
        self.max_character_per_group = max_character_per_group

    # group() takes in playersPerTask and 
    # distribution them so that no 2 players are from the same account
    def group(self, player_per_task):
        ret = defaultdict(list)
        # these are players that could not be fully grouped per 5
        leftover_players_per_task = defaultdict(list)
        for task, players in player_per_task.items():
            remaining_players = set(players)
            group_key_index = 0
            while True:
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
                candidates = []
                for incompatible in incompatible_groups:
                    candidates.append(incompatible[0])
                    to_drop.add(incompatible[0])
                    if len(candidates) == self.max_character_per_group:
                        break
                
                if len(candidates) == self.max_character_per_group:
                    group_key = "{0}-{1}".format(task, group_key_index+1)
                    assert group_key not in ret
                    ret[group_key] = list(candidates)
                else:
                    leftover_players_per_task[task].extend(candidates)
                    
                remaining_players = [x for x in remaining_players if x not in to_drop]
                group_key_index += 1

                # we cannot process further than this
                if len(to_drop) == 0:
                    break

        return ret, leftover_players_per_task

