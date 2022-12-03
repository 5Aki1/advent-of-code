import os
import string

def main():
    score_sheet = {string.ascii_letters[i]: i+1 for i in range(52)}
    score = []
    
    # Part 1
    f = open(os.path.dirname(__file__) + 'input.txt', "r")
    for line in f:
        length = len(line.strip())
        first, second = line[:length//2], line[length//2:]
        score.append(''.join(set(first).intersection(second)))
        
    score1 = [score_sheet[x] for x in score if score_sheet.get(x)]
    print(f"Part 1: {sum(score1)}")
    
    # Part 2
    lines = open('input.txt').read().split('\n')
    groups = []
    
    for idx in range(0, len(lines), 3):
        entries = lines[idx:idx+3]
        groups.append(''.join(set.intersection(*map(set, entries))))
        
    score2 = [score_sheet[x] for x in groups if score_sheet.get(x)]
    print(f"Part 2: {sum(score2)}")
    
        
if __name__ == '__main__':
    main()

