import pygame, sys, time, random
import numpy as np
from pygame.locals import *

TestDuration = 30 #Seconds 
TotalNumberOfLoadedWords = 1000

WindowWidth = 1500
WindowHeight = 900

Black = (0  ,0  ,0  )
White = (255,255,255)
Red   = (255,0  ,0  )
Green = (0  ,255,0  )
Gray  = (50 ,50 ,50 )

FPS =  60
BasicFontSize = 125
StatsFontSize = 50
StartScreenFontSize = 100

TextY = 200
CompletedOffSet = 0

KeyBoardTopLeft = 325,500
KeyImg = pygame.image.load("key.gif")
KeyWidth = KeyImg.get_width()
KeySpacing = KeyWidth / 5

TabImg = pygame.image.load("tab.gif")
CapsLockImg = pygame.image.load("capsLock.gif")
ShiftImg = pygame.image.load("shift.gif")
ShiftTwoImg = pygame.image.load("shift2.gif")
BackSpaceImg = pygame.image.load("backSpace.gif")
EnterImg = pygame.image.load("enter.gif")
SpaceImg = pygame.image.load("space.gif")

ImgArray = [KeyImg, BackSpaceImg, TabImg, EnterImg, CapsLockImg, ShiftImg, ShiftTwoImg, SpaceImg]
KeyOrder = [96, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 45, 61, 8, 9, 113, 119, 101, 114, 116, 121, 117, 105, 111, 112, 91, 93, 13, 301, 97, 115, 100, 102, 103, 104, 106, 107, 108, 59, 39, 92, 304, 60, 122, 120, 99, 118, 98, 110, 109, 44, 46, 47, 303, 32]
CorrespondingValues = ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "BACKSPACE", "TAB", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "ENTER", "CAPSLOCK", "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "#", "SHIFT", "SLASH", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/", "SHIFTTWO", " "]
Dictionary = ["makeshift", "clap", "metal", "slip", "cluttered", "tap", "thank", "cautious", "wonder", "chief", "pot", "analyse", "irritating", "prevent", "psychotic", "sturdy", "lettuce", "bake", "amusement", "macho", "obedient", "fertile", "true", "pet", "judge", "messy", "mint", "bloody", "daffy", "simplistic", "ruthless", "precious", "nappy", "slap", "fresh", "home", "star", "sail", "curious", "expect", "phone", "sun", "word", "color", "necessary", "eatable", "ossified", "knit", "stop", "marble", "sock", "plants", "cheap", "voyage", "nut", "lavish", "racial", "spill", "humorous", "nippy", "cat", "mailbox", "correct", "ill", "instinctive", "icicle", "lacking", "maid", "pizzas", "tomatoes", "walk", "yielding", "tan", "sugar", "organic", "touch", "quicksand", "crazy", "bait", "puncture", "throat", "manage", "egg", "unbiased", "cart", "righteous", "understood", "surprise", "obtainable", "stain", "protective", "terrific", "periodic", "dry", "hat", "whistle", "feigned", "knowledgeable", "brainy", "disturbed", "adaptable", "deserted", "chess", "hope", "fixed", "reason", "ink", "ban", "solid", "place", "poor", "books", "excite", "trashy", "friends", "deserve", "absorbed", "noise", "branch", "grain", "servant", "materialistic", "mighty", "account", "melted", "extra-small", "tramp", "youthful", "fallacious", "kindly", "curtain", "fit", "obsequious", "root", "descriptive", "separate", "test", "loving", "act", "frail", "turkey", "better", "sigh", "low", "cycle", "silky", "touch", "remove", "lie", "command", "smile", "transport", "needless", "waste", "battle", "trouble", "material", "sincere", "rifle", "seal", "profuse", "helpful", "abrupt", "prefer", "cattle", "rate", "toothbrush", "record", "change", "nest", "disagreeable", "shoe", "depend", "join", "grass", "dad", "oval", "ruddy", "fruit", "selfish", "purpose", "meek", "mountainous", "acrid", "full", "thankful", "stretch", "exuberant", "fair", "smelly", "common", "foot", "peep", "mixed", "yard", "zinc", "cold", "current", "habitual", "tranquil", "thundering", "anger", "misty", "drip", "aback", "snakes", "crayon", "meaty", "kiss", "best", "degree", "fearful", "bawdy", "things", "dear", "glossy", "handle", "lace", "double", "quaint", "board", "match", "hour", "equable", "wrathful", "cars", "floor", "existence", "condition", "bouncy", "flesh", "unhealthy", "new", "pause", "legs", "toy", "moan", "desk", "motionless", "thirsty", "old", "hideous", "cannon", "name", "push", "married", "subsequent", "cut", "repeat", "communicate", "confuse", "even", "friend", "potato", "aspiring", "tree", "grey", "wish", "irate", "pull", "giant", "valuable", "large", "unwieldy", "interrupt", "complex", "cheer", "annoyed", "depressed", "closed", "eyes", "handy", "milk", "spade", "naughty", "judge", "classy", "false", "station", "trip", "womanly", "sloppy", "dispensable", "chunky", "seed", "accidental", "harm", "earn", "stormy", "roof", "jittery", "hollow", "delay", "scattered", "snail", "cute", "talented", "thread", "unused", "adhesive", "snow", "toad", "volcano", "fireman", "useless", "house", "knot", "insidious", "beef", "slow", "escape", "decision", "mass", "object", "cow", "inform", "north", "meal", "property", "income", "lopsided", "injure", "competition", "snobbish", "educate", "sore", "cause", "smooth", "doctor", "channel", "alcoholic", "look", "ultra", "avoid", "mourn", "oven", "rhythm", "bike", "strap", "soda", "stamp", "employ", "expansion", "cent", "rebel", "aunt", "drum", "enjoy", "female", "railway", "son", "sin", "evanescent", "birds", "airplane", "lazy", "tempt", "festive", "action", "loaf", "whirl", "scent", "cobweb", "steadfast", "notebook", "grouchy", "tremble", "eager", "guess", "thrill", "memory", "health", "duck", "laugh", "serious", "abortive", "futuristic", "complain", "muddle", "hammer", "skin", "learn", "wash", "unruly", "destroy", "straw", "breath", "thin", "amusing", "arrest", "wave", "dinosaurs", "pump", "unkempt", "guide", "picayune", "vacuous", "dog", "rule", "waves", "wood", "paste", "boot", "strengthen", "memorise", "waste", "lighten", "opposite", "selection", "onerous", "shelf", "toys", "productive", "bomb", "wry", "cherries", "group", "frightening", "spot", "spiders", "kitty", "sticky", "jump", "school", "ship", "frequent", "romantic", "watch", "animal", "available", "side", "undress", "appreciate", "direction", "control", "title", "calm", "creepy", "rainy", "skinny", "tremendous", "ashamed", "far-flung", "jealous", "left", "axiomatic", "square", "hapless", "wide-eyed", "stage", "resonant", "cushion", "splendid", "size", "tail", "black-and-white", "angle", "endurable", "nose", "care", "gratis", "flawless", "hanging", "company", "flood", "tough", "ear", "gather", "present", "tenuous", "call", "offer", "party", "precede", "jellyfish", "raise", "domineering", "girls", "include", "right", "hysterical", "yoke", "flame", "mammoth", "cabbage", "cave", "three", "trite", "lewd", "ducks", "ludicrous", "receipt", "gaping", "gigantic", "confess", "eye", "border", "afterthought", "inconclusive", "conscious", "boiling", "refuse", "hushed", "brass", "dead", "increase", "present", "noisy", "hot", "harmonious", "screw", "error", "queen", "noiseless", "interesting", "relax", "battle", "tin", "door", "unit", "provide", "puzzling", "complete", "jagged", "example", "window", "pin", "square", "invite", "reaction", "wish", "hook", "attractive", "striped", "natural", "oafish", "tightfisted", "ice", "first", "chew", "hard", "excellent", "concerned", "man", "accessible", "earthy", "questionable", "educated", "horn", "grade", "alarm", "pollution", "burn", "wrap", "history", "bulb", "outgoing", "disagree", "daughter", "marvelous", "level", "horses", "earsplitting", "brief", "lunch", "glistening", "trick", "fowl", "birth", "troubled", "town", "pipe", "plant", "muscle", "chalk", "dangerous", "bizarre", "belief", "park", "trouble", "force", "shut", "point", "turn", "elastic", "basket", "utopian", "hissing", "play", "exciting", "brick", "level", "payment", "bright", "class", "freezing", "behave", "wire", "wave", "kiss", "milk", "aberrant", "demonic", "fire", "land", "divergent", "skillful", "wary", "quarrelsome", "sign", "thirsty", "quince", "report", "knife", "purring", "milky", "second", "spoon", "powder", "addition", "telephone", "geese", "observation", "mine", "wheel", "cure", "superficial", "exercise", "wanting", "superb", "insurance", "stimulating", "salt", "print", "dizzy", "creator", "carve", "children", "match", "corn", "direful", "wail", "borrow", "blushing", "switch", "building", "lovely", "cloistered", "pretty", "incandescent", "brave", "childlike", "amuck", "acid", "coast", "search", "steam", "frightened", "linen", "argue", "bite-sized", "rock", "redundant", "veil", "start", "iron", "busy", "summer", "lunchroom", "fast", "whine", "bolt", "curve", "overconfident", "sneeze", "goofy", "rely", "chilly", "found", "electric", "representative", "crow", "cowardly", "coal", "acoustics", "long", "brown", "sparkle", "windy", "use", "jam", "wooden", "bury", "sweltering", "religion", "peel", "permit", "writing", "rain", "spring", "holiday", "handsome", "farm", "interfere", "art", "scatter", "improve", "flat", "stop", "absorbing", "ocean", "agreement", "dress", "rail", "suck", "ancient", "locket", "staking", "tired", "bikes", "imperfect", "scene", "unarmed", "sisters", "unite", "blade", "wiry", "celery", "smoke", "hobbies", "yarn", "visitor", "subtract", "longing", "substantial", "fix", "verdant", "dysfunctional", "fog", "deceive", "quartz", "awful", "shame", "knot", "nerve", "big", "well-groomed", "zephyr", "mature", "road", "please", "stupendous", "shape", "order", "embarrass", "different", "soak", "meat", "back", "neighborly", "long-term", "spiteful", "moldy", "shave", "steady", "invincible", "rice", "satisfying", "powerful", "obscene", "notice", "afford", "innate", "cagey", "oceanic", "seashore", "name", "obsolete", "price", "crooked", "self", "trail", "sheet", "overflow", "week", "lonely", "various", "quilt", "exotic", "reflective", "thumb", "oatmeal", "repulsive", "thing", "belong", "machine", "minister", "division", "deranged", "bedroom", "tip", "swim", "business", "twist", "arch", "hose", "screw", "tow", "elated", "knotty", "ceaseless", "beautiful", "capricious", "fire", "sordid", "minor", "x-ray", "decorate", "responsible", "respect", "silver", "spot", "roll", "voracious", "purple", "obeisant", "preserve", "chivalrous", "sheep", "support", "club", "activity", "chubby", "lip", "attend", "entertain", "proud", "tasty", "fax", "bump", "separate", "grease", "murky", "riddle", "ray", "flock", "somber", "underwear", "bee", "rotten", "obtain", "boundary", "foolish", "apparel", "suspect", "wax", "clean", "mice", "bat", "weight", "comb", "blot", "detect", "stone", "drink", "handsomely", "magic", "plane", "cheat", "slip", "thoughtless", "whispering", "damaging", "fill", "diligent", "gullible", "request", "creature", "medical", "box", "coat", "buzz", "jumpy", "unpack", "elderly", "treat", "blink", "accurate", "test", "phobic", "passenger", "card", "faint", "carpenter", "rainstorm", "hands", "remarkable", "breakable", "raspy", "annoy", "end", "range", "vanish", "sand", "nutritious", "pocket", "fade", "shoes", "well-to-do", "agonizing", "trains", "tasteless", "puzzled", "dusty", "hand", "coordinated", "high", "venomous", "signal", "mine", "sweet", "utter", "twist", "suit", "industrious", "complete", "force", "crush", "illegal", "contain", "dream", "authority", "hot", "huge", "settle", "miss", "rot", "mindless", "mute", "crawl", "tank", "military", "offend", "position", "dogs", "tire", "greedy", "team", "alert", "frame", "hope", "jam", "rapid", "decorous", "abiding", "jail", "prickly", "high-pitched", "malicious", "plant", "apathetic", "wash", "education", "roasted", "deer", "heal", "useful", "day", "gruesome", "flippant", "violent", "water", "labored", "black", "slim", "automatic", "uninterested", "cherry", "instrument", "pop", "unequal", "back", "sidewalk", "giddy", "taste", "zonked", "quack", "collect", "ethereal", "supply", "cactus", "invention", "blind", "disapprove", "harass", "pig", "faulty", "expert", "snails", "calculating", "steep", "plough", "explain", "knock", "delight", "cough", "realise", "flagrant", "itchy", "giraffe", "bead", "fall", "remind", "garrulous", "peace", "unaccountable", "intelligent", "grandmother", "second-hand", "possessive", "reward", "zip", "tiger", "acoustic", "clean", "wine", "abhorrent", "scary", "start", "lamentable", "field", "royal", "amused", "flight", "smile", "squeak", "hateful", "bed", "need", "reign", "need", "plug", "breathe", "kneel", "adamant", "space", "nauseating", "obey", "jump", "tug", "special", "mark", "real", "cool", "impolite", "laborer", "mist", "try", "check", "trade", "count", "cover", "vengeful", "drop", "end", "pencil", "dare", "male", "mere", "known", "fine", "absurd", "pathetic", "describe", "fancy", "cellar", "knowledge", "spark", "concentrate", "part", "idiotic", "room", "like", "measly", "snake", "kind", "rake", "wealth", "prepare", "red", "momentous", "happen", "quarter", "broad", "parallel", "guttural", "wholesale", "towering", "tender", "groan", "murder", "upset", "modern", "twig", "brake", "mean", "blue-eyed", "likeable", "outrageous", "punch", "point", "cloth", "unnatural", "used", "rabbit", "scrawny", "answer", "rambunctious", "bathe", "alive", "needle", "dashing", "steer", "afternoon", "clear", "downtown", "small", "condemned", "rush", "spicy", "low", "kindhearted", "melt", "ten", "jobless", "fuel", "rhetorical", "mind", "grate", "attack", "film", "basin", "coach", "worry", "bells", "spectacular", "rub", "fascinated", "inexpensive", "warn", "float", "tickle", "hurried", "lyrical", "change", "ambitious", "sack", "fierce", "slippery", "heartbreaking", "girl", "balance", "attraction", "tooth", "time", "kaput", "rose", "flowers", "colossal", "free", "shaky", "announce", "hesitant", "majestic", "next", "uttermost", "belligerent", "liquid", "stem", "achiever", "famous", "outstanding", "nutty", "bucket", "omniscient", "bushes", "peck", "stir", "glass", "rustic", "unsightly", "pink", "interest", "moor", "cable", "yellow", "adjoining", "move", "bow", "pumped", "abandoned", "dress", "ground", "sticks", "arrive", "agreeable", "voiceless", "wreck", "tense", "crown", "nation", "bleach", "prick", "angry", "able", "weigh", "didactic", "fold", "fuzzy", "imminent", "quill", "wasteful", "obese", "wait", "orange", "aquatic", "popcorn", "grin", "desert", "sip", "winter", "wiggly", "kick", "homely", "roomy", "can", "stick", "dance", "envious", "chase", "cooing", "hurry", "compete", "wall", "defective", "airport", "quiver", "bubble", "driving", "appear", "scarce", "aloof", "protest", "debt", "absent", "level", "tasteful", "fasten", "stretch", "hulking", "open", "dirt", "honey", "cooperative", "tacit", "women", "stare", "pick", "live", "aboriginal", "hover", "soap", "woman", "texture", "string", "design", "ahead", "gleaming", "tearful", "far", "shock", "simple", "whisper", "public", "eight", "box", "teeny-tiny", "flower", "balance", "penitent", "scrape", "fence", "scientific", "wide", "hospital", "paltry", "imported", "naive", "last", "tumble", "promise", "science", "gifted", "scare", "preach", "basketball", "shop", "badge", "sharp", "playground", "serve", "army", "disgusted", "hair", "wool", "program", "gaze", "governor", "forgetful", "bored", "prose", "spotted", "aboard", "plastic", "meeting", "rabbits", "retire", "toothpaste", "hungry", "wrench", "animated", "allow", "silent", "abrasive", "spark", "wriggle", "ambiguous", "annoying", "enthusiastic", "admit", "discover", "sour", "sophisticated", "whip", "pleasure", "sweater", "daily", "enormous", "shake", "unequaled", "deadpan", "threatening", "terrible", "humdrum", "country", "shy", "tiny", "flash", "fail", "curved", "houses", "frame", "believe", "many", "attract", "spare", "sparkling", "shirt", "yummy", "limping", "future", "store", "loss", "voice", "burst", "half", "excuse", "enchanting", "stereotyped", "air", "fly", "exclusive", "determined", "nine", "gusty", "elfin", "jaded", "question", "scandalous", "picture", "fear", "regular", "pour", "light", "partner", "pale", "bitter", "hurt", "grape", "mix", "intend", "curvy", "ill-fated", "circle", "muddled", "boorish", "scale", "obnoxious", "request", "profit", "sound", "super", "stamp", "talk", "itch", "dynamic", "quickest", "poison", "glove", "baby", "fish", "replace", "interest", "scribble", "temper", "value", "ugliest", "bore", "attempt", "pail", "rigid", "versed", "oil", "five", "substance", "amuse", "insect", "smoggy", "rough", "base", "sack", "unlock", "fortunate", "haircut", "heat", "industry", "good", "beds", "adjustment", "uneven", "scissors", "care", "scarf", "acceptable", "advertisement", "flavor", "cows", "friendly", "crabby", "toe", "premium", "cause", "jolly", "cakes", "vague", "wistful", "dock", "sulky", "unfasten", "dependent", "song", "sick", "furtive", "waggish", "glamorous", "juggle", "decay", "wilderness", "boundless", "time", "internal", "silent", "lush", "mark", "committee", "learned", "haunt", "copy", "flashy", "soothe", "drop", "crowd", "empty", "gray", "grumpy", "pigs", "changeable", "taboo", "swift", "feeling", "magenta", "continue", "trot", "clover", "form", "neck", "flaky", "like", "cake", "miniature", "fairies", "optimal", "subdued", "teeny", "late", "flap", "risk", "umbrella", "pedal", "wrestle", "middle", "queue", "helpless", "bat", "treatment", "psychedelic", "sleep", "overwrought", "therapeutic", "grip", "argument", "amount", "healthy", "craven", "head", "roll", "pleasant", "elegant", "victorious", "hospitable", "store", "cough", "place", "vulgar", "practise", "bad", "hydrant", "swanky", "rat", "possible", "distinct", "moaning", "skip", "butter", "noxious", "smoke", "carriage", "comfortable", "furniture", "shivering", "unadvised", "snow", "reproduce", "numerous", "glue", "chance", "one", "holistic", "weather", "work", "salty", "nosy", "tub", "warm", "branch", "cute", "brush", "important", "miscreant", "close", "energetic", "babies", "tour", "dramatic", "beneficial", "juicy", "receive", "stupid", "rabid", "wacky", "paddle", "judicious", "whistle", "nimble", "irritate", "story", "experience", "collar", "economic", "oranges", "well-made", "horrible", "cloudy", "juice", "suspend", "squash", "event", "combative", "piquant", "clever", "disgusting", "ripe", "night", "chemical", "heat", "spiritual", "hug", "repair", "berry", "dime", "fretful", "observe", "mother", "doubt", "connection", "bubble", "grotesque", "chop", "resolute", "zebra", "smash", "violet", "fear", "meddle", "connect", "strange", "step", "extra-large", "stew", "deafening", "reply", "pass", "plate", "advice", "label", "ants", "well-off", "man", "spray", "loutish", "addicted", "eminent", "spy", "dam", "race", "drain", "alluring", "perpetual", "uppity", "furry", "vigorous", "quick", "wealthy", "sneaky", "part", "sink", "suggestion", "stingy", "writer", "jelly", "vase", "ritzy", "delightful", "panoramic", "shrill", "year", "easy", "clam", "development", "delicate", "coil", "little", "kittens", "worthless", "motion", "ugly", "exchange", "reminiscent", "magnificent", "wicked", "needy", "nifty", "gainful", "cry", "load", "use", "defiant", "bite", "clip", "careless", "shade", "functional", "porter", "morning", "ill-informed", "spurious", "ski", "nervous", "draconian", "walk", "gamy", "form", "train", "maddening", "near", "embarrassed", "whip", "squeamish", "gate", "shock", "territory", "ubiquitous", "baseball", "laughable", "screeching", "visit", "thunder", "vein", "rare", "tax", "taste", "beginner", "letter", "dry", "type", "cruel", "water", "dislike", "office", "welcome", "testy", "leg", "talk", "delicious", "damp", "encouraging", "wild", "robin", "claim", "drab", "hate", "bone", "help", "tent", "familiar", "pull", "idea", "cover", "number", "greet", "bit", "smart", "barbarous", "decide", "pricey", "wrong", "shrug", "surprise", "frog", "receptive", "attach", "cast", "challenge", "aggressive", "quiet", "lively", "pump", "admire", "spotty", "follow", "auspicious", "number", "curve", "edge", "untidy", "bless", "rob", "nonchalant", "boil", "pray", "skate", "occur", "ad", "hoc", "actor", "robust", "gabby", "zoom", "nasty", "tawdry", "scrub", "wound", "macabre", "step", "hard-to-find", "sort", "boring", "engine", "capable", "wakeful", "chicken", "probable", "mushy", "theory", "dreary", "war", "shop", "crowded", "attack", "assorted", "calculator", "plantation", "quizzical", "icky", "stocking", "guarantee", "post", "seemly", "unwritten", "punishment", "relieved", "cheerful", "courageous", "lumber", "upbeat", "tiresome", "frighten", "pear", "sofa", "perfect", "six", "alike", "husky", "marry", "amazing", "mom", "consist", "fact", "abashed", "perform", "toothsome", "kill", "trap", "guiltless", "file", "guarded", "jewel", "thoughtful", "zipper", "nostalgic", "pets", "slope", "matter", "disappear", "blow", "poised", "letters", "hate", "warm", "mellow", "uptight", "trucks", "deeply", "discovery", "crack", "long", "glib", "look", "acidic", "zealous", "blue", "note", "aromatic", "terrify", "thick", "pack", "rightful", "nondescript", "fancy", "hand", "cracker", "selective", "accept", "tense", "mouth", "expensive", "decisive", "sense", "foregoing", "dolls", "apparatus", "round", "pointless", "devilish", "fat", "satisfy", "hilarious", "joke", "face", "fantastic", "short", "lowly", "cumbersome", "knee", "finicky", "loose", "silk", "unique", "mess", "up", "dull", "owe", "alert", "crib", "few", "elite", "ignorant", "brawny", "difficult", "travel", "hook", "luxuriant", "lock", "instruct", "bottle", "stomach", "bashful", "average", "beg", "numberless", "godly", "painstaking", "compare", "bewildered", "straight", "whimsical", "previous", "grubby", "join", "graceful", "caption", "recognise", "limit", "vegetable", "squalid", "trip", "birthday", "wet", "greasy", "suffer", "nonstop", "shiny", "songs", "wonderful", "ruin", "stuff", "coil", "measure", "cheese", "dinner", "sleet", "filthy", "homeless", "drag", "mountain", "inject", "move", "zoo", "sore", "thought", "woozy", "month", "doll", "tedious", "face", "groovy", "want", "license", "nod", "hop", "green", "past", "knowing", "breezy", "paint", "finger", "cuddly", "paper", "own", "sedate", "supreme", "explode", "save", "safe", "curly", "drain", "dazzling", "share", "vagabond", "fragile", "boat", "drawer", "nest", "awesome", "warlike", "impulse", "arm", "pushy", "gentle", "punish", "abounding", "tart", "gold", "push", "efficient", "friction", "workable", "bent", "entertaining", "van", "mask", "enchanted", "soft", "physical", "spotless", "men", "loud", "rude", "polite", "lumpy", "orange", "caring", "shade", "quiet", "bridge", "colour", "tray", "petite", "stranger", "sable", "money", "lean", "blood", "hall", "possess", "turn", "grip", "grandfather", "swing", "melodic", "hill", "temporary", "hang", "tangible", "heavenly", "question", "fanatical", "scream", "volleyball", "mend", "train", "abstracted", "boast", "successful", "flower", "heavy", "spoil", "neat", "scold", "examine", "bath", "legal", "massive", "rinse", "minute", "immense", "deep", "truck", "cub", "anxious", "open", "rock", "wobble", "love", "nebulous", "languid", "painful", "snore", "lucky", "rampant", "tidy", "statement", "pies", "undesirable", "damage", "launch", "language", "fold", "choke", "horse", "rejoice", "telling", "eggs", "reach", "radiate", "trick", "identify", "tall", "dapper", "clumsy", "last", "detailed", "foamy", "disastrous", "mundane", "wretched", "soup", "mate", "succinct", "trust", "blush", "watery", "system", "strong", "route", "broken", "vast", "old-fashioned", "magical", "squeal", "detail", "concern", "sassy", "statuesque", "halting", "cats", "effect", "fool", "government", "land", "trace", "book", "overjoyed", "vest", "sea", "pan", "truculent", "society", "fluttering", "vessel", "general", "polish", "work", "relation", "plan", "vacation", "ladybug", "parcel", "stream", "disillusioned", "deliver", "plucky", "approve", "grieving", "boy", "exultant", "sign", "moon", "jar", "teeth", "silly", "squealing", "squeeze", "tick", "fork", "ragged", "uncle", "reflect", "river", "bounce", "lake", "waiting", "aware", "zany", "exist", "produce", "bang", "cynical", "panicky", "sister", "standing", "hum", "abundant", "unsuitable", "whole", "frantic", "rule", "cultured", "unknown", "wandering", "worried", "plot", "observant", "mug", "parched", "arrange", "fetch", "suit", "puny", "plant", "sponge", "chin", "ignore", "press", "enter", "sleepy", "flag", "nice", "tame", "offbeat", "return", "pat", "ratty", "hunt", "certain", "adorable", "person", "cap", "charge", "worm", "adventurous", "saw", "abnormal", "innocent", "stale", "hallowed", "line", "snatch", "normal", "impress", "two", "incredible", "remain", "divide", "cross", "camp", "merciful", "love", "narrow", "trees", "bag", "march", "scratch", "shiver", "recess", "fearless", "erect", "death", "scorch", "typical", "power", "lock", "permissible", "excited", "laugh", "view", "plain", "truthful", "book", "literate", "awake", "lackadaisical", "heady", "teaching", "willing", "lick", "car", "symptomatic", "befitting", "thaw", "spiky", "pretend", "camera", "living", "rescue", "stitch", "overrated", "kick", "ajar", "snotty", "calculate", "bell", "tease", "yawn", "savory", "torpid", "four", "hole", "guide", "bear", "funny", "ball", "pest", "island", "wrist", "library", "coach", "crate", "imagine", "abject", "guitar", "dust", "berserk", "giants", "stay", "earthquake", "impossible", "pancake", "produce", "doubtful", "apologise", "increase", "billowy", "arrogant", "chickens", "extend", "hammer", "fabulous", "jog", "camp", "equal", "tie", "agree", "hypnotic", "table", "afraid", "careful", "surround", "growth", "sniff", "record", "fluffy", "behavior", "rich", "political", "elbow", "sudden", "spooky", "keen", "smiling", "succeed", "imaginary", "debonair", "fry", "evasive", "young", "reading", "weary", "harmony", "nail", "glow", "defeated", "sneeze", "stove", "regret", "spiffy", "hellish", "untidy", "wise", "finger", "flow", "bare", "lively", "ticket", "historical", "market", "abusive", "pickle", "null", "bright", "grandiose", "appliance", "frogs", "cook", "destruction", "infamous", "protect", "erratic", "list", "puffy", "brash", "zesty", "lethal", "scarecrow", "reject", "fumbling", "rod", "slave", "rest", "invent", "pie", "strip", "desire", "tongue", "actually", "listen", "dust", "remember", "crack", "confused", "rub", "brake", "front", "vivacious", "wind", "key", "rural", "early", "shocking", "drunk", "astonishing", "private", "efficacious", "crime", "head", "inquisitive", "note", "beam", "colorful", "comparison", "jumbled", "curl", "play", "brother", "throne", "eggnog", "watch", "clammy", "fang", "pine", "soggy", "secretary", "kettle", "gaudy", "leather", "unusual", "disarm", "smell", "lying", "delirious", "slimy", "harbor", "shelter", "verse", "harsh", "quixotic", "show", "faded", "mitten", "dark", "flowery", "jail", "peaceful", "faithful", "thinkable", "bruise", "gorgeous", "impartial", "scared", "slow", "dusty", "alleged", "sky", "monkey", "transport", "discreet", "suppose", "jazzy", "sad", "reduce", "heap", "flimsy", "jeans", "zippy", "ready", "toes", "juvenile", "distance", "arithmetic", "volatile", "offer", "planes", "smell", "ring", "spell", "multiply", "button", "credit", "honorable", "canvas", "consider", "white", "sail", "digestion", "bumpy", "structure", "bomb", "run", "suggest", "uncovered", "yak", "ask", "wren", "sprout", "feeble", "squirrel", "secret", "humor", "lamp", "scintillating", "wing", "witty", "wipe", "donkey", "pen", "weak", "order", "calendar", "third", "synonymous", "shaggy", "influence", "encourage", "marked", "wink", "unbecoming", "odd", "grateful", "cemetery", "gun", "tested", "page", "mysterious", "clear", "tacky", "cream", "aftermath", "measure", "shallow", "smash", "secretive", "advise", "petite", "tight", "crash", "trousers", "develop", "cup", "icy", "add", "tendency", "support", "crook", "plausible", "dirty", "abaft", "quirky", "ablaze", "bustling", "incompetent", "pastoral", "ordinary", "approval", "same", "church", "trade", "grab", "madly", "drown", "unable", "guard", "applaud", "placid", "tangy", "earth", "overt", "rhyme", "coherent", "way", "steel", "joyous", "pinch", "tricky", "great", "seat", "recondite", "skirt", "woebegone", "food", "glorious", "maniacal", "callous", "yell", "charming", "bird", "lame", "rings", "introduce", "top", "ghost", "empty", "sound", "discussion", "distribution", "stroke", "release", "rain", "damaged", "street", "illustrious", "regret", "carry", "poke", "wander", "expand", "stitch", "tame", "copper", "plastic", "stiff", "happy", "parsimonious", "yam", "burly", "highfalutin"]

class TouchTyper:
	def __init__(self):
		pygame.init()

		self.DisplayScreen = pygame.display.set_mode((WindowWidth,WindowHeight))

		self.clock = pygame.time.Clock()

		self.initGame()

	def initGame(self):
		self.gameState = 0

		self.coordDict = self.createcoordDict()
		self.pressedKeys = []

		self.seconds = TestDuration 
		self.secondFractions = 0
		self.wordCount = 0
		self.missClicks = 0

		self.BasicFont = pygame.font.SysFont("courier", BasicFontSize, bold=True)
		self.StatsFont = pygame.font.SysFont("courier", StatsFontSize, bold=True)
		self.StartFont = pygame.font.SysFont("courier", StartScreenFontSize, bold=True)

		self.fullText = self.appendRandomWords([], TotalNumberOfLoadedWords)
		self.fullText = self.formatText(self.fullText)

		self.currentTextLocation = 0

		self.manageTextContent()

	def appendRandomWords(self, array, noOfWords):
		for x in range(noOfWords):
			array.append(Dictionary[np.random.randint(len(Dictionary))])

		return array

	def manageTextContent(self):
		if self.currentTextLocation + 10 < len(self.fullText):
			endOfIndex = self.currentTextLocation + 10
		else:
			endOfIndex = len(fullText)

		self.currentText = self.fullText[self.currentTextLocation: endOfIndex]

		if self.currentTextLocation - 10 > 0:
			startOfIndex = self.currentTextLocation - 10
		else:
			startOfIndex = 0

		self.completedText = self.fullText[startOfIndex: self.currentTextLocation]

		while len(self.completedText) < 10:
			self.completedText = " " + self.completedText

	def formatText(self, array):
		string = ""
		for item in array:
			string += item + " "
		return string 

	def createcoordDict(self):
		coordDict = {}
		z = 0
		for x in range(13):
			coordDict[z] = (x * KeyWidth + (x * KeySpacing) + KeyBoardTopLeft[0] - (KeyWidth + (KeySpacing * 5)), KeyBoardTopLeft[1]), 0
			z += 1
		coordDict[z] = (KeyBoardTopLeft[0] + (KeyWidth + KeySpacing) * 11 + KeySpacing * 2 + 5, KeyBoardTopLeft[1]), 1
		z += 1
		coordDict[z] = (KeyBoardTopLeft[0] - KeyWidth * 2 + 5,KeyBoardTopLeft[1] + (KeyWidth + KeySpacing)), 2
		z += 1
		for x in range(12):
			coordDict[z] = (x * KeyWidth + (x * KeySpacing) + KeyBoardTopLeft[0], KeyBoardTopLeft[1] + (KeyWidth + KeySpacing)), 0
			z += 1
		coordDict[z] = (KeyBoardTopLeft[0] + (KeyWidth + KeySpacing) * 12, KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 1)), 3
		z += 1
		coordDict[z] = (KeyBoardTopLeft[0] - KeyWidth * 2 + 5,KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 2)), 4
		z += 1
		for x in range(12):
			coordDict[z] = (x * KeyWidth + (x * KeySpacing) + KeyBoardTopLeft[0] + KeySpacing, KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 2)), 0
			z += 1
		coordDict[z] = (KeyBoardTopLeft[0] - KeyWidth * 2 + 5,KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 3)), 5
		z += 1
		for x in range(11):
			coordDict[z] = (x * KeyWidth + (x * KeySpacing) + KeyBoardTopLeft[0] - KeySpacing, KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 3)), 0
			z += 1	
		coordDict[z] = (KeyBoardTopLeft[0] + (KeyWidth + KeySpacing) * 11 - KeySpacing + 2, KeyBoardTopLeft[1] + ((KeyWidth + KeySpacing) * 3)), 6 
		z += 1
		coordDict[z] = ((KeyBoardTopLeft[0]  + (KeyWidth + KeySpacing) * 3 - KeySpacing, KeyBoardTopLeft[1] + (KeyWidth + KeySpacing) * 4), 7)

		return coordDict

	def drawKeyBoard(self):
		for coord in self.coordDict:
			notPressed = True
			for key in self.pressedKeys:
				if coord == key:
					notPressed = False
			if notPressed:
				self.DisplayScreen.blit(ImgArray[self.coordDict[coord][1]], self.coordDict[coord][0])

	def drawText(self):
		currentTextRect = self.BasicFont.render("%s" %(self.currentText), True, White)
		self.DisplayScreen.blit(currentTextRect, (WindowWidth / 2, TextY))
		completedTextRect = self.BasicFont.render("%s" %(self.completedText), True, Gray)
		self.DisplayScreen.blit(completedTextRect, (CompletedOffSet, TextY))

	def drawTimer(self):
		timerTextRect = self.StatsFont.render("Time Remaining: %s" %(self.seconds), True, White)
		self.DisplayScreen.blit(timerTextRect, (WindowWidth / 5 * 3, 0))

	def drawWordCount(self):
		wordCountRect = self.StatsFont.render("Word Count: %s" %(self.wordCount), True, White)
		self.DisplayScreen.blit(wordCountRect, (20,0))

	def drawMissClicks(self):
		missClicksRect = self.StatsFont.render("Missclicks: %s" %(self.missClicks), True, White)
		self.DisplayScreen.blit(missClicksRect, (20, 100))

	def drawStartScreen(self):
		startTextRect = self.StartFont.render("Touch Typing Trainer", True, White)
		instructionRect = self.StatsFont.render("Press Space to Start", True, White)
		self.DisplayScreen.blit(startTextRect, (125,200))
		self.DisplayScreen.blit(instructionRect, (450,700))		
		
	def drawStatsScreen(self):
		wordCountRect = self.StartFont.render("Your Typing Speed Was", True, White)
		wordCountRect2 = self.StartFont.render("%s Words Per Minute" %(self.wordCount / float(TestDuration) * 60), True, White)
		wordCountRect3 = self.StartFont.render("Over %s Seconds" %(TestDuration), True, White)
		rectangle = wordCountRect.get_rect()
		rectangle2 = wordCountRect2.get_rect()
		rectangle3 = wordCountRect3.get_rect()
		self.DisplayScreen.blit(wordCountRect, ((WindowWidth / 2) - (rectangle[2] / 2), (WindowHeight / 2) - rectangle[3] * 2))
		self.DisplayScreen.blit(wordCountRect2, ((WindowWidth / 2) - (rectangle2[2] / 2), (WindowHeight / 2) - rectangle2[3]))	
		self.DisplayScreen.blit(wordCountRect3, ((WindowWidth / 2) - (rectangle3[2] / 2), (WindowHeight / 2)))	

		

	def terminate(self):
		pygame.quit()
		sys.exit()

	def run(self):
		while self.gameState == 0:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.terminate()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.terminate()
					else:
						if event.key == K_SPACE:
							self.gameState = 1

			self.drawStartScreen()
			pygame.display.update()
			self.clock.tick(FPS)
				

		while self.gameState == 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.terminate()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.terminate()
					else:	
						if event.key in KeyOrder:
							self.pressedKeys.append(KeyOrder.index(event.key))
							if CorrespondingValues[KeyOrder.index(event.key)] == self.currentText[0]:
								self.currentTextLocation += 1
								self.manageTextContent()
								if event.key == K_SPACE:
									self.wordCount += 1 
							else:
								self.missClicks += 1

				elif event.type == KEYUP:
					if event.key in KeyOrder:
						if len(self.pressedKeys) > 0:
							self.pressedKeys.remove(KeyOrder.index(event.key))

			self.secondFractions += 1
			if self.secondFractions >= FPS:
				self.seconds -= 1
				self.secondFractions = 0
				if self.seconds <= 0:
					self.DisplayScreen.fill(Black)
					self.drawStatsScreen()
					pygame.display.update()
					time.sleep(2)
					self.gameState = 2
					
			
			keys = pygame.key.get_pressed()
			self.DisplayScreen.fill(Black)
			self.drawKeyBoard()
			self.drawText()
			self.drawTimer()
			self.drawWordCount()
			self.drawMissClicks()
			pygame.display.update()
			self.clock.tick(FPS)

		while self.gameState == 2:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.terminate()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.terminate()
					else:
						TouchTyper().run()

			self.DisplayScreen.fill(Black)
			self.drawStatsScreen()
			pygame.display.update()
			self.clock.tick(FPS)
		

if __name__ == '__main__':
	TouchTyper().run()=