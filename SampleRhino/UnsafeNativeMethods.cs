using System.Runtime.InteropServices;

namespace SampleRhino
{
  internal static class Import
  {
#if ON_RUNTIME_WIN
    public const string lib = "SampleLibrary.dll";
#else // ON_RUNTIME_MAC
    public const string lib = "SampleLibrary";
#endif // ON_RUNTIME_WIN
  }

  /// <summary>
  /// http://msdn.microsoft.com/en-us/library/aa288468(VS.71).aspx
  /// http://www.mono-project.com/docs/advanced/pinvoke/
  /// </summary>
  internal static class UnsafeNativeMethods
  {
    [DllImport(Import.lib, CallingConvention = CallingConvention.Cdecl)]
    internal static extern double Add(double a, double b);
  }
}
