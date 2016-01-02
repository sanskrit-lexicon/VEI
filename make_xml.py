# coding=utf-8
""" make_xml.py for vei. 2014-06-22
 Reads/Writes utf-8
"""
import xml.etree.ElementTree as ET
import sys, re,codecs
import transcoder
transcoder.transcoder_set_dir("");
xmlroot = "vei"
import headword
reHeadword0 = headword.reHeadword
reHeadword = re.compile(reHeadword0)

def adjust_tag(x,j):
 # none of these: see check_takgs
 if re.search(r'<C1>',x):
  x = re.sub(r'<C1>','<br/><C1/>',x)
 if re.search(r'<C2>',x):
  x = re.sub(r'<C2>','<C2/>',x)
 if re.search(r'<C3>',x):
  x = re.sub(r'<C3>','<C3/>',x)
 
 if re.search(r'^<>',x):
  x = re.sub(r'<>','<br/>',x)
 elif re.search(r'^<P>',x):
  x = re.sub(r'<P>','<br/>',x)
 elif re.search(r'^<H>',x):
  x = re.sub(r'<H>','<H/>',x)
 return x
def add_tag(x,j):
 # compare to check_curly
 # add tags for {@@} = <b></b> 
 # {%} = <i></i>
 # {kh} => <kh/> (underlined)
 # {greek} => <greek/>
 x = re.sub(r'{@','<b>',x)
 x = re.sub(r'@}','</b>',x)
 x = re.sub(r'{%','<i>',x) 
 x = re.sub(r'%}','</i>',x)
 return x

def unused_adjust_hk(m):
 x = m.group(1)
 # re.split(r'(<[^>]+>)',s)(&.*;)
 outarr = []
 parts = re.split(r'(<[^>]+>)',x) # xml tags
 for part in parts: 
  if (part == ''):
   pass
  elif (part[0] == '<'):
   outarr.append(part)
  else:
   parts1 = re.split(r'(&.*;)',part) # xml entity
   for part1 in parts1:
    if (part1 == ''):
     pass
    elif (part1[0] == '&'):
     outarr.append(part1)
    else: # assume text in hk. Convert to slp1
     z = re.sub(r'\|','.',part1) # text has non-standard | for danda
     if z == 'oMM':
      y = 'o~' # OM
     else:
      y = transcoder.transcoder_processString(z,'hk','slp1')
     outarr.append(y)
 ans = ''.join(outarr)
 return "<s>%s</s>" % ans

def dbgout(fout,s):
 if fout:
  fout.write("%s\n" % s)

