using System.Runtime.InteropServices;

namespace SampleRhino
{
  internal static class UnsafeNativeMethods
  {
#if ON_RUNTIME_WIN
    [DllImport("SampleLibrary.dll", CallingConvention = CallingConvention.Cdecl)]
#else // ON_RUNTIME_APPLE
    [DllImport("SampleLibrary", CallingConvention = CallingConvention.Cdecl)]
#endif // ON_RUNTIME_WIN
    internal static extern double Add(double a, double b);
  }
}
