/* totris.c
 * This version of totris renders using full block unicode characters, 
 * printed double wide to remain square.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <termios.h>
#include <fcntl.h>

#define ROWS 20
#define COLS 10
#define OFFSET 1 // Offset from border

#define BLOCK_FULL   "██"
#define BLOCK_SHADOW "░░"
#define BLOCK_EMPTY  "  "

#define BORDER_URC  "┐"
#define BORDER_ULC  "┌"
#define BORDER_LRC  "┘"
#define BORDER_LLC  "└"
#define BORDER_VERT "│"
#define BORDER_HORZ "─"

struct termios orig_termios;

bool debug_mode = false;

typedef struct {
  bool state;  // 0: empty, 1: full
  uint color : 3; // \x1b[3_m (0-7) ANSI
} Cell;

typedef struct {
  uint row, col; // Position in grid
  bool shape[4][4];
  uint color : 3;
} Totromino;

Cell grid[ROWS][COLS] = {0};
Totromino current;
uint score = 0;

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

void parse_args(int argc, char** argv) {
  for (int i = 1; i < argc; i++) {
    if (strcmp(argv[i], "--debug") == 0) {
      debug_mode = true;
    }
  }
}

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

void draw_border() {
  const uint score_box_width = 8;
  const uint score_box_height = 4;
  const uint width = COLS;
  const uint height = ROWS;

  // Body rows
  for (uint r = 0; r <= height; r++) {
    if (r == 0) { // 1st row
      printf(BORDER_ULC);
      for (uint i = 0; i < width; i++) printf(BLOCK_EMPTY);
      printf(BORDER_URC);

      if (debug_mode)
        printf("%02u ", r);
      else
        printf("  ");
      printf(BORDER_ULC);
      for (uint i = 0; i < score_box_width - 2; i++) printf(BORDER_HORZ);
      printf(BORDER_URC "\n");
    } else if (r < height) { // Middle rows
      printf(BORDER_VERT);
      for (uint c = 0; c < width; c++) {
        printf(BLOCK_EMPTY);
      }
      printf(BORDER_VERT);

      if (debug_mode)
        printf("%02u ", r);
      else
        printf("  ");

      if (r <= score_box_height - 2) { // Score box
        printf(BORDER_VERT);
        for (uint i = 0; i < score_box_width - 2; i++) printf(" ");
        printf(BORDER_VERT "\n");
      } else if (r == 3) {
        printf(BORDER_LLC);
        for (uint i = 0; i < score_box_width - 2; i++) printf(BORDER_HORZ);
        printf(BORDER_LRC "\n");
      } else {
        printf("\n");
      }
    } else { // Last row
      printf(BORDER_LLC);
      for (uint i = 0; i < width; i++) printf(BORDER_HORZ BORDER_HORZ);
      printf(BORDER_LRC);
    }
  }
}

void draw_score() {
  if (!debug_mode) {
    move_cursor (1, COLS*2 + 4);
    printf("Score:");
    move_cursor (2, COLS*2 + 4);
    printf("%06u", score);
  } else {
    move_cursor (1, COLS*2 + 5);
    printf("Score:");
    move_cursor (2, COLS*2 + 5);
    printf("%06u", score);
  }
}

void draw_cell(uint r, uint c) {
  if (r >= ROWS) return;

  bool filled = grid[r][c].state;
  uint color = grid[r][c].color;

  move_cursor(r, c*2);
  set_color(color);

  if (!filled) {
    printf(BLOCK_EMPTY);
  } else {
    printf(BLOCK_FULL);
  }

  reset_color();
  fflush(stdout);
}

void print_grid() {
  printf("\x1b[%d;%dH", ROWS + 4, 1);
  for (uint r = 0; r < ROWS; r++) {
    for (uint c = 0; c < COLS; c++) {
      printf("%u", grid[r][c].state);
    }
    printf(" %02u\n", r);
  }
}

bool can_place(const Totromino* t, int row, int col) {
  for (uint r = 0; r < 4; r++) {
    for (uint c = 0; c < 4; c++) {
      if (t->shape[r][c]) {
        uint gr = row + r;
        uint gc = col + c;

        if (gr < 0 || gr >= ROWS || gc < 0 || gc >= COLS) {
          return false;
        }
        
        if (grid[gr][gc].state) {
          return false;
        }
      }
    }
  }
  return true;
}

void place_totromino(Totromino* t, uint filled) {
  for (uint r = 0; r < 4; r++) {
    for (uint c = 0; c < 4; c++) {
      if (t->shape[r][c]) {
        uint gr = t->row + r;
        uint gc = t->col + c;
        grid[gr][gc].state = filled ? 1 : 0;
        grid[gr][gc].color = t->color;
        draw_cell(gr, gc);
      }
    }
  }
}

void rotate_totromino(Totromino* t) {
  bool temp[4][4];
  for (uint r = 0; r < 4; r++) {
    for (uint c = 0; c < 4; c++) {
      temp[c][3 - r] = t->shape[r][c]; // Rotate 90deg clockwise
    }
  }

  Totromino rotated = *t;
  memcpy(rotated.shape, temp, sizeof(temp));
  if (can_place(&rotated, rotated.row, rotated.col)) {
    memcpy(t->shape, temp, sizeof(temp));
  }
}

void spawn_totromino() {
  current.col = COLS/2 - 2;
  current.row = 0;
  memcpy(current.shape, shapes[rand() % 7], sizeof(current.shape));
  current.color = rand() % 7 + 1;
}

void insta_drop(Totromino* t) {
  place_totromino(t, 0);
  while (can_place(t, t->row + 1, t->col)) {
    t->row++;
  }
  place_totromino(t, 1);
}

bool clear_lines() {
  uint cleared = 0;
  for (uint r = ROWS - 1; r > 0; r--) {
    bool full = true;
    for (uint c = 0; c < COLS; c++) {
      if (!grid[r][c].state) {
        full = false;
        break;
      }
    }
  
    if (full) {
      cleared++;
      for (uint row = r; row > 0; row--) {
        for (uint col = 0; col < COLS; col++) {
          grid[row][col] = grid[row-1][col];
          draw_cell(row, col);
        }
      }
      for (uint col = 0; col < COLS; col++) {
        grid[0][col].state = 0;
        draw_cell(0, col);
      }
      r++;
    }
  }

  switch (cleared) {
    case 1: score += 100; break;
    case 2: score += 300; break;
    case 3: score += 500; break;
    case 4: score += 1000; break;
  }
  return cleared;
}

void game_loop() {
  uint tick = 0;

  while (1) {
    usleep(50000); // 50ms
    tick++;

    char c;
    if (read(STDIN_FILENO, &c, 1) == 1) {
      place_totromino(&current, 0);

      uint new_row = current.row;
      uint new_col = current.col;
      
      if (c == 'a') new_col--;
      else if (c == 'd') new_col++;
      else if (c == 's') new_row++;
      else if (c == 'w') rotate_totromino(&current);
      else if (c == ' ') { insta_drop(&current); tick = 10; }
      
      if (c == 'a' || c == 'd' || c == 's') {
        if (can_place(&current, new_row, new_col)) {
          current.row = new_row;
          current.col = new_col;
        }
      }

      place_totromino(&current, 1);
    }

    if (tick % 10 == 0) {
      place_totromino(&current, 0);
      int new_row = current.row + 1;

      if (can_place(&current, new_row, current.col)) {
        current.row = new_row;
      } else {
        place_totromino(&current, 1);

        if (clear_lines())
          draw_score();
        spawn_totromino();
        if (!can_place(&current, current.row, current.col)) {
          move_cursor(ROWS + 1, 0);
          printf("Game Over!\n");
          break;
        }
      }
    }
    place_totromino(&current, 1);
    
    if (debug_mode) print_grid();
  }
}

int main(int argc, char** argv) {
  parse_args(argc, argv);

  enable_raw_input();
  clear_screen();

  draw_border();
  draw_score();
  spawn_totromino();
  game_loop();
  
  disable_raw_input();
  return 0;
}
