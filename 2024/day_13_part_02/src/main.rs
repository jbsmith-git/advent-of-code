use regex::Regex;
use std::fs;

const TOKENS_REQUIRED_BUTTON_A: u8 = 3;
const TOKENS_REQUIRED_BUTTON_B: u8 = 1;
const CONVERSION_ERROR: u64 = 10_u64.pow(13);

struct ClawMachine {
    button_a: [u8; 2],
    button_b: [u8; 2],
    prize_location: [u64; 2],
}

impl ClawMachine {
    fn new(button_a: [u8; 2], button_b: [u8; 2], prize_location: [u64; 2]) -> ClawMachine {
        ClawMachine {
            button_a,
            button_b,
            prize_location,
        }
    }
}

fn parse_input_file() -> Vec<ClawMachine> {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");

    let re = Regex::new(concat!(
        r"Button A: X\+([0-9]{1,2}), Y\+([0-9]{1,2})\r\n",
        r"Button B: X\+([0-9]{1,2}), Y\+([0-9]{1,2})\r\n",
        r"Prize: X=([0-9]{1,5}), Y=([0-9]{1,5})"
    ))
    .unwrap();

    let mut claw_machines = Vec::new();
    for claw_machine_description in input.split("\r\n\r\n") {
        if let Some(claw_machine_numbers) = re.captures(claw_machine_description) {
            claw_machines.push(ClawMachine::new(
                [
                    claw_machine_numbers[1].parse::<u8>().unwrap(),
                    claw_machine_numbers[2].parse::<u8>().unwrap(),
                ],
                [
                    claw_machine_numbers[3].parse::<u8>().unwrap(),
                    claw_machine_numbers[4].parse::<u8>().unwrap(),
                ],
                [
                    claw_machine_numbers[5].parse::<u64>().unwrap() + CONVERSION_ERROR,
                    claw_machine_numbers[6].parse::<u64>().unwrap() + CONVERSION_ERROR,
                ],
            ));
        } else {
            panic!("Claw machine description didn't match regex")
        }
    }

    return claw_machines;
}

fn find_tokens_required(machine: ClawMachine) -> u64 {
    // Use linear algebra instead of iterating

    let pushes_a: f64 = (machine.button_b[1] as f64 * machine.prize_location[0] as f64
        - machine.button_b[0] as f64 * machine.prize_location[1] as f64)
        / (machine.button_b[1] as f64 * machine.button_a[0] as f64
            - machine.button_b[0] as f64 * machine.button_a[1] as f64);

    let pushes_b: f64 = (machine.button_a[0] as f64 * machine.prize_location[1] as f64
        - machine.button_a[1] as f64 * machine.prize_location[0] as f64)
        / (machine.button_b[1] as f64 * machine.button_a[0] as f64
            - machine.button_b[0] as f64 * machine.button_a[1] as f64);

    if pushes_a.trunc() == pushes_a
        && pushes_b.trunc() == pushes_b
        && pushes_a >= 0.0
        && pushes_b >= 0.0
    {
        pushes_a as u64 * TOKENS_REQUIRED_BUTTON_A as u64
            + pushes_b as u64 * TOKENS_REQUIRED_BUTTON_B as u64
    } else {
        0
    }
}

fn main() {
    let claw_machines = parse_input_file();

    let mut total_tokens_used: u64 = 0;
    for machine in claw_machines {
        total_tokens_used += find_tokens_required(machine);
    }

    println!("Day 13 Part 2: {}", total_tokens_used);
}
