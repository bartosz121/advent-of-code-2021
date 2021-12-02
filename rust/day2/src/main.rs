fn part_1(input: &str) -> i64 {
    let mut horiz_pos = 0;
    let mut depth = 0;

    for line in input.trim().split('\n') {
        let mut p = line.split(' ');
        let command = p.next().unwrap();
        let value = p.next().unwrap().parse::<i64>().unwrap();

        match command {
            "forward" => horiz_pos += value,
            "down" => depth += value,
            "up" => depth -= value,
            _ => println!("{}", command),
        }
    }

    horiz_pos * depth
}

fn part_2(input: &str) -> i64 {
    let mut horiz_pos = 0;
    let mut depth = 0;
    let mut aim = 0;

    for line in input.trim().split('\n') {
        let mut p = line.split(' ');
        let command = p.next().unwrap();
        let value = p.next().unwrap().parse::<i64>().unwrap();

        match command {
            "forward" => {
                horiz_pos += value;
                depth += aim * value;
            }
            "down" => aim += value,
            "up" => aim -= value,
            _ => panic!(),
        }
    }

    horiz_pos * depth
}

// fn part_1(input: &str) -> i64 {}

fn main() {
    let input = include_str!("../input.txt");
    let p1 = part_1(input);
    println!("Part 1: {}", p1);

    let p2 = part_2(input);
    println!("Part 2: {}", p2);
}
