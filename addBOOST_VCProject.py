#!/usr/bin/python
## ##################################################
##  Visual Studio Project File Updater 
##   Add $(BOOST_INCLUDE) to Includepath
##   Add $(BOOST_LIB)     to Librarypath
## ##################################################

# coding: UTF-8
import xml.etree.ElementTree as ET
import re
import sys

##  Check Command Line
##
if( len(sys.argv) < 2 ):
    print("Usage:: addBOOST_VCProject.py <Visual Studio Project File(**.vcxproj)>")
    quit()

## Get VC Project File Path
filename = sys.argv[1]
print("Visual Studio Project File ::",filename)

## Parse XML
tree = ET.parse(filename)
root = tree.getroot()

## root.tag から、xmlns値を取る
##   <Project DefaultTargets="Build" ToolsVersion="15.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003"> 
hdr = re.search(r"(\{.*\})", root.tag)
hdrstr= ".//"+hdr.group()
print("")

## Update "IncludePath"
##
##
found = root.findall(hdrstr+"IncludePath")
for d in found:
    print("  FOUNDED(tag)::",d.tag)
    print("  FOUNDED     ::",d.text)
    print("")
    d.text=d.text+";$(BOOST_INCLUDE)"

## Update "LibraryPath"
##
##
found = root.findall(hdrstr+"LibraryPath")
for d in found:
    print("  FOUNDED(tag)::",d.tag)
    print("  FOUNDED     ::",d.text)
    d.text=d.text+";$(BOOST_LIB)"
    print("")

## Output ...
##
tree_new = ET.ElementTree(root)

newfilename = filename+".mod"
tree_new.write(newfilename)
print("... Generated ",newfilename)
print("Done")
