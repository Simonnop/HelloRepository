// new

const int SIZE = 12;



int[,] dots = new int[SIZE, SIZE];

string line = null;
string states = null;
string edges = null;

int count = 0;

void RunCode()
{
    CreateMap();
    GetPoints();
}

void CreateMap()
{
    // 设置路径点
    for (int i = 1; i < SIZE - 1; i++)
    {
        for (int j = 1; j < SIZE - 1; j++)
        {
            dots[i, j] = 1;
        }
    }
    // 设置非路径点
    for (int i = 1; i < SIZE - 1; i++)
    {
        dots[i, i] = 2;
    }
    // 输出地图
    for (int i = 1; i < SIZE - 1; i++)
    {
        for (int j = 1; j < SIZE - 1; j++)
        {
            switch (dots[i, j])
            {
                case 1: line += ". "; break;
                case 2: line += "0 "; break;
            }
        }
        Console.WriteLine(line);
        line = null;
    }
}


// 添加点状态
String StateAdd(int id, int x, int y, int theta)
{
    string tmpeLine;
    tmpeLine = "{\"state_id\":\"" + id + "\",\"pos\":{\"x\":" + x + ",\"y\":" + y + ",\"theta\":" + theta + "}}";
    tmpeLine += ",";
    tmpeLine += "\n";
    return tmpeLine;
}

// 添加边状态
// String EdgesAdd(int id, int x, int y, int theta)
// {

// }

// 对AGV位于的点判断
void GetPoints()
{
    for (int i = 1; i < SIZE - 1; i++)
    {
        for (int j = 1; j < SIZE - 1; j++)
        {
            if (dots[i, j] == 1)
            {

                if (dots[i, j - 1] == 1)
                {
                    states += StateAdd(count, i, j, 0);
                    count++;
                }
                if (dots[i + 1, j] == 1)
                {
                    states += StateAdd(count, i, j, 90);
                    count++;
                }
                if (dots[i, j + 1] == 1)
                {
                    states += StateAdd(count, i, j, 180);
                    count++;
                }
                if (dots[i - 1, j] == 1)
                {
                    states += StateAdd(count, i, j, 270);
                    count++;
                }

                Console.Write(states);
                states = null;
            }
        }
    }
}

RunCode();