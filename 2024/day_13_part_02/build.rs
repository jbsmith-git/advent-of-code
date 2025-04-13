use std::fs;

fn main() {
    let src = "src/input.txt";
    let debug_dest = "target/debug/input.txt";
    let release_dest = "target/release/input.txt";

    fs::copy(src, debug_dest).expect("Failed to copy input.txt");
    fs::copy(src, release_dest).expect("Failed to copy input.txt");
}
