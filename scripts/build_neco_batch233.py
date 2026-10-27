"""Batch 233 - WAEC Government round 8 (WAEC top-up, R47).

Grows WAEC Government from 274 toward ~299 with angles verified
absent from the whole Government pool (1,374 items across JAMB, WAEC
and NECO): Ujamaa (Nyerere); Universal Declaration of Human Rights;
Universal Basic Education; extradition; Council of State;
supplementary budget; functions of local government; good
neighbourliness; political thuggery; ethnic politics; constituted
authority; backbencher; concession; public-private partnership;
refugee; achievements of military rule; the 1975 bloodless coup;
the 1976 Dimka coup; e-governance; Treasury Single Account;
retrenchment; fake news; special advisers; the cabinet; minimum age
for President (35). Checked and avoided (already banked): Imoudu
strike item, Udoji Commission, amnesty programme/asylum option,
Amnesty International, Enahoro's motions (x2), Willink Commission
(x2), cession of Lagos 1861, interprets-the-law organ item,
councillors-represent-wards, economic and citizen diplomacy, Senate
109/House 360 items, bicameral/unicameral, four-year term, elective
principle, Clifford-to-Lyttleton family, self-government motions,
republic 1963, Governor-General family, Balewa/Shagari items,
Macaulay, Zikist, Berlin Conference, assimilation, protectorates,
decrees, Chief Justice family, Sharia Court of Appeal options,
highest-court family, independence-of-judiciary items, freedom of
press, one-party system, ballot family, polling unit, opposition
role, ministerial confirmation (x2), caucus, patronage, collective
responsibility, green chamber (x2), OAU/AU, General Assembly,
Security Council/veto, OPEC, federation account, IGR, budget family,
civil service commission, merit/spoils, impartiality, chairman
family, council of chiefs, theocracy, means of production, permanent
secretary, human-rights bodies in civic pool (NHRC banked in Civic
R45 - avoided as cross-subject twin).

    python3 scripts/build_neco_batch233.py -> content/batch_233_waec_gov8.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CONC = "Basic Political Concepts"
T_INTL = "International Organisations"
T_EXEC = "The Executive"
T_FPI = "Nigerian Foreign Policy"
T_ORG = "Organs of Government"
T_NASS = "The National Assembly"
T_LOCG = "Local Government"
T_ELEC = "Electoral Systems"
T_PARTY = "Political Parties and Party Systems"
T_MIL = "The Military in Nigerian Politics"
T_CIV = "The Civil Service"
T_MEDIA = "The Media"

PASSAGES = []
PQ = []

Q = [
    (T_CONC, "Hard", "The African socialist policy of Julius Nyerere of Tanzania, under which people were settled in planned villages and worked the land together, was called",
     "Ujamaa", "Ubuntu",
     "Harambee", "Pan-Africanism", "A",
     "The Swahili word for familyhood named the village."),
    (T_INTL, "Medium", "The United Nations document of 1948 which sets out the basic rights that every person in the world should enjoy, such as life, liberty and freedom of belief, is the",
     "Universal Declaration of Human Rights", "United Nations Charter of Rights",
     "Geneva Convention on War", "Helsinki Accord", "A",
     "Ten December 1948 gave the world its rights charter."),
    (T_EXEC, "Medium", "The federal programme which guarantees nine years of free and compulsory schooling for every Nigerian child, from primary to junior secondary, is the",
     "Universal Basic Education programme", "Universal Adult Suffrage scheme",
     "National Youth Service Corps", "Mass Literacy Campaign", "A",
     "Every child's early schooling rests on its promise."),
    (T_FPI, "Hard", "The legal process by which a person accused of a crime in one country is handed over by another country to face trial is called",
     "extradition", "expatriation",
     "expulsion", "extra-territoriality", "A",
     "The fugitive is sent home to answer."),
    (T_ORG, "Medium", "The advisory body of former presidents, former chief justices and state governors which the President consults on matters of national importance is the",
     "Council of State", "Council of Ministers",
     "National Council of Nigerian Citizens", "Body of Benchers", "A",
     "Old heads counsel the sitting one."),
    (T_NASS, "Medium", "When the money approved in the main budget runs out before the year ends and government needs more, the President presents to the National Assembly a",
     "supplementary budget", "supplementary register",
     "supplemental petition", "second republic budget", "A",
     "The first envelope proved too small."),
    (T_LOCG, "Easy", "Maintaining markets and motor parks, registering births and deaths, and keeping local roads and drains clean are all",
     "functions of local government", "functions of the Senate",
     "exclusive federal duties", "functions of embassies", "A",
     "The work closest to the people's doorstep."),
    (T_FPI, "Easy", "Nigeria's policy of maintaining friendly and cooperative relations with Benin, Niger, Chad, Cameroon and other nearby states is called",
     "good neighbourliness", "the big-brother doctrine",
     "the iron-curtain policy", "containment", "A",
     "No wall stands between good neighbours."),
    (T_ELEC, "Easy", "Politicians who hire rough young men to snatch ballot boxes, beat opponents and scare voters at polling units are guilty of using",
     "political thuggery", "political patronage",
     "political socialisation", "political lobbying", "A",
     "The gun is brought where the vote should speak."),
    (T_PARTY, "Medium", "The practice of choosing candidates and supporters for office on the basis of their ethnic group or region, rather than their ability, is called",
     "ethnic politics", "party discipline",
     "party realignment", "elite consensus", "A",
     "The tribe votes before the man is seen."),
    (T_CONC, "Easy", "Any person or body of persons vested with the legitimate power and authority to govern a community — whether a president, a governor or a school principal — is a",
     "constituted authority", "constitutional lawyer",
     "constituent assembly", "institution of chartered status", "A",
     "Legitimate power, rightly vested in an office."),
    (T_NASS, "Medium", "In the British parliament from which Nigeria borrowed much, an ordinary member who sits behind the front benches and holds no ministerial or shadow office is called a",
     "backbencher", "frontbencher",
     "crossbencher by office", "bench clerk", "A",
     "He sits at the back and votes with his conscience."),
    (T_MIL, "Hard", "Under the privatisation reforms, the handing over of a public enterprise to a private company to run for a fixed period, while the state still owns it, is called",
     "concession", "confiscation",
     "conscription", "consolidation", "A",
     "The keys are lent; the title stays with the state."),
    (T_MIL, "Medium", "An arrangement in which a government and private investors jointly finance and run a project such as a toll road or a power plant, sharing cost, risk and profit, is",
     "a public-private partnership", "a public confession of projects",
     "a private seizure of public funds", "a party-political partnership", "A",
     "Public purpose and private purse build together."),
    (T_INTL, "Medium", "A person who has been forced to flee his own country because of war, persecution or disaster and seeks safety in another country is a",
     "refugee", "defector",
     "diplomat", "deportee", "A",
     "He carries his home in his memory."),
    (T_MIL, "Medium", "Of the following, one commonly cited achievement of military regimes in Nigeria is that they",
     "created states and built key works", "abolished the armed forces altogether",
     "conducted general elections every year", "ended every foreign debt owed", "A",
     "The barracks also drew lines on the map."),
    (T_MIL, "Medium", "The bloodless coup of 29 July 1975, in which General Yakubon Gowon was removed while away at an OAU summit in Kampala, brought to power",
     "General Murtala Mohammed", "General Olusegun Obasanjo only",
     "General Muhammadu Buhari", "Major Chukwuma Nzeogwu", "A",
     "Kampala heard the news before Lagos did."),
    (T_MIL, "Hard", "The failed coup of 13 February 1976, in which General Murtala Mohammed was assassinated on his way to work, was led by",
     "Lt-Colonel Buka Suka Dimka", "Major Gideon Orkar",
     "Major Kaduna Nzeogwu", "Colonel Joe Nanven Garba", "A",
     "The Dodan Barracks plot failed within hours."),
    (T_CIV, "Medium", "The delivery of government services and information through electronic means, such as online portals for licences, taxes and records, is called",
     "e-governance", "e-commerce",
     "e-journalism", "e-parade", "A",
     "The queue moves from the counter to the screen."),
    (T_CIV, "Hard", "The policy under which all government income is paid into one consolidated account at the Central Bank, ending the era of scattered accounts in many banks, is the",
     "Treasury Single Account", "Tax Sharing Account",
     "Total Savings Arrangement", "Trade Settlement Account", "A",
     "One pot now holds the government's money."),
    (T_CIV, "Medium", "The deliberate reduction of the size of the public service, usually by laying off workers declared surplus to need, is called",
     "retrenchment", "recruitment",
     "secondment", "staff validation", "A",
     "The pay roll grows shorter; the burden lighter."),
    (T_MEDIA, "Medium", "False stories, doctored pictures and manufactured reports spread rapidly on social media to deceive the public are collectively called",
     "fake news", "breaking news",
     "feature stories", "editorials", "A",
     "It wears the dress of news but speaks with a forked tongue."),
    (T_EXEC, "Medium", "Officials appointed by the President or a governor, outside the civil service, to give expert political advice in their offices are called",
     "special advisers", "special constables",
     "statutory officers", "state counsellors", "A",
     "They serve at the pleasure of their principal."),
    (T_EXEC, "Easy", "In Nigeria's presidential system, the body of ministers appointed by the President to head the various ministries and assist him in running the government is collectively called the",
     "cabinet", "caucus",
     "presidium", "council of elders", "A",
     "Each member holds one portfolio of the nation's work."),
    (T_EXEC, "Easy", "For a person to qualify to be elected President of Nigeria, the constitution requires, among other things, that the person must have attained the age of",
     "thirty-five years", "thirty years",
     "forty years", "twenty-five years", "A",
     "The same age opens the Senate's door."),
]

build_batch(
    S,
    "batch_233_waec_gov8.json",
    "233",
    "WAEC Government round 8 (R47 top-up): Ujamaa; Universal "
    "Declaration of Human Rights; Universal Basic Education; "
    "extradition; Council of State; supplementary budget; functions "
    "of local government; good neighbourliness; political thuggery; "
    "ethnic politics; constituted authority; backbencher; "
    "concession; public-private partnership; refugee; achievements "
    "of military rule; the 1975 bloodless coup; the 1976 Dimka coup; "
    "e-governance; Treasury Single Account; retrenchment; fake "
    "news; special advisers; the cabinet; minimum age of thirty-five "
    "for President. Scanned against the whole Government pool (JAMB, "
    "WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
