using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CleanWikiParallel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBoxPath.Text = @"D:\SoftwareProjects\SemanticRelations\Korpora\Wikipedia\pages\";
            textBoxStart.Text = "0";
            textBoxEnd.Text = "1";
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private static List<string> GetFiles(string path)
        {
            if (Directory.Exists(path))
            {
                return Directory.GetFiles(path).ToList();
            }
            else
            {
                return new List<string>(); 
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime time = DateTime.Now;
            labelTime.Text = (DateTime.Now - time).ToString();
            List<string> myEnumerable = new List<string>();
            int start = 0;
            Int32.TryParse(textBoxStart.Text, out start);
            int end = 0;
            Int32.TryParse(textBoxEnd.Text, out end);

            for (int i = start; i < end; ++i)
            {
                myEnumerable.AddRange(GetFiles(textBoxPath.Text + i ));
            }
            labelFiles.Text = myEnumerable.Count + "";
            /*
            List<string> list = new List<string>();
            for (int i = 0; i < 200; i++)
            {
                list.Add(myEnumerable.ElementAt(i));
            }
            */
            Parallel.ForEach(myEnumerable, obj =>
            {

                //ProcessStartInfo perlStartInfo = new ProcessStartInfo(@"C:\Perl64\bin\perl.exe");
                ProcessStartInfo perlStartInfo = new ProcessStartInfo(@"C:\Windows\System32\cmd.exe");
                string output = " > "+Path.GetDirectoryName(obj)+@"\texts\text" + Path.GetFileName(obj) + ".txt";
                perlStartInfo.Arguments = @"/c perl D:\SoftwareProjects\SemanticRelations\Einarbeitung\Word2Vec\Test1\wikicleaner.pl " + obj + output;
                perlStartInfo.UseShellExecute = false;
                perlStartInfo.RedirectStandardOutput = true;
                perlStartInfo.RedirectStandardError = true;
                perlStartInfo.CreateNoWindow = true;

                Process perl = new Process();
                perl.StartInfo = perlStartInfo;
                perl.Start();
                perl.WaitForExit();
                output = perl.StandardOutput.ReadToEnd();
                
                int i;
                Int32.TryParse(textBoxStart.Text, out i);

            });
            labelTime.Text = (DateTime.Now - time).ToString();
            Count();
            System.Console.WriteLine("Done.");
        }

        private void Count()
        {
            List<string> myEnumerable = new List<string>();
            int start = 0;
            Int32.TryParse(textBoxStart.Text, out start);
            int end = 0;
            Int32.TryParse(textBoxEnd.Text, out end);

            for (int i = start; i < end; ++i)
            {
                myEnumerable.AddRange(GetFiles(textBoxPath.Text + i + @"\texts\"));
            }
            labelProcessed.Text = myEnumerable.Count.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Count();
        }
        
        static int _value;

        private void button3_Click(object sender, EventArgs e)
        {
            List<string> myEnumerable = new List<string>();
            int start = 0;
            Int32.TryParse(textBoxStart.Text, out start);
            int end = 0;
            Int32.TryParse(textBoxEnd.Text, out end);
            string word = textBoxSearch.Text;

            Parallel.For(start, end, num =>
                {
                    string fullpath = textBoxPath.Text + num + @"\texts\";
                    //Thread newThread = new Thread(new ParameterizedThreadStart(Work.A));
                    //newThread.Start(new Wrapper(fullpath, word));
                    //newThread.Join();
                    var ret = GetFiles(fullpath);
                    int count = ret.Where(x => Path.GetFileName(x).StartsWith(word)).Count();

                    Interlocked.Add(ref Form1._value, count);

                    Console.WriteLine(Form1._value);
                    
                }
                
                );

            //Thread thread1 = new Thread(Form1.A);
            //Thread thread2 = new Thread(A);
            //thread1.Start(1);
            //thread2.Start(2);
            //thread1.Join();
            //thread2.Join();
	        Console.WriteLine(Form1._value);
            textBoxSearchReturn.Text = Form1._value.ToString();

        }
        public class Wrapper
        {
            public string mPath;
            public string mWord;
            public Wrapper(string path, string word)
            {
                mPath = path;
                mWord = word;
            }

        }
        public class Work
        {
            public static void A(object input)
            {
                var value= (Wrapper)input;

                var ret = GetFiles(value.mPath);
                int count = ret.Where(x=>x.StartsWith(value.mWord)).Count();

                Interlocked.Add(ref Form1._value, count);
            }

        }
        
        
    }
}
