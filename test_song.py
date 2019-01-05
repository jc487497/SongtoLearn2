""" Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required == ""

# test initial-value song
song2 = Song("I Want to Hold Your Hand","The Beatles","The Beatles","y")
print(song2)
# TODO: write tests to show this initialisation works

# test mark_learned()
song2.mark_learned()
print(song2)
# TODO: write tests to show the mark_learned() method works
