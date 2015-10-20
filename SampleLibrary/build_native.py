#!/usr/bin/env python
import subprocess
import sys
import getopt
import os
import glob
import logging
import distutils.dir_util
import shutil
from sys import platform as _platform
from os import listdir
from os.path import isfile, isdir, join

verbose = False
overwrite = False
has_built_osx = False
windows = False
osx = False
linux = False

# OS X globals
is_ready_for_osx_build = False
did_build_for_osx_successfully = False


def check_osx():
    print ""
    print "OS X Pre-build check-----------------------------------------"
    check_xcodeproj()
    check_xcode_tools()
    check_has_built_for_osx()

    global is_ready_for_osx_build

    if has_xcodeProj and has_xcodeTools:
        is_ready_for_osx_build = True
        print "STATUS: Ready to build libSampleLibrary.dylib for OS X"
    else:
        is_ready_for_osx_build = False

    if not is_ready_for_osx_build:
        print "STATUS: NOT ready for OSX build.  Please address the following:"

        if not has_xcodeProj:
            print " ---ERROR: Script in wrong location or xcodeproj missing----------------"
            print "  This script must be placed in the SampleLibrary project folder. This folder"
            print "  should contain the SampleLibrary.xcodeproj file that is used in "
            print "  the command line build.  If this script is in the SampleLibrary folder,"
            print "  and you are getting this error message, then you are likely missing"
            print "  the XCode project. "

        if not has_xcodeTools:
            print " ---ERROR: XCode Command Line Tools Missing-----------------------------"
            print "  Building the native binary requires xcodebuild.  This utility"
            print "  is included with Apple's XCode Command Line Tools.  As of XCode 4.3,"
            print "  Command Line Tools are optional.  To install Command Line tools, open"
            print "  XCode > Preferences > Downloads Tab > Components > Command Line Tools."
            print "  Download and install.  Be sure to close/restart your terminal session"
            print "  before running this command again."
        return


def check_xcodeproj():
    sys.stdout.write(" Checking for xcodeproj                ")
    global has_xcodeProj
    if os.path.exists("SampleLibrary.xcodeproj"):
        sys.stdout.write("...Found\n")
        has_xcodeProj = True
    else:
        sys.stdout.write("...SampleLibrary.xcodeproj NOT FOUND\n")
        has_xcodeProj = False


def check_xcode_tools():
    sys.stdout.write(" Checking for XCode command line tools ")
    global has_xcodeTools

    if which("xcodebuild") is None:
        sys.stdout.write("...xcodebuild NOT FOUND\n")
        has_xcodeTools = False
    else:
        sys.stdout.write("...Found\n")
        has_xcodeTools = True


def check_has_built_for_osx():
    sys.stdout.write(" Checking for existing builds          ")
    global has_built_osx
    if os.path.exists("build/Debug/libSampleLibrary.dylib"):
        if os.path.exists("build/Release/libSampleLibrary.dylib"):
            sys.stdout.write("...Found\n")
            has_built_osx = True
    else:
        sys.stdout.write("...Not Found\n")
        has_built_osx = False


def create_build_folders_for_osx():
    if not os.path.exists("build"):
        os.mkdir("build")

    #check to make sure the folder was created successfully
    if not os.path.exists("build"):
        print "ERROR: Unable to create build folders.  Please make sure you have admin privileges and try again."
        sys.exit()

    if not os.path.exists("build/Debug"):
        os.mkdir("build/Debug")

    #check to make sure the folder was created successfully
    if not os.path.exists("build/Debug"):
        print "ERROR: Unable to create build folders.  Please make sure you have admin privileges and try again."
        sys.exit()


