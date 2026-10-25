"""Batch 189 - NECO Civic Education round 6 (NECO top-up, R36).

Grows NECO Civic from 221 toward ~246 with angles not yet in the
bank: limited government; the constitution's supremacy; the
deportation of undesirable aliens; the naira's two signatures;
driving against traffic; monogamy defined; gender equality; the
value of courage; self-reliance; transparency; election observers;
impeachment; the police; the NSCDC; the fire service; colonialism
defined; ethnicism; disability rights; the UBE programme;
arbitration; freedom of association; made-in-Nigeria goods; fake
news; hate speech; examination malpractice. Scanned against NECO
rounds 1-5, WAEC Civic (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch189.py -> content/batch_189_neco_civic6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Civic Education"

T_VAL = "Values"
T_CON = "Constitution and Democracy"
T_CIT = "Citizenship and aliens"
T_SYM = "National Symbols"
T_TRA = "Traffic and Orderliness"
T_FAM = "Family and Society"
T_SEC = "Security Agencies"
T_RIG = "Rights and the Law"
T_ELE = "Elections"
T_DUT = "Duties and Nationalism"
T_ILL = "Modern Social Ills"

PASSAGES = []
PQ = []

Q = [
    (T_CON, "Medium", "A government whose powers are held in check by the constitution and the courts is described as",
     "limited government", "absolute government",
     "a military junta", "an oligarchy of elders", "A",
     "Law, not whim, draws its boundaries."),
    (T_CON, "Medium", "The 1999 Constitution stands above every other law in Nigeria. This position is called its",
     "supremacy", "flexibility",
     "popularity", "legality of age", "A",
     "Any law that fights it falls."),
    (T_CIT, "Medium", "A foreigner who seriously breaches Nigeria's laws may, besides prosecution, be",
     "deported to his home country", "made a citizen by force",
     "promoted in his firm", "fined by his embassy only", "A",
     "The alien is sent back whence he came."),
    (T_SYM, "Hard", "Nigerian currency notes carry the signatures of the Central Bank Governor and the",
     "Minister of Finance", "President of the Senate",
     "Chief Justice of Nigeria", "Inspector-General of Police", "A",
     "Two hands stand behind every naira."),
    (T_TRA, "Medium", "A driver who enters a one-way street against the flow of oncoming traffic commits the offence of",
     "driving against traffic", "over-speeding",
     "dangerous parking", "drunk driving", "A",
     "The wrong way in is the wrong way out."),
    (T_FAM, "Easy", "A marriage in which one man is wedded to one wife is called",
     "monogamy", "polygamy",
     "polyandry", "bigamy", "A",
     "One husband, one wife, one union."),
    (T_FAM, "Medium", "The principle that men and women should enjoy equal opportunities in education and work is",
     "gender equality", "gender bias",
     "male dominance", "positive discrimination", "A",
     "Talent, not sex, should open the door."),
    (T_VAL, "Medium", "A witness who tells the truth in court even when friends beg him to lie shows the value of",
     "courage", "contentment",
     "prudence", "simplicity", "A",
     "Fear bows out when courage speaks."),
    (T_VAL, "Medium", "A young graduate who earns his own living instead of idling at home displays",
     "self-reliance", "nepotism",
     "vanity", "extravagance", "A",
     "His own hands feed his own mouth."),
    (T_VAL, "Medium", "Running public affairs in the open, where every citizen may see and question them, is",
     "transparency", "secrecy",
     "diplomacy", "autocracy", "A",
     "Sunlight on the books keeps hands clean."),
    (T_ELE, "Medium", "Local and international groups licensed to watch the conduct of polls on election day are called",
     "election observers", "party agents",
     "returning officers", "poll canvassers", "A",
     "Their reports tell the world what they saw."),
    (T_CON, "Hard", "The power of the National Assembly to remove a president found guilty of gross misconduct is exercised through",
     "impeachment", "recall",
     "a vote of no confidence", "judicial review", "A",
     "Two-thirds of both chambers must concur."),
    (T_SEC, "Easy", "The security agency chiefly charged with maintaining internal law and order across Nigeria is the",
     "Nigeria Police Force", "Nigerian Army",
     "State Security Service", "Nigeria Customs Service", "A",
     "Its constables walk the nation's beats."),
    (T_SEC, "Medium", "The corps that guards oil pipelines, power installations and other critical national infrastructure is the",
     "NSCDC", "FRSC",
     "NDLEA", "NIA", "A",
     "The civil defence corps stands watch."),
    (T_SEC, "Easy", "Rescue from fire outbreaks and fire prevention education belong to the",
     "Fire Service", "Police Force",
     "Road Safety Corps", "Civil Defence Corps", "A",
     "Their hoses and ladders answer every alarm."),
    (T_DUT, "Medium", "The rule of one country over another people, chiefly for exploitation, is called",
     "colonialism", "nationalism",
     "federalism", "communalism", "A",
     "The flag followed the trade and the tax."),
    (T_ILL, "Medium", "Judging every matter by the interest of one's own ethnic group above others is called",
     "ethnicism", "federal character",
     "nationalism", "pluralism", "A",
     "The tribe's narrow wall blocks the nation's road."),
    (T_RIG, "Medium", "Denying qualified persons opportunity because of their physical disability amounts to",
     "discrimination", "affirmative action",
     "equity", "positive liberty", "A",
     "Ability, not the body's shape, should count."),
    (T_RIG, "Easy", "The federal programme that guarantees nine years of free basic schooling is",
     "UBE", "NYSC",
     "SURE-P", "N-Power", "A",
     "Universal Basic Education opens the school gate."),
    (T_RIG, "Medium", "Submitting a quarrel to a neutral third person whose decision both parties accept is called",
     "arbitration", "litigation by trick",
     "confrontation", "negotiation only", "A",
     "The arbitrator's word settles the matter."),
    (T_RIG, "Easy", "Joining any lawful association, club or union of one's choice is an exercise of freedom of",
     "association", "movement",
     "religion", "the press", "A",
     "Friends may lawfully gather and organise."),
    (T_DUT, "Easy", "A citizen who deliberately buys made-in-Nigeria goods helps chiefly to",
     "create jobs at home", "avoid paying tax",
     "please the customs service", "raise import duties", "A",
     "Every local factory fed is a family fed."),
    (T_ILL, "Easy", "Unverified stories spread online to deceive readers and cause panic are collectively called",
     "fake news", "editorials",
     "press releases", "advertisements", "A",
     "Shared in haste, regretted at leisure by all."),
    (T_ILL, "Medium", "Speech that attacks or demeans people merely because of their tribe or religion is known as",
     "hate speech", "free speech",
     "criticism", "parody", "A",
     "The law frowns at words that set neighbours ablaze."),
    (T_ILL, "Medium", "Candidates who smuggle answers into the hall to pass examinations practise",
     "examination malpractice", "effective revision",
     "private study", "group discussion", "A",
     "The certificate lies even before it is issued."),
]

build_batch(
    S,
    "batch_189_neco_civic6.json",
    "189",
    "NECO Civic round 6 (R36 top-up): limited government; the "
    "constitution's supremacy; deportation of undesirable aliens; "
    "the naira's two signatures; driving against traffic; monogamy; "
    "gender equality; courage; self-reliance; transparency; "
    "election observers; impeachment; the police; NSCDC; fire "
    "service; colonialism; ethnicism; disability discrimination; "
    "UBE; arbitration; freedom of association; made-in-Nigeria "
    "goods; fake news; hate speech; examination malpractice. "
    "Scanned against NECO rounds 1-5, WAEC Civic (all rounds) and "
    "the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
