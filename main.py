def move_rover(grid, position, commands):
    directions = ['N', 'E', 'S', 'W']
    moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    
    x, y, direction = position
    
    for command in commands:
        if command not in {'L', 'R', 'M'}:
            raise ValueError(f"Invalid command: {command}")
        if command == 'L':
            direction = directions[(directions.index(direction) - 1) % 4]
        elif command == 'R':
            direction = directions[(directions.index(direction) + 1) % 4]
        elif command == 'M':
            dx, dy = moves[direction]
            nx, ny = x + dx, y + dy
            # Vérifier les limites de la grille
            if 0 <= nx <= grid[0] and 0 <= ny <= grid[1]:
                x, y = nx, ny

    return x, y, direction
