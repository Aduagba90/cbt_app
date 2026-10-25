"""Batch 161 - NECO Civic Education round 5 (NECO top-up, R30).

Grows NECO Civic from 186 toward ~224 with angles not yet in the
bank: the bill's journey (readings, committee stage, assent, veto
override, public hearing, recall); election machinery (petition
tribunals, party registration spread, Boundary Commission); federal
character, quota and national integration; national symbols (flag
colours, coat of arms beasts and bands, NYSC's founding purpose,
FRSC); EFCC vs ICPC and the Code of Conduct Bureau; duties of
citizens (tax, obedience, vigilance); representative democracy, free
election features, majority tyranny; limits on rights; national
consciousness; inter-communal conflict resolution; popular
participation; responsible leadership and followership. Scanned
against NECO rounds 1-4, WAEC Civic (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch161.py -> content/batch_161_neco_civic5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_LEGI = "How Laws Are Made"
T_ELEC = "Elections Further"
T_INT = "Federal Character and Integration"
T_SYM = "National Symbols Further"
T_ANTIG = "Anti-Corruption Further"
T_DUT = "Duties of Citizens"
T_DEM = "Democracy Further"
T_LEAD = "Leadership and Followership"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- how laws are made
    (T_LEGI, "Medium", "A proposed law laid before the legislature is called a",
     "bill", "decree", "gazette", "writ", "A",
     "Until passed, it is only a proposal."),
    (T_LEGI, "Medium", "The stage at which a bill's title is merely read out, without debate, is the",
     "first reading", "second reading", "committee stage", "third reading", "A",
     "Its name is announced to the house."),
    (T_LEGI, "Hard", "The stage where members examine a bill clause by clause and amend it is the",
     "committee stage", "first reading", "second reading", "gazetting", "A",
     "Every comma faces the knife."),
    (T_LEGI, "Hard", "A public hearing on a bill is held chiefly to",
     "gather citizens' views before passage", "punish opponents of the bill", "raise money for parties", "elect new leaders", "A",
     "The people whisper into the law."),
    (T_LEGI, "Medium", "A bill passed by both chambers becomes law only after the president's",
     "assent", "verdict", "decree", " pardon", "A",
     "His signature is the door out."),
    (T_LEGI, "Hard", "The president withholds his assent, yet both chambers repass the bill by two-thirds. The bill",
     "becomes law without him", "dies at once", "goes to the courts only", "waits for a new president", "A",
     "The override is the Assembly's power."),
    (T_LEGI, "Hard", "The process by which registered voters can remove a non-performing legislator before term's end is",
     "recall", "impeachment", "referendum", "plebiscite", "A",
     "Signatures can unseat him."),

    # ------------------------------------------------------------- elections
    (T_ELEC, "Medium", "A candidate who believes the count was crooked takes the matter to the",
     "election petition tribunal", "police council", "council of chiefs", "party's secretariat", "A",
     "The courtroom follows the count."),
    (T_ELEC, "Hard", "A new political association applying for INEC registration will be rejected unless it can demonstrate",
     "national spread of support", "a wealthy foreign sponsor", "its own radio licence", "a serving governor", "A",
     "National spread is the entry gate."),
    (T_ELEC, "Hard", "Constituency boundaries in Nigeria are drawn not by INEC but by the",
     "Boundary Commission", "Central Bank", "police command", "senate committee alone", "A",
     "INEC runs polls; another body draws maps."),

    # ------------------------------------------------------------- integration
    (T_INT, "Hard", "Appointments to federal posts reflecting all parts of the country obey the principle of",
     "federal character", "seniority rule", "rotation of parties", "quota of age", "A",
     "Every zone gets a chair at the table."),
    (T_INT, "Medium", "Admitting students to unity schools so that each state fills a share of places aims at",
     "national integration", "cheaper schooling", "private profit", "longer courses", "A",
     "Classrooms mix the nation."),
    (T_INT, "Medium", "Deliberate policies that bind Nigerians of all tongues into one loyal people pursue",
     "national consciousness", "ethnic loyalty", "party supremacy", "religious bond only", "A",
     "One flag above many tongues."),

    # ------------------------------------------------------------- symbols
    (T_SYM, "Medium", "When Taiwo Akinkunmi designed the flag in 1959, the green he chose spoke of Nigeria's",
     "farms and forests", "bank vaults and money", "army barracks", "ocean riches", "A",
     "Green fields feed the nation."),
    (T_SYM, "Hard", "On the coat of arms, the eagle above the shield stands for",
     "Nigeria's strength", "the morning sun", "peace and plenty", "long life", "A",
     "Pride rides on the coat's crest."),
    (T_SYM, "Hard", "The two silver wavy bands crossing the black shield recall the rivers",
     "Niger and Benue", "Ogun and Osun", "Kaduna and Sokoto", "Niger and Nile", "A",
     "Their meeting is drawn on the arms."),
    (T_SYM, "Hard", "Posting graduates to serve in states far from home, the corps founded in 1973 set out to",
     "reconcile Nigerians after the war", "train soldiers for battle", "replace the police", "staff embassies", "A",
     "Graduates bridge the divides."),
    (T_SYM, "Medium", "FRSC marshals flag down over-speeding lorries because their commission exists chiefly to",
     "reduce road accidents", "collect highway tolls", "guard oil pipelines", "run motor parks", "A",
     "Its marshals patrol the highways."),

    # ------------------------------------------------------------- anti-corruption
    (T_ANTIG, "Hard", "The agency that chiefly investigates economic and financial crimes like advance-fee fraud is the",
     "EFCC", "ICPC", "NAFDAC", "SON", "A",
     "Its brief is the money crime."),
    (T_ANTIG, "Hard", "Bribery and gratification in the civil service fall chiefly under the mandate of the",
     "ICPC", "EFCC", "FRSC", "NYSC", "A",
     "The commission pursues the quiet graft."),
    (T_ANTIG, "Hard", "Senior public officers' asset declarations are received by the",
     "Code of Conduct Bureau", "Central Bank", "Stock Exchange", "civil service commission", "A",
     "The form is filed before office."),

    # ------------------------------------------------------------- duties
    (T_DUT, "Medium", "Declaring one's honest income and paying the tax due is a citizen's duty of",
     "taxation obedience", "optional charity", "party funding", "community service", "A",
     "Schools and roads drink that money."),
    (T_DUT, "Medium", "Obeying lawful traffic rules, even at midnight with no officer in sight, shows the duty of",
     "obedience to law", "fear of punishment", "personal convenience", "party loyalty", "A",
     "The law watches without eyes."),
    (T_DUT, "Hard", "Reporting a broken pipeline or strange movement to the authorities is the civic duty of",
     "vigilance", "neutrality", "anonymity", "delegation", "A",
     "The alert citizen guards all."),
    (T_DUT, "Medium", "Voting in elections, though voluntary in law, is widely treated as a citizen's duty of",
     "political participation", "tax compliance", "judicial service", "military service", "A",
     "Silence surrenders the choice."),

    # ------------------------------------------------------------- democracy further
    (T_DEM, "Medium", "In Nigeria's representative democracy, laws are made chiefly by",
     "elected legislators", "all adults directly", "the courts", "traditional rulers", "A",
     "Chosen voices speak for all."),
    (T_DEM, "Hard", "A free and fair election requires, among other things, that voters choose",
     "without fear or bribery", "only at night", "under army supervision only", "by open show of hands", "A",
     "The secret ballot guards the conscience."),
    (T_DEM, "Hard", "Unlimited majority rule that crushes a minority turns into",
     "tyranny of the majority", "pure federalism", "balanced cabinet", "constitutional monarchy", "A",
     "Numbers alone can also wound."),
    (T_DEM, "Hard", "Your right to move freely may be lawfully restricted during",
     "a declared emergency", "your own wedding", "a football season", "a market day", "A",
     "Public danger narrows freedom."),

    # ------------------------------------------------------------- leadership & followership
    (T_LEAD, "Medium", "A leader who accounts openly for public money and decisions demonstrates",
     "accountability", "impunity", "popularity", "seniority", "A",
     "The books face the people."),
    (T_LEAD, "Hard", "Followers who praise every act of a leader, right or wrong, abandon their duty of",
     "constructive criticism", "blind obedience", "quiet sabotage", "total silence", "A",
     "Truth keeps power honest."),
    (T_LEAD, "Medium", "Obeying a leader's LAWFUL instructions while rejecting illegal ones defines followership that is",
     "responsible", "rebellious", "slavish", "indifferent", "A",
     "Law is the line between the two."),
    (T_LEAD, "Medium", "Community members coming out to repair the ward's only bridge show civic",
     "participation", "resignation", "protest", "litigation", "A",
     "Hands, not complaints, fix the crossing."),
    (T_LEAD, "Hard", "When two communities quarrel over farmland, the settlement approach that preserves peace best is",
     "mediation by a neutral body", "reprisal attacks", "endless litigation only", "army occupation", "A",
     "A neutral table cools hot blood."),
    (T_LEAD, "Medium", "The greatest enemy of popular participation in governance is widespread",
     "political apathy", "curiosity", "debate", "schooling", "A",
     "The absent voter empowers the few."),
]

build_batch(
    S,
    "batch_161_neco_civic5.json",
    "161",
    "NECO Civic round 5 (R30 top-up): bill readings, committee stage, "
    "public hearing, assent, two-thirds override, recall; petition "
    "tribunals, party registration spread, Boundary Commission; federal "
    "character, unity-school quota, national consciousness; flag's "
    "green, eagle, Niger-Benue bands, NYSC 1973, FRSC; EFCC vs ICPC "
    "mandates, Code of Conduct; tax and obedience duties, vigilance, "
    "voting; representative lawmaking, secret ballot, majority "
    "tyranny, emergency limits; accountability, constructive "
    "criticism, lawful followership, community participation, "
    "mediation of land quarrels, apathy as the enemy. Scanned against "
    "NECO rounds 1-4, WAEC Civic (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
