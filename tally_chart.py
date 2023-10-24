# Order list of candidates by votes

def sort(data, candidate_number):
    for this_index in range(len(data) - 1):
        swap_index = find_smallest(data, this_index)
        if swap_index != this_index:
            swap(data, swap_index, this_index, candidate_number)


def find_smallest(sort_data, start_index):
    swap_index = start_index
    for index in range(start_index + 1, len(sort_data)):
        if sort_data[index] > sort_data[swap_index]:
            swap_index = index
    return swap_index


def swap(swap_data, from_index, to_index, candidate_data):
    swap_data[from_index], swap_data[to_index] =\
        swap_data[to_index], swap_data[from_index]
    candidate_data[from_index], candidate_data[to_index] = \
        candidate_data[to_index], candidate_data[from_index]


candidates = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"]
candidate_votes = [0, 0, 0, 0, 0]
vote = 0
while vote != -1:
    print("List of candidates:")
    for candidate in candidates:
        print(candidate, end='    ')
    print()
    vote = int(input("Enter which candidate you wish to vote for (1 to 5): "))
    print()
    if 1 <= vote <= 5:
        for candidate in range(5):
            if vote == candidate + 1:
                candidate_votes[candidate] += 1

    elif vote == -1:
        print("End of voting")

    else:
        print("Invalid input. Candidate needs to be between 1 and 5.")

sort(candidate_votes, candidates)

print()
print("The final votes are:")
for candidate in range(5):
    print(candidates[candidate] + ":", candidate_votes[candidate], "votes")
