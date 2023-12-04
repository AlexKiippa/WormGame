#include <conio.h>
#include <iostream>
#include <windows.h>
#include <ctime>

using namespace std;

// Constants for game dimensions
const int kWidth = 80;
const int kHeight = 20;

// Snake head and food coordinates
int headX, headY;
int foodX, foodY;

// Player's score and snake tail
int score;
int tailX[100], tailY[100];
int tailLength;

// Enum to represent movement direction
enum Direction { STOP = 0, LEFT, RIGHT, UP, DOWN };
Direction dir;

// Flag to track game over state
bool gameOver;

// Initialize game variables
void InitializeGame()
{
    // Seed the random number generator with current time
    srand(static_cast<unsigned>(time(0)));

    gameOver = false;
    dir = STOP;
    headX = kWidth / 2;
    headY = kHeight / 2;
    foodX = rand() % kWidth;
    foodY = rand() % kHeight;
    score = 0;
    tailLength = 0; // Reset snake's length
}

// ... (rest of the code remains unchanged) ...


// Render the game board
void RenderGame(string playerName)
{
    system("cls");

    // Draw top walls
    for (int i = 0; i < kWidth + 2; i++)
        cout << "-";
    cout << endl;

    // Draw game area
    for (int i = 0; i < kHeight; i++)
    {
        for (int j = 0; j <= kWidth; j++)
        {
            if (j == 0 || j == kWidth)
                cout << "|"; // Draw side walls
            else if (i == headY && j == headX)
                cout << "O"; // Draw snake head
            else if (i == foodY && j == foodX)
                cout << "#"; // Draw food
            else
            {
                bool printTail = false;
                // Check and print snake tail
                for (int k = 0; k < tailLength; k++)
                {
                    if (tailX[k] == j && tailY[k] == i)
                    {
                        cout << "o";
                        printTail = true;
                    }
                }
                if (!printTail)
                    cout << " ";
            }
        }
        cout << endl;
    }

    // Draw bottom walls
    for (int i = 0; i < kWidth + 2; i++)
        cout << "-";
    cout << endl;

    // Display player's score
    cout << playerName << "'s Score: " << score << endl;
}

// Update the game state
void UpdateGame()
{
    int prevX = tailX[0];
    int prevY = tailY[0];
    int prev2X, prev2Y;
    tailX[0] = headX;
    tailY[0] = headY;

    // Update snake tail
    for (int i = 1; i < tailLength; i++)
    {
        prev2X = tailX[i];
        prev2Y = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    // Move snake head based on direction
    switch (dir)
    {
    case LEFT:
        headX--;
        break;
    case RIGHT:
        headX++;
        break;
    case UP:
        headY--;
        break;
    case DOWN:
        headY++;
        break;
    }

    // Check for collision with walls
    if (headX >= kWidth || headX < 0 || headY >= kHeight || headY < 0)
        gameOver = true;

    // Check for collision with snake tail
    for (int i = 0; i < tailLength; i++)
    {
        if (tailX[i] == headX && tailY[i] == headY)
            gameOver = true;
    }

    // Check for collision with food
    if (headX == foodX && headY == foodY)
    {
        score += 10;
        foodX = rand() % kWidth;
        foodY = rand() % kHeight;
        tailLength++;
    }
}

// Set the game difficulty level
int SetDifficulty()
{
    int delay, choice;
    cout << "\nSET DIFFICULTY\n1: Easy\n2: Medium\n3: Hard "
         << "\nNOTE: If not chosen or pressed any other key, the difficulty will be automatically set to medium\nChoose difficulty level: ";
    cin >> choice;

    // Set delay based on difficulty
    switch (choice)
    {
    case 1:
        delay = 50;
        break;
    case 2:
        delay = 100;
        break;
    case 3:
        delay = 150;
        break;
    default:
        delay = 100;
    }

    return delay;
}

// Handle user input for controlling the snake
void GetUserInput()
{
    if (_kbhit())
    {
        // Get the pressed key
        switch (_getch())
        {
        case 'a':
            dir = LEFT;
            break;
        case 'd':
            dir = RIGHT;
            break;
        case 'w':
            dir = UP;
            break;
        case 's':
            dir = DOWN;
            break;
        case 'x':
            gameOver = true;
            break;
        }

        // Clear input buffer
        while (_kbhit())
            _getch();
    }
}

// Ask the player if they want to play again
bool AskForReplay()
{
    char replayChoice;
    cout << "Your final score: " << score << endl;
    cout << "Do you want to play again? (y/n): ";
    cin >> replayChoice;
    return (replayChoice == 'y' || replayChoice == 'Y');
}

// Main game loop
int main()
{
    string playerName;
    cout << "Player name: ";
    cin >> playerName;
    int delay = SetDifficulty();

    do
    {
        InitializeGame();
        while (!gameOver)
        {
            RenderGame(playerName);
            GetUserInput();
            UpdateGame();
            Sleep(delay);
        }
   } while (AskForReplay()); 

	
}
