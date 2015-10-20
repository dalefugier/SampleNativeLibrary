# SampleNativeLibrary
RhinoCommon cross-platform native library sample

##Overview
This sample demonstrates how to create a RhinoCommon plug-in that utilizes functions from a native C++ library. 

##Building Sample

###Windows
To build the sample on Windows, you are going to need:

* Rhino 6 for Windows (WIP, http://discourse.mcneel.com/)
* Microsoft Visual C# 2013
* Microsoft Visual C++ 2013

To build both the Rhino plug-in and the native library, load the **SampleNativeLibrary.sln** solution in Visual Studio 2013. Then, click **Build -> Build Solution**. Note, you might want to unload the **SampleRhino.Mac** project before building. You can do this by right-clicking on the project and clicking **Unload project**.

###Mac
To build the sample on OS X, you are going to need:

* Rhino 5 for Mac (5.1)
* Xamarin Studio 5.9
* Apple Xcode 6.4

Building the Rhino plug-in the native library are separate processes.

To build the Rhino plug-in, load the **SampleNativeLibrary.sln** solution in Xamarin Studio. Then, click **Build -> Build All**" Note, you may want to unload both the **SampleLibrary** and **SampleRhino.Win** projects before building. You can do this by right-clicking on each project and clicking **Unload**.

To build the native library, load the **SampleLibrary.xcodeproj** into Xcode. Then click **Product -> Build**. Note, you will need to copy the output library, **libSampleLibrary.dylib**, to the Rhino plug-in output folder. Also, copy **SampleRhino.dll.config**, found in the **SampleLibrary** project folder, to the Rhino plug-in folder. For more information on the config file, see the Mono Project notes found in the Useful Links section below.

###Useful Links
* https://msdn.microsoft.com/en-us/library/aa288468(VS.71).aspx
* http://www.mono-project.com/docs/advanced/pinvoke/

###Legal Stuff
Copyright © 2015 Robert McNeel & Associates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT EXPRESS OR IMPLIED WARRANTY. ALL IMPLIED WARRANTIES OF FITNESS FOR ANY PARTICULAR PURPOSE AND OF MERCHANTABILITY ARE HEREBY DISCLAIMED.

Rhinoceros is a registered trademark of Robert McNeel & Associates.
