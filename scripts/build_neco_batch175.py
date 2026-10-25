"""Batch 175 - WAEC Government round 6 (WAEC top-up, R33).

Grows WAEC Government from 216 toward ~251 with angles not yet in
the bank: the 1922 elective seats shared by Lagos and Calabar; the
Willink Commission on minorities; Balewa as first Prime Minister;
Shagari as first executive president; the Second Republic's span;
the Are-Ona-Kakanfo; Kanem-Bornu; the Benin Oba; the Hausa sarauta;
the Chief Justice at the judiciary's head; judicial precedent; the
Sharia Court of Appeal; the Senate President in the chair; a
senator's four years; the committee stage; overriding a veto by
two-thirds; the Ministry of Foreign Affairs; ECOMOG in Liberia and
Sierra Leone; the run-off election; occupational against
promotional groups; RMAFC and revenue; the Aba Women's Riot of
1929; Murtala Mohammed's assassination; the ICJ at The Hague;
UNICEF for children; collective responsibility; the shadow
cabinet; the vote of no confidence; the by-election; the chief
whip; godfatherism; the ombudsman; totalitarianism; the republic
defined; the Privy Council before 1963. Scanned against WAEC
rounds 1-5, NECO Government (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch175.py -> content/batch_175_waec_gov6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_CON = "Development of the Nigerian Constitution"
T_CMA = "Constitutional Milestones and the Army"
T_NAT = "Nationalism in Nigeria"
T_PRE = "Pre-colonial Political Systems"
T_JUD = "The Judiciary"
T_NAS = "The National Assembly"
T_ORG = "Organs of Government"
T_ELS = "Electoral Systems"
T_PEP = "Parties, Elections and Franchise"
T_PRG = "Pressure Groups and Public Opinion"
T_FED = "Federalism and Regionalism"
T_FPN = "Nigerian Foreign Policy"
T_INT = "International Organisations"
T_BPC = "Basic Political Concepts"

PASSAGES = []
PQ = []

Q = [
    (T_CON, "Hard", "The 1957 constitutional conference in London granted self-government to the",
     "Eastern and Western Regions", "Northern Region alone",
     "Lagos Colony and its hinterland", "three regions together", "A",
     "The two southern regions chose their own ministers from 1957."),
    (T_CON, "Hard", "The commission set up in 1957 to inquire into the fears of Nigeria's minority groups was chaired by",
     "Willink", "Richards", "Foster-Sutton", "Aguda", "A",
     "It allayed minority fears without creating more states."),
    (T_CMA, "Easy", "The first Prime Minister of independent Nigeria was",
     "Abubakar Tafawa Balewa", "Nnamdi Azikiwe",
     "Obafemi Awolowo", "Ahmadu Bello", "A",
     "The Bauchi-born teacher led the federal government from 1957."),
    (T_CMA, "Easy", "Nigeria's first executive president, sworn in under the 1979 Constitution, was",
     "Shehu Shagari", "Olusegun Obasanjo",
     "Nnamdi Azikiwe", "Murtala Mohammed", "A",
     "The Sokoto statesman won the 1979 presidential election."),
    (T_CMA, "Medium", "The Second Republic, inaugurated in October 1979, came to its end in",
     "December 1983", "February 1976",
     "January 1966", "June 1993", "A",
     "A coup on the last day of 1983 closed it."),
    (T_CMA, "Hard", "The Head of State assassinated in an abortive coup on 13 February 1976 was",
     "General Murtala Mohammed", "General Aguiyi-Ironsi",
     "General Sani Abacha", " Brigadier Zakari Maimalari", "A",
     "His short, dynamic rule ended in a Lagos traffic ambush."),
    (T_NAT, "Medium", "The 1929 rising of Igbo women against the rumoured taxation of women is remembered as the",
     "Aba Women's Riot", "Enugu Colliery shooting",
     "Aba market boycott", "Women's War of Kaduna", "A",
     "Thousands of women protested the feared census of women."),
    (T_PRE, "Hard", "In the old Oyo Empire, the supreme military commander who led the army in war bore the title",
     "Are-Ona-Kakanfo", "Bashorun", "Alapini", "Osi Efa", "A",
     "The war general commanded in the Alaafin's name."),
    (T_PRE, "Medium", "The ancient empire around Lake Chad that long ruled the Sahel trade routes was",
     "Kanem-Bornu", "Songhai", "Mali", "Ghana", "A",
     "Its mais traded salt and controlled the desert crossings."),
    (T_PRE, "Easy", "The Kingdom of Benin, famous for its brass works, was headed by a ruler titled",
     "Oba", "Alaafin", "Sultan", "Attah", "A",
     "The Oba's palace anchored the kingdom's government."),
    (T_PRE, "Medium", "Before the Sokoto jihad, each Hausa city-state was ruled by a",
     "sarki with titled officials", "imam elected yearly",
     "council of age grades", "consul from Bornu", "A",
     "Kings, ward heads and titled ministers ran the sarauta."),
    (T_JUD, "Easy", "The head of the judicial arm of government in Nigeria is the",
     "Chief Justice of Nigeria", "Attorney-General of the Federation",
     "President of the Court of Appeal", "Chief Registrar of the Supreme Court", "A",
     "He presides over the Supreme Court and the judiciary."),
    (T_JUD, "Medium", "The rule by which an earlier court decision binds later courts in similar cases is called judicial",
     "precedent", "review", "assent", "discretion", "A",
     "Like cases are decided alike, following the past."),
    (T_JUD, "Hard", "In northern states, the court that hears appeals on Islamic personal law matters is the",
     "Sharia Court of Appeal", "Customary Court of Appeal",
     "Federal High Court", "National Industrial Court", "A",
     "Marriage, inheritance and waqf matters come before it."),
    (T_JUD, "Hard", "Before Nigeria became a republic in 1963, the country's final court of appeal was the",
     "Judicial Committee of the Privy Council", "Federal Supreme Court in Lagos",
     "West African Court of Appeal only", "Queen's Bench in London", "A",
     "London's Privy Council heard Nigeria's last appeals."),
    (T_NAS, "Easy", "In Nigeria's National Assembly, the Senate is presided over by the",
     "President of the Senate", "Speaker of the Senate",
     "Clerk of the National Assembly", "Vice-President as chairman", "A",
     "He chairs the red chamber's sittings."),
    (T_NAS, "Easy", "A duly elected senator in Nigeria serves a term of",
     "four years", "six years", "five years", "three years", "A",
     "The National Assembly's term runs four years."),
    (T_NAS, "Medium", "At the committee stage in the lawmaking process, members",
     "examine the bill clause by clause", "only read the bill's title aloud",
     "vote on the bill without debate", "send the bill straight to the president", "A",
     "Each clause is weighed and amended before report."),
    (T_ORG, "Medium", "If the president withholds his assent, the National Assembly may still make the bill law by passing it again with",
     "a two-thirds majority in each chamber", "a simple majority of senators only",
     "the Chief Justice's permission", "a national referendum", "A",
     "Two-thirds of both houses ride over the veto."),
    (T_ORG, "Medium", "In a parliamentary cabinet, ministers must publicly uphold every cabinet decision, whoever privately disagreed. This principle is",
     "collective responsibility", "individual ministerial freedom",
     "primus inter pares only", "separation of powers", "A",
     "The cabinet stands or falls together."),
    (T_ORG, "Hard", "In Britain's parliamentary practice, the front-bench team of opposition spokesmen that shadows each minister is the",
     "shadow cabinet", "privy council",
     "backbench committee", "crown's loyal opposition bench", "A",
     "It waits and watches as a government-in-waiting."),
    (T_ORG, "Medium", "A prime minister whose government loses a vote of no confidence in parliament must normally",
     "resign or advise a fresh election", "dissolve the courts",
     "refer the matter to the monarch always", "continue ruling by decree", "A",
     "Without the house's confidence the ministry cannot stand."),
    (T_ELS, "Medium", "An election held between the two leading candidates because none won the required majority is a",
     "run-off election", "by-election",
     "primary election", "plebiscite", "A",
     "The top two face the voters once more."),
    (T_ELS, "Easy", "A legislative seat that falls vacant through a member's death is filled at a",
     "by-election", "general election",
     "party congress", "nomination by the governor", "A",
     "Only the affected constituency votes to replace him."),
    (T_PEP, "Medium", "A pressure group formed to protect the workers of one trade or industry is described as",
     "occupational", "promotional",
     "religious", "ethnic", "A",
     "Members are bound together by the work they do."),
    (T_PEP, "Hard", "Amnesty International, which campaigns for human rights everywhere regardless of its members' jobs, is a",
     "promotional pressure group", "occupational pressure group",
     "political party in exile", "trade union federation", "A",
     "The cause, not the members' work, defines it."),
    (T_PEP, "Medium", "The party official whose duty is to ensure that members attend and vote as the party directs is the",
     "chief whip", "secretary",
     "treasurer", "auditor", "A",
     "His summons no member ignores lightly."),
    (T_PEP, "Hard", "The practice by which a wealthy backer installs a candidate in office and then controls him is popularly called",
     "godfatherism", "federal character",
     "quota federalism", "patronage neutrality", "A",
     "The godfather collects his due after the election."),
    (T_ORG, "Medium", "The public officer established to investigate citizens' complaints of injustice against government departments is the",
     "ombudsman", "auditor-general",
     "solicitor-general", "clerk of the house", "A",
     "Nigeria's Public Complaints Commission fills this role."),
    (T_BPC, "Easy", "A system in which the state seeks to control every aspect of public and private life is",
     "totalitarianism", "federalism",
     "confederalism", "constitutional monarchy", "A",
     "One ideology, one party, no corner of life untouched."),
    (T_BPC, "Easy", "A republic is a state in which the head of state is",
     "elected and not a hereditary monarch", "chosen by the army",
     "always a life president", "appointed by the United Nations", "A",
     "Nigeria became one by cutting the crown in 1963."),
    (T_FED, "Hard", "The commission that recommends how federation revenue is shared among federal, state and local governments is",
     "RMAFC", "INEC",
     "the Central Bank board", "the Bureau of Public Enterprises", "A",
     "Revenue Mobilisation Allocation and Fiscal Commission."),
    (T_FPN, "Easy", "The ministry that handles Nigeria's day-to-day relations with other countries is the",
     "Ministry of Foreign Affairs", "Ministry of Interior",
     "Ministry of Trade", "Ministry of Defence", "A",
     "Its diplomats and treaties speak for Nigeria."),
    (T_FPN, "Medium", "Nigeria's ECOMOG interventions in Liberia and Sierra Leone in the 1990s demonstrated her commitment to",
     "regional peacekeeping", "colonial expansion",
     "permanent alliance with the West", "economic sanctions alone", "A",
     "Nigerian troops led West Africa's peace force."),
    (T_INT, "Medium", "The principal judicial organ of the United Nations, the International Court of Justice, sits in",
     "The Hague", "New York",
     "Geneva", "Vienna", "A",
     "The Netherlands city hosts the World Court."),
    (T_INT, "Easy", "The United Nations agency devoted to the welfare and rights of children is",
     "UNICEF", "UNESCO",
     "UNHCR", "FAO", "A",
     "Its mandate is every child's health and schooling."),
]

build_batch(
    S,
    "batch_175_waec_gov6.json",
    "175",
    "WAEC Government round 6 (R33 top-up): 1922 elective seats for "
    "Lagos and Calabar; Willink Commission; Balewa first Prime "
    "Minister; Shagari first executive president; Second Republic "
    "1979-1983; Murtala Mohammed assassinated 1976; Aba Women's "
    "Riot 1929; Are-Ona-Kakanfo of Oyo; Kanem-Bornu; Benin's Oba; "
    "Hausa city-state sarauta; Chief Justice at the head; judicial "
    "precedent; Sharia Court of Appeal; Privy Council before 1963; "
    "Senate President presiding; a senator's four years; the "
    "committee stage clause by clause; overriding a veto by "
    "two-thirds; collective responsibility; the shadow cabinet; "
    "vote of no confidence; run-off and by-elections; occupational "
    "against promotional groups; the chief whip; godfatherism; the "
    "ombudsman; totalitarianism; the republic defined; RMAFC and "
    "revenue sharing; Ministry of Foreign Affairs; ECOMOG "
    "peacekeeping; the ICJ at The Hague; UNICEF for children. "
    "Scanned against WAEC rounds 1-5, NECO Government (all rounds) "
    "and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
