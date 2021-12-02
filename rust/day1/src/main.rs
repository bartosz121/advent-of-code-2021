fn part_1(input: &str) -> i64 {
    let v: Vec<i64> = input
        .trim()
        .split('\n')
        .map(|n| n.parse::<i64>().unwrap())
        .collect();

    let mut counter = 0;
    for i in 1..v.len() {
        if v[i] > v[i - 1] {
            counter += 1;
        }
    }

    counter
}

fn part_2(input: &str) -> i64 {
    let v: Vec<i64> = input
        .trim()
        .split('\n')
        .map(|n| n.parse::<i64>().unwrap())
        .collect();

    let mut prev_measurment = v[0] + v[1] + v[2];
    let mut counter = 0;

    for i in 3..v.len() {
        let latest_measurment = v[i - 2] + v[i - 1] + v[i];
        if latest_measurment > prev_measurment {
            counter += 1;
        }
        prev_measurment = latest_measurment;
    }

    counter
}

fn main() {
    let input = include_str!("../input.txt");

    let p1 = part_1(input);
    println!("Part 1: {}", p1);

    let p2 = part_2(input);
    println!("Part 2: {}", p2);
}
