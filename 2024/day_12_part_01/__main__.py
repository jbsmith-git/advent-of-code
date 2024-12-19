from dataclasses import dataclass


@dataclass(frozen=True)
class GardenPlot:
    plant_type: str
    plot_coords: frozenset[tuple]


def import_input() -> tuple[tuple[str]]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    garden_map = tuple(tuple(row.replace("\n", "")) for row in lines)

    return garden_map


def find_plots_in_map(garden_map: tuple[tuple[str]]) -> set[GardenPlot]:

    map_height = len(garden_map)
    map_width = len(garden_map[0])

    garden_plots = set()
    coords_in_plots = set()

    for r, row in enumerate(garden_map):
        for c, plant in enumerate(row):

            if (r, c) in coords_in_plots:
                continue

            plot_coords = set()
            candidate_plot_coords = [(r, c)]
            while len(candidate_plot_coords) > 0:

                candidate = candidate_plot_coords[0]
                candidate_plot_coords.pop(0)

                if candidate in plot_coords:
                    continue

                if not (0 <= candidate[0] < map_height and 0 <= candidate[1] < map_width):
                    continue

                if garden_map[candidate[0]][candidate[1]] == plant:
                    plot_coords.add(candidate)

                    for direction in {(1, 0), (-1, 0), (0, 1), (0, -1)}:
                        candidate_plot_coords.append(
                            (candidate[0] + direction[0], candidate[1] + direction[1])
                        )

            coords_in_plots.update(plot_coords)
            garden_plots.add(GardenPlot(plant, frozenset(plot_coords)))

    return garden_plots


def compute_plot_perimeter(plot: GardenPlot, map_height: int, map_width: int) -> int:

    plot_perimeter = 0
    for r, c in plot.plot_coords:

        adjacent_coords = {(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)}
        for ar, ac in adjacent_coords:

            if not (0 <= ar < map_height and 0 <= ac < map_width):
                plot_perimeter += 1

            elif (ar, ac) not in plot.plot_coords:
                plot_perimeter += 1

    return plot_perimeter


if __name__ == "__main__":

    garden_map = import_input()
    garden_plots = find_plots_in_map(garden_map)

    total_fence_price = 0
    for plot in garden_plots:
        area = len(plot.plot_coords)
        perimeter = compute_plot_perimeter(plot, len(garden_map), len(garden_map[0]))
        total_fence_price += area * perimeter

    print("Day 12 Part 1:", total_fence_price)
