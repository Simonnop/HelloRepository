#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#include <unistd.h>

#define High 25
#define Width 50

int position_x, position_y;
int enemy_x1, enemy_y1;
int enemy_x2, enemy_y2;
int enemy_x3, enemy_y3;

double score = 0.0;
int canvas[High][Width] = {0};

int boss_x, boss_y;

void startup();
void show();
void updateWithInput();
void updateWithoutInput();
void gotoxy(int x, int y);
void HideCursor();
void Boss();

int main(void)
{
    startup();

    while (1)
    {
        Boss();
        show();
        updateWithoutInput();
        updateWithInput();
    }
    return 0;
}

void Boss()
{
    if (score == 20)
    {
        boss_x = 25;
        boss_y = 0;
        canvas[boss_y][boss_x] = 4;
        score += 0.1;
    }
}

void startup()
{
    position_y = High / 2;
    position_x = Width / 2;

    enemy_x1 = rand() % Width;
    enemy_y1 = 0;
    enemy_x2 = rand() % Width;
    enemy_y2 = 2;
    enemy_x3 = rand() % Width;
    enemy_y3 = 1;

    score = 0;

    canvas[position_y][position_x] = 1;
    canvas[enemy_y1][enemy_x1] = 3;
    canvas[enemy_y2][enemy_x2] = 3;
    canvas[enemy_y3][enemy_x3] = 3;

    HideCursor();
}

void show()
{
    gotoxy(0, 0);
    system("cls");
    int i, j, a;
    for (j = 0; j < High; j++)
    {
        for (i = 0; i < Width; i++)
        {
            if (canvas[j][i] == 1)
            {
                printf("  *  \n");

                for (a = 0; a < i; a++)
                {
                    printf(" ");
                }
                printf("*****\n");
                for (a = 0; a < i; a++)
                {
                    printf(" ");
                }
                printf(" * * \n");
            }
            else if (canvas[j][i] == 0)
            {
                printf(" ");
            }
            else if (canvas[j][i] == 2)
            {
                printf("  |");
            }
            else if (canvas[j][i] == 3)
            {
                printf("  $");
            }
            else if (canvas[j][i] == 4)
            {
                printf("*****\n");
                for (a = 0; a < i; a++)
                {
                    printf(" ");
                }
                printf(" *** \n");
                for (a = 0; a < i; a++)
                {
                    printf(" ");
                }
                printf("  *  \n");
            }
        }
        printf("\n");
    }
    printf("得分:%.0f\n", score);
    if (score < 10)
    {
        printf("得分达到10分，武器将会升级。\n");
    }
    if (score >= 10)
    {
        printf("武器已经升级，敌机速度加快。\n");
    }
    if (score >= 20)
    {
        printf("BOSS已经出现，BOSS达到底部即为失败！\n");
    }

    Sleep(10);
}

