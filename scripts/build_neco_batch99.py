"""Batch 099 - WAEC Financial Accounting round 2 (WAEC lift, Round 19).

WAEC Accounting Paper 1 draws 50 items; the bank stood at 63. This lift adds
fresh items - buyer's debit note, invoice for credit sales, sales day book,
returns inwards book, nominal and real accounts, the golden rule, balance
c/d, bad debts recovered, rent excluded from trading, discount allowed in
P&L, gross profit b/d, net profit to capital, wages vs salaries, drawings
of goods, liquidity order, working capital numeric, subscriptions in
arrears, receipts and payments nature, appropriation account, partner's
salary, current accounts, authorised vs issued capital, share premium,
control reconciliation, spreadsheets, markup vs margin, acid test, gross
pay components, pension, obsolescence, provision as contra, fund
accounting, opening entries - scanned against WAEC r1, NECO rounds 1-2 and
the JAMB Accounting banks.

    python3 scripts/build_neco_batch99.py -> content/batch_099_waec_accounting2.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_DOC = "Source Documents and Books"
T_LED = "The Ledger"
T_ADJ = "Adjustments and Year-End"
T_FIN = "Final Accounts"
T_PART = "Partnership and Company Accounts"
T_NPO = "Non-Profit and Public Sector"
T_ERR = "Controls and Errors"
T_PAY = "Payroll and Miscellaneous"
T_IT = "ICT in Accounting"

PASSAGES = []
PQ = []

Q = [
    # ---------------------------------------------------------------- documents and books
    (T_DOC, "Hard", "When a buyer returns damaged goods, the document he sends with them to claim credit is a",
     "debit note", "credit note", "proforma invoice", "statement of account", "A",
     "The buyer debits the supplier."),
    (T_DOC, "Easy", "An invoice is raised whenever goods are sold",
     "on credit", "for cash only", "free of charge", "in error", "A",
     "Credit sales breathe invoices."),
    (T_DOC, "Medium", "All credit sales for a week are first written up in the",
     "sales day book", "purchases day book", "cash book", "general journal", "A",
     "The day book lists them daily."),
    (T_DOC, "Medium", "Goods brought back by dissatisfied customers are logged in the",
     "returns inwards day book", "returns outwards day book", "sales journal", "petty cash book", "A",
     "Inwards means back to us."),
    (T_DOC, "Hard", "The entries needed to open a new set of books go into the",
     "general journal", "sales day book", "cash book", "petty cash book", "A",
     "Opening entries journal through."),
    # ---------------------------------------------------------------- ledger
    (T_LED, "Medium", "Accounts of expenses and incomes belong to the class called",
     "nominal accounts", "real accounts", "personal accounts", "impersonal", "A",
     "Nominal names the gains and losses."),
    (T_LED, "Medium", "Accounts for assets like machinery and buildings are",
     "real accounts", "nominal accounts", "personal accounts", "suspense accounts", "A",
     "Real things own real accounts."),
    (T_LED, "Easy", "'Debit all expenses and losses; credit all incomes and gains' is",
     "a golden rule of double entry", "a law of the stock exchange", "the doctrine of prudence", "a tax regulation", "A",
     "The golden rule never misleads."),
    (T_LED, "Hard", "To make an account's two sides agree at year end, the smaller side receives the",
     "balance c/d", "balance b/d", "double entry", "closing entry", "A",
     "Carried down completes the page."),
    (T_LED, "Medium", "The total of the sales day book is posted monthly to the credit of the",
     "sales account", "cash account", "purchases account", "debtor's account only", "A",
     "Sales totals credit sales."),
    # ---------------------------------------------------------------- adjustments
    (T_ADJ, "Hard", "Money received later from a debtor already written off is credited to",
     "bad debts recovered", "sales account", "bad debts account", "suspense account", "A",
     "The recovery revives income."),
    (T_ADJ, "Medium", "Which of these items would NEVER appear in the trading account?",
     "rent paid", "purchases", "sales returns", "carriage inwards", "A",
     "Rent belongs in the P&L only."),
    (T_ADJ, "Medium", "Discount allowed to credit customers is an expense reported in the",
     "profit and loss account", "trading account", "balance sheet", "capital account", "A",
     "The discount eats profit."),
    (T_ADJ, "Hard", "A machine becoming useless because better models exist suffers depreciation from",
     "obsolescence", "physical wear", "lapse of time", "depletion", "A",
     "New technology buries the old."),
    (T_ADJ, "Medium", "The provision for depreciation account normally carries a",
     "credit balance", "debit balance", "nil balance", "suspense balance", "A",
     "It stands against the asset."),
    # ---------------------------------------------------------------- final accounts
    (T_FIN, "Medium", "The gross profit for the year travels into the profit and loss account as",
     "gross profit b/d", "gross profit c/d", "gross margin", "net profit", "A",
     "Brought down starts the P&L."),
    (T_FIN, "Medium", "After the P&L account is closed, the net profit is transferred to the",
     "capital account", "cash book", "trading account", "suspense account", "A",
     "Profit fattens the capital."),
    (T_FIN, "Medium", "In a trading business, wages of shop workers enter the trading account while office salaries go to the",
     "profit and loss account", "trading account", "balance sheet", "wages account", "A",
     "Where the work happens decides."),
    (T_FIN, "Hard", "When the owner takes goods from the shop for personal use, the entry debits",
     "drawings at cost", "purchases", "sales at selling price", "capital", "A",
     "Cost price follows the goods."),
    (T_FIN, "Medium", "In the balance sheet, current assets are listed in order of",
     "liquidity", "size of amount", "alphabet", "date purchased", "A",
     "Cash, then debtors, then stock."),
    (T_FIN, "Medium", "Current assets of N80,000 and current liabilities of N30,000 give working capital of",
     "N50,000", "N110,000", "N30,000", "N80,000", "A",
     "The surplus oils the wheels."),
    # ---------------------------------------------------------------- partnership and company
    (T_PART, "Hard", "The account that shares net profit among partners by their agreed terms is the",
     "appropriation account", "trading account", "suspense account", "current account alone", "A",
     "Appropriation divides the cake."),
    (T_PART, "Medium", "A partner entitled to a yearly salary has it credited to his",
     "current account", "capital account", "loan account", "drawing", "A",
     "Current account carries the dues."),
    (T_PART, "Hard", "Partners' drawings during the year are posted to the debit of their",
     "current accounts", "capital accounts", "salary accounts", "cash book only", "A",
     "The current account absorbs drawings."),
    (T_PART, "Medium", "The maximum number of shares a company may issue, stated in its documents, is the",
     "authorised capital", "issued capital", "called-up capital", "paid-up capital", "A",
     "Authorised sets the ceiling."),
    (T_PART, "Hard", "Shares issued at a price above their face value carry a",
     "share premium", "share discount", "stock dividend", "bonus reserve", "A",
     "The extra paid is premium."),
    # ---------------------------------------------------------------- non-profit and public
    (T_NPO, "Hard", "Subscriptions owed by members but not yet received appear in the balance sheet as",
     "a current asset", "a current liability", "accumulated fund", "income", "A",
     "The club is owed the money."),
    (T_NPO, "Medium", "The receipts and payments account of a club is simply a summary of",
     "cash movements", "all incomes earned", "all expenses incurred", "assets held", "A",
     "Cash in, cash out, nothing more."),
    (T_NPO, "Medium", "Government accounting that keeps separate books for each fund is described as",
     "fund accounting", "unit costing", "batch accounting", "trust accounting", "A",
     "Each fund answers its name."),
    # ---------------------------------------------------------------- controls and errors
    (T_ERR, "Medium", "At month end, the control account total should be checked against the",
     "sum of the schedule", "bank statement", "cash book", "trial balance alone", "A",
     "The list of balances proves it."),
    (T_ERR, "Hard", "A transposition error, such as writing 690 for 960, throws the trial balance out by a figure divisible by",
     "9", "2", "5", "11", "A",
     "Digit swaps always divide by nine."),
    (T_ERR, "Medium", "A bookkeeper posts N500 to the debit side only. What will expose this slip?",
     "the trial balance totals", "the balance sheet date", "the profit figure", "nothing at all", "A",
     "Unequal totals raise the flag."),
    # ---------------------------------------------------------------- payroll and misc
    (T_PAY, "Medium", "An employee's gross pay is made up of basic salary plus",
     "allowances and overtime", "taxes and deductions", "net pay and pension", "net pay only", "A",
     "Everything earned is gross."),
    (T_PAY, "Easy", "Under the pension scheme, contributions come from",
     "both employer and employee", "the employee alone", "the employer alone", "the government alone", "A",
     "Both parties fund the pension pot."),
    (T_PAY, "Hard", "While markup is calculated on cost, margin is calculated on",
     "sales", "capital", "assets", "purchases", "A",
     "The base decides the name."),
    (T_PAY, "Hard", "The 'acid test' ratio excludes stock because stock is",
     "the least liquid current asset", "never owned by the firm", "always worthless", "the largest asset", "A",
     "Quick assets only, please."),
    (T_PAY, "Medium", "A customer's deposit shows as a CREDIT in the bank's books because, to the bank, the customer is a",
     "creditor", "debtor", "partner", "guarantor", "A",
     "The bank owes the depositor."),
    # ---------------------------------------------------------------- ICT
    (T_IT, "Easy", "Microsoft Excel, used widely by accountants, is a",
     "spreadsheet", "database", "browser", "compiler", "A",
     "Rows and columns hold the figures."),
    (T_IT, "Medium", "A chief benefit of accounting software over manual books is that it",
     "computes totals instantly and accurately", "removes the need for source documents", "guarantees profit every year", "files the tax returns itself", "A",
     "The machine never mis-adds."),
    (T_IT, "Medium", "Before switching to a new accounting package, the wise accountant first",
     "backs up all existing data", "deletes the old records", "prints the letterheads", "buys new calculators", "A",
     "No backup invites disaster."),
]

build_batch(
    S,
    "batch_099_waec_accounting2.json",
    "099",
    "WAEC Accounting round 2 (Round 19 lift): buyer's debit note, invoice "
    "on credit sales, sales day book, returns inwards book, opening "
    "entries, nominal and real accounts, golden rule, balance c/d, sales "
    "total posting, bad debts recovered, rent outside trading, discount "
    "allowed in P&L, obsolescence, provision as contra credit, gross "
    "profit b/d, net profit to capital, wages vs salaries, drawings at "
    "cost, liquidity order, working capital N50,000, appropriation "
    "account, partner's salary and drawings in current account, "
    "authorised vs issued capital, share premium, subscriptions in "
    "arrears, receipts and payments nature, fund accounting, control vs "
    "list, transposition divisible by 9, trial balance limits, gross pay "
    "components, joint pension, markup vs margin, acid test, bank's "
    "debtor view, Excel, software accuracy, backups. Scanned against WAEC "
    "r1, NECO rounds 1-2 and the JAMB Accounting banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
