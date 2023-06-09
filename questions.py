from string import ascii_lowercase
import random

NUM_QUESTIONS_PER_QUIZ = 7
QUESTIONS_SPORTS = {
    "Which NBA legend is undefeated in the finals winning a total of 6 rings?":
    ["Michael Jordan", "Lebron James", "Magic Johnson", "Larry Bird"],

    "In addition to the New England Patriots, what NFL team is tied for the most Super Bowl wins?":
    ["Pittsburgh Steelers", "Washington Redskins", "Golden State Warriors", "Dallas Cowboys"],

    "Which former NFL player was known as 'the bus'?":
    ["Jerome Bettis", "LaDanian Tomlinson", "Barry Sanders", "Buster Harris"],

    "Considered by most to be the greatest UFC fighter of all time, my nickname is 'bones', i am..":
    ["Jon Jones", "Roy Jones Jr", "Tito Ortiz", "Brock Lesnar"],

    "Which long-time NFL team is uses the slogan/chant: 'Who Dey'?":
    ["Cincinnati Bengals", "New Orleans Saints", "Charolotte Hornets", "Green Bay Packers"],

    "Fans from this historical NFL team are often known as 'cheeseheads'...":
    ["Green Bay Packers", "New York Giants", "Pittsburgh Steelers", "Wisconsin Badgers"],

    "Which boxing legend once said, 'float like a butterfly, sting like a bee'?":
    ["Muhammad Ali", "Tyson Fury", "Mike Tyson", "Joe Frazier"],

    "Who is the most decorated swimmer of all time?":
    ["Michael Phelps", "Ryan Lochte", "Usain Bolt", "Aquaman"],

    "Who holds the record for the fastest 100m ever ran?":
    ["Usain Bolt", "Michael Johnson", "Chris Johnson", "Jessie Owens"],

    "In what year did Tom Brady win his first super bowl?":
    ["2002", "2003", "1999", "2008"],

    "Who holds the all-time home run record?":
    ["Barry Bonds", "Hank Aaron", "Babe Ruth", "Willie Mays"],

    "The NHL was formed in...":
    ["1917", "1921", "1968", "1940"],

    "Which NFL legend holds the all-time rushing TD's record?":
    ["Emmit Smith", "Adrian Peterson","Ladanian Tomlinson", "Barry Sanders"],

    "Who holds the all-time best batting average?":
    ["Ty Cobb", "Derrick Jeter", "Reggie Miller", "Babe Ruth"],

    "Behind Bill Belichick, what NFL head coach has won the most Super Bowls?":
    ["Chuck Noll", "Andy Reid", "Vince Lombardi", "John Madden"],

    "What NBA great has won the most all-time championships?":
    ["Bill Russell", "Michael Jordan", "Lebron James", "Kobe Bryant"]
}




QUESTIONS_HISTORY = {
    "This French general has won 38 out of all 43 listed battles he leads his troops into battle...": [
        "Napoleon Bonaparte", "Toussaint Louverture", "Oscar-Claude Monet", "Joan of Arc"
    ],
    "What general was in command of the United States Army during World War I?": [
        "George S. Patton", "Geranimo", "George Washington", "William T. Sherman"
    ],
    "This volcano eruption was one of the deadliest and most destructive volcanic events in recorded history, what was the volcano called?": [
        "Krakatoa", "Pompei", "Rincon de la Vieja", "Great Sitkin"
    ],
    "Who holds the record in the mile run?": [
        "Hicham El Guerrouj",
        "Haile Gebrselassie",
        "Jim Ryan",
        "Bill Bowerman",
    ],
    "Who was the ruler of the Mongolian Empirer?": [
        "Genghis Khan", "Kublai Khan", "Amir Khan", "Shah Rukh Khan"
    ],
    "This general fought Alexander the great and defeated him with elephants during the punic wars? Who is this general?": [
        "Hanibal Barca", "Scipio Africanus", "Hanno I the Great", "Mago III"
    ],
    "Who was the Persian king from (486–465 bce), the son and successor of Darius I?": [
        "Xerxes I",
        "Cyrus the Great",
        "Nebuchadnezzar",
        "Artaxerxes I",
    ],
    "Who was the 35th presidant of the United States?'": [
        "John F Kennedy", "Richard Nixon", "Abraham Lincoln", "Harry S. Truman"
    ],
    "What is ther biggest island in the world?": [
        "New Guinea", "Japan", "Great Britain", "Tasmania"
    ],
    "Who is the first nordic person to be documented sailing and landing in the Americas?": [
        "Leif Erikson", "while", "each", "loop"
    ],
    "What family ruled Japan from 1603 until the Meiji Restoration in 1868": [
        "Tokugawa", "Fujiwara", "Musashi", "Yamamoto"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "1826", "while", "each", "loop"
    ],
    "Where was the first city to have elecric street lights?": [
        "1880 Wabash, Indiana",
        "1864 Topeka, Kansas",
        "1803 New York, New York",
        "1810 Detroit, Michigan",
    ],

    "What century was the rifle created?": [
        "15th Century",
        "14th Century",
        "16th Century",
        "13th Century",
    ]
}

QUESTIONS_MOVIES = {


"in citizen kane, what is rosebud?":
['a sled', 'a horse', 'his nickname for a lost love', 'a fast-casual dining experience'],
"who framed roger rabbit?": 
['judge doom', 'mickey mouse', 'that one cartoon baddie with with red hair', 'bob hoskins'],
"the movie 'the king and i' took place in which fictional country?":
 ['3', 'xin zhao', 'tai shein', 'flushing'],
"call yourself a scorcese fan? name 5 of his movies lol":
 ["'taxi driver, 'the king of comedy', 'cape fear', 'casino', 'bringing out the dead'", 
   "'goodfellas', 'the color of money', 'apocalypse now', 'lost in translation', 'gangs of new york'",
   "'mean streets', 'new york, new york', 'the irishman', 'john wick', 'hugo'",
   "'the wolf of wall street, 'the departed', 'the age of innocence', 'limitless', 'shutter island'"],
  "in jaws, new england town hires an eccentric fisherman Quint to hunt a killer shark. what's the name of Quints leaky ole' fishing boat ":
  ["Orca", "Pequod", "Mary Lee", "Indianapolis"],
  "Which of these did Indiana Jones never attempt to recover during his silver-screen adventures":
  ["the cross of jesus", "an alien skull", "sankara stone", "the ark of the covenant"],
  "which actor id not appear in the 1972 classic 'the godfather'":
  ["robert deniro", "talia shire", "sterling hayden", "robert duvall"],
  "which actor has never played dracula onscreen": [
    "frank langella",
    "nic cage",
    "gary oldman",
    "boris karloff",
  ],
  "which of the following was never ranked as the top grossing movie of all time":
  ['the sound of music', 'avengers infinity war', 'titanic', 'gone with the wind'],
  "in 'the breakfast club' molly ringwald surprises the other detentionés by eating what for lunch?" :
  ['sushi','overnight oats', 'caviar', 'dog'],
  "walt disney released his first fully animated feature, snow white and the seven dwarfs, in 1937. what was his second animated film?" : 
  ['pinoccio','fantasia', 'bambi', 'cinderella'],
  "the iconic line 'im mad as hell, and im not going to take this anymore!` comes from which movie?" : 
  ['network', 'one flew over the cuckoos nest', 'the shining', 'dog day afternoon'],
  "which of the following did not win the oscar for best picture?" : 
  ['fargo', 'birdman', 'shakespear in love', 'amadeus' ],

}

def play_game(player, category):
    print(''':.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.::.:.:.:.:.:''')
    print(f"WELOME TO TRIVIA {player.name}!!!")
    if category == 'F':
        QUESTIONS = QUESTIONS_MOVIES
    elif category == 'S':
        QUESTIONS = QUESTIONS_SPORTS
    else:
        QUESTIONS = QUESTIONS_HISTORY

    num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
    questions = random.sample(list(QUESTIONS.items()), k=num_questions)

    num_correct = 0
    # for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        correct_answer = alternatives[0]
        labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
        for label, alternative in labeled_alternatives.items():
            print(f"  {label}) {alternative}")

        while (answer_label := input("\nAnswer? ")) not in labeled_alternatives:
            print(f"Please answer one of {', '.join(labeled_alternatives)}")

        answer = labeled_alternatives[answer_label]
        if answer == correct_answer:
            num_correct += 1
            print("""
            🌱 🌱 🌱 🌱 🌱
              🌱 🌱 🌱 🌱 🌱
               🌱 🌱 🌱 🌱 🌱
          
                  so good !  🫶
                 
                🌱 🌱 🌱 🌱 🌱
               🌱 🌱 🌱 🌱 🌱
              🌱 🌱 🌱 🌱 🌱
            """)
            print(f"{player.name} Current Score:")
            print(num_correct)
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
            

    print(f"\n{player.name} got {num_correct} correct out of {num} questions")
    print(f"{player.name}'s new total score is {player.score + num_correct}")
    return num_correct