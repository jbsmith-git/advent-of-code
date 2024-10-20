#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std; 

vector<vector<char>> import_input()
{
    vector<vector<char>> rows;
    ifstream fin("input.txt");

    vector<char> col;
    char x;
    while (fin >> x)
    {
        col.push_back(x);
        if (col.size() == 140)
        {
            rows.push_back(col);
            col.clear();
        }
    }

    fin.close();
    return rows;
}

int expand_number_on_row(vector<char> row, int c)
{
    vector<int> digits = {row[c] - '0'};

    // Go to the right
    for (int go_right = 1; go_right < 9; go_right++)
    {
        if (c+go_right > 139)
        {
            break;
        }
        if (not isdigit(row[c+go_right]))
        {
            break;
        }
        digits.push_back(row[c+go_right] - '0');
    }

    // Go to the left
    for (int go_left = -1; go_left > -9; go_left--)
    {
        if (c+go_left < 0)
        {
            break;
        }
        if (not isdigit(row[c+go_left]))
        {
            break;
        }
        digits.insert(digits.begin(), row[c+go_left] - '0');
    }

    // Convert vector to integer
    int part_number = 0;
    for (int p = 0; p < digits.size(); p++)
    {
        part_number += digits[digits.size()-p-1]*pow(10, p);
    }

    return part_number;
}

int compute_gear_ratio(vector<vector<char>> input, int r, int c)
{
    vector<int> surrounding_part_numbers;

    // Search row above
    if (r != 0)
    {
        if (isdigit(input[r-1][c]))
        {
            surrounding_part_numbers.push_back(expand_number_on_row(input[r-1], c));
        }
        else
        {
            if (c != 0)
            {
                if (isdigit(input[r-1][c-1]))
                {
                    surrounding_part_numbers.push_back(expand_number_on_row(input[r-1], c-1));
                }
            }
            if (c != 139)
            {
                if (isdigit(input[r-1][c+1]))
                {
                    surrounding_part_numbers.push_back(expand_number_on_row(input[r-1], c+1));
                }
            }
        }
    }

    // Search row below
    if (r != 139)
    {
        if (isdigit(input[r+1][c]))
        {
            surrounding_part_numbers.push_back(expand_number_on_row(input[r+1], c));
        }
        else
        {
            if (c != 0)
            {
                if (isdigit(input[r+1][c-1]))
                {
                    surrounding_part_numbers.push_back(expand_number_on_row(input[r+1], c-1));
                }
            }
            if (c != 139)
            {
                if (isdigit(input[r+1][c+1]))
                {
                    surrounding_part_numbers.push_back(expand_number_on_row(input[r+1], c+1));
                }
            }
        }
    }
   
    // Search the same row
    if (c != 0)
    {
        if (isdigit(input[r][c-1]))
        {
            surrounding_part_numbers.push_back(expand_number_on_row(input[r], c-1));
        }
    }
    if (c != 139)
    {
        if (isdigit(input[r][c+1]))
        {
            surrounding_part_numbers.push_back(expand_number_on_row(input[r], c+1));
        }
    }

    // Compute gear ratio
    if (surrounding_part_numbers.size() == 2)
    {
        // cout << surrounding_part_numbers[0] << ", " << surrounding_part_numbers[1] << '\n';
        return surrounding_part_numbers[0] * surrounding_part_numbers[1];
    }
    else
    {
        return 0;
    }
}

int main()
{
    vector<vector<char>> input = import_input();

    int gear_ratio_sum = 0;
    for (int r = 0; r < 140; r++)
    {
        for (int c = 0; c < 140; c++)
        {
            if (input[r][c] == '*')
            {
                gear_ratio_sum += compute_gear_ratio(input, r, c);
            }
        }
    }

    cout << "Day 3 Part 2: " << gear_ratio_sum;
    
    cin.ignore();
    return 0;
}