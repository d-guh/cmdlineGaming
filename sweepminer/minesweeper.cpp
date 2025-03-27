#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <string>
#include <algorithm>
#include <termios.h>
#include <unistd.h>

using namespace std;

const int WIDTH = 24;
const int HEIGHT = 24;
const int MINES = 99;

struct Cell {
  bool mine = false;
  bool revealed = false;
  bool flagged = false;
  int adjacent_mines = 0;
};

vector<vector<Cell>> grid(HEIGHT, vector<Cell>(WIDTH));
int cursor_x = 0, cursor_y = 0;
bool first_move = true;

void setRawMode(bool enable){
  static struct termios oldt, newt;
  if(enable){
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
  }else{
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
  }
}

void placeMines(int first_x, int first_y){
  srand(time(nullptr));
  int mines_placed = 0;

  while(mines_placed < MINES){
    int x = rand() % WIDTH;
    int y = rand() % HEIGHT;

    if(!grid[y][x].mine &&!(x >= first_x - 1 && x <= first_x + 1 && y >= first_y - 1 && y <= first_y + 1)){
      grid[y][x].mine = true;
      mines_placed++;
    }
  }
}

void firstMoveReveal(int y, int x){
  if(grid[y][x].mine || grid[y][x].revealed) {
    return;
  }
  
  grid[y][x].revealed = true;

  if(grid[y][x].adjacent_mines == 0){
    for(int dy = -1; dy <= 1; dy++){
      for(int dx = -1; dx <= 1; dx++){
        int ny = y + dy;
        int nx = x + dx;
        if(ny >= 0 && ny < HEIGHT && nx >= 0 && nx < WIDTH){
          firstMoveReveal(ny, nx);
        }
      }
    }
  }
}

void processCell(int x, int y) {
    if (grid[y][x].mine) return;

    for (int dy = -1; dy <= 1; dy++) {
        for (int dx = -1; dx <= 1; dx++) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx >= 0 && nx < WIDTH && ny >= 0 && ny < HEIGHT && grid[ny][nx].mine) {
                grid[y][x].adjacent_mines++;
            }
        }
    }
}

void calcAdjacentMines() {
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            processCell(x, y);
        }
    }
}

void revealCell(int y, int x){
  if(y < 0 || y >= HEIGHT || x < 0 || x >= WIDTH || grid[y][x].revealed || grid[y][x].flagged) return;

  grid[y][x].revealed = true;

  if(grid[y][x].adjacent_mines == 0 && !grid[y][x].mine){
    for(int dy = -1; dy <= 1; dy++){
      for(int dx = -1; dx <= 1; dx++){
        revealCell(y + dy, x + dx);
      }
    }
  }
}

bool checkWin(){
  for(int y = 0; y < HEIGHT; y++){
    for(int x = 0; x < WIDTH; x++){
      if((grid[y][x].mine && !grid[y][x].flagged) || (!grid[y][x].mine && !grid[y][x].revealed)){
        return false;
      }
    }
  }
  return true;
}

void drawGrid(){
  for(int y = 0; y < HEIGHT; y++){
    for(int x = 0; x < WIDTH; x++){
      bool shouldHighlight = (y == cursor_y && x == cursor_x && !(grid[y][x].revealed && grid[y][x].mine));

      if(shouldHighlight){
        cout << "\033[7m";
      }

      if(grid[y][x].revealed){
        if(grid[y][x].mine){
          cout << "\033[101m*\033[0m"; 
        }else{
          int mines = grid[y][x].adjacent_mines;
          switch(mines){
            case 1: cout << "\033[36m1\033[0m"; break;
            case 2: cout << "\033[92m2\033[0m"; break;
            case 3: cout << "\033[91m3\033[0m"; break;
            case 4: cout << "\033[94m4\033[0m"; break;
            case 5: cout << "\033[93m5\033[0m"; break;
            case 6: cout << "\033[90m6\033[0m"; break;
            case 7: cout << "\033[95m7\033[0m"; break;
            case 8: cout << "\033[96m8\033[0m"; break;
            default: cout << " "; break;
          }
        }
      }else if(grid[y][x].flagged){
        cout << "\033[105mF\033[0m";
      }else{
        cout << "*";
      }
      
      if(shouldHighlight){
        cout << "\033[0m";
      }
      cout << " ";
    }
    cout << endl;
  }
}

void handleInput(char input, bool isEscape = false){
  if(isEscape){
    switch(input){
      case 'A': cursor_y = max(0, cursor_y - 1); break;
      case 'B': cursor_y = min(HEIGHT - 1, cursor_y + 1); break;
      case 'D': cursor_x = max(0, cursor_x - 1); break;
      case 'C': cursor_x = min(WIDTH - 1, cursor_x + 1); break;
    }
  }else{
    switch(input){
      case 'r':
        if(!grid[cursor_y][cursor_x].flagged){
          if(first_move){
            first_move = false;
            placeMines(cursor_x, cursor_y);
            calcAdjacentMines();
            firstMoveReveal(cursor_y, cursor_x);
          }else if(grid[cursor_y][cursor_x].mine){
            grid[cursor_y][cursor_x].revealed = true;
            system("clear");
            drawGrid();
            setRawMode(false);
            cout << "You hit a mine, stay out of Afghanistan next time\n";
            char keyPress;
            read(STDIN_FILENO, &keyPress, 1);
            exit(0);
          }else{
            revealCell(cursor_y, cursor_x);
          }
        }
        break;
      case 'f':
        if(!grid[cursor_y][cursor_x].revealed){
          grid[cursor_y][cursor_x].flagged = !grid[cursor_y][cursor_x].flagged;
        }
        break;
    }
  }
}


int main(){
  setRawMode(true);

  while(true){
    system("clear");
    drawGrid();
    cout << "Use arrow keys to move, 'r' to reveal, 'f' to flag, and 'q' to quit.\n";

    if(checkWin()){
      setRawMode(false);
      system("clear");
      cout << "You Win\n";
      break;
    }

    char input;
    if(read(STDIN_FILENO, &input, 1) == 1){
      if(input == '\033'){
        char seq[2];
        if(read(STDIN_FILENO, &seq, 2) == 2){
          handleInput(seq[1], true);
        }
      }else if(input == 'q'){
        break;
      }else{
        handleInput(input);
      }
    }
  }

  setRawMode(false);
  cout << "Game Over\n";
  return 0;
}
