#pragma once

#if defined(_WIN32)

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols

class CSampleLibraryApp : public CWinApp
{
public:
	CSampleLibraryApp();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};

#endif // _WIN32