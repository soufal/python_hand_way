#A first class example

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I dont's want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["Tey rally around tha family",
                        "With pockets full of shells"])

my_song = ["Lalalalalala",
            "Hahahahahaha",
            "Heiheiheihei"]
my_bad_song = Song(my_song)
my_bad_song.sing_me_a_song()
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()