public class Program
{    
    public static void Main()
    {
        List<string> text_from_file = File.ReadAllLines("input.txt").ToList();
        int[] digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        int total_sum = 0;
        foreach (string line in text_from_file)
        {
            Boolean first_found = false;
            int latest_digit = -100;
            int store_first_digit = 0;
            char[] characters = line.ToCharArray();
            for (int j = 0; j < characters.Length; j++)
            {
                int result;
                if (int.TryParse(characters[j].ToString(), out result) == true)
                {
                    int digit = characters[j] - '0';
                    if (first_found == false)
                    {
                        first_found = true;
                        store_first_digit = digit;
                    }
                    else
                    {
                        latest_digit = digit;
                    }
                }
            }
            if (latest_digit == -100)
            {
                latest_digit = store_first_digit;
            }
            total_sum += int.Parse(store_first_digit.ToString() + latest_digit.ToString());
        }
        Console.WriteLine("Day 1 Part 1: " + total_sum);
    }
}