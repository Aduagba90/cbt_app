"""Batch 205 - NECO Financial Accounting round 7 (NECO top-up, R40).

Grows NECO Accounting from 239 toward ~260 with angles not yet in
the bank: trade discount; cash discount; bad debts defined; bad
debts recovered; the returns inwards book; capital vs revenue
receipts; drawings defined; the partnership deed; dividends
defined; interim dividends; the going concern, dual aspect,
business entity, prudence and money measurement concepts; ordinary
shares; fixed assets and liabilities defined; debtors and
creditors. Scanned against the whole Accounting pool (WAEC and
NECO stems, 497 items).

    python3 scripts/build_neco_batch205.py -> content/batch_205_neco_acct7.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_TRD = "Trading Operations"
T_BAD = "Bad and Doubtful Debts"
T_CON = "Accounting Concepts"
T_PAR = "Partnership Accounts"
T_CMP = "Company Accounts"
T_BSH = "The Balance Sheet"

PASSAGES = []
PQ = []

Q = [
    (T_TRD, "Medium", "A reduction in the listed price of goods granted by a seller to a customer who buys in bulk is called",
     "trade discount", "cash discount",
     "allowance for bulk", "commission on sales", "A",
     "It is deducted on the invoice itself."),
    (T_TRD, "Medium", "A deduction granted to a customer who settles his account within an agreed period is",
     "cash discount", "trade discount",
     "rebate on list price", "bad debt recovered", "A",
     "Prompt payment earns a price off."),
    (T_TRD, "Easy", "The book in which goods returned by customers are recorded before posting to the ledger is the",
     "returns inwards book", "returns outwards book",
     "sales day book", "petty cash book", "A",
     "What went out has come back through the door."),
    (T_BAD, "Easy", "An amount due from a customer that has proved impossible to collect is written off as",
     "a bad debt", "a provision",
     "an accrual", "a reserve fund", "A",
     "The debtor's account is closed in sorrow."),
    (T_BAD, "Hard", "Money unexpectedly received from a customer whose debt had earlier been written off is credited to",
     "bad debts recovered account", "the customer's old account",
     "sales account afresh", "capital account directly", "A",
     "The dead debt comes back to life as income."),
    (T_CON, "Easy", "The concept that a business will continue to operate for the foreseeable future and need not be sold off is the",
     "going concern concept", "realisation concept",
     "consistency concept", "accrual concept", "A",
     "Assets are valued on the belief of continued life."),
    (T_CON, "Medium", "The concept that every transaction has two aspects, a debit and a credit, is the",
     "dual aspect concept", "matching concept",
     "materiality concept", "prudence concept", "A",
     "Each entry bows twice in the books."),
    (T_CON, "Medium", "The concept which requires that revenue be recognised in the books when it is earned rather than when cash is finally received is the",
     "realisation concept", "accrual concept",
     "consistency concept", "objectivity concept", "A",
     "The sale counts on the day it is made."),
    (T_CON, "Medium", "The concept that guides accountants to record losses as soon as they are foreseen but profits only when earned is",
     "prudence", "consistency",
     "objectivity", "neutrality", "A",
     "Never count your chickens before they hatch."),
    (T_CON, "Hard", "The concept that restricts the accounting records of a business to facts that can be expressed in money terms is",
     "money measurement", "substance over form",
     "realisation", "periodicity", "A",
     "The books speak only in naira and kobo."),
    (T_PAR, "Medium", "The written agreement among partners covering profit sharing, salaries, interest on capital and dissolution is the",
     "partnership deed", "memorandum of association",
     "articles of association", "prospectus", "A",
     "Partners settle their rights on paper."),
    (T_PAR, "Hard", "In the absence of a partnership deed, the Partnership Act provides that profits and losses are shared",
     "equally among the partners", "in the ratio of capital",
     "by seniority of age", "as the senior partner directs", "A",
     "Equal shares where the deed is silent."),
    (T_CMP, "Easy", "The return paid to shareholders out of a company's profit is called",
     "dividend", "interest",
     "commission", "debenture premium", "A",
     "The shareholders' share of the spoils."),
    (T_CMP, "Hard", "A dividend paid to shareholders in the middle of the trading year, before the annual accounts are ready, is an",
     "interim dividend", "final dividend",
     "opening dividend", "cumulative dividend", "A",
     "A first taste before the full meal."),
    (T_CMP, "Medium", "Shares that carry no fixed rate of dividend but enjoy voting rights and a share of surplus profit are",
     "ordinary shares", "preference shares",
     "debenture stocks", "deferred bonds", "A",
     "The owners of the company proper."),
    (T_BSH, "Easy", "Assets bought for long-term use in the business rather than for resale are",
     "fixed assets", "current assets",
     "liquid assets", "floating charges", "A",
     "Machines and premises serve for years."),
    (T_BSH, "Medium", "The amounts which a business owes to outsiders and must settle in the course of trade are its",
     "liabilities", "assets",
     "drawings", "capital", "A",
     "The creditors' claims stand against the firm."),
    (T_BSH, "Easy", "Persons who owe money to a business for goods sold to them on credit are its",
     "debtors", "creditors",
     "shareholders", "benefactors", "A",
     "They owe; the business awaits their payment."),
    (T_BSH, "Easy", "Persons to whom a business owes money for goods supplied on credit are its",
     "creditors", "debtors",
     "partners", "trustees", "A",
     "The business owes; their bills await payment."),
    (T_TRD, "Hard", "Money received from the sale of old equipment differs from sales revenue because it is a",
     "capital receipt", "revenue receipt",
     "deferred income", "accrued income", "A",
     "Selling the goose is not selling eggs."),
    (T_TRD, "Medium", "Goods, cash or personal items which the owner takes from his own business for private use are recorded as",
     "drawings", "expenses",
     "purchases", "dividends", "A",
     "The owner's hand withdraws his own share."),
]

build_batch(
    S,
    "batch_205_neco_acct7.json",
    "205",
    "NECO Financial Accounting round 7 (R40 top-up): trade vs cash "
    "discount; returns inwards book; bad debts defined; bad debts "
    "recovered; going concern; dual aspect; business entity; "
    "prudence; money measurement; the partnership deed; equal "
    "sharing where no deed exists; dividends defined; interim "
    "dividend; ordinary shares; fixed assets; liabilities; debtors "
    "and creditors; capital vs revenue receipts; drawings. Scanned "
    "against the whole Accounting pool (WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
