"""Batch 212 - NECO Civic Education round 7 (NECO top-up, R42).

Grows NECO Civic from 246 toward ~270 with angles not yet in the
bank: vote buying; ballot snatching; advance fee fraud; money
laundering; the Child's Right Act; girl-child education; women's
empowerment; the abolition of slavery; the national flower; the
secret ballot; the multi-party system; popular sovereignty; the
state of emergency; peaceful coexistence; NAFDAC; public opinion;
freedom of information; War Against Indiscipline; drug
trafficking; responsible leadership; citizenship as a status;
law and order; the national conference idea of dialogue; respect
for elders; dignity of labour. Scanned against the whole Civic
pool (WAEC and NECO stems, 511 items).

    python3 scripts/build_neco_batch212.py -> content/batch_212_neco_civic7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_ILL = "Modern Social Ills"
T_RIG = "Rights and the Law"
T_ELE = "Elections and Democracy"
T_SYM = "National Symbols"
T_VAL = "Values"
T_DUT = "Duties and Obligations"
T_ORD = "Orderliness and Society"

PASSAGES = []
PQ = []

Q = [
    (T_ILL, "Medium", "A politician who hands out money to voters on election day so that they will vote for him is guilty of",
     "vote buying", "campaigning lawfully",
     "political awareness", "party mobilisation", "A",
     "The naira buys the ballot and steals the choice."),
    (T_ILL, "Medium", "Thugs who seize ballot boxes at a polling unit on election day commit the crime of",
     "ballot snatching", "peaceful protest",
     "electoral observation", "party canvassing", "A",
     "The stolen box silences a whole village."),
    (T_ILL, "Medium", "The crime in which a fraudster obtains money from a victim by promising huge returns or a false inheritance is popularly called",
     "advance fee fraud", "money laundering",
     "petty theft", "smuggling of goods", "A",
     "The '419' letter always asks for a small fee first."),
    (T_ILL, "Hard", "The crime of moving money made illegally through many accounts so that it appears to come from a lawful source is",
     "money laundering", "tax evasion",
     "advance fee fraud", "counterfeiting", "A",
     "Dirty money is washed till it looks clean."),
    (T_ILL, "Medium", "The unlawful movement of banned drugs across borders for sale is called",
     "drug trafficking", "drug abuse",
     "drug prescription", "drug inspection", "A",
     "The mule carries the poison and the risk."),
    (T_RIG, "Medium", "The law which protects Nigerian children against child marriage, child labour and harmful practices is the",
     "Child's Right Act", "Trade Union Act",
     "Land Use Act", "Fire Arms Act", "A",
     "It stands between the child and every harm."),
    (T_RIG, "Medium", "Educating the girl-child is important to the nation chiefly because it",
     "builds healthier families", "reduces the number of schools built",
     "increases early marriages", "fills the civil service only", "A",
     "An educated mother raises an educated people."),
    (T_RIG, "Medium", "Giving women equal access to education, employment and decision-making is referred to as",
     "women's empowerment", "gender preference",
     "family planning", "positive discrimination", "A",
     "Half the sky must not be held down."),
    (T_RIG, "Easy", "The cruel trade in which human beings were once bought and sold as property has been abolished by law. This is the abolition of",
     "slavery", "child labour",
     "human trafficking", "forced marriage", "A",
     "No price tag may hang on a person again."),
    (T_ELE, "Medium", "The voting system in which a voter marks his ballot in secret so that nobody can know his choice is the",
     "secret ballot", "open ballot",
     "electoral college", "queue voting", "A",
     "The booth keeps every citizen's mind his own."),
    (T_ELE, "Medium", "A political system in which many parties compete freely for power is described as a",
     "multi-party system", "one-party system",
     "no-party system", "single candidacy", "A",
     "Many voices contest for the people's ear."),
    (T_ELE, "Hard", "The principle that all power in a state finally belongs to the people, who lend it to their leaders, is",
     "popular sovereignty", "judicial immunity",
     "executive privilege", "federal character", "A",
     "Government is a trust held for the owners."),
    (T_RIG, "Hard", "A formal declaration by the President, approved by the National Assembly, that temporarily gives special powers to restore order in a crisis is a",
     "state of emergency", "state of origin",
     "declaration of war", "curfew by police", "A",
     "Ordinary law bows briefly to urgent need."),
    (T_ORD, "Medium", "The situation in which people of different religions and ethnic groups live together without fighting is called",
     "peaceful coexistence", "political neutrality",
     "social equality", "cultural dominance", "A",
     "Different drums, one dance floor."),
    (T_ILL, "Medium", "The government agency that checks the quality and safety of foods and drugs sold in Nigeria is",
     "NAFDAC", "NOTAP",
     "NBTE", "NPC", "A",
     "Its seal guards the medicine bottle."),
    (T_ELE, "Medium", "The general beliefs and wishes of ordinary people on matters of public interest are together called",
     "public opinion", "public service",
     "mass mobilisation", "press release", "A",
     "Leaders ignore the people's murmur at their peril."),
    (T_RIG, "Medium", "The right of citizens to obtain information held by government, which helps them hold leaders accountable, is freedom of",
     "information", "movement",
     "worship", "contract", "A",
     "Sunlight on the files keeps hands clean."),
    (T_DUT, "Medium", "The War Against Indiscipline launched in 1984 tried to cure Nigerians of queue-jumping, lateness and",
     "filthiness in public places", "foreign travel",
     "private enterprise", "newspaper reading", "A",
     "Its whistle blew for neatness and order."),
    (T_VAL, "Medium", "A leader who accounts honestly for public money and submits himself to the law demonstrates",
     "responsible leadership", "political sagacity",
     "economic nationalism", "party loyalty", "A",
     "Power held in trust is power well reported."),
    (T_RIG, "Easy", "A person's standing as a recognised member of a state, with the rights and duties that follow, is his",
     "citizenship", "residence permit",
     "birth certificate", "voter's card", "A",
     "It is more than living within the borders."),
    (T_ORD, "Medium", "A country where citizens obey laws, respect authority and settle quarrels peacefully is said to enjoy",
     "law and order", "martial rule",
     "equality of income", "one-party peace", "A",
     "The quiet street is its certificate."),
    (T_ORD, "Medium", "When communities in dispute sit together with mediators to talk out their differences instead of fighting, they are engaged in",
     "dialogue", "litigation",
     "demonstration", "electioneering", "A",
     "The talking table replaces the battlefield."),
    (T_VAL, "Easy", "Greeting and caring for older people in the family and community is the duty of",
     "respect for elders", "elders for youth",
     "equality of ages", "seniority payment", "A",
     "The young honour the grey head."),
    (T_VAL, "Medium", "A student who takes pride in doing his own work well, however humble, has learnt the",
     "dignity of labour", "profit of idleness",
     "art of delegation", "value of connection", "A",
     "Every honest sweat earns its honour."),
]

build_batch(
    S,
    "batch_212_neco_civic7.json",
    "212",
    "NECO Civic round 7 (R42 top-up): vote buying; ballot "
    "snatching; advance fee fraud; money laundering; drug "
    "trafficking; the Child's Right Act; girl-child education; "
    "women's empowerment; abolition of slavery; secret ballot; "
    "multi-party system; popular sovereignty; state of emergency; "
    "peaceful coexistence; NAFDAC; public opinion; freedom of "
    "information; War Against Indiscipline; responsible "
    "leadership; citizenship as status; law and order; dialogue; "
    "respect for elders; dignity of labour. Scanned against the "
    "whole Civic pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
