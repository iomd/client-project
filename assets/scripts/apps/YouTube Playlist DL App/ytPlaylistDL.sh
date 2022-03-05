#!/bin/bash

echo "playlistURL" ;
read playlistURL ;

python3 ytPlaylistDL.py $playlistURL ~/Downloads ;