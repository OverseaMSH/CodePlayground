def knight_moves(n, k, x, y, remaining_moves, visited):
    if remaining_moves == 0:
        visited.add((x, y))
        return

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
             (1, -2), (1, 2), (2, -1), (2, 1)]

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < n and 0 <= new_y < n:
            knight_moves(n, k, new_x, new_y, remaining_moves - 1, visited)


def count_reachable_positions(n, k):
    visited = set()
    knight_moves(n, k, 0, 0, k, visited)
    return len(visited)


n, k = map(int, input().split())
print(count_reachable_positions(n, k))
