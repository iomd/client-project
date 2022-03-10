#!/usr/bin/python3
# -*- coding: utf8 -*-
# :Author: Chris Shanklin <ice.fetty@gmail.com>
# :Copyright: © 2022 Icepit Productions.
# :License:
#
# :Revision: v0.01
# :Date: $Date: 2022-03-04 00:19:43 -0500 $

"""comments
filename.type
======

it reads the variables, then prints them out.
"""

# album_metadata
album = "album"
year = 2022
tracks = 8
artists = "artist1, artist2"
producers = "producer1, producer2"

album_metadata = (album , year , tracks , artists , producers)

# song_metadata
title = "untitled"
version = 0.01
artist = "artist"
producer = "producer"
year = 2022
bpm = 140
key = "11A"

song_metadata = (title , version , artist , producer , year , bpm , key)

print(album_metadata , song_metadata)