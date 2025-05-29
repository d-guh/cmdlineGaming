#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <termios.h>

#define ROWS 20
#define COLS 10
#define OFFSET 1 // Offset from border

#define BLOCK_FULL   "█"
#define BLOCK_TOP    "▀"
#define BLOCK_BOTTOM "▄"
#define BLOCK_EMPTY  " "

struct termios orig_termios;

typedef struct {
  bool state;  // 0: empty, 1: full
  uint color : 3; // \x1b[3_m (0-7)
} Cell;

typedef struct {
  uint row, col; // Position
  bool shape[4][4];
  uint color : 3; // \x1b[3_m (0-7)
} Totromino;

Cell grid[ROWS][COLS] = {0};
Totromino current;

const char* border =
"┌          ┐00 01\n"
"│          │02 03\n"
"│          │04 05\n"
"│          │06 07\n"
"│          │08 09\n"
"│          │10 11\n"
"│          │12 13\n"
"│          │14 15\n"
"│          │16 17\n"
"│          │18 19\n"
"└──────────┘\n"
;

const bool shapes[][4][4] = {
  { // I
    {1, 1, 1, 1},
    {0, 0, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // J
    {1, 0, 0, 0},
    {1, 1, 1, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // L
    {0, 0, 0, 1},
    {0, 1, 1, 1},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // O
    {1, 1, 0, 0},
    {1, 1, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // S
    {0, 1, 1, 0},
    {1, 1, 0, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // T
    {0, 1, 0, 0},
    {1, 1, 1, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  },
  { // Z
    {1, 1, 0, 0},
    {0, 1, 1, 0},
    {0, 0, 0, 0},
    {0, 0, 0, 0}
  }
};

void disable_raw_input() {
  tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios);
  printf("\x1b[?25h"); // Show cursor
}

void enable_raw_input() {
  tcgetattr(STDIN_FILENO, &orig_termios);

  struct termios raw = orig_termios;
  raw.c_lflag &= ~(ICANON | ECHO); // Disable line buffering and echo
  raw.c_cc[VMIN] = 0;
  raw.c_cc[VTIME] = 0;

  tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
  printf("\x1b[?25l"); // Hide cursor
}

void clear_screen() {
  printf("\x1b[2J");
  printf("\x1b[H");
}

void move_cursor(uint row, uint col) {
  printf("\x1b[%d;%dH", row + 1, col + 1 + OFFSET);
}

void set_color(uint color) {
  printf("\x1b[3%dm", color);
}

void reset_color() {
  printf("\x1b[0m");
}

void draw_cell(uint r, uint c) {
  if (r >= ROWS) return;

  uint screen_r = r / 2;

  bool filled = grid[r][c].state;
  bool upper = (r % 2) == 0;
  bool lower = (r % 2) == 1;
  uint color = grid[r][c].color;

  move_cursor(screen_r, c);
  set_color(color);

  if (!filled) {
    printf(BLOCK_EMPTY);
  } else {
    if (upper && lower) {
      printf(BLOCK_FULL);
    } else if (upper) {
      printf(BLOCK_TOP);
    } else if (lower) {
      printf(BLOCK_BOTTOM);
    } else {
      printf("?");
    }
  }

  reset_color();
  fflush(stdout);
}

void draw_grid() {
  printf(border);
  for (uint r = 0; r < ROWS; r+=2) {
    for (uint c = 0; c < COLS; c++) {
      draw_cell(r, c);
    }
  }
}

void print_grid() {
  printf("\x1b[%d;%dH", ROWS/2 + 4, 1);
  for (uint r = 0; r < ROWS; r++) {
    for (uint c = 0; c < COLS; c++) {
      printf("%u", grid[r][c].state);
    }
    printf(" %02u\n", r);
  }
}

void place_totromino(Totromino* t, uint filled) {
  for (uint r = 0; r < 4; r++) {
    for (uint c = 0; c < 4; c++) {
      if (t->shape[r][c]) {
        uint gr = t->row + r;
        uint gc = t->col + c;
        if (gr >= 0 && gr < ROWS && gc >= 0 && gc < COLS) {
          grid[gr][gc].state = filled ? 1 : 0;
          grid[gr][gc].color = t->color;
          draw_cell(gr, gc);
        }
      }
    }
  }
}

void spawn_totromino() {
  current.col = COLS/2 - 2;
  current.row = 0;
  memcpy(current.shape, shapes[0], sizeof(current.shape));
  current.color = 2;
  place_totromino(&current, 1);
}

void game_loop() {
  uint tick = 0;

  while (1) {
    usleep(50000); // 100ms
    print_grid();
    tick++;

    char c;
    if (read(STDIN_FILENO, &c, 1) == 1) {
      place_totromino(&current, 0);
      if (c == 'a')
        current.col--;
      else if (c == 'd')
        current.col++;
      else if (c == 's')
        current.row++;
      place_totromino(&current, 1);
    }

    if (tick % 10 == 0) {
      place_totromino(&current, 0);
      current.row++;
      if (current.row >= ROWS) {
        move_cursor(ROWS/2 + 1, 0);
        printf("Game Over!\n");
        break;
      }
      place_totromino(&current, 1);
    }
  }
}

int main() {
  enable_raw_input();
  clear_screen();

  draw_grid();
  spawn_totromino();
  game_loop();
  
  disable_raw_input();
  return 0;
}
