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
    vector<int> card_number;
    vector<int> winning_numbers;
    vector<int> chosen_numbers;
    for (int r = 0; r < 192; r++)
    {
        card_number.push_back(digits_to_int({grid[r][5], grid[r][6], grid[r][7]}));
        for (int i = 10; i <= 37; i += 3)
        {
            winning_numbers.push_back(digits_to_int({grid[r][i], grid[r][i+1]}));
        }
        for (int i = 42; i <= 114; i += 3)
        {
            chosen_numbers.push_back(digits_to_int({grid[r][i], grid[r][i+1]}));
        }

        card["CARD_NUMBER"] = card_number;
        card["WINNING_NUMBERS"] = winning_numbers;
        card["CHOSEN_NUMBERS"] = chosen_numbers;
        cards.push_back(card);

        card_number.clear();
        winning_numbers.clear();
        chosen_numbers.clear();
        card.clear();
    }
    return cards;
}

int compute_card_matches(map<string, vector<int>> card)
{
    int matches = 0;
    for (int n : card["CHOSEN_NUMBERS"])
    {
        matches += count(card["WINNING_NUMBERS"].begin(), card["WINNING_NUMBERS"].end(), n);
    }
    return matches;
}

map<int, vector<int>> generate_card_map(vector<map<string, vector<int>>> input)
{
    map<int, vector<int>> card_map;
    vector<int> new_card_numbers;
    for (map<string, vector<int>> card : input)
    {
        int matches = compute_card_matches(card);
        for (int m = 1; m <= matches; m++)
        {
            new_card_numbers.push_back(card["CARD_NUMBER"][0] + m);
        }
        card_map[card["CARD_NUMBER"][0]] = new_card_numbers;
        new_card_numbers.clear();
    }
    return card_map;
}

int compute_card_count(vector<map<string, vector<int>>> input, map<int, vector<int>> card_map)
{
    vector<int> unscored_cards;
    for (map<string, vector<int>> card : input)
    {
        unscored_cards.push_back(card["CARD_NUMBER"][0]);
    }
    vector<int> new_card_numbers;

    int card_index = 0;
    while (card_index < unscored_cards.size())
    {
        // Pull out the card at card_index from unscored cards
        int card_number = unscored_cards[card_index];

        // For each 'win' on that card, add subsequent cards to unscored cards
        new_card_numbers = card_map[card_number];
        unscored_cards.insert(unscored_cards.end(), new_card_numbers.begin(), new_card_numbers.end());
        new_card_numbers.clear();

        card_index++;
    }

    return unscored_cards.size();
}

int main()
{
    vector<map<string, vector<int>>> input = import_input();

    map<int, vector<int>> card_map = generate_card_map(input);

    cout << "Day 4 Part 2: " << compute_card_count(input, card_map);

    cin.ignore();
    return 0;
}