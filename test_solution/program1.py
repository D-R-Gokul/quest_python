#distribution of deck of cards
#given a dek of cards

#function to distribute card and return return matrix
def card_distribute(card_sequence):
    n = int(len(card_sequence)/2)
    card_matrix = []
    for i in range(n):
        row = [card_sequence[i], card_sequence[n*2 -1 -i]]
        card_matrix.append(row)
    return card_matrix

#taking in number of cards
number_of_cards = int(input("Enter thr number of cards (enter even number): "))
if number_of_cards%2 !=0:
    print("You have entered an invalid (odd) number")
else:
    #getting sequence 
    card_sequence = list(map(int, input(f'Enter {number_of_cards} positive number of ').split()))
    card_sequence.sort()  #sorting the sequence
    card_distributed_matrix = card_distribute(card_sequence)  #calling the function
    #printing 
    for row in card_distributed_matrix:
        for numbers in row:
            print('%-4s'%(numbers), end='')
        print()

