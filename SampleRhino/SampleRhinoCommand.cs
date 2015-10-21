using System;
using Rhino;
using Rhino.Commands;

namespace SampleRhino
{
  public class SampleRhinoCommand : Command
  {
    private int First { get; set; }
    private double Second { get; set; }

    /// <returns>
    /// The command name as it appears on the Rhino command line.
    /// </returns>
    public override string EnglishName
    {
      get { return "SampleRhinoCommand"; }
    }

    /// <summary>
    /// Called by Rhino to "run" your command.
    /// </summary>
    protected override Result RunCommand(Rhino.RhinoDoc doc, RunMode mode)
    {
      var rc = Result.Success;

      var first = First;
      rc = Rhino.Input.RhinoGet.GetInteger("First number to add", false, ref first);
      if (rc != Result.Success)
        return rc;

      var second = Second;
      rc = Rhino.Input.RhinoGet.GetNumber("Second number to add", false, ref second);
      if (rc != Result.Success)
        return rc;

      var result = RhinoMath.UnsetValue;
      try
      {
        result = UnsafeNativeMethods.Add(first, second);
      }
      catch (Exception ex)
      {
        RhinoApp.WriteLine(ex.Message);        
        return Result.Failure;
      }

      var str = string.Format("{0} + {1} = {2}", first, second, result);
      if (mode == RunMode.Interactive)
        Rhino.UI.Dialogs.ShowMessage(str, EnglishName);
      else
        RhinoApp.WriteLine(str);

      First = first;
      Second = second;

      return Result.Success;
    }
  }
}
