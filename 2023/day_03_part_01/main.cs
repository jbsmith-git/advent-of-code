public class Program
{    
    public static void Main()
    {
        List<string> input_file = File.ReadAllLines("input.txt").ToList();
        int[] digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        char[] char_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        char[] non_symbols = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'};
        int part_number_sum = 0;
        string current_number = "";
        input_file.Add("............................................................................................................................................");
        input_file.Insert(0, "............................................................................................................................................");
        input_file.Add("............................................................................................................................................");
        input_file.Insert(0, "............................................................................................................................................");
        for (int j = 0; j < input_file.Count; j++)
        {
            input_file[j] = ".." + input_file[j] + "..";
            // Console.WriteLine(input_file[j]);
        }
        for (int line_num = 1; line_num < 143; line_num++)
        {
            current_number = "";
            for (int i = 1; i < 143; i++)
            {
                if (char_digits.Contains(input_file[line_num][i]))
                {
                    current_number += input_file[line_num][i];
                }
                else
                {
                    if (current_number != "")
                    {
                        int part_candidate = int.Parse(current_number);
                        current_number = "";
                        if (part_candidate >= 100)
                        {
                            if (!(non_symbols.Contains(input_file[line_num][i]) && non_symbols.Contains(input_file[line_num][i - 4]) && non_symbols.Contains(input_file[line_num - 1][i]) && non_symbols.Contains(input_file[line_num - 1][i - 1]) && non_symbols.Contains(input_file[line_num - 1][i - 2]) && non_symbols.Contains(input_file[line_num - 1][i - 3]) && non_symbols.Contains(input_file[line_num - 1][i - 4]) && non_symbols.Contains(input_file[line_num + 1][i]) && non_symbols.Contains(input_file[line_num + 1][i - 1]) && non_symbols.Contains(input_file[line_num + 1][i - 2]) && non_symbols.Contains(input_file[line_num + 1][i - 3]) && non_symbols.Contains(input_file[line_num+1][i-4])))
                            {
                                part_number_sum += part_candidate;
                            }
                        }
                        if (part_candidate >= 10 && part_candidate < 100)
                        {
                            if (!(non_symbols.Contains(input_file[line_num][i]) && non_symbols.Contains(input_file[line_num][i - 3]) && non_symbols.Contains(input_file[line_num - 1][i]) && non_symbols.Contains(input_file[line_num - 1][i - 1]) && non_symbols.Contains(input_file[line_num - 1][i - 2]) && non_symbols.Contains(input_file[line_num - 1][i - 3]) && non_symbols.Contains(input_file[line_num + 1][i]) && non_symbols.Contains(input_file[line_num + 1][i - 1]) && non_symbols.Contains(input_file[line_num + 1][i - 2]) && non_symbols.Contains(input_file[line_num + 1][i - 3])))
                            {
                                part_number_sum += part_candidate;
                            }
                        }
                        if (part_candidate < 10)
                        {
                            if (!(non_symbols.Contains(input_file[line_num][i]) && non_symbols.Contains(input_file[line_num][i - 2]) && non_symbols.Contains(input_file[line_num - 1][i]) && non_symbols.Contains(input_file[line_num - 1][i - 1]) && non_symbols.Contains(input_file[line_num - 1][i - 2]) && non_symbols.Contains(input_file[line_num + 1][i]) && non_symbols.Contains(input_file[line_num + 1][i - 1]) && non_symbols.Contains(input_file[line_num + 1][i - 2])))
                            {
                                part_number_sum += part_candidate;
                            }
                        }
                    }
                }
            }
        }
        Console.WriteLine("Day 3 Part 1: " + part_number_sum);
    }
}