using System;
using System.Windows.Forms;

namespace PSSDKMethodScriptExamples
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            var sandBox = new FrmSandBox();
            if (args.Length > 0)
            {
                sandBox.LoadScript(args[args.Length - 1]);
            }

            Application.Run(new FrmSandBox());
        }
    }
}