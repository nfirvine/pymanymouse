#!/bin/sh
MANYMOUSEREV=74
svn export -r $MANYMOUSEREV --force svn://svn.icculus.org/manymouse/trunk/ .
make 
make -f Makefile.python python