void updateWithoutInput()
{
    int i, j;
    static int hit = 0;
    for (i = 0; i < High; i++)
    {
        for (j = 0; j < Width; j++)
        {
            if (canvas[i][j] == 2)
            {
                if ((i == enemy_y1) && (j == enemy_x1))
                {
                    score++;
                    canvas[enemy_y1][enemy_x1] = 0;
                    enemy_x1 = rand() % Width;
                    enemy_y1 = 0;
                    canvas[enemy_y1][enemy_x1] = 3;
                    canvas[i][j] = 0;
                }

                if ((i == enemy_y2) && (j == enemy_x2))
                {
                    score++;
                    canvas[enemy_y2][enemy_x2] = 0;
                    enemy_x2 = rand() % Width;
                    enemy_y2 = 0;
                    canvas[enemy_y2][enemy_x2] = 3;
                    canvas[i][j] = 0;
                }

                if ((i == enemy_y3) && (j == enemy_x3))
                {
                    score++;
                    canvas[enemy_y3][enemy_x3] = 0;
                    enemy_x3 = rand() % Width;
                    enemy_y3 = 0;
                    canvas[enemy_y3][enemy_x3] = 3;
                    canvas[i][j] = 0;
                }

                if ((i == boss_y) && (j == boss_x))
                {
                    hit++;
                    canvas[i][j] = 0;
                }

                if (hit == 20)
                {
                    printf("BOSS已被击败，游戏胜利！");
                    Sleep(1000);
                    system("pause");
                    exit(0);
                }
            }

            if (canvas[i][j] == 2)
            {
                canvas[i][j] = 0;
                if (i > 0)
                {
                    canvas[i - 1][j] = 2;
                }
            }
        }
    }

    if (((position_x == enemy_x1) && (position_y == enemy_y1)) || ((position_x == enemy_x2) && (position_y == enemy_y2)) || ((position_x == enemy_x3) && (position_y == enemy_y3)))
    {
        printf("游戏失败!!!\n");
        Sleep(1000);
        system("pause");
        exit(0);
    }

    if (boss_y == (High - 1))
    {
        printf("游戏失败!!!\n");
        Sleep(1000);
        system("pause");
        exit(0);
    }

    if (enemy_y1 == (High - 1))
    {
        canvas[enemy_y1][enemy_x1] = 0;
        enemy_x1 = rand() % Width;
        enemy_y1 = 0;
        canvas[enemy_y1][enemy_x1] = 3;

        score--;
    }

    if (enemy_y2 == (High - 1))
    {
        canvas[enemy_y2][enemy_x2] = 0;
        enemy_x2 = rand() % Width;
        enemy_y2 = 0;
        canvas[enemy_y2][enemy_x2] = 3;

        score--;
    }

    if (enemy_y3 == (High - 1))
    {
        canvas[enemy_y3][enemy_x3] = 0;
        enemy_x3 = rand() % Width;
        enemy_y3 = 0;
        canvas[enemy_y3][enemy_x3] = 3;

        score--;
    }

    static int speed = 0;
    if (speed < 15)
    {
        speed++;
    }
    if ((speed < 15) && (score >= 10))
    {
        speed++;
    }

    if (speed >= 15)
    {
        if (enemy_y1 < (High - 1))
        {
            canvas[enemy_y1++][enemy_x1] = 0;
            canvas[enemy_y1][enemy_x1] = 3;
            speed = 0;
        }
        if (enemy_y2 < (High - 1))
        {
            canvas[enemy_y2++][enemy_x2] = 0;
            canvas[enemy_y2][enemy_x2] = 3;
            speed = 0;
        }
        if (enemy_y3 < (High - 1))
        {
            canvas[enemy_y3++][enemy_x3] = 0;
            canvas[enemy_y3][enemy_x3] = 3;
            speed = 0;
        }
        if ((boss_y < (High - 1)) && (score >= 20))
        {
            canvas[boss_y++][boss_x] = 0;
            canvas[boss_y][boss_x] = 4;
            speed = 0;
        }
    }
}

void updateWithInput()
{
    char input;
    if ((kbhit()))
    {
        input = getch();
        if (input == 'a')
        {
            if (position_x > 0)
            {
                canvas[position_y][position_x--] = 0;
                canvas[position_y][position_x] = 1;
            }
        }
        if (input == 'd')
        {
            if (position_x < (Width - 1))
            {
                canvas[position_y][position_x++] = 0;
                canvas[position_y][position_x] = 1;
            }
        }
        if (input == 'w')
        {
            if (position_y > 0)
            {
                canvas[position_y--][position_x] = 0;
                canvas[position_y][position_x] = 1;
            }
        }
        if (input == 's')
        {
            if (position_y < (High - 1))
            {
                canvas[position_y++][position_x] = 0;
                canvas[position_y][position_x] = 1;
            }
        }
        if (input == ' ')
        {
            if (position_y < (High - 1))
            {
                if (score < 10)
                {
                    canvas[position_y - 1][position_x] = 2;
                }
                if (score >= 10)
                {
                    canvas[position_y - 1][position_x - 3] = 2;
                    canvas[position_y - 1][position_x - 2] = 2;
                    canvas[position_y - 1][position_x - 1] = 2;
                }
            }
        }
    }
}

void gotoxy(int x, int y)
{
    HANDLE handle = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD pos;
    pos.X = x;
    pos.Y = y;
    SetConsoleCursorPosition(handle, pos);
}

void HideCursor()
{
    CONSOLE_CURSOR_INFO cursor_info = {1, 0};
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursor_info);
}
