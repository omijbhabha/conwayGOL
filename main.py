import time
import pygame
import numpy as np

COLOR_BG = (10,10,10)
COLOR_GRID = (40,40,40)
COLOR_DIE_NEXT = (170,170,170)
COLOR_ALIVE_NEXT = (255,255,255)

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros(cells.shape)
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[max(row-1,0):row+2, max(col-1,0):col+2]) - cells[row, col]
        if cells[row, col] == 1:
            if alive == 2 or alive == 3:
                updated_cells[row, col] = 1
                color = COLOR_ALIVE_NEXT
            else:
                color = COLOR_DIE_NEXT if with_progress else COLOR_BG
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                color = COLOR_ALIVE_NEXT if with_progress else COLOR_BG
            else:
                color = COLOR_BG
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    return updated_cells

def main():
    pygame.init()
    cell_size = 10
    width, height = 800, 600
    cols, rows = width // cell_size, height // cell_size
    screen = pygame.display.set_mode((width, height))
    cells = np.zeros((rows, cols))
    screen.fill(COLOR_GRID)
    update(screen, cells, cell_size)
    pygame.display.flip()
    running = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, cell_size)
                    pygame.display.update()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            cells[pos[1] // cell_size, pos[0] // cell_size] = 1
            update(screen, cells, cell_size)
            pygame.display.update()
        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, cell_size, with_progress=True)
            pygame.display.update()
            time.sleep(0.05)
        else:
            update(screen, cells, cell_size)
            pygame.display.update()
            time.sleep(0.01)

if __name__ == "__main__":
    main()