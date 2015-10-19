using System.Reflection;
using System.Runtime.InteropServices;
using Rhino.PlugIns;

// Plug-in Description Attributes - all of these are optional
// These will show in Rhino's option dialog, in the tab Plug-ins
[assembly: PlugInDescription(DescriptionType.Address, "3670 Woodland Park Ave N\n\nSeattle, WA 98103")]
[assembly: PlugInDescription(DescriptionType.Country, "United States")]
[assembly: PlugInDescription(DescriptionType.Email, "devsupport@mcneel.com")]
[assembly: PlugInDescription(DescriptionType.Phone, "(206) 545-6877")]
[assembly: PlugInDescription(DescriptionType.Fax, "(206) 545-7321")]
[assembly: PlugInDescription(DescriptionType.Organization, "Robert McNeel & Associates")]
[assembly: PlugInDescription(DescriptionType.UpdateUrl, "http://www.rhino3d.com")]
[assembly: PlugInDescription(DescriptionType.WebSite, "http://www.rhino3d.com")]

// Information about this assembly is defined by the following attributes.
// Change them to the values specific to your project.

[assembly: AssemblyTitle("SampleRhino")]
[assembly: AssemblyDescription("RhinoCommon cross-platform native library sample")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("Robert McNeel & Associates")]
[assembly: AssemblyProduct("SampleRhino")]
[assembly: AssemblyCopyright("Copyright © 2015, Robert McNeel & Associates")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]

// Version information for an assembly consists of the following four values:
//
//      Major Version
//      Minor Version 
//      Build Number
//      Revision
//
// You can specify all the values or you can default the Build and Revision Numbers 
// by using the '*' as shown below:
// [assembly: AssemblyVersion("1.0.*")]
[assembly: AssemblyVersion("1.0.0.0")]
[assembly: AssemblyFileVersion("1.0.0.0")]

// Rhino requires a Guid assigned to the assembly. Xamarin Studio can't insert a Guid in file templates automatically.
[assembly: Guid("0b79bf6d-9d2c-4c19-84ff-d015c84b0a6b")]
