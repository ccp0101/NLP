#!/usr/bin/env python
import os
import sys
import codecs

def gbk2utf8(file_in, file_out):
    fi = codecs.open(file_in, "r", encoding="gb18030")
    try:
        content = fi.read()
    except:
        print "Cannot convert %s" % file_in
        return
    finally:
        fi.close()
    fo = codecs.open(file_out, "w", encoding="utf8")
    fo.write(content)
    fo.close()

def drop_utf8s(dir):
    for path, subdirs, files in os.walk(dir):
        for name in files:
            filepath = os.path.join(path, name)
            if filepath.endswith(".utf8.txt"):
                print filepath
                os.remove(filepath)

def drop_originals(dir):
     for path, subdirs, files in os.walk(dir):
        for name in files:
            filepath = os.path.join(path, name)
            if filepath.endswith(".txt") and not filepath.endswith(".utf8.txt"):
                # print filepath
                os.remove(filepath)

# def gbk2utf8(file_in, file_out):
#     os.system("iconv -f GB18030 -t utf8 %s > %s" % (file_in, file_out))

def walk_directory(dir):
    for path, subdirs, files in os.walk(dir):
        for name in files:
            filepath = os.path.join(path, name)
            prefix, ext = os.path.splitext(name)
            if ext.lower() == ".txt" and not name.endswith(".utf8.txt"):
                print os.path.join(path, prefix + ".utf8" + ext.lower())
                gbk2utf8(filepath, os.path.join(path, prefix + ".utf8" + ext.lower()))

drop_originals(sys.argv[1])