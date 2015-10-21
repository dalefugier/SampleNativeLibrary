#include "stdafx.h"
#include "SampleLibrary.h"

#if defined(_WIN32)

//
//TODO: If this DLL is dynamically linked against the MFC DLLs,
//		any functions exported from this DLL which call into
//		MFC must have the AFX_MANAGE_STATE macro added at the
//		very beginning of the function.
//
//		For example:
//
//		extern "C" BOOL PASCAL EXPORT ExportedFunction()
//		{
//			AFX_MANAGE_STATE(AfxGetStaticModuleState());
//			// normal function body here
//		}
//
//		It is very important that this macro appear in each
//		function, prior to any calls into MFC.  This means that
//		it must appear as the first statement within the 
//		function, even before any object variable declarations
//		as their constructors may generate calls into the MFC
//		DLL.
//
//		Please see MFC Technical Notes 33 and 58 for additional
//		details.
//

// CSampleLibraryApp

BEGIN_MESSAGE_MAP(CSampleLibraryApp, CWinApp)
END_MESSAGE_MAP()

CSampleLibraryApp::CSampleLibraryApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

// The one and only CSampleLibraryApp object
CSampleLibraryApp theApp;

BOOL CSampleLibraryApp::InitInstance()
{
	CWinApp::InitInstance();

	return TRUE;
}

#endif // _WIN32


// Sample C Exports

SAMPLELIBRARY_C_FUNCTION
double Add(int a, double b)
{
  return a + b;
}
