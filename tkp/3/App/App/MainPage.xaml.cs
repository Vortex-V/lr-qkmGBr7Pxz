using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using Xamarin.Forms.PlatformConfiguration.AndroidSpecific;

namespace App
{
    public partial class MainPage : ContentPage
    {
        public static string patternHelloText = "Здравствуйте, товарищ {data}!";
        public static string patternRepeatCountText = "Тунеядцев найдено: {count}.";
        public static string patternCountText = "Тунеядец наказан {count} раз.";

        private int count = 0;
        private int repeatCount = 0;

        public MainPage()
        {
            InitializeComponent();
        }

        private void FioChanged(object sender, EventArgs e)
        {
            labelHello.Text = patternHelloText.Replace("{data}", fioEntry.Text);
        }

        private void ButtonRepeat(object sender, EventArgs e)
        {
            repeatCount += 1;
            count = 0;
            labelRepeatCount.Text = replace(patternRepeatCountText, repeatCount);
            labelClickcount.Text = replace(patternCountText, count);
        }

        private void ButtonClick(object sender, EventArgs e)
        {
            count += 1;
            labelClickcount.Text = replace(patternCountText, count);
        }

        private string replace(string pattern, int count)
        {
            return pattern.Replace("{count}", count.ToString());
        }
    }
}
