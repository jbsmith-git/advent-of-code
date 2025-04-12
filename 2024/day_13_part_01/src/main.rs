use regex::Regex;
use std::fs;

const TOKENS_REQUIRED_BUTTON_A: u16 = 3;
const TOKENS_REQUIRED_BUTTON_B: u16 = 1;
const MAX_BUTTON_PRESSES: u16 = 100;

struct ClawMachine {
    button_a: [u16; 2],
    button_b: [u16; 2],
    prize_location: [u16; 2],
}

impl ClawMachine {
    fn new(button_a: [u16; 2], button_b: [u16; 2], prize_location: [u16; 2]) -> ClawMachine {
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
                    claw_machine_numbers[1].parse::<u16>().unwrap(),
                    claw_machine_numbers[2].parse::<u16>().unwrap(),
                ],
                [
                    claw_machine_numbers[3].parse::<u16>().unwrap(),
                    claw_machine_numbers[4].parse::<u16>().unwrap(),
                ],
                [
                    claw_machine_numbers[5].parse::<u16>().unwrap(),
                    claw_machine_numbers[6].parse::<u16>().unwrap(),
                ],
            ));
        } else {
            panic!("Claw machine description didn't match regex")
        }
    }

    return claw_machines;
}

fn find_tokens_required(machine: ClawMachine) -> u16 {
    let mut x: u16 = 0;
    let mut y: u16 = 0;
    let mut b_pushed: u16 = 0;

    while x <= machine.prize_location[0]
        && y <= machine.prize_location[1]
        && b_pushed <= MAX_BUTTON_PRESSES
    {
        let remaining_x: u16 = machine.prize_location[0] - x;
        let remaining_y: u16 = machine.prize_location[1] - y;

        if remaining_x / machine.button_a[0] == remaining_y / machine.button_a[1]
            && remaining_x % machine.button_a[0] == 0
            && remaining_y % machine.button_a[1] == 0
            && remaining_x / machine.button_a[0] <= MAX_BUTTON_PRESSES
        {
            return b_pushed * TOKENS_REQUIRED_BUTTON_B
                + remaining_x / machine.button_a[0] * TOKENS_REQUIRED_BUTTON_A;
        }

        x += machine.button_b[0];
        y += machine.button_b[1];
        b_pushed += 1;
    }

    return 0;
}

fn main() {
    let claw_machines = parse_input_file();

    let mut total_tokens_used: u16 = 0;
    for machine in claw_machines {
        total_tokens_used += find_tokens_required(machine);
    }

    println!("Day 13 Part 1: {}", total_tokens_used);
}
