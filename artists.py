#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')
THE_GREAT_QUESTION.split('. ')
STATEMENTS = THE_GREAT_QUESTION.split('. ')
ARTISTS = STATEMENTS[0:4]
len(ARTISTS)
NUM_ARTISTS = len(ARTISTS)
len(THE_GREAT_QUESTION)
CHARACTERS = len(THE_GREAT_QUESTION)
if ( 'Creators' in THE_GREAT_QUESTION):
	print "Creators is in the variable"
else:
	print "Creators not in the variable"

if ( 'SPLINTER' in ARTISTS):
	print "SPLINTER is in the variable"
else:
	print "SPLINTER is not in the variable"



