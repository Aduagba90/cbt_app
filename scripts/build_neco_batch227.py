"""Batch 227 - NECO Government round 7 (NECO top-up, R46).

Grows NECO Government from 252 toward ~277 with angles verified
absent from the whole Government pool (1,349 items across JAMB, WAEC
and NECO): onshore-offshore dichotomy; joint session; VP completes
term; underage voting; 2014 national conference; indigene-settler;
Democracy Day; features of a state; committee system; political
apathy; habeas corpus; criminal vs civil law; national honours;
Oputa Panel; commission of inquiry; fuel subsidy; notice of
election; campaign spending limits; fiscal vs monetary policy;
inconclusive/supplementary election; service chiefs; independent
candidate; constituent assembly; Resident Electoral Commissioner;
red chamber. Checked and avoided (already banked): carpet-crossing,
census controversies, Aburi, derivation, three Rs, Ghana-must-go,
Decree 34, ASUU, godfatherism, Electoral Act 2022, technical aid,
quorum, Speaker items, Senate presiding officer, state of
emergency, referendum, public opinion, foreign policy objectives
(Section 19), SGF/Head of Service, EFCC, Land Use Decree, oath of
office, habeas-as-option in judicial review items, local government
autonomy (July 2024), restructuring/true federalism, Umar-Hijri
calendar (multiple), Badr-to-Tabuk battles, muakhah, Bahira,
Halimah, Hilf al-Fudul, Hudaybiyyah, Aqabah, Mi'raj.

    python3 scripts/build_neco_batch227.py -> content/batch_227_neco_gov7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_FED = "Federalism and Power Division"
T_PARL = "Parliamentary Machinery"
T_EXEC = "The Executive Further"
T_ELEC = "Electoral Systems"
T_POL = "Political Parties and Elections"
T_CONC = "Basic Political Concepts"
T_ORG = "Organs of Government"
T_CONST = "Constitutions and Constitutionalism"
T_NIG = "Nigerian Constitutions and History"
T_LOCG = "Local Government"
T_JUD = "Structures of Power"
T_NAT = "Political Life"

PASSAGES = []
PQ = []

Q = [
    (T_FED, "Hard", "The rule that separates oil revenue into what is earned from wells on land and what is earned from wells at sea, for sharing purposes, is the",
     "onshore-offshore dichotomy", "open-door doctrine",
     "offshore allocation bar", "onshore savings rule", "A",
     "Where the well sits decides which pocket fills."),
    (T_PARL, "Medium", "The occasion on which both the Senate and the House of Representatives sit together in one chamber, as when the President presents the budget, is called a",
     "joint session", "joint committee",
     "congress of parties", "closed sitting", "A",
     "Both chambers meet under one roof, one presiding officer."),
    (T_EXEC, "Medium", "If a President dies in office, resigns or is removed, the constitution provides that the Vice President",
     "acts for ninety days at most", "completes the remaining term of office",
     "only oversees a fresh election", "hands over to the Senate President", "B",
     "The deputy steps in and serves out the years."),
    (T_ELEC, "Easy", "Registering a child of fifteen as a voter, or allowing such a child to vote, is an electoral offence known as",
     "underage voting", "multiple voting",
     "spoil-ballot casting", "proxy voting", "A",
     "The voter is younger than the law allows."),
    (T_POL, "Medium", "The national conference convoked in 2014 by President Goodluck Jonathan, at which delegates from all parts of Nigeria debated the country's problems, is commonly called the",
     "2014 National Conference", "Aburi conference",
     "Constituent Assembly of 2014", "Sovereign Conference of 1966", "A",
     "Its members met for months and produced a long report."),
    (T_NAT, "Medium", "Tensions that arise in some Nigerian states between those regarded as original inhabitants of an area and those regarded as later settlers are described as the",
     "indigene-settler question", "insider-outsider quota",
     "electoral indigene rule", "residency franchise issue", "A",
     "Birthplace divides citizens into two classes."),
    (T_NAT, "Easy", "Since 2019, Nigeria's Democracy Day has been marked on the twelfth of June in honour of the annulled 1993 presidential election. Before then it was marked on",
     "29 May", "1 October",
     "1 January", "27 May", "A",
     "The date moved to remember a famous election."),
    (T_CONC, "Medium", "A politically organised community with a defined territory, a government, a population and sovereignty is called",
     "a state", "a society",
     "a nation", "an association", "A",
     "All four marks together make it one."),
    (T_PARL, "Medium", "Because the whole House cannot examine every matter in detail, bills and investigations are first handled by smaller groups of members called",
     "committees", "caucuses",
     "commissions of inquiry", "courts of the House", "A",
     "They do the detailed work and report to the whole House."),
    (T_POL, "Medium", "The situation in which citizens show indifference to politics — refusing to vote, join parties or follow public affairs — is called",
     "political apathy", "political asylum",
     "political pluralism", "political patronage", "A",
     "The people turn their backs on public life."),
    (T_JUD, "Hard", "The court order directing that a person held in detention be brought before the court, so that the reason for holding him may be shown, is called",
     "habeas corpus", "mandamus",
     "certiorari", "injunction", "A",
     "'Produce the body' is the old meaning of its Latin name."),
    (T_ORG, "Medium", "The branch of law that deals with offences against the state, where the state prosecutes and punishment may include imprisonment, is",
     "criminal law", "civil law",
     "company law", " customary law", "A",
     "The whole society is treated as the wronged party."),
    (T_NAT, "Easy", "The awards that the government of Nigeria confers on citizens and friends of the country for outstanding service, such as GCON and CFR, are called",
     "national honours", "national awards of courts",
     "civil service medals", "party merit awards", "A",
     "They are conferred on special days by the President."),
    (T_NIG, "Hard", "The commission headed by Justice Chukwudifu Oputa, set up in 1999 to hear complaints of past human rights abuses, is popularly called the",
     "Oputa Panel", "Uwais Committee",
     "Justice Ayo Salami Panel", "Murtala Purge Board", "A",
     "Its public sittings aired the wounds of the past."),
    (T_ORG, "Medium", "A body formally set up by government, with a judge or respected figure at its head, to inquire into a matter of public concern and report its findings, is a",
     "commission of inquiry", "commission on sales",
     "house committee", "public tribunal of trade", "A",
     "It gathers evidence and reports to the government."),
    (T_NIG, "Medium", "The payment the government makes to keep the pump price of petrol below its real cost, so that citizens buy it cheaper, is called a",
     "subsidy", "tariff",
     "levy", "toll", "A",
     "The treasury quietly pays part of the price."),
    (T_ELEC, "Medium", "The timetable and formal notice of election, fixing the dates for party primaries, campaigns, and the election days themselves, is issued by",
     "the electoral commission", "the Council of State",
     "the political parties jointly", "the courts", "A",
     "Every step of the election is dated from it."),
    (T_ELEC, "Medium", "The law places an upper limit on the amount of money a candidate may lawfully spend on his campaign. This limit exists to",
     "check money's influence on politics", "raise the parties' income",
     "shorten the campaign period", "keep journalists fully employed", "A",
     "Wealth alone should not buy an office."),
    (T_NIG, "Medium", "When a presidential election fails to produce a clear winner and the law requires a second election between the leading candidates, the second election is called a",
     "run-off election", "by-election",
     "general election", "primary election", "A",
     "The top two face the voters again."),
    (T_ELEC, "Medium", "An election that the commission declares neither concluded nor won, and which is later completed in the affected polling units, is said to be",
     "inconclusive", "nulled and abandoned",
     "postponed for a decade", "reversed by the Senate", "A",
     "The unfinished parts are voted another day."),
    (T_EXEC, "Medium", "The Chief of Defence Staff and the other heads of the armed formations, collectively called the service chiefs, are appointed by the President",
     "subject to confirmation by the National Assembly", "with the approval of INEC only",
     "by the Council of State alone", "at the sole discretion of the judiciary", "A",
     "The lawmakers must nod before they take office."),
    (T_POL, "Easy", "A candidate who contests an election without belonging to or being sponsored by any political party is called",
     "an independent candidate", "an interim candidate",
     "a nominated trustee", "a consensus candidate", "A",
     "He carries no party's flag."),
    (T_CONST, "Medium", "A body of persons specially elected or appointed for the single purpose of drawing up a new constitution for a country is called a",
     "constituent assembly", "constitutional court",
     "council of elders", "caretaker committee", "A",
     "It exists to write the country's basic law."),
    (T_ELEC, "Easy", "The official of the electoral commission who takes charge of the conduct of elections throughout one state, under the national chairman, is the",
     "Resident Electoral Commissioner", "Returning Officer",
     "State Party Chairman", "Chief Press Secretary", "A",
     "He superintends every polling unit in his state."),
    (T_PARL, "Easy", "Because the Senate chamber in the National Assembly is furnished in red, the Senate is often nicknamed the",
     "red chamber", "green chamber",
     "upper green house", "blue chamber", "A",
     "Its seats and carpets carry the deep colour."),
]

build_batch(
    S,
    "batch_227_neco_gov7.json",
    "227",
    "NECO Government round 7 (R46 top-up): onshore-offshore "
    "dichotomy; joint session; VP completes the term; underage "
    "voting; 2014 National Conference; indigene-settler question; "
    "Democracy Day moved to June 12; features of a state; committee "
    "system; political apathy; habeas corpus; criminal vs civil law; "
    "national honours; Oputa Panel; commission of inquiry; fuel "
    "subsidy; notice of election/timetable; campaign spending "
    "limits; run-off election; inconclusive and supplementary "
    "elections; service chiefs' confirmation; independent candidate; "
    "constituent assembly; Resident Electoral Commissioner; red "
    "chamber. Scanned against the whole Government pool (JAMB, WAEC "
    "and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
