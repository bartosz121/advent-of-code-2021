fn part_1(input: &str) -> i64 {
    let crabs: Vec<i64> = input
        .trim()
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    let min = *crabs.iter().min().unwrap();
    let max = *crabs.iter().max().unwrap();
    let mut best_result = i64::MAX;

    for p in min..=max {
        let mut result = 0;
        for crab in &crabs {
            result += (crab - p).abs()
        }

        best_result = best_result.min(result)
    }

    best_result
}

fn part_2(input: &str) -> i64 {
    let crabs: Vec<i64> = input
        .trim()
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    let min = *crabs.iter().min().unwrap();
    let max = *crabs.iter().max().unwrap();
    let mut best_result = i64::MAX;

    for p in min..=max {
        let mut result = 0;
        for crab in &crabs {
            let d = (crab - p).abs();
            result += d * (d + 1) / 2;
        }

        best_result = best_result.min(result)
    }

    best_result
}

fn main() {
    let input = include_str!("../input.txt");
    let part_1 = part_1(input);
    let part_2 = part_2(input);

    println!("Part 1: {}", part_1);
    println!("Part 2: {}", part_2);
}
