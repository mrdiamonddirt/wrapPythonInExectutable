using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace CommandLineMenu
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get a list of all the scripts in the current directory
            string[] scripts = Directory.GetFiles(Directory.GetCurrentDirectory(), "*.py");

            // Display the menu
            Console.WriteLine("Please select a script to run:");
            for (int i = 0; i < scripts.Length; i++)
            {
                Console.WriteLine($"{i + 1}. {Path.GetFileNameWithoutExtension(scripts[i])}");
            }

            // Read the user's selection
            int selection = ReadSelection(scripts.Length);

            // Run the selected script
            RunScript(scripts[selection - 1]);
        }

        static int ReadSelection(int maxSelection)
        {
            int selection = 0;
            ConsoleKeyInfo key;
            do
            {
                key = Console.ReadKey(true);
                if (key.Key == ConsoleKey.DownArrow && selection < maxSelection)
                {
                    selection++;
                }
                else if (key.Key == ConsoleKey.UpArrow && selection > 1)
                {
                    selection--;
                }
                Console.SetCursorPosition(0, Console.CursorTop);
                Console.Write(new string(' ', Console.BufferWidth));
                Console.SetCursorPosition(0, Console.CursorTop - 1);
                Console.Write($"Selection: {selection}");
            } while (key.Key != ConsoleKey.Enter);

            Console.WriteLine();
            return selection;
        }

        static void RunScript(string scriptPath)
        {
            Process.Start("python", scriptPath);
        }
    }
}
