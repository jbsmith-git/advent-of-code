class Map:

    def __init__(self, map_from: str, map_to: str, map_list) -> None:
        self.map_from = map_from
        self.map_to = map_to
        self.map_list = map_list

    def apply_map(self, input: int) -> int:
        for map in self.map_list:
            if map[1] <= input < map[1] + map[2]:
                return map[0] + input - map[1]
        return input


def import_input():

    ## Read lines from file
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    ## Extract seeds
    seeds = [int(s) for s in lines[0][7:-1].split(" ")]
    lines = lines[2:]

    ## Extract each mapping
    all_maps = []
    for line in lines:
        line = line.replace("\n", "")
        if line.count("map") == 1:
            all_maps.append(Map(line.split("-")[0], line.split(" ")[0].split("-")[-1], []))
        elif line == "":
            continue
        else:
            line = [int(n) for n in line.split(" ")]
            all_maps[-1].map_list.append(tuple(line))

    return seeds, all_maps


if __name__ == "__main__":

    seeds, all_maps = import_input()
    locations = []

    for s in seeds:
        info_type = "seed"
        while info_type != "location":
            for map in all_maps:
                if map.map_from == info_type:
                    # print(f"{map.map_from}: {s} -> {map.map_to}: {map.apply_map(s)}")
                    s = map.apply_map(s)
                    info_type = map.map_to
        locations.append(s)

    print("Day 5 Part 1:", min(locations))
