"""Batch 081 - WAEC Financial Accounting, Paper 1 Objective round 1.

WASSCE Financial Accounting Paper 1 (Objective) is a 50-item paper (1 hr;
official 2026 second-series timetable, paper 1041). This batch covers the
WASSCE syllabus with FRESH angles and phrasings - mini-scenario entries
(Bola sells to Ade on credit, stamps from the float, the lorry's wear),
numeric mini-computations (capital from assets minus liabilities, cost of
sales, imprest refunds), Nigerian regulatory bodies (ICAN, FRC,
Auditor-General) and question-form stems - because the near-dup scan checks
every item against the JAMB, WAEC and NECO banks, including the large JAMB
Accounting banks (batches 035-036) and our 62-item NECO Accounting bank.

    python3 scripts/build_neco_batch81.py -> content/batch_081_waec_accounting.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_NAT = "Nature and Purpose of Accounting"
T_LED = "The Ledger and Double Entry"
T_BOOK = "Books of Prime Entry"
T_FIN = "Final Accounts and Adjustments"
T_CASH = "Cash Book and Bank Reconciliation"
T_ERR = "Trial Balance, Errors and Control"
T_REG = "Regulation and Ethics"
T_OTH = "Partnership, Company and Other Accounts"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- nature and purpose
    (T_NAT, "Easy", "The main purpose of accounting is to",
     "provide financial information", "increase profits directly", "employ more accountants", "advertise the business", "A",
     "Users need information to decide."),
    (T_NAT, "Medium", "Bookkeeping differs from accounting because accounting goes further to",
     "analyse and interpret records", "record entries in the books", "issue receipts to debtors", "count the cash daily", "A",
     "Analysis lifts facts into insight."),
    (T_NAT, "Easy", "The N200,000 loan Emeka's shop owes the bank is classified as a",
     "liability", "fixed asset", "capital item", "drawing item", "A",
     "Owed sums sit among liabilities."),
    (T_NAT, "Medium", "A business owns N250,000 and owes N90,000. Its capital stands at",
     "N160,000", "N340,000", "N90,000", "N250,000", "A",
     "Capital is assets minus debts."),
    (T_NAT, "Hard", "The double entry system was first described by",
     "Luca Pacioli", "Adam Smith", "J.M. Keynes", "Charles Babbage", "A",
     "The Italian monk wrote it in 1494."),
    (T_NAT, "Medium", "Users of accounting information outside the business include",
     "tax authorities and investors", "the office messenger", "the sales clerk alone", "the store keeper alone", "A",
     "Outsiders too steer by the figures."),
    (T_NAT, "Hard", "The historic cost convention records assets at",
     "what was paid for them", "their current market price", "their replacement value", "their insured value", "A",
     "Cost, not market, enters the books."),
    # ---------------------------------------------------------------- ledger and double entry
    (T_LED, "Medium", "For goods sold to Tunde on credit, Tunde's account in the seller's ledger is",
     "debited", "credited", "closed off", "left unposted", "A",
     "The buyer's account takes the debit."),
    (T_LED, "Medium", "Paying cash for goods for resale debits purchases and credits",
     "the cash account", "the purchases account", "the sales account", "the drawings account", "A",
     "Cash goes out, so cash is credited."),
    (T_LED, "Easy", "In the ledger, an asset grows by a",
     "debit entry", "credit entry", "footing mark", "journal folio", "A",
     "Debits build the asset side."),
    (T_LED, "Medium", "The ledger folio column in a journal shows",
     "the page of the posting", "the date of the entry", "the name of the trader", "the amount in words", "A",
     "It points to where it was posted."),
    (T_LED, "Medium", "A credit balance brought down on a supplier's account means the supplier is a",
     "creditor", "debtor", "customer", "partner", "A",
     "We still owe the balance owing."),
    (T_LED, "Medium", "Accounts bearing the names of customers and suppliers are called",
     "personal accounts", "real accounts", "nominal accounts", "cash accounts", "A",
     "Persons, firms, and names live there."),
    (T_LED, "Medium", "When the owner takes cash for personal use, the account credited is",
     "cash account", "drawings account", "capital account", "salary account", "A",
     "Cash leaves; drawings are debited."),
    (T_LED, "Easy", "Posting simply means",
     "carrying entries to ledgers", "recording in the journal first", "adding a folio number", "checking the trial balance", "A",
     "Journal entries travel to ledgers."),
    (T_LED, "Hard", "Goods returned by a customer, in the seller's books, are credited to",
     "the sales returns account", "the purchases account", "the customer's account", "the cash account", "A",
     "Returns in reduce the sales made."),
    # ---------------------------------------------------------------- books of prime entry
    (T_BOOK, "Medium", "Invoices received from suppliers for goods bought on credit go first into the",
     "purchases day book", "sales day book", "cash book", "petty cash book", "A",
     "Credit purchases begin in this book."),
    (T_BOOK, "Medium", "The double-column book recording cash and bank movements is the",
     "two-column cash book", "purchases journal", "general journal", "petty cash book", "A",
     "Cash and bank stand side by side."),
    (T_BOOK, "Easy", "The clerk pays N200 for postage stamps from the float. The record goes to the",
     "petty cash book", "purchases journal", "sales journal", "general journal", "A",
     "Small expenses ride the float."),
    (T_BOOK, "Hard", "The imprest system works by refunding the float to",
     "its original fixed amount", "double the last balance", "any sum the clerk wants", "the amount spent plus profit", "A",
     "The float returns to its level."),
    (T_BOOK, "Hard", "A trade discount granted by a supplier is",
     "not entered in the books", "credited to discount received", "debited to discount allowed", "carried to profit and loss", "A",
     "Only the net figure is posted."),
    (T_BOOK, "Medium", "When Ade returns damaged goods, Bola issues him a",
     "credit note", "debit note", "proforma invoice", "statement of account", "A",
     "The note reduces Ade's debt."),
    (T_BOOK, "Easy", "Cheques received from customers are first entered in the",
     "cash book", "sales journal", "petty cash book", "general journal", "A",
     "The bank column receives them."),
    # ---------------------------------------------------------------- final accounts and adjustments
    (T_FIN, "Easy", "Gross profit emerges in which final account?",
     "the trading account", "the profit and loss account", "the balance sheet", "the cash book", "A",
     "It nets trading results alone."),
    (T_FIN, "Medium", "Opening stock nil, purchases N30,000, closing stock N5,000; cost of sales is",
     "N25,000", "N35,000", "N30,000", "N5,000", "A",
     "Purchases minus closing stock gives it."),
    (T_FIN, "Medium", "Net profit is arrived at after deducting",
     "all expenses from gross profit", "only cost of sales", "drawings and capital", "liabilities from assets", "A",
     "Every expense must clear out."),
    (T_FIN, "Medium", "The annual charge for a lorry's wear is debited to profit and loss as",
     "depreciation", "carriage outwards", "capital expense", "accrued rent", "A",
     "Wear and tear becomes expense."),
    (T_FIN, "Hard", "The reducing balance method charges depreciation at",
     "a fixed percentage of book value", "the original cost each year", "the scrap value only", "the market price each year", "A",
     "The base shrinks year by year."),
    (T_FIN, "Hard", "Provision for doubtful debts is charged against",
     "debtors' balances", "creditors' balances", "cash balances", "stock balances", "A",
     "Doubtful debts spring from debtors."),
    (T_FIN, "Hard", "Accrued expenses owing at the year end appear in the balance sheet as",
     "a current liability", "a fixed asset", "a current asset", "an income item", "A",
     "Owed but unpaid, still a debt."),
    (T_FIN, "Medium", "Prepaid rent at year end appears in the balance sheet as",
     "a current asset", "a current liability", "a long-term loan", "an expense only", "A",
     "The benefit still lies ahead."),
    (T_FIN, "Medium", "A balance sheet lays out",
     "assets, liabilities and capital", "income and expenses only", "cash receipts and payments", "purchases and sales only", "A",
     "Position, not performance, is shown."),
    (T_FIN, "Medium", "Working capital is the excess of",
     "current assets over current liabilities", "fixed assets over fixed liabilities", "capital over drawings made", "sales over purchases made", "A",
     "The short-term cushion of the firm."),
    # ---------------------------------------------------------------- cash book and bank reconciliation
    (T_CASH, "Easy", "A bank statement is sent by",
     "the bank to the customer", "the customer to the bank", "the auditor to the firm", "the supplier to the buyer", "A",
     "The bank reports the account."),
    (T_CASH, "Hard", "Unpresented cheques leave the cash book balance",
     "lower than the bank statement's", "higher than the bank statement's", "equal to the statement's", "unaffected by the cheques", "A",
     "The bank has not yet paid them out."),
    (T_CASH, "Medium", "Bank charges appearing only on the statement are corrected by",
     "crediting the cash book", "debiting the cash book", "ignoring them till year end", "raising a fresh debit note", "A",
     "Charges reduce our bank money."),
    (T_CASH, "Hard", "A lodgement credited on the statement but not yet entered in the cash book requires",
     "a debit in the cash book", "a credit in the cash book", "no entry at all", "an entry in the petty cash", "A",
     "Money in debits the cash book."),
    (T_CASH, "Hard", "Standing orders on the statement but not in the cash book are",
     "credited to the cash book", "debited to the cash book", "posted to the day books", "added to unpresented cheques", "A",
     "The bank paid on our behalf."),
    (T_CASH, "Hard", "A customer's cheque returned dishonoured is, on notice,",
     "credited in the cash book", "debited in the cash book", "destroyed and forgotten", "added to the bank balance", "A",
     "The earlier debit is reversed."),
    (T_CASH, "Medium", "The cash book serves both as a",
     "journal and a ledger", "ledger and a trial balance", "journal and a balance sheet", "day book and cash flow", "A",
     "It records and classifies at once."),
    (T_CASH, "Hard", "Contra entries between the cash and bank columns appear",
     "on both sides of the cash book", "only in the general journal", "in the petty cash book only", "in the trial balance only", "A",
     "Cash to bank runs both columns."),
    # ---------------------------------------------------------------- trial balance, errors and control
    (T_ERR, "Medium", "The agreement of debit and credit totals in a trial balance chiefly proves",
     "arithmetical accuracy", "the year's profit figure", "the stock valuation", "the owner's honesty", "A",
     "Debits must equal the credits."),
    (T_ERR, "Hard", "Which error still leaves the trial balance balanced?",
     "error of complete reversal", "adding an item twice on one side", "omitting one account's balance", "posting N50 to one side only", "A",
     "Both sides carry the same figures."),
    (T_ERR, "Hard", "A suspense account is opened whenever",
     "the trial balance fails to agree", "profit cannot be computed", "stock is missing at year end", "the bank refuses a cheque", "A",
     "It parks the difference pending."),
    (T_ERR, "Hard", "When a capital item is treated as a revenue expense, the error is one of",
     "principle", "original entry", "single entry", "compensation", "A",
     "Right amount, wrong class of account."),
    (T_ERR, "Medium", "A typewriter bought for the office but debited to purchases is",
     "an error of principle", "an error of commission", "an error of omission", "a compensating error", "A",
     "Asset spending hid inside expenses."),
    (T_ERR, "Medium", "Individual debtors' accounts are kept in the",
     "sales ledger", "purchases ledger", "general ledger", "cash book", "A",
     "Debtors follow the sales side."),
    (T_ERR, "Hard", "Credit purchases stand in the creditors control account as",
     "credit entries", "debit entries", "suspense entries", "contra entries", "A",
     "We owe, so the account credits."),
    (T_ERR, "Medium", "An error of omission leaves the trial balance",
     "still balanced", "badly unbalanced", "showing double the amount", "impossible to prepare", "A",
     "Nothing was posted at all."),
    # ---------------------------------------------------------------- regulation and ethics
    (T_REG, "Easy", "The main professional body of chartered accountants in Nigeria is",
     "ICAN", "NMA", "NUT", "COREN", "A",
     "ICAN charters the accountants."),
    (T_REG, "Hard", "The body that currently sets financial reporting standards in Nigeria is the",
     "Financial Reporting Council", "Corporate Affairs Commission", "Central Bank of Nigeria", "Nigerian Deposit Insurance", "A",
     "The FRC issues the standards."),
    (T_REG, "Medium", "An accountant who keeps two sets of books breaches",
     "integrity and honesty", "the matching concept", "the money measure unit", "prudence and nothing more", "A",
     "Honesty is the first tool of trade."),
    (T_REG, "Medium", "Audited accounts inspire confidence because they carry",
     "an independent opinion", "the owner's own promise", "the bank's approval seal", "the staff's joint signature", "A",
     "The auditor has no stake in it."),
    (T_REG, "Medium", "Confidentiality forbids an accountant to",
     "divulge client information", "sign the audit report", "visit the client's office", "charge professional fees", "A",
     "Client secrets stay locked away."),
    (T_REG, "Hard", "Public sector accounts in Nigeria are audited by the",
     "Auditor-General", "ICAN president", "CBN governor", "Senate committee", "A",
     "The constitution gives the office."),
    # ---------------------------------------------------------------- partnership, company and other accounts
    (T_OTH, "Hard", "In a manufacturing account, prime cost equals",
     "direct materials plus direct labour", "all factory overheads alone", "office salaries and rent", "sales minus gross profit", "A",
     "Direct costs build prime cost."),
    (T_OTH, "Medium", "Work-in-progress appears in the balance sheet as",
     "a current asset", "a current liability", "sales revenue", "a fixed liability", "A",
     "Unfinished goods still hold value."),
    (T_OTH, "Hard", "Subscriptions received in advance by a club are",
     "its current liabilities", "its current assets", "its income for the year", "its accumulated fund", "A",
     "The service is still owed members."),
    (T_OTH, "Medium", "A club's income and expenditure account matches a firm's",
     "profit and loss account", "trading account", "cash book", "balance sheet", "A",
     "It shows the year's surplus or deficit."),
    (T_OTH, "Hard", "Interest on drawings in partnership accounts is",
     "debited to partners' accounts", "credited to the partners", "ignored when sharing profit", "paid out in cash monthly", "A",
     "Drawings cost the drawer interest."),
    (T_OTH, "Hard", "Goodwill arises when a business is bought for more than its",
     "net assets in the books", "gross profit for the year", "total sales turnover", "stock of goods at cost", "A",
     "The extra paid names the reputation."),
    (T_OTH, "Medium", "A company's shares that carry a fixed rate of dividend are",
     "preference shares", "ordinary shares", "founders' shares", "bonus shares", "A",
     "Preference dividend comes first."),
    (T_OTH, "Easy", "Debentures held against a company are",
     "long-term loans", "owners' capital", "current assets", "sales revenue", "A",
     "Lenders, not owners, hold them."),
]

build_batch(
    S,
    "batch_081_waec_accounting.json",
    "081",
    "WAEC Financial Accounting Paper 1 round 1 (Round 16e): the WASSCE "
    "syllabus with FRESH angles - mini-scenario entries (Bola sells to Ade, "
    "stamps from the float, the lorry's wear, the customer's bounced "
    "cheque), numeric mini-computations (capital N60,000, cost of sales "
    "N25,000), Nigerian regulatory bodies (ICAN, FRC, Auditor-General) and "
    "question-form stems - because the near-dup scan checks every item "
    "against the JAMB, WAEC and NECO banks INCLUDING the large JAMB "
    "Accounting banks (035-036) and the 62-item NECO Accounting bank. "
    "Topics: nature and purpose, the ledger, books of prime entry, final "
    "accounts and adjustments, cash book and bank reconciliation, trial "
    "balance and errors, regulation and ethics, partnership and company "
    "accounts.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