def construct_data(datalines,key1,lnum,page,col,n1,fout=None):
 # construct data analogous to the way it is in mw
 # replace extended ascii in all lines
 datalines1 = []
 # parse head info from first line
 line = datalines[0]
 line = line.strip()
 line0 = line
 dbgout(fout,"chk1: %s\n" % line)
 m = re.search(r'^(<P>[1-8. ]*{@.*?@})(.*)$' ,line)  # may need vertical-bar
 if not m:
  print "CONSTRUCT_DATA ERROR at n1=",n1
  exit(1)
 head = m.group(1)
 rest = m.group(2)
 m = re.search(reHeadword,head)
 if not m:
  out = "ERROR: headword expected. line = %s\n" % line
  print out.encode('utf-8')
  out = "HEAD=%s" % head
  print out.encode('utf-8')
  exit(1)
 hkey2a = m.group(1) 
 #hkey2a = re.sub(' ([A-Z])',lambda m:' '+m.group(1).lower(),hkey2a) # trial by Dhaval 2 Jan 2016
 hom = ''
 #key1a  = transcoder.transcoder_processString(hkey1a,'hk','slp1')
 key2a = transcoder.transcoder_processString(hkey2a,'hk','slp1')
 head = re.sub('<P>','',head)
 datalines[0] = "%s %s" %(head,rest)
 for line in datalines:
  line = line.strip()
  if line == '':
   continue  # skip blank line
  datalines1.append(line)
 # 1. h (head)
 key2 = key2a  #adjust_key2(key2a)
 h = "<key1>%s</key1><key2>%s</key2>" % (key1,key2)
 dbgout(fout,"chk2: %s" % h)  
 #2. construct tail
 #ipage = int(page)
 ipage = page
 tail = "<L>%s</L><pc>%s</pc>" % (lnum,ipage)
 dbgout(fout,"chk3: %s\n" % tail)  
 #3. construct body
 bodylines = []
 j = n1
 for x in datalines1:
  x = x.strip()
  #if re.search(r'<H>',x):
  # continue
  x = adjust_tag(x,j) # j not used here
  x = add_tag(x,j)
  # convert <s>X</s> to slp1  AUG 2013. Do this after lines are joined!
  #x = re.sub(r'<s>(.*?)</s>',adjust_hk,x)
  j = j + 1
  dbgout(fout,"chk3: %s" % x)
  bodylines.append(x)
 body0 = ' '.join(bodylines)
 dbgout(fout,"chk4: %s" % body0)
 # Mar 17, 2014. Leave Sanskrit in its AS form.
 body = body0
 dbgout(fout,"chk5: %s" % body0)
 #4. construct result
 data = "<H1><h>%s</h><body>%s</body><tail>%s</tail></H1>" % (h,body,tail)
 dbgout(fout,"chk6: %s" % body0)
 return data

def make_xmlfun(filein,filein1,fileout):
 # slurp txt file into list of lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
    inlines = f.readlines()
 # open output xml file, and write header
 fout = codecs.open(fileout,'w','utf-8')
  
 # write header lines
# write the preface pages
 text = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE %s SYSTEM "%s.dtd">
<!-- Copyright Universitat Koln 2013 -->
<%s>
""" % (xmlroot,xmlroot,xmlroot)
 lines = text.splitlines()
 nout = 0  # count of lines written
 for line in lines:
  line = line.strip()
  if (line != ''):
   out = "%s\n" %line
   fout.write(out)
   nout = nout + 1
 # read headword lines, and generate output
 f = open(filein1,'r')
 n = 0 # count of lines read
 lnum = 0 # generate record number for xml records constructed
 for line in f:
  n = n+1
  if n > 1000000:
   print "debug stopping"
   break
  line = line.strip() # remove starting or ending whitespace
  try:
   (pagecol,hwslp,linenum12) = re.split('[:]',line)
  except:
   print "Problem at line %s = %s" %(n,line)
   exit(1)
  (linenum1,linenum2) = re.split(',',linenum12)
  (page,col) = re.split('[,-]',pagecol)
  #col = 1 # there is no column 
  n1 = int(linenum1) - 1 # make 0-based
  n2 = int(linenum2) - 1
  datalines = inlines[n1:n2+1]
  # construct output
  lnum = lnum + 1
  key1 = hwslp
  # Mar 20, 2014. Display pagecol.
  #data = construct_data(datalines,key1,lnum,page,col,n1,fout=None)
  data = construct_data(datalines,key1,lnum,pagecol,col,n1,fout=None)
  out = "%s\n" % data
  try:
   fout.write( out)
  except:
   out1 = "ERROR WRITING line# %s" % n1
   print out1
   exit(1)
  # check that out is well-formed xml
  try:
   root = ET.fromstring(out.encode('utf-8'))
  except:
   out = "xml error: n=%s,line=%s" %(n,out)
   print out.encode('utf-8')
 # write closing line
 out = "</%s>\n" % xmlroot
 fout.write(out)
 fout.close()

if __name__=="__main__":
 filein = sys.argv[1] # vei.txt
 filein1 = sys.argv[2] #veihw2.txt
 fileout = sys.argv[3] # vei.xml
 make_xmlfun(filein,filein1,fileout)
