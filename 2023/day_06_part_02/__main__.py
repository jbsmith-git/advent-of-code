class Race:

    def __init__(self, time, record_distance):
        self.time = time
        self.record_distance = record_distance

    def compute_record_charge_times(self) -> list:
        record_charge_times = []
        for charge_time in range(0, self.time + 1):
            distance = (self.time - charge_time) * charge_time
            if distance > self.record_distance:
                record_charge_times.append(charge_time)
        return record_charge_times


def import_input() -> Race:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    formatted_lines = []
    for line in lines:
        for l in range(10, 0, -1):
            line = line.replace(l * " ", "")
        line = line.replace("\n", "")
        line = line.split(":")
        formatted_lines.append(line[1])

    race = Race(int(formatted_lines[0]), int(formatted_lines[1]))

    return race


if __name__ == "__main__":

    race = import_input()

    record_charge_times = len(race.compute_record_charge_times())

    print("Day 6 Part 2:", record_charge_times)
