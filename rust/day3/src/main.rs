use std::collections::HashMap;

/// Keep count of how many 1s are there in given position
/// 0s count will be calculated by substraction; `line_count - 1s count`
fn part_1(input: &str) -> i64 {
    let mut ones_counter: HashMap<usize, i64> = HashMap::new();
    let mut line_count = 0;

    for line in input.trim().split('\n') {
        line_count += 1;
        for (i, c) in line.chars().enumerate() {
            if c == '1' {
                *ones_counter.entry(i).or_default() += 1
            }
        }
    }

    let mut binary_length = 0;
    // TODO is there a better way of getting max key?
    for key in ones_counter.keys() {
        if key > &binary_length {
            binary_length = *key;
        }
    }

    let mut gamma: i64 = 0;
    let mut epsilon: i64 = 0;

    for (position, ones_count) in &ones_counter {
        let zeroes_count = line_count - ones_count;
        if ones_count > &zeroes_count {
            gamma += i64::pow(2, (binary_length - position).try_into().unwrap());
        } else {
            epsilon += i64::pow(2, (binary_length - position).try_into().unwrap());
        }
    }

    gamma * epsilon
}

/// most_common = true -> oxygen generator
/// most_common = false -> co2 scrubber
fn part_2(input: &str, most_common: bool) -> i64 {
    let mut numbers: Vec<_> = input.trim().split('\n').collect();

    let mut bit_index = 0;

    while numbers.len() > 1 {
        let numbers_length = numbers.len();
        let mut ones_count = 0;

        for number in &numbers {
            let value = number.chars().nth(bit_index).unwrap();

            if value == '1' {
                ones_count += 1;
            }
        }

        let zeroes_count = numbers_length - ones_count;
        let mut to_keep_char = '0';

        if ones_count >= zeroes_count {
            if most_common {
                to_keep_char = '1';
            }
        } else if !most_common {
            to_keep_char = '1';
        }

        numbers = numbers
            .into_iter()
            .filter(|n| n.chars().collect::<Vec<_>>()[bit_index] == to_keep_char)
            .collect();

        bit_index += 1;
    }

    i64::from_str_radix(numbers[0], 2).unwrap()
}

fn main() {
    let input = include_str!("../input.txt");
    let p1_answer = part_1(input);
    println!("Part 1: {}", p1_answer);

    let oxygen_generator = part_2(input, true);
    let co2_scrubber = part_2(input, false);

    println!("Part 2: {}", oxygen_generator * co2_scrubber);
}
