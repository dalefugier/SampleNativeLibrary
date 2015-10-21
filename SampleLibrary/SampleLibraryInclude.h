#pragma once

// Windows build
#if defined (_WIN32)
#if defined (SAMPLELIBRARY_DLL_EXPORTS)
#define SAMPLELIBRARY_CPP_CLASS __declspec(dllexport)
#define SAMPLELIBRARY_CPP_FUNCTION __declspec(dllexport)
#define SAMPLELIBRARY_C_FUNCTION extern "C" __declspec(dllexport)
#else
#define SAMPLELIBRARY_CPP_CLASS __declspec(dllimport)
#define SAMPLELIBRARY_CPP_FUNCTION __declspec(dllimport)
#define SAMPLELIBRARY_C_FUNCTION extern "C" __declspec(dllimport)
#endif // SAMPLELIBRARY_DLL_EXPORTS
#endif // _WIN32

// Apple build
#if defined(__APPLE__)
#define SAMPLELIBRARY_CPP_CLASS __attribute__ ((visibility ("default")))
#define SAMPLELIBRARY_CPP_FUNCTION __attribute__ ((visibility ("default")))
#define SAMPLELIBRARY_C_FUNCTION extern "C" __attribute__ ((visibility ("default")))
#endif // __APPLE__


// Sample C Exports

SAMPLELIBRARY_C_FUNCTION
double Add(int a, double b);