def build_for_osx():
    print ""
    print "OSX Build-------------------------------------------------------"
    print "Making dynamic libSampleLibrary.dylib for OSX..."

    sys.stdout.write(" Compiling Debug version               ")
    if verbose:
        subprocess.call(
            ["xcodeBuild", "-project", "SampleLibrary.xcodeproj", "-target", "SampleLibrary", "-configuration", "Debug",
             "clean", "build"])
    else:
        devnull = open(os.devnull, 'w')
        subprocess.call(
            ["xcodeBuild", "-project", "SampleLibrary.xcodeproj", "-target", "SampleLibrary", "-configuration", "Debug",
             "clean", "build"], stdout=devnull, stderr=devnull)

    if os.path.exists("build/Debug/libSampleLibrary.dylib"):
        sys.stdout.write("...Done\n")
    else:
        sys.stdout.write("...FAILED\n")
        sys.exit()

    sys.stdout.write(" Compiling Release version             ")
    if verbose:
        subprocess.call(
            ["xcodeBuild", "-project", "SampleLibrary.xcodeproj", "-target", "SampleLibrary", "-configuration",
             "Release", "clean", "build"])
    else:
        devnull = open(os.devnull, 'w')
        subprocess.call(
            ["xcodeBuild", "-project", "SampleLibrary.xcodeproj", "-target", "SampleLibrary", "-configuration",
             "Release", "clean", "build"], stdout=devnull, stderr=devnull)

    if os.path.exists("build/Release/libSampleLibrary.dylib"):
        sys.stdout.write("...Done\n")
    else:
        sys.stdout.write("...FAILED\n")
        sys.exit()

    sys.stdout.write("...Done\n")

    global did_build_for_osx_successfully
    did_build_for_osx_successfully = True


def write_osx_finished_message():
    print "STATUS: OS X Build Complete.  Libraries are in build/Debug"


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def usage():
    print ""
    print("build_native.py - script for building native openNURBS library")
    print "usage: ./build_native.py -p [argument] --check --help --verbose"
    print ""
    print " option:            arguments:    description:"
    print " ---------------    ----------    ---------------------------------------"
    print " -p   --platform    all           build libSampleLibrary for all platforms"
    if osx:
        print "                    osx           build libopennurbs.dylib for OS X"
    print " -c   --check       all           pre-requisites check for all platforms"
    if osx:
        print "                    osx           pre-requisites check for OS X"
    print " -h   --help                      display this screen"
    print " -v   --verbose                   show verbose build messages"
    print " -o   --overwrite                 overwrite existing builds"
    print ""
    print "Examples:"
    if osx:
        print "./build_native.py -p all         (build for all platforms)"
        print "./build_native.py -p osx -v      (build OS X with verbose messages)"
        print "./build_native.py -c osx         (check pre-requisites for OS X)"
        print "./build_native.py -p osx -o      (build for OS X overwriting existing)"
    print ""
    print "NOTE: Builds are stored in the build/Debug/ folder."
    print ""
    return


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvoc:p:", ["help", "verbose", "overwrite", "check=", "platform="])
    except getopt.GetoptError as err:
        # print help information and exit:
        usage()
        sys.exit(2)
    platform = None
    check = None

    #check os
    global linux
    global osx
    global windows

    if _platform == "linux" or _platform == "linux2":
        linux = True
    elif _platform == "darwin":
        osx = True
    elif _platform == "win32" or _platform == "cygwin":
        windows = True

    for o, a in opts:
        if o == "-v" or o == "--verbose":
            global verbose
            verbose = True
        elif o == "-o" or o == "--overwrite":
            global overwrite
            overwrite = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-p", "--platform"):
            platform = a
        elif o in ("-c", "--check"):
            check = a
        else:
            assert False, "unhandled option"

    #user has not entered any arguments...
    if platform is None and check is None:
        usage()
        sys.exit()

    #check prerequisites
    if check == "all":
        if osx:
            check_osx()
    elif check == "osx":
        if osx:
            check_osx()
        else:
            print ("ERROR: Targeting OS X requires running this script on Mac OS X 10.9.2 +")

    #platform compiles
    if platform == "all":
        if osx:
            check_osx()

        if osx:

            if overwrite or not has_built_osx:
                create_build_folders_for_osx()
            elif has_built_osx and not overwrite:
                print ("STATUS: Existing OS X build found.  NOT BUILDING.  (Use -o argument to overwrite existing.)")

        if osx:
            if overwrite and is_ready_for_osx_build:
                build_for_osx()
            elif not has_built_osx and is_ready_for_osx_build:
                build_for_osx()

        if osx:
            if did_build_for_osx_successfully:
                write_osx_finished_message()

    elif platform == "osx":
        if osx:
            check_osx()
        else:
            print ("ERROR: Targeting iOS or OS X requires running this script on Mac OS X 10.9.2 +")
            sys.exit()

        if has_built_osx and not overwrite:
            print ("STATUS: Existing build found.  NOT BUILDING.  Use -o argument to overwrite the existing builds")
            sys.exit()

        if overwrite or not has_built_osx:
            create_build_folders_for_osx()

            if is_ready_for_osx_build:
                build_for_osx()
            else:
                sys.exit()

            if did_build_for_osx_successfully:
                write_osx_finished_message()


if __name__ == "__main__":
    main()