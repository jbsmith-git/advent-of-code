public class Program
{    
    public static void Main()
    {
        List<string> text_from_file = File.ReadAllLines("input.txt").ToList();
        string[] delimiters = {"Game ", ": "};
        int game_id_sum = 0;
        int game_id = -1;
        foreach (string line in text_from_file)
        {
            var split_line = new List<string> (line.Split(delimiters, System.StringSplitOptions.RemoveEmptyEntries).ToList());
            game_id = int.Parse(split_line[0]);
            if (split_line[1].Contains("13 red") || split_line[1].Contains("14 red") || split_line[1].Contains("15 red") || split_line[1].Contains("16 red") || split_line[1].Contains("17 red") || split_line[1].Contains("18 red") || split_line[1].Contains("19 red") || split_line[1].Contains("20 red") || split_line[1].Contains("15 blue") || split_line[1].Contains("16 blue") || split_line[1].Contains("17 blue") || split_line[1].Contains("18 blue") || split_line[1].Contains("19 blue") || split_line[1].Contains("20 blue") || split_line[1].Contains("14 green") || split_line[1].Contains("15 green") || split_line[1].Contains("16 green") || split_line[1].Contains("17 green") || split_line[1].Contains("18 green") || split_line[1].Contains("19 green") || split_line[1].Contains("20 green"))
            {
                game_id_sum += game_id;
            }
        }
        Console.WriteLine("Day 2 Part 1: " + (5050-game_id_sum));
    }
}