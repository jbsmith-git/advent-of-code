def is_connected(pipe_grid, pipe_coords_a, pipe_coords_b) -> bool:

    pipe_a = pipe_grid[pipe_coords_a[0]][pipe_coords_a[1]]
    pipe_b = pipe_grid[pipe_coords_b[0]][pipe_coords_b[1]]

    ## Check they are actually pipes
    if pipe_a == "." or pipe_b == ".":
        return False

    north_connecting_pipes = {"|", "L", "J", "S"}
    east_connecting_pipes = {"-", "L", "F", "S"}
    south_connecting_pipes = {"|", "7", "F", "S"}
    west_connecting_pipes = {"-", "J", "7", "S"}

    ## Pipes on the same row
    if pipe_coords_a[0] == pipe_coords_b[0]:
        if pipe_coords_b[1] > pipe_coords_a[1]:
            if pipe_a in east_connecting_pipes and pipe_b in west_connecting_pipes:
                return True
        else:
            if pipe_a in west_connecting_pipes and pipe_b in east_connecting_pipes:
                return True
    ## Pipes on the same column
    else:
        if pipe_coords_b[0] > pipe_coords_a[0]:
            if pipe_a in south_connecting_pipes and pipe_b in north_connecting_pipes:
                return True
        else:
            if pipe_a in north_connecting_pipes and pipe_b in south_connecting_pipes:
                return True

    return False


def import_input() -> tuple[tuple]:

    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    pipe_grid = []
    for line in lines:
        line = tuple(line.replace("\n", ""))
        pipe_grid.append(line)

    return tuple(pipe_grid)


if __name__ == "__main__":

    pipe_grid = import_input()

    ## Locate the S
    for r in range(len(pipe_grid)):
        for c in range(len(pipe_grid[r])):
            if pipe_grid[r][c] == "S":
                pipe_coords = (r, c)
                break

    pipe_length = 0
    pipe_coords_history = {pipe_coords}
    while pipe_grid[pipe_coords[0]][pipe_coords[1]] != "S" or pipe_length == 0:
        ## Check all orthogonally adjacent pipes
        for coord_delta in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
            candidate_new_pipe_coords = (
                pipe_coords[0] + coord_delta[0],
                pipe_coords[1] + coord_delta[1],
            )
            ## Check coords are in the grid
            if (
                candidate_new_pipe_coords[0] >= len(pipe_grid)
                or candidate_new_pipe_coords[0] < 0
                or candidate_new_pipe_coords[1] >= len(pipe_grid[0])
                or candidate_new_pipe_coords[1] < 0
            ):
                continue
            if (
                candidate_new_pipe_coords not in pipe_coords_history
                or (
                    pipe_grid[candidate_new_pipe_coords[0]][candidate_new_pipe_coords[1]] == "S"
                    and pipe_length > 1
                )
            ) and is_connected(pipe_grid, pipe_coords, candidate_new_pipe_coords):
                pipe_coords = candidate_new_pipe_coords
                pipe_coords_history.add(pipe_coords)
                pipe_length += 1
                break

    print("Day 10 Part 1:", int(pipe_length / 2))
