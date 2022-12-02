use itertools::Itertools;

fn main() {
    let total_calories: Vec<u64> = include_str!("../calories.txt")
        .split("\n\n") // Iterator for double new line
        .map(|elf| {    // Assign each to elf
            elf.split('\n') // split elf calories by new line
                .map(|food| food.parse::<u64>()
                .expect("Could parse"))
                .sum()
        })
        .sorted() // For getting top elves
        .rev()
        .collect();

    println!("Top elf: {}", total_calories[0]);
    println!("Sum top three elves: {}", total_calories.iter().take(3).sum::<u64>());
}
