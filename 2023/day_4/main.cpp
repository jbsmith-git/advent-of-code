#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <map>
#include <bits/stdc++.h>
using namespace std; 

int digits_to_int(vector<char> digits)
{
    int combined_int = 0;
    for (int p = 0; p < digits.size(); p++)
    {
        if (digits[digits.size()-p-1] != '.')
        {
            combined_int += (digits[digits.size()-p-1] - '0')*pow(10, p);
        }
    }
    return combined_int;
}

vector<map<string, vector<int>>> import_input()
{
    // Replaced spaces with '.' in input file to make import easier
    // Import input file as grid
    ifstream fin("input.txt");
    vector<vector<char>> grid;
    vector<char> col;
    char x;
    while (fin >> x)
    {
        col.push_back(x);
        if (col.size() == 116)
        {
            grid.push_back(col);
            col.clear();
        }
    }
    fin.close();

    // Convert to more useful map
    vector<map<string, vector<int>>> cards;
    map<string, vector<int>> card;
    vector<int> winning_numbers;
    vector<int> chosen_numbers;
    for (int r = 0; r < 192; r++)
    {
        for (int i = 10; i <= 37; i += 3)
        {
            winning_numbers.push_back(digits_to_int({grid[r][i], grid[r][i+1]}));
        }
        for (int i = 42; i <= 114; i += 3)
        {
            chosen_numbers.push_back(digits_to_int({grid[r][i], grid[r][i+1]}));
        }

        card["WINNING_NUMBERS"] = winning_numbers;
        card["CHOSEN_NUMBERS"] = chosen_numbers;
        cards.push_back(card);

        winning_numbers.clear();
        chosen_numbers.clear();
        card.clear();
    }
    return cards;
}

int compute_card_score(map<string, vector<int>> card)
{
    int score = 0;
    for (int n : card["CHOSEN_NUMBERS"])
    {
        int matches = count(card["WINNING_NUMBERS"].begin(), card["WINNING_NUMBERS"].end(), n);
        if (matches > 0)
        {
            if (score == 0)
            {
                score = 1;
            }
            else
            {
                score *= 2;
            }
        }
    }
    return score;
}

int main()
{
    vector<map<string, vector<int>>> input = import_input();

    int score_sum = 0;
    for (int c = 0; c < 192; c++)
    {
        score_sum += compute_card_score(input[c]);
    }

    cout << "Day 4 Part 1: " << score_sum;
    
    cin.ignore();
    return 0;
}