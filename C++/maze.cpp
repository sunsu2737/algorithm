#include <iostream>
#include <queue>
using namespace std;
int N, M;
int Hx, Hy;
int Ex, Ey;
int maze[2][1001][1001];

int movealbe(int x, int y, int z)
{
    if (z == 1)
    {
        if (0 < x && x <= N && 0 < y && y <= M && maze[0][x][y] == 0)
        {
            return z;
        }
        else if (0 < x && x <= N && 0 < y && y <= M && maze[0][x][y] == 1 )
        {
            return 0;
        }
    }
    else if (z == 0)
    {
        if (0 < x && x <= N && 0 < y && y <= M && maze[1][x][y] == 0)
        {
            return z;
        }
    }
    return -1;
}

typedef struct
{
    int x, y, z, cnt;
} xyzcnt;

void maze_run()
{
    queue<xyzcnt> idx;
    idx.push({Hx, Hy, 1, 0});
    maze[0][Hx][Hy]=-1;
    maze[1][Hx][Hy]=-1;
    while (!idx.empty())
    {

        int x = idx.front().x;
        int y = idx.front().y;
        int z = idx.front().z;
        int cnt = idx.front().cnt;

        idx.pop();

        if (x == Ex && y == Ey)
        {
            cout << -cnt;
            return;
        }
        cnt--;
        int A = movealbe(x + 1, y, z);
        if (A != -1)
        {
            idx.push({x + 1, y, A, cnt});
            if (A == 1)
            {
                maze[0][x+1][y] = cnt;
                maze[1][x+1][y] = cnt;
            }
            else if (A == 0)
            {
                maze[1][x+1][y] = cnt;
            }
        }
        A = movealbe(x, y + 1, z);
        if (A != -1)
        {
            idx.push({x, y + 1, A, cnt});
            if (A == 1)
            {
                maze[0][x][y +1] = cnt;
                maze[1][x][y +1] = cnt;
            }
            else if (A == 0)
            {
                maze[1][x][y +1] = cnt;
            }
        }
        A = movealbe(x - 1, y, z);
        if (A != -1)
        {
            idx.push({x - 1, y, A, cnt});
            if (A == 1)
            {
                maze[0][x-1][y ] = cnt;
                maze[1][x-1][y ] = cnt;
            }
            else if (A == 0)
            {
                maze[1][x-1][y ] = cnt;
            }
        }
        A = movealbe(x, y - 1, z);
        if (A != -1)
        {
            idx.push({x, y - 1, A, cnt});
            if (A == 1)
            {
                maze[0][x][y - 1] = cnt;
                maze[1][x][y - 1] = cnt;
            }
            else if (A == 0)
            {
                maze[1][x][y - 1] = cnt;
            }
        }
    }
    cout << -1;
}

int main()
{
    cin >> N >> M >> Hx >> Hy >> Ex >> Ey;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin >> maze[0][i][j];
            maze[1][i][j] = maze[0][i][j];
        }
    }
    maze_run();
    
}