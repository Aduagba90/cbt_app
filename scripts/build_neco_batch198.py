"""Batch 198 - WAEC Civic Education round 7 (WAEC top-up, R39).

Grows WAEC Civic from 239 toward ~265 with angles not yet in the
bank: empathy; gratitude; orderliness; queues; the zebra
crossing; the driver's licence; direct democracy; Lincoln's
definition of democracy; rule of law; citizenship defined; by
registration; national service; the government's duty of
amenities; youth empowerment; skills acquisition; the peer group;
mass media and school as agents of socialisation; community
service; the national motto; the pledge's aim; citizenship
education's objective; limits of rights; the purpose of laws;
patriotism. Scanned against the whole Civic pool (WAEC and NECO
stems, 485 items).

    python3 scripts/build_neco_batch198.py -> content/batch_198_waec_civic7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_VAL = "Values"
T_ORD = "Orderliness and Road Use"
T_DEM = "Democracy and the Rule of Law"
T_CIT = "Citizenship"
T_DUT = "Duties and Obligations"
T_SOC = "Socialisation and Community"
T_SYM = "National Symbols"

PASSAGES = []
PQ = []

Q = [
    (T_VAL, "Easy", "The ability to share and understand what another person is feeling is called",
     "empathy", "sympathy of strangers",
     "pity", "tolerance", "A",
     "You put yourself in the other person's shoes."),
    (T_VAL, "Easy", "A student who writes a thank-you note to a helper has shown the value of",
     "gratitude", "contentment",
     "prudence", "humility", "A",
     "A grateful heart acknowledges every kindness."),
    (T_VAL, "Medium", "The readiness to serve and defend one's country at all times, even at personal cost, is",
     "patriotism", "nationalism of parties",
     "hero worship", "partisanship", "A",
     "The patriot puts country before self."),
    (T_ORD, "Medium", "A state of affairs in which people obey rules, respect one another and take their proper turn is called",
     "orderliness", "obedience by force",
     "discipline of soldiers", "punctuality", "A",
     "Everything moves in its proper order."),
    (T_ORD, "Medium", "Passengers at a motor park who queue calmly instead of struggling for seats enjoy",
     "fairer and faster service", "cheaper fares by half",
     "fewer taxes on travel", "shorter bus routes", "A",
     "The queue serves everyone in turn."),
    (T_ORD, "Easy", "The white stripes painted across a road to show where pedestrians have the right of way is the",
     "zebra crossing", "stop sign",
     "roundabout", "flyover", "A",
     "Cars halt while walkers cross the stripes."),
    (T_ORD, "Easy", "Before a person may legally drive a car on Nigerian roads, he must first obtain a",
     "valid driver's licence", "voter's card",
     "national passport", "tax certificate", "A",
     "The licence says the holder has passed the test."),
    (T_DEM, "Medium", "A system of government in which the citizens themselves meet and make the laws directly, as in ancient Athens, is",
     "direct democracy", "representative democracy",
     "a constitutional monarchy", "an oligarchy", "A",
     "Every citizen is his own lawmaker."),
    (T_DEM, "Medium", "Government of the people, by the people and for the people is the famous definition of",
     "democracy", "federalism",
     "socialism", "communism", "A",
     "Abraham Lincoln gave it at Gettysburg."),
    (T_DEM, "Medium", "The principle that every person, rulers included, is subject to the known law of the land is the",
     "rule of law", "rule of might",
     "law of nature", "divine right of kings", "A",
     "No one stands above the law's reach."),
    (T_CIT, "Medium", "The legal bond between an individual and a state, carrying both rights and duties, is",
     "citizenship", "nationalism",
     "residency", "kinship", "A",
     "It ties the person to the country in law."),
    (T_CIT, "Hard", "A Nigerian who simultaneously holds the citizenship of another country is said to have",
     "dual citizenship", "honorary citizenship",
     "alien status", "stateless status", "A",
     "Two flags, one person, by law."),
    (T_DUT, "Medium", "Graduates serving under the NYSC scheme for one year are performing the citizen's duty of",
     "national service", "forced labour",
     "political apprenticeship", "military conscription", "A",
     "The nation calls and the youth answer."),
    (T_DUT, "Easy", "The provision of roads, schools, hospitals and pipe-borne water for the people is chiefly the duty of",
     "government", "the richest citizens",
     "foreign donors only", "traditional rulers", "A",
     "The people's common wealth serves them all."),
    (T_SOC, "Medium", "Empowering young people with the skills and opportunities to earn a living by themselves is called",
     "youth empowerment", "child labour",
     "youth restiveness", "social welfare", "A",
     "The young learn to stand on their own feet."),
    (T_SOC, "Medium", "A school leaver who enrols at a vocational centre to learn tailoring is engaging in",
     "skills acquisition", "job racketeering",
     "child trafficking", "idleness", "A",
     "A trade in the hand outlasts a job begged for."),
    (T_SOC, "Medium", "The group of age-mates whose approval strongly shapes a teenager's habits and choices is the",
     "peer group", "age grade of elders",
     "family council", "class committee", "A",
     "Teenagers dress and talk like their mates."),
    (T_SOC, "Medium", "By shaping what people watch, read and hear, radio and television act as agents of",
     "socialisation", "transportation",
     "legislation", "taxation", "A",
     "The screens teach as much as the school."),
    (T_SOC, "Medium", "Besides the family, the institution that most formally trains a child in the values and skills of society is the",
     "school", "market",
     "law court", "motor park", "A",
     "Its walls are society's first classroom."),
    (T_SOC, "Easy", "Students who join volunteers to sweep the market square on sanitation day are performing",
     "community service", "punishment for offences",
     "paid employment", "political campaign", "A",
     "They give their labour to their own people."),
    (T_SYM, "Easy", "The motto written on the Nigerian coat of arms is",
     "Unity and Faith, Peace and Progress", "One Nigeria, One People",
     "Strength in Diversity Forever", "Freedom and Justice for All", "A",
     "The black shield carries the nation's creed."),
    (T_SYM, "Medium", "The daily recitation of the national pledge in schools chiefly aims at building",
     "loyalty and patriotism in the young", "fear of punishment",
     "skill in public speaking", "rivalry among classes", "A",
     "Hearts are trained alongside voices."),
    (T_CIT, "Medium", "Citizenship education is included in the Nigerian school curriculum mainly to",
     "responsible citizens", "fill the timetable fully",
     "train future soldiers", "replace religious studies", "A",
     "The classroom builds the country's future."),
    (T_DEM, "Medium", "The rights of one citizen are lawfully limited whenever they",
     "threaten the rights of others", "displease the rich",
     "annoy government officials", "differ from tradition", "A",
     "My freedom ends where yours begins."),
    (T_ORD, "Easy", "Laws are made in every society primarily to",
     "keep peace and order", "punish the poor for the rich",
     "fill government gazettes", "please foreign powers", "A",
     "Where law ends, disorder begins."),
    (T_ORD, "Medium", "A town where drivers ignore traffic rules altogether will most likely suffer",
     "frequent road accidents", "cheaper vehicle prices",
     "better fuel supply", "quicker journey times", "A",
     "Every ignored light collects its toll."),
]

build_batch(
    S,
    "batch_198_waec_civic7.json",
    "198",
    "WAEC Civic round 7 (R39 top-up): empathy; gratitude; "
    "patriotism; orderliness; calm queues; the zebra crossing; the "
    "driver's licence; direct democracy; Lincoln's definition; "
    "rule of law; citizenship defined; citizenship by "
    "registration; NYSC as national service; government's duty of "
    "amenities; youth empowerment; skills acquisition; the peer "
    "group; mass media and school as agents of socialisation; "
    "community service; the national motto; the pledge's aim; "
    "citizenship education's objective; limits of rights; the "
    "purpose of laws; consequences of ignoring traffic rules. "
    "Scanned against the whole Civic pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
