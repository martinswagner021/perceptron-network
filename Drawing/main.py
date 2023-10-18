from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing with AI")

def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)
    for button in buttons:
        button.draw(win)
    pygame.display.update()

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (i*PIXEL_SIZE, j*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS):
            pygame.draw.line(win, GRAY, (0, i*PIXEL_SIZE), (WIDTH, i*PIXEL_SIZE))
        for i in range(COLS):
            pygame.draw.line(win, GRAY, (i*PIXEL_SIZE, 0), (i*PIXEL_SIZE, HEIGHT-TOOLBAR_HEIGHT))           

def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def get_row_col_from_pos(pos):
    x,y = pos
    row = x//PIXEL_SIZE
    col = y//PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    
    return row, col

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)

buttons_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25

buttons = [
    Button(10, buttons_y, 70, 50, BLACK, "Limpar"),
    Button(90, buttons_y, 70, 50, BLACK, "Testar"),
    Button(170, buttons_y, 70, 50, BLACK, "", GREEN)
]

while run:
    clock.tick(FPS)
    img = [[]]
    for i in grid:
        for j in i:
            img[0].append(j[0])
    img = np.array(img)
    res = make_prediction(img)
    buttons[2].update_txt(str(res), WIN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = WHITE
                grid[row][col+1] = WHITE
                grid[row][col-1] = WHITE
                grid[row+1][col] = WHITE
                grid[row-1][col] = WHITE
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    if button.text == "Limpar":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                    if button.text == "Testar":
                        print(img)
                        

    draw(WIN, grid, buttons)

pygame.quit()


