from collections import defaultdict


# class hand():
#     def __init__(self,hand_str) -> None:
#         pass
#     ...
def func1(fname="test.txt"):
    ans = 1

    with open(fname) as f:
        hands = []
        bids = []
        sorted_hands = []
        hand_kind = []
        for (
            idx,
            line,
        ) in enumerate(f):
            hands.append(line.strip().split(" ")[0])
            bids.append(int(line.strip().split(" ")[1]))
    print(hands)
    print(bids)

    def find_hand_kind(hand):
        if hand[0][1] == 5:
            return 6
        if hand[0][1] == 4:
            return 5
        if hand[0][1] == 3:
            if hand[1][1] == 2:
                return 4
            return 3
        if hand[0][1] == 2:
            if hand[1][1] == 2:
                return 2
            return 1
        return 0

    for hand in hands:
        d = defaultdict(int)
        for card in hand:
            d[card] += 1
        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        sorted_hands.append(sorted_d)

        hk = find_hand_kind(sorted_d)
        print("hands kind and hands", hk, hand)
        hand_kind.append(hk)
    print("hand_kind", hand_kind)

    # find ids, that has the same hand_kind
    # dic[ids] = []
    hand_kind_to_idx = [[] for _ in range(7)]
    for idx, kind_id in enumerate(hand_kind):
        hand_kind_to_idx[kind_id].append(idx)
    print("hand_kind_to_idx", hand_kind_to_idx)

    def sort_same_kind(sorted_hands, same_kind_ids):
        """
        same_kind = [2,3]
        sorted_hands =
        """
        same_kind_ids_to_score = defaultdict(int)
        for hand_id in same_kind_ids:
            hand_dic = sorted_hands[hand_id]
            for i, card in enumerate("".join(reversed(hands[hand_id]))):
                same_kind_ids_to_score[hand_id] += (13 ** (i + 1)) * str_rank_table[
                    card
                ]
            # print('hand_dic',hand_dic)

        ans_ = sorted(same_kind_ids_to_score.items(), key=lambda item: item[1])
        return ans_

    ans = 0
    total_rank_asc = 1
    for same_kind_ids in hand_kind_to_idx:
        # same_kind = [2,3]
        # print('same_hand',same_kind_ids)
        for card_id in sort_same_kind(sorted_hands, same_kind_ids):
            print(card_id[0])
            ans += total_rank_asc * bids[card_id[0]]
            total_rank_asc += 1

    return ans


# all_str= ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
# str_rank = [len(all_str)-id for id,x in enumerate(all_str)]
# str_rank_table = {a:s for a,s in zip(all_str,str_rank)}
# # print('check str rank table',str(str_rank_table))
# assert func1('test.txt') == 6440, func1()
# print(func1('input.txt'))


def func2(fname="test.txt"):
    ans = 1

    with open(fname) as f:
        hands = []
        bids = []
        sorted_hands = []
        hand_kind = []
        for (
            idx,
            line,
        ) in enumerate(f):
            hands.append(line.strip().split(" ")[0])
            bids.append(int(line.strip().split(" ")[1]))
    print(hands)
    print(bids)

    def find_hand_kind(hand):
        if hand[0][1] == 5:
            return 6
        if hand[0][1] == 4:
            return 5
        if hand[0][1] == 3:
            if hand[1][1] == 2:
                return 4
            return 3
        if hand[0][1] == 2:
            if hand[1][1] == 2:
                return 2
            return 1
        return 0

    for hand in hands:
        d = defaultdict(int)
        for card in hand:
            d[card] += 1

        sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        assert sum([x[1] for x in sorted_d]) == 5
        print("sorted_d", sorted_d)
        if sorted_d[0][0] == "J":
            if sorted_d[0][1] != 5:
                sorted_d[1] = (sorted_d[1][0], sorted_d[1][1] + sorted_d[0][1])
                if d["J"] != 0:
                    if sorted_d[0][0] == "J":
                        sorted_d[0] = ("J", 0)
                    sorted_d = sorted(sorted_d, key=lambda x: x[1], reverse=True)
                print("sorted_d for case1J", sorted_d)
        else:
            sorted_d[0] = (sorted_d[0][0], sorted_d[0][1] + d["J"])
            if d["J"] != 0:
                for sd_idx in range(len(sorted_d)):
                    if sorted_d[sd_idx][0] == "J":
                        assert sorted_d[sd_idx][1] == d["J"]
                        sorted_d[sd_idx] = ("J", 0)
                        sorted_d = sorted(sorted_d, key=lambda x: x[1], reverse=True)
                        break
        assert sum([x[1] for x in sorted_d]) == 5
        sorted_hands.append(sorted_d)

        hk = find_hand_kind(sorted_d)
        hand_kind.append(hk)
    # print('hand_kind', hand_kind)

    # find ids, that has the same hand_kind
    hand_kind_to_idx = [[] for _ in range(7)]
    for idx, kind_id in enumerate(hand_kind):
        hand_kind_to_idx[kind_id].append(idx)

    def sort_same_kind(same_kind_ids):
        """
        same_kind = [2,3]
        sorted_hands =
        """
        same_kind_ids_to_score = defaultdict(int)
        for hand_id in same_kind_ids:
            for i, card in enumerate(hands[hand_id]):
                same_kind_ids_to_score[hand_id] += (
                    len(all_str) ** (5 - i)
                ) * str_rank_table[card]
        ans_ = sorted(same_kind_ids_to_score.items(), key=lambda item: item[1])
        return ans_

    ans = 0
    total_rank_asc = 1
    ordered_card_ids = []
    for same_kind_ids in hand_kind_to_idx:
        # x=sort_same_kind(same_kind_ids)
        # print('xxxxxxxxxxxxxx',x)
        for card_id in sort_same_kind(same_kind_ids):
            # print(card_id[0])
            ans += total_rank_asc * bids[card_id[0]]
            total_rank_asc += 1
            ordered_card_ids.append(card_id[0])
    print("ordered_card-ids ", ordered_card_ids)
    return ans


all_str = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
str_rank = [len(all_str) - id for id, x in enumerate(all_str)]
str_rank_table = {a: s for a, s in zip(all_str, str_rank)}
print(str_rank_table)

assert func2("test.txt") == 5905, func2()
print(func2("input.txt"))  # 249138943 247175270
