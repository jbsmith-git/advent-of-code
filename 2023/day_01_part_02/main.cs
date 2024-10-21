public class Program
{    
    public static void Main()
    {
        List<string> text_from_file = File.ReadAllLines("input.txt").ToList();
        var digits = new List<string> {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        var text_digits = new List<string> {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        var non_text_digits = new List<string> {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        int total_sum = 0;
        foreach (string line in text_from_file)
        {
            string first_digit = "XXX";
            Boolean first_digit_found = false;
            string last_digit = "XXX";
            char[] split_line = line.ToCharArray();
            for (int i = 0; i < split_line.Length; i++)
            {
                for (int j = i; j < split_line.Length; j++)
                {
                    string char_string = "";
                    for (int k = i; k < j+1; k++)
                    {
                        char_string += split_line[k];
                    }
                    int result = digits.IndexOf(char_string);
                    if (result != -1)
                    {
                        if (first_digit_found == false)
                        {
                            first_digit_found = true;
                            first_digit = char_string;
                            last_digit = char_string;
                        }
                        else
                        {
                            last_digit = char_string;
                        }
                    }
                }
            }
            if (text_digits.IndexOf(first_digit) != -1)
            {
                first_digit = non_text_digits[text_digits.IndexOf(first_digit)];
            }
            if (text_digits.IndexOf(last_digit) != -1)
            {
                last_digit = non_text_digits[text_digits.IndexOf(last_digit)];
            }
            total_sum += int.Parse(first_digit + last_digit);
        }
        Console.WriteLine("Day 1 Part 2: " + total_sum);
    }
}