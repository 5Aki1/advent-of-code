fn score_card_p1(line: &[(char, char); 1]) -> usize {
    line.iter()
        .map(|(op, me)| match (op, me) {
        // X = Rock(1), Y = Paper(2), Z = Scissors(3)
        // All wins
        ('A', 'Y') => 6 + 2,
        ('B', 'Z') => 6 + 3,
        ('C', 'X') => 6 + 1,
        // All draws
        ('A', 'X') => 3 + 1,
        ('B', 'Y') => 3 + 2,
        ('C', 'Z') => 3 + 3,
        // All losses
        ('A', 'Z') => 0 + 3,
        ('B', 'X') => 0 + 1,
        ('C', 'Y') => 0 + 2,
        _ => panic!(),
    })
    .sum()
}

fn score_card_p2(line: &[(char, char); 1]) -> usize {
    let out = match line {
        // All wins
        [('A', 'Z')] => ('A', 'Y'),
        [('B', 'Z')] => ('B', 'Z'),
        [('C', 'Z')] => ('C', 'X'),
        // All draws
        [('A', 'Y')] => ('A', 'X'),
        [('B', 'Y')] => ('B', 'Y'),
        [('C', 'Y')] => ('C', 'Z'),
        // All losses
        [('A', 'X')] => ('A', 'Z'),
        [('B', 'X')] => ('B', 'X'),
        [('C', 'X')] => ('C', 'Y'),
        _ => panic!(),
    };
    
    return score_card_p1(&[out]);
}

fn main() {
    let input = include_str!("../input.txt");
    let  (mut score_p1, mut score_p2) = (0, 0);

    // let mut p2_vec:Vec<Vec<(char, char)>> = vec![];

    for line in input.lines() {
        let mut parts = line.split_whitespace();
        let [(op, me)] = [(parts.next().unwrap().parse::<char>().unwrap(), 
                                    parts.next().unwrap().parse::<char>().unwrap())];

        // P1
        score_p1 += score_card_p1(&[(op, me)]);

        // P2
        score_p2 += score_card_p2(&[(op, me)]);
    }

    println!("Score part1: {:?}", score_p1);
    println!("Score part2: {:?}", score_p2);

}
