from tkinter import *

def mostrar(album):
    resultado.config(text="\n".join(albuns[album]))

albuns = {
    "Please Please Me (1963)": [
        "I Saw Her Standing There", "Misery", "Anna (Go to Him)", "Chains",
        "Boys", "Ask Me Why", "Please Please Me", "Love Me Do",
        "P.S. I Love You", "Baby It's You", "Do You Want to Know a Secret",
        "A Taste of Honey", "There's a Place", "Twist and Shout"
    ],

    "With The Beatles (1963)": [
        "It Won't Be Long", "All I've Got to Do", "All My Loving",
        "Don't Bother Me", "Little Child", "Till There Was You",
        "Please Mr. Postman", "Roll Over Beethoven", "Hold Me Tight",
        "You Really Got a Hold on Me", "I Wanna Be Your Man", "Devil in Her Heart",
        "Not a Second Time", "Money"
    ],

    "A Hard Day's Night (1964)": [
        "A Hard Day's Night", "I Should Have Known Better", "If I Fell",
        "I'm Happy Just to Dance with You", "And I Love Her",
        "Tell Me Why", "Can't Buy Me Love", "Any Time at All",
        "I'll Cry Instead", "Things We Said Today", "When I Get Home",
        "You Can't Do That", "I'll Be Back"
    ],

    "Beatles for Sale (1964)": [
        "No Reply", "I'm a Loser", "Baby's in Black", "Rock and Roll Music",
        "I'll Follow the Sun", "Mr. Moonlight", "Kansas City/Hey-Hey-Hey-Hey!",
        "Eight Days a Week", "Words of Love", "Honey Don't",
        "Every Little Thing", "I Don't Want to Spoil the Party",
        "What You're Doing", "Everybody's Trying to Be My Baby"
    ],

    "Help! (1965)": [
        "Help!", "The Night Before", "You've Got to Hide Your Love Away",
        "I Need You", "Another Girl", "You're Going to Lose That Girl",
        "Ticket to Ride", "Act Naturally", "It's Only Love",
        "You Like Me Too Much", "Tell Me What You See", "I've Just Seen a Face",
        "Yesterday", "Dizzy Miss Lizzy"
    ],

    "Rubber Soul (1965)": [
        "Drive My Car", "Norwegian Wood", "You Won't See Me",
        "Nowhere Man", "Think for Yourself", "The Word",
        "Michelle", "What Goes On", "Girl", "I'm Looking Through You",
        "In My Life", "Wait", "If I Needed Someone", "Run for Your Life"
    ],

    "Revolver (1966)": [
        "Taxman", "Eleanor Rigby", "I'm Only Sleeping", "Love You To",
        "Here, There and Everywhere", "Yellow Submarine", "She Said She Said",
        "Good Day Sunshine", "And Your Bird Can Sing", "For No One",
        "Doctor Robert", "I Want to Tell You", "Got to Get You into My Life",
        "Tomorrow Never Knows"
    ],

    "Sgt. Pepper's Lonely Hearts Club Band (1967)": [
        "Sgt. Pepper's Lonely Hearts Club Band", "With a Little Help from My Friends",
        "Lucy in the Sky with Diamonds", "Getting Better", "Fixing a Hole",
        "She's Leaving Home", "Being for the Benefit of Mr. Kite!",
        "Within You Without You", "When I'm Sixty-Four", "Lovely Rita",
        "Good Morning Good Morning", "Sgt. Pepper (Reprise)", "A Day in the Life"
    ],

    "Magical Mystery Tour (1967)": [
        "Magical Mystery Tour", "The Fool on the Hill", "Flying",
        "Blue Jay Way", "Your Mother Should Know", "I Am the Walrus",
        "Hello, Goodbye", "Strawberry Fields Forever", "Penny Lane",
        "Baby You're a Rich Man", "All You Need Is Love"
    ],

    "The Beatles (White Album) (1968)": [
        "Back in the U.S.S.R.", "Dear Prudence", "Glass Onion",
        "Ob-La-Di, Ob-La-Da", "Wild Honey Pie", "The Continuing Story of Bungalow Bill",
        "While My Guitar Gently Weeps", "Happiness Is a Warm Gun",
        "Martha My Dear", "I'm So Tired", "Blackbird", "Piggies",
        "Rocky Raccoon", "Don't Pass Me By", "Why Don't We Do It in the Road?",
        "I Will", "Julia", "Birthday", "Yer Blues", "Mother Nature's Son",
        "Everybody's Got Something to Hide Except Me and My Monkey",
        "Sexy Sadie", "Helter Skelter", "Long, Long, Long",
        "Revolution 1", "Honey Pie", "Savoy Truffle", "Cry Baby Cry",
        "Revolution 9", "Good Night"
    ],

    "Abbey Road (1969)": [
        "Come Together", "Something", "Maxwell's Silver Hammer",
        "Oh! Darling", "Octopus's Garden", "I Want You (She's So Heavy)",
        "Here Comes the Sun", "Because", "You Never Give Me Your Money",
        "Sun King", "Mean Mr Mustard", "Polythene Pam",
        "She Came in Through the Bathroom Window", "Golden Slumbers",
        "Carry That Weight", "The End", "Her Majesty"
    ],

    "Let It Be (1970)": [
        "Two of Us", "Dig a Pony", "Across the Universe",
        "I Me Mine", "Dig It", "Let It Be", "Maggie Mae",
        "I've Got a Feeling", "One After 909", "The Long and Winding Road",
        "For You Blue", "Get Back"
    ]
}

janela = Tk()
janela.title("The Beatles - Discografia")
janela.geometry("700x500")

linha = 0
for album in albuns:
    Button(janela, text=album, command=lambda a=album: mostrar(a)).grid(column=0, row=linha, sticky="w")
    linha += 1

resultado = Label(janela, text="", justify=LEFT, anchor="w")
resultado.grid(column=1, row=0, rowspan=linha, sticky="nw")

janela.mainloop()
