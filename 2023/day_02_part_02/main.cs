public class Program
{    
    public static void Main()
    {
        List<string> text_from_file = File.ReadAllLines("input.txt").ToList();
        string[] line_delimiters = {": ", "; "};
        string[] pull_delimiters = {", "};
        string[] draw_delimiters = {" "};
        int power_sum = 0;
        foreach (string line in text_from_file)
        {
            int power = 0;
            int red_min = 0;
            int blue_min = 0;
            int green_min = 0;
            string[] split_line = line.Split(line_delimiters, System.StringSplitOptions.RemoveEmptyEntries);
            split_line = split_line.Skip(1).ToArray();
            foreach (string pull in split_line)
            {
                string[] split_pull = pull.Split(pull_delimiters, System.StringSplitOptions.RemoveEmptyEntries);
                foreach (string draw in split_pull)
                {
                    string[] split_draw = draw.Split(draw_delimiters, System.StringSplitOptions.RemoveEmptyEntries);
                    if (draw.Contains("red"))
                    {
                        if (int.Parse(split_draw[0]) > red_min)
                        {
                            red_min = int.Parse(split_draw[0]);
                        }
                    }
                    if (draw.Contains("blue"))
                    {
                        if (int.Parse(split_draw[0]) > blue_min)
                        {
                            blue_min = int.Parse(split_draw[0]);
                        }
                    }
                    if (draw.Contains("green"))
                    {
                        if (int.Parse(split_draw[0]) > green_min)
                        {
                            green_min = int.Parse(split_draw[0]);
                        }
                    }
                }
            }
            power = red_min * blue_min * green_min;
            power_sum += power;
        }
        Console.WriteLine("Day 2 Part 2: " + power_sum);
    }
}