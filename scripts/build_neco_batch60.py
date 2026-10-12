"""Batch 060 - NECO Government top-up (round 2).

Grows the Government bank from 80 to 150 items so students get two full
practice papers without repeats. New angles: de facto/de jure, political
socialisation, confederation vs federation, delegated legislation,
impeachment, NYM and Zikist Movement, state creation, SIEC, ECOMOG,
OPEC membership, UNICEF. Near-dup scanned against JAMB, WAEC and the
existing NECO bank (round-1 items included).

    python3 scripts/build_neco_batch60.py -> content/batch_060_neco_government2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Government"

T_SCOPE = "Meaning and Scope of Government"
T_CONCEPT = "Basic Political Concepts"
T_CONST = "Constitutions"
T_ORGANS = "Organs of Government"
T_PARTY = "Political Parties and Party Systems"
T_PRESS = "Pressure Groups and Public Opinion"
T_ELECT = "Electoral Systems"
T_NIGCON = "Development of the Nigerian Constitution"
T_COLON = "Colonial Administration"
T_NAT = "Nationalism in Nigeria"
T_FED = "Federalism and Regionalism"
T_LOCAL = "Local Government"
T_CIVIL = "The Civil Service"
T_PUB = "Public Corporations"
T_MIL = "The Military in Nigerian Politics"
T_FOREIGN = "Nigerian Foreign Policy"
T_INT = "International Organisations"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------- scope of govt
    (T_SCOPE, "Medium", "Sovereignty means that a state is",
     "supreme over its territory", "poorer than its neighbours",
     "part of an empire", "ruled by elders", "A",
     "A sovereign state answers to no higher earthly authority."),
    (T_SCOPE, "Hard", "A de facto government is one that",
     "holds power without legal recognition", "is elected in a free poll",
     "is approved by courts", "rules only in the North", "A",
     "'De facto' means in fact: it rules whether or not law approves."),
    (T_SCOPE, "Hard", "A nation differs from a state because a nation is",
     "a people of shared feeling", "always a legal entity",
     "the same as a province", "made up of officials", "A",
     "Nations are communities of feeling; states are legal structures."),
    (T_SCOPE, "Medium", "A government that is under the constitution and not above it is described as",
     "constitutional", "revolutionary", "military", "hereditary", "A",
     "Constitutional government operates within legal limits."),

    # ------------------------------------------------------- political concepts
    (T_CONCEPT, "Hard", "The process by which citizens acquire their political beliefs and attitudes is",
     "political socialisation", "political alienation",
     "gerrymandering", "impeachment", "A",
     "Family, school and media socialise citizens into politics."),
    (T_CONCEPT, "Easy", "Franchise means the",
     "right to vote in elections", "duty to pay taxes",
     "power to make laws", "right to own property", "A",
     "The franchise is the citizen's voting right."),
    (T_CONCEPT, "Medium", "In a direct democracy, decisions are taken by",
     "the citizens themselves", "elected representatives alone",
     "traditional rulers", "the judiciary", "A",
     "Ancient Athens practised direct citizen decision-making."),
    (T_CONCEPT, "Medium", "Rule by a small powerful group is called",
     "oligarchy", "democracy", "monarchy", "republic", "A",
     "Oligos means few: a few people hold power."),
    (T_CONCEPT, "Hard", "A confederation differs from a federation because in a confederation the",
     "member units keep their sovereignty", "centre is all-powerful",
     "units have no governments", "people elect the centre", "A",
     "Confederations retain ultimate power in the component units."),

    # ------------------------------------------------------------- constitutions
    (T_CONST, "Medium", "A constitution is described as flexible when it can be amended by",
     "the ordinary lawmaking process", "a military coup only",
     "the courts alone", "foreign powers", "A",
     "Britain's constitution changes by simple statute."),
    (T_CONST, "Medium", "The Nigerian constitution draws its authority from",
     "the people of Nigeria", "the Queen of England",
     "the armed forces", "registered parties", "A",
     "'We the people' opens the 1999 Constitution."),
    (T_CONST, "Hard", "A provision is said to be entrenched when it",
     "cannot be altered by ordinary law", "is written in English",
     "appears in the gazette", "is approved by lawyers", "A",
     "Entrenched clauses need special amendment procedures."),
    (T_CONST, "Medium", "Constitutionalism means that government must be conducted according to",
     "the constitution's limits", "the ruler's wishes",
     "military decrees", "party manifestos", "A",
     "Power is exercised within constitutional limits."),

    # ------------------------------------------------------------------- organs
    (T_ORGANS, "Easy", "The National Assembly of Nigeria consists of the Senate and the",
     "House of Representatives", "House of Lords",
     "Council of State", "Federal Executive Council", "A",
     "Nigeria's legislature is bicameral at the federal level."),
    (T_ORGANS, "Medium", "A legislature made up of two chambers is described as",
     "bicameral", "unicameral", "confederal", "unitary", "A",
     "Bi means two: two houses make the legislature."),
    (T_ORGANS, "Medium", "Before a passed bill becomes law in Nigeria, the President must",
     "give presidential assent", "read it on television",
     "hand it to the courts", "print the ballot papers", "A",
     "Assent turns a bill into an act; the veto can be overridden."),
    (T_ORGANS, "Medium", "Nigeria's executive president combines the offices of",
     "head of state and government", "senator and judge",
     "governor and minister", "speaker and clerk", "A",
     "The presidential system merges both roles in one person."),
    (T_ORGANS, "Hard", "The formal removal of a Nigerian president for gross misconduct is called",
     "impeachment", "renunciation", "prorogation",
     "dissolution of parliament", "A",
     "Impeachment follows the constitution's two-thirds procedure."),
    (T_ORGANS, "Hard", "Rules made by ministers under powers granted by an act of parliament are called",
     "delegated legislation", "constitutional amendments",
     "judicial precedents", "treaties", "A",
     "Parliament delegates detail-making to ministers and agencies."),

    # ---------------------------------------------------------------- parties
    (T_PARTY, "Easy", "The document that sets out a political party's programmes and promises is its",
     "manifesto", "constitution", "gazette", "register", "A",
     "Voters judge parties largely by their manifestos."),
    (T_PARTY, "Medium", "The main function of political parties during elections is to",
     "present candidates to the voters", "count the ballots alone",
     "pay the electors", "audit INEC accounts", "A",
     "Parties select and present candidates for public office."),
    (T_PARTY, "Hard", "The two political parties registered for the 1992-93 transition under Babangida were the",
     "SDP and NRC", "NPN and UPN", "NCNC and NPC",
     "AG and NEPU", "A",
     "Only the Social Democratic Party and National Republican Convention were allowed."),
    (T_PARTY, "Medium", "Allied parties sharing power after none wins an outright majority have formed a",
     "coalition government", "caretaker committee",
     "military council", "royal court", "A",
     "Partners join forces to command a parliamentary majority."),
    (T_PARTY, "Easy", "A legislator who abandons the party under which he was elected for another party is said to have",
     "defected", "dissolved", "abstained", "recounted", "A",
     "Cross-carpeting or defection switches party allegiance."),

    # ----------------------------------------------------------- pressure groups
    (T_PRESS, "Medium", "The Civil Liberties Organisation, which campaigns for human rights, is an example of a",
     "promotional pressure group", "political party",
     "public corporation", "trade mission", "A",
     "Promotional groups pursue causes benefiting society at large."),
    (T_PRESS, "Medium", "An association of medical doctors pressing government for better hospital funding is best classified as a",
     "sectional pressure group", "promotional group",
     "political party", "civil service union", "A",
     "Sectional groups defend their members' occupational interests."),
    (T_PRESS, "Easy", "Public opinion refers to the",
     "prevailing views of citizens on public issues", "editorial policy of newspapers",
     "verdict of the courts", "advice of elders", "A",
     "Government policy is shaped by the climate of public views."),
    (T_PRESS, "Medium", "A group that uses protests, memoranda and court suits but never contests elections is a",
     "pressure group", "political party", "parastatal",
     "congressional committee", "A",
     "Influence without seeking office defines pressure groups."),

    # ----------------------------------------------------------------- elections
    (T_ELECT, "Easy", "The register of voters contains the names of",
     "citizens registered to vote", "all elected officers",
     "party chairmen", "civil servants", "A",
     "Only persons on the register may vote on election day."),
    (T_ELECT, "Medium", "A run-off election becomes necessary when",
     "no candidate wins the required majority", "voters boycott the poll",
     "results are announced late", "parties merge", "A",
     "The top candidates contest again to produce a winner."),
    (T_ELECT, "Medium", "Snatching of ballot boxes during an election is an act of",
     "electoral malpractice", "civil disobedience",
     "lawful protest", "party discipline", "A",
     "Violence and theft of materials invalidate honest elections."),
    (T_ELECT, "Medium", "The card reader was introduced into Nigerian elections mainly to",
     "verify voters' fingerprints", "count ballot papers faster",
     "print results sheets", "pay ad-hoc staff", "A",
     "Biometric verification cut multiple voting and impersonation."),

    # --------------------------------------------------- Nigerian constitutions
    (T_NIGCON, "Medium", "The elective seats created under the Clifford Constitution of 1922 were for",
     "Lagos and Calabar", "Kano and Ibadan",
     "Enugu and Port Harcourt", "Abuja and Jos", "A",
     "Only Lagos and Calabar returned elected members."),
    (T_NIGCON, "Medium", "The Independence Constitution of 1960 was modelled on the",
     "British parliamentary system", "American presidential system",
     "French communal system", "Soviet council system", "A",
     "Nigeria inherited the Westminster arrangement in 1960."),
    (T_NIGCON, "Medium", "Under the 1963 Republican Constitution, the President of Nigeria was",
     "a ceremonial head of state", "the head of government",
     "commander of the army", "an appointed colonial officer", "A",
     "Effective power stayed with Prime Minister Balewa."),
    (T_NIGCON, "Hard", "The Constitution Drafting Committee of 1975-76 was chaired by",
     "Chief F.R.A. Williams", "Dr Nnamdi Azikiwe",
     "General Murtala Mohammed", "Alhaji Ahmadu Bello", "A",
     "The learned SAN led the committee that drafted the 1979 document."),
    (T_NIGCON, "Medium", "The 1999 Constitution came into force through",
     "a military decree", "a referendum",
     "an act of the National Assembly", "a court judgement", "A",
     "Decree 24 of 1999 promulgated it before the handover."),
    (T_NIGCON, "Hard", "The Richards Constitution of 1946 was significant for bringing",
     "the North and South together", "independence to Nigeria",
     "party government to Lagos", "the elective principle", "A",
     "One legislative framework briefly covered both halves of the country."),

    # -------------------------------------------------------- colonial admin
    (T_COLON, "Medium", "At Nigeria's independence in 1960, the Governor-General was",
     "Nnamdi Azikiwe", "Obafemi Awolowo",
     "Tafawa Balewa", "Ahmadu Bello", "A",
     "Ziki served as Governor-General until the 1963 republic."),
    (T_COLON, "Medium", "Under the Clifford Constitution, the Legislative Council made laws for",
     "the Southern provinces only", "the whole country",
     "the North alone", "the colony of Lagos alone", "A",
     "The North was governed by the Governor's proclamations."),
    (T_COLON, "Medium", "The policy of assimilation in West Africa was practised by the",
     "French", "British", "Portuguese", "Germans", "A",
     "France sought to turn colonial subjects into Frenchmen."),
    (T_COLON, "Medium", "The Royal Niger Company is remembered for its role in the",
     "British takeover of the Niger area", "introduction of the railway",
     "founding of Lagos city", "abolition of the slave trade", "A",
     "Its trading posts and treaties preceded the 1900 protectorates."),

    # ------------------------------------------------------------- nationalism
    (T_NAT, "Medium", "The great strength of the Nigerian Youth Movement in its early years was its",
     "support across ethnic groups", "wealth from cocoa sales",
     "army of hired thugs", "newspaper in Hausa", "A",
     "NYM drew support from all regions in its early years."),
    (T_NAT, "Hard", "Obafemi Awolowo's newspaper and party organisation began with the formation of the Action Group in",
     "1951", "1937", "1963",
     "1949", "A",
     "The Action Group grew out of the Yoruba cultural association in 1951.",
     "1951"),
    (T_NAT, "Medium", "The West African Pilot founded by Azikiwe started publication in",
     "1937", "1922", "1948",
     "1956", "A",
     "The Pilot began in 1937 and became nationalism's loudest voice.",
     "1937"),
    (T_NAT, "Medium", "The Abeokuta Women's Union led by Funmilayo Ransome-Kuti is celebrated for",
     "fighting unjust taxation of women", "founding the first bank",
     "winning a seat in parliament", "ending colonial rule alone", "A",
     "Her union's protests forced the removal of unfair levies."),
    (T_NAT, "Hard", "The Zikist Movement of the 1940s demanded",
     "immediate self-government", "colonial rule forever",
     "higher taxes for Nigerians", "an end to schooling", "A",
     "The militant youth wing pressed for speedy independence."),

    # ------------------------------------------------------------ federalism
    (T_FED, "Medium", "Matters on the Concurrent Legislative List may be legislated upon by",
     "both federal and state governments", "the federal government alone",
     "local councils alone", "the courts", "A",
     "Education and health are classic concurrent subjects."),
    (T_FED, "Medium", "Matters not listed in the Exclusive or Concurrent lists fall under the",
     "Residual List", "Federal List", "Privy List",
     "Concurrent List", "A",
     "Residual matters belong to the states."),
    (T_FED, "Easy", "The number of states in Nigeria's present federation is",
     "36", "21", "30",
     "12", "A",
     "The 1996 creation brought the states to thirty-six plus Abuja.",
     "36"),
    (T_FED, "Hard", "The first creation of states in 1967 by the Gowon government produced",
     "12 states", "19 states",
     "4 regions", "6 zones", "A",
     "The four regions gave way to twelve states in May 1967.",
     "12"),

    # ---------------------------------------------------------- local government
    (T_LOCAL, "Medium", "A caretaker committee runs a local government council when",
     "there is no elected council", "the chairman travels",
     "revenue is high", "there is no market", "A",
     "Appointed committees administer councils pending elections."),
    (T_LOCAL, "Medium", "Council chairmanship polls within a Nigerian state are organised by",
     "the State Electoral Commission", "INEC",
     "the police", "the council clerks", "A",
     "SIECs run council polls while INEC handles federal ones."),
    (T_LOCAL, "Medium", "Which of these functions is performed by the federal rather than local government?",
     "Defence of the country", "Collection of market rates",
     "Registration of marriages", "Maintenance of motor parks", "A",
     "Defence is an exclusive federal function."),
    (T_LOCAL, "Medium", "Rates and levies collected by a local council belong to its",
     "internally generated revenue", "federal allocation",
     "state grant", "party funds", "A",
     "Councils raise part of their money from local rates."),

    # ------------------------------------------------------------ civil service
    (T_CIVIL, "Medium", "The accounting officer of a ministry is the",
     "permanent secretary", "minister",
     "director of audits", "governor", "A",
     "The permanent secretary answers for the ministry's funds."),
    (T_CIVIL, "Medium", "The principle of anonymity requires civil servants to",
     "avoid public praise or blame", "work without salaries",
     "join political parties", "live in secret places", "A",
     "Ministers take public responsibility for ministry actions."),
    (T_CIVIL, "Medium", "Appointment and promotion of civil servants are handled by the",
     "Civil Service Commission", "political parties",
     "trade unions", "state assemblies", "A",
     "The commission keeps the service merit-based."),
    (T_CIVIL, "Hard", "The public service differs from the civil service because it also includes staff of",
     "corporations and agencies", "private companies",
     "foreign embassies", "political parties", "A",
     "The public service is the wider government family."),

    # --------------------------------------------------------- public corps
    (T_PUB, "Medium", "The Nigerian National Petroleum Corporation was established to",
     "manage the oil industry", "import foreign cars",
     "train secondary students", "regulate elections", "A",
     "NNPC oversees upstream and downstream oil operations."),
    (T_PUB, "Medium", "Privatisation is the transfer of government-owned enterprises to",
     "private investors", "traditional rulers",
     "foreign governments", "the civil service", "A",
     "Shares move from state hands to individuals and firms."),
    (T_PUB, "Medium", "The Bureau of Public Enterprises is the agency charged with Nigeria's",
     "privatisation programme", "population census",
     "border defence", "school feeding", "A",
     "BPE prepares public firms for sale or commercialisation."),
    (T_PUB, "Medium", "A recurring problem of public corporations in Nigeria is",
     "political interference", "too much profit",
     "excess staff discipline", "foreign admiration", "A",
     "Appointments and policy are often politicised."),

    # ---------------------------------------------------------------- military
    (T_MIL, "Medium", "The January 1966 coup brought which officer to power as Head of State?",
     "Major-General Aguiyi-Ironsi", "General Yakubu Gowon",
     "General Murtala Mohammed", "General Olusegun Obasanjo", "A",
     "Ironsi took over after the January 1966 coup."),
    (T_MIL, "Medium", "The military government that handed power to civilians in May 1999 was led by",
     "General Abdulsalami Abubakar", "General Sani Abacha",
     "General Ibrahim Babangida", "General Muhammadu Buhari", "A",
     "Abubakar's short transition restored the republic."),
    (T_MIL, "Medium", "The Nigerian Civil War ended in",
     "1970", "1967", "1963",
     "1975", "A",
     "The war ran from 1967 to January 1970.",
     "1970"),
    (T_MIL, "Medium", "A prominent feature of military rule in Nigeria was the",
     "suspension of the constitution", "growth of parliament",
     "daily party primaries", "expansion of courts", "A",
     "Decrees replaced the constitution under military governments."),

    # ------------------------------------------------------------ foreign policy
    (T_FOREIGN, "Medium", "Nigeria was a founding member of the Organisation of African Unity in",
     "1963", "1960", "1975",
     "1980", "A",
     "The OAU was born at Addis Ababa in 1963.",
     "1963"),
    (T_FOREIGN, "Medium", "Nigeria's leadership of ECOMOG in the 1990s demonstrated its commitment to",
     "peacekeeping in West Africa", "trade with Asia",
     "nuclear research", "space exploration", "A",
     "Nigerian troops stabilised Liberia and Sierra Leone."),
    (T_FOREIGN, "Hard", "Nigeria broke diplomatic relations with France in 1961 in protest at French nuclear tests in the",
     "Sahara", "Alps", "Mediterranean",
     "Pacific", "A",
     "The Sahara tests threatened West African safety."),
    (T_FOREIGN, "Easy", "Nigerian missions abroad are normally headed by",
     "ambassadors", "governors",
     "senators", "judges", "A",
     "High commissioners serve within the Commonwealth."),

    # --------------------------------------------------- international bodies
    (T_INT, "Easy", "The UN agency devoted to children's welfare is",
     "UNICEF", "UNESCO", "WHO",
     "ILO", "A",
     "UNICEF funds child health and education programmes."),
    (T_INT, "Medium", "In the UN General Assembly, member states each have",
     "one vote", "votes by population",
     "two votes each", "no vote", "A",
     "Sovereign equality gives every member a single vote."),
    (T_INT, "Medium", "Nigeria's admission into the oil producers' cartel OPEC took place in",
     "1971", "1960", "1975",
     "1986", "A",
     "Nigeria became OPEC's member in 1971.",
     "1971"),
    (T_INT, "Medium", "A Nigerian can visit Ghana without a visa under the ECOWAS protocol on",
     "free movement of persons", "common currency",
     "joint external tariffs", "collective defence", "A",
     "Community citizens cross ECOWAS borders with ease."),
    (T_INT, "Hard", "The International Court of Justice primarily settles disputes between",
     "states", "individuals and firms",
     "companies only", "football clubs", "A",
     "Only states may be parties before the World Court."),
]

build_batch(
    S,
    "batch_060_neco_government2.json",
    "060",
    "NECO Government top-up (round 2): grows the bank to 150 items so "
    "students get two full 60-question papers without repeats. New angles "
    "- de facto government, political socialisation, confederation, "
    "entrenchment, delegated legislation, impeachment, SDP/NRC, "
    "Zikist Movement, NYM, 1967 state creation, SIEC, BPE, ECOMOG, "
    "OPEC membership, ICJ - near-duplicate scanned against the JAMB, "
    "WAEC and existing NECO banks (round-1 items included).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
