using System.Runtime.InteropServices;

namespace SampleRhino
{
  internal static class Import
  {
    public const string lib = "SampleLibrary.dll";
  }

  /// <summary>
  /// http://msdn.microsoft.com/en-us/library/aa288468(VS.71).aspx
  /// http://www.mono-project.com/docs/advanced/pinvoke/
  /// </summary>
  internal static class UnsafeNativeMethods
  {
    [DllImport(Import.lib, CallingConvention = CallingConvention.Cdecl)]
    internal static extern double Add(int a, double b);
  }
}
