#!/bin/ruby
# coding: utf-8
# ================================================================================
# == C/C++ のヘッダー部 のテンプレートを生成
# == 
# == 
# ================================================================================

if(  ARGV.size == 0 )then
  print " Generate C/C++ Header\n"
  print " (Usage) > mkhder.rb  <C/C++ Hedder File Name>\n\n"
  exit
end

## File Name
c_header = ARGV[0];

## Compile Guard
c_header_str  = "__"+c_header.gsub(/\./,"_")
c_header_str.upcase!

File.open(c_header,"w") do |f|
  f.print "#ifndef "+c_header_str+"\n"
  f.print "#define "+c_header_str+"\n"
  f.print "// ================================================================================\n" 
  f.print "// = "+c_header+"\n"
  f.print "// = \n"
  f.print "// = [Description]\n"
  f.print "// = \n"
  f.print "// ================================================================================\n" 
  f.print "namespace NXXX{\n"
  f.print "\n"
  f.print "// --------------------------------------------------\n"
  f.print "// -- Variable\n"
  f.print "// --------------------------------------------------\n"
  f.print "\n"
  f.print "// --------------------------------------------------\n"
  f.print "// -- Class\n"
  f.print "// --------------------------------------------------\n"
  f.print "class CXXX {\n"
  f.print "\n"
  f.print "};\n"
  f.print "\n"
  f.print "\n"
  f.print "}; // namespace NXXX{\n"
  f.print "#endif // #ifndef "+c_header_str+"\n"
end


print " ... done(c_header)\n\n"
