"""Batch 072 - NECO Financial Accounting, Paper III Objective round 1.

NECO SSCE Financial Accounting Paper III (Objective) is a 60-item paper
allowed 1 hr 20 min (official 2026 External timetable, paper 3003).
Covers the double entry system, books of prime entry, final accounts,
adjustments, bank reconciliation, control accounts and more. Numeric
answers machine-verified. Near-dup scanned against JAMB, WAEC and the
existing NECO banks.

    python3 scripts/build_neco_batch72.py -> content/batch_072_neco_accounting.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_INTRO = "Nature and Purpose of Accounting"
T_EQ = "The Accounting Equation"
T_LED = "The Ledger and Double Entry"
T_PRIME = "Books of Prime Entry"
T_TB = "The Trial Balance"
T_FIN = "Final Accounts"
T_ADJ = "Adjustments"
T_BANK = "Bank Reconciliation"
T_CTRL = "Control Accounts"
T_MANU = "Manufacturing Accounts"
T_NP = "Accounts of Non-Profit Bodies"
T_ERR = "Errors and the Suspense Account"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------ nature and purpose
    (T_INTRO, "Easy", "Book-keeping differs from accounting in that book-keeping is mainly the",
     "recording of transactions", "interpretation of accounts",
     "auditing of accounts", "setting of taxes", "A",
     "Book-keepers record; accountants analyse and interpret."),
    (T_INTRO, "Easy", "The primary purpose of accounting is to provide",
     "financial information for decisions", "money for the government",
     "jobs for book-keepers", "goods for customers", "A",
     "Users from owners to tax men depend on accounts."),
    (T_INTRO, "Medium", "The accounting concept that requires every transaction to be recorded in money terms is",
     "the money measurement concept", "the prudence concept",
     "the consistency concept", "the dual aspect concept", "A",
     "Only what money can measure enters the books."),
    (T_INTRO, "Medium", "Assets are customarily divided into fixed assets and",
     "current assets", "liquid liabilities", "long debts only",
     "capital reserves", "A",
     "Current assets circulate within a year."),
    (T_INTRO, "Hard", "The concept that treats the owner and the business as separate persons is",
     "the business entity concept", "the going concern concept",
     "the accrual concept", "the matching concept", "A",
     "The owner's pocket is not the business till."),
    (T_INTRO, "Medium", "The users of accounting information include all EXCEPT",
     "a rival company's spies", "the owner", "the bank manager",
     "the tax authority", "A",
     "Legitimate users need accounts for decisions."),

    # ------------------------------------------------------------ equation
    (T_EQ, "Easy", "The accounting equation states that assets equal",
     "capital plus liabilities", "income minus expenses",
     "cash plus bank", "sales minus purchases", "A",
     "What the business owns is funded by owner and creditors."),
    (T_EQ, "Medium", "If total assets are ₦900,000 and liabilities ₦350,000, capital is",
     "₦550,000", "₦1,250,000", "₦900,000",
     "₦350,000", "A",
     "Capital = 900,000 − 350,000.",
     "900000-350000"),
    (T_EQ, "Medium", "A business owns ₦600,000 in assets; its owner's capital is ₦400,000. Liabilities are",
     "₦200,000", "₦1,000,000", "₦600,000",
     "₦150,000", "A",
     "Liabilities = 600,000 − 400,000.",
     "600000-400000"),
    (T_EQ, "Hard", "If a trader introduces an extra ₦100,000 cash into the business, the accounting equation changes by",
     "assets and capital rising ₦100,000", "assets rising, capital falling",
     "liabilities rising ₦100,000", "no change at all", "A",
     "Cash (asset) and capital grow together."),

    # --------------------------------------------------------- ledger/double entry
    (T_LED, "Easy", "The double entry principle requires every debit to have",
     "an equal credit entry", "a bigger credit",
     "no credit at all", "a smaller credit", "A",
     "Each transaction balances both sides."),
    (T_LED, "Easy", "Purchases of goods for cash are entered as debit purchases account and credit",
     "cash account", "sales account", "capital account",
     "debtor account", "A",
     "Cash goes out, so cash is credited."),
    (T_LED, "Medium", "The account that records amounts owed by customers is the",
     "sales ledger (debtors)", "purchases ledger (creditors)",
     "cash book only", "nominal ledger only", "A",
     "Debtors' accounts live in the sales ledger."),
    (T_LED, "Medium", "When goods are sold on credit to Mr. Bello, the debit entry goes to",
     "Mr. Bello's account", "sales account", "cash account",
     "purchases account", "A",
     "The debtor is debited with what he owes."),
    (T_LED, "Hard", "The personal accounts of suppliers from whom goods are bought on credit are kept in the",
     "purchases ledger", "sales ledger", "general ledger only",
     "private ledger only", "A",
     "Creditors fill the purchases ledger."),
    (T_LED, "Medium", "The book regarded as the principal book of accounts is the",
     "ledger", "cash book only", "journal only",
     "trial balance only", "A",
     "All accounts are kept in the ledger."),

    # --------------------------------------------------------- books of prime entry
    (T_PRIME, "Easy", "The book that records all transactions involving cash and bank is the",
     "cash book", "sales day book", "purchases day book",
     "petty cash book only", "A",
     "The two-column cash book covers both."),
    (T_PRIME, "Medium", "Invoices received from suppliers are first listed in the",
     "purchases day book", "sales day book", "cash book",
     "journal proper", "A",
     "Credit purchases enter through it."),
    (T_PRIME, "Medium", "The sales day book records",
     "credit sales only", "cash sales only", "all sales and purchases",
     "returns outwards", "A",
     "Cash sales go straight to the cash book."),
    (T_PRIME, "Medium", "Small payments like stamps and bus fares are recorded in the",
     "petty cash book", "purchases day book", "sales ledger",
     "journal proper", "A",
     "The petty cashier handles small change."),
    (T_PRIME, "Hard", "The returns outwards book records goods",
     "sent back by the business to suppliers", "received back from customers",
     "sold for cash", "bought for cash", "A",
     "Outwards returns leave the business."),
    (T_PRIME, "Medium", "The book used to open accounts, correct errors and record unusual items is the",
     "journal proper", "petty cash book", "sales day book",
     "cash book", "A",
     "The journal proper narrates each entry."),

    # ------------------------------------------------------------- trial balance
    (T_TB, "Easy", "A trial balance is prepared mainly to",
     "check the ledger's arithmetic", "show profit for the year",
     "calculate tax due", "value the closing stock", "A",
     "Agreeing sides suggest balanced books."),
    (T_TB, "Easy", "A trial balance is a list of all ledger balances arranged as debits and credits on a particular",
     "date", "month only", "decade",
     "hour", "A",
     "It snapshots the balances on one day."),
    (T_TB, "Medium", "If the debit column of a trial balance exceeds the credit column by ₦5,000, the difference is placed on the",
     "credit side as suspense account", "debit side as discount",
     "profit and loss account", "balance sheet alone", "A",
     "The suspense account holds the gap."),
    (T_TB, "Hard", "Which error would NOT be revealed by a trial balance?",
     "An error of complete reversal", "An error of addition in one account",
     "Posting ₦700 instead of ₦70", "Omitting one side of an entry", "A",
     "Reversal keeps both sides equal, so it hides."),

    # ------------------------------------------------------------ final accounts
    (T_FIN, "Easy", "The trading account is used to calculate",
     "gross profit", "net profit", "total assets",
     "closing capital", "A",
     "Sales over cost of goods sold gives gross profit."),
    (T_FIN, "Medium", "If sales are ₦250,000 and cost of goods sold ₦150,000, gross profit is",
     "₦100,000", "₦400,000", "₦250,000",
     "₦60,000", "A",
     "Gross profit = 250,000 − 150,000.",
     "250000-150000"),
    (T_FIN, "Easy", "The profit and loss account is prepared to find",
     "net profit", "gross profit", "total purchases",
     "fixed assets", "A",
     "Expenses deducted from gross profit give net profit."),
    (T_FIN, "Medium", "Gross profit ₦120,000 less expenses ₦80,000 gives a net profit of",
     "₦40,000", "₦200,000", "₦120,000",
     "₦80,000", "A",
     "Net profit = 120,000 − 80,000.",
     "120000-80000"),
    (T_FIN, "Easy", "The statement showing assets and liabilities at a given date is the",
     "balance sheet", "trial balance", "cash book",
     "journal", "A",
     "The balance sheet photographs the position."),
    (T_FIN, "Medium", "In the balance sheet, current liabilities are those payable within",
     "one year", "ten years", "one month only",
     "one trading cycle of ten years", "A",
     "Creditors and overdrafts fall due in a year."),
    (T_FIN, "Hard", "Working capital is calculated as current assets minus",
     "current liabilities", "fixed assets", "long-term loans",
     "sales", "A",
     "The margin covers short-term duties."),
    (T_FIN, "Medium", "In the trading account, opening stock plus purchases gives goods available for sale; subtracting closing stock gives the",
     "cost of goods sold", "net profit", "gross profit",
     "sales revenue", "A",
     "Available stock less what remains was sold."),

    # ---------------------------------------------------------------- adjustments
    (T_ADJ, "Medium", "The systematic writing off of a fixed asset's cost over its useful life is",
     "depreciation", "appreciation", "depletion only",
     "valuation", "A",
     "Usage and time consume the asset's worth."),
    (T_ADJ, "Medium", "A machine costs ₦100,000 with a scrap value of ₦10,000 and a life of 5 years. Annual depreciation by the straight line method is",
     "₦18,000", "₦20,000", "₦10,000",
     "₦90,000", "A",
     "(100,000 − 10,000) ÷ 5 = 18,000.",
     "(100000-10000)/5"),
    (T_ADJ, "Medium", "The depreciation method that applies a fixed percentage to the reducing book value each year is",
     "diminishing balance", "straight line", "reevaluation only",
     "sinking fund", "A",
     "The charge falls as the book value falls."),
    (T_ADJ, "Medium", "Rent paid in advance at the year end is treated in the final accounts as a",
     "current asset (prepayment)", "current liability",
     "fixed asset", "long-term loan", "A",
     "The unused rent belongs to next year."),
    (T_ADJ, "Medium", "Electricity consumed but not yet paid for at the year end is an",
     "accrued expense due now", "accrued income",
     "prepayment", "capital reserve", "A",
     "The bill waits in next year, but belongs now."),
    (T_ADJ, "Hard", "A debt finally confirmed uncollectable is written off to the",
     "profit and loss account", "balance sheet only",
     "trading account", "capital account", "A",
     "Bad debts are expenses of the period."),
    (T_ADJ, "Medium", "A provision for doubtful debts is created out of",
     "prudence alone", "profit for expansion",
     "capital for shares", "sales for discounts", "A",
     "Anticipated losses are provided for."),

    # ---------------------------------------------------------------- bank rec
    (T_BANK, "Medium", "A bank reconciliation statement is prepared to explain differences between the",
     "cash book and the bank statement", "trial balance and ledger",
     "trading and P&L accounts", "debtors and creditors", "A",
     "Timing and errors separate the two records."),
    (T_BANK, "Medium", "Unpresented cheques are cheques that have been issued but not yet",
     "presented to the bank for payment", "received by customers",
     "recorded in the cash book", "paid into the bank", "A",
     "The bank knows nothing of them yet."),
    (T_BANK, "Medium", "In preparing a reconciliation starting from the bank statement balance, unpresented cheques are",
     "deducted", "added", "ignored",
     "doubled", "A",
     "They will reduce the bank balance when paid."),
    (T_BANK, "Medium", "Standing orders and bank charges appear on the bank statement first, so they must be entered in the",
     "cash book", "sales day book", "journal proper only",
     "petty cash book", "A",
     "The cash book must catch up with the bank."),
    (T_BANK, "Hard", "A credit transfer received by the bank on behalf of a customer but not yet entered in the cash book will cause the bank statement to show",
     "more than the cash book", "a lower balance",
     "an equal balance", "a nil balance", "A",
     "The bank has added money the trader has not."),

    # ---------------------------------------------------------- control accounts
    (T_CTRL, "Medium", "The sales ledger control account summarises all the accounts in the",
     "sales ledger", "purchases ledger", "nominal ledger",
     "cash book", "A",
     "One control mirrors many debtor accounts."),
    (T_CTRL, "Medium", "The total of the sales day book is debited to the",
     "sales ledger control account", "cash account",
     "purchases ledger control", "capital account", "A",
     "Credit sales swell the debtors' control."),
    (T_CTRL, "Hard", "The purchase of a motor van on credit from Leventis Motors appears in the purchases ledger control account as",
     "a credit entry", "a debit entry", "no entry",
     "a contra entry only", "A",
     "The supplier of the van is a creditor."),
    (T_CTRL, "Medium", "Cheques received from customers that were later dishonoured are recorded in the control account as",
     "debits", "credits", "contra items only",
     "discounts allowed", "A",
     "The debtor's debt springs back."),

    # ------------------------------------------------- manufacturing accounts
    (T_MANU, "Medium", "A manufacturing account is prepared to find the",
     "cost of producing goods", "net profit of a trader",
     "value of total assets", "cash position", "A",
     "Factory costs are gathered first."),
    (T_MANU, "Medium", "In a manufacturing account, prime cost is the total of direct materials, direct labour and",
     "direct expenses", "factory rent alone",
     "office salaries", "selling costs", "A",
     "Prime cost gathers direct costs only."),
    (T_MANU, "Hard", "Factory overheads include all EXCEPT",
     "office cleaning wages", "factory rent",
     "factory power", "supervisor's salary", "A",
     "Office costs belong to the P&L account."),
    (T_MANU, "Medium", "Work in progress at the end of the year is valued as",
     "partly finished goods", "fully finished goods",
     "raw materials only", "sold goods", "A",
     "It stands between raw materials and finished goods."),

    # --------------------------------------------------------- non-profit bodies
    (T_NP, "Medium", "The account of a social club that merely summarises money received and paid is the",
     "receipts and payments account", "income and expenditure account",
     "trading account", "balance sheet only", "A",
     "Like a cash book, it ignores accruals."),
    (T_NP, "Medium", "The account that shows the true surplus or deficit of a non-profit organisation is the",
     "income and expenditure account", "receipts and payments account",
     "subscription account only", "cash book", "A",
     "It matches income with expenses for the year."),
    (T_NP, "Hard", "A club's income and expenditure account replaces which account of a trading firm?",
     "The profit and loss account", "The balance sheet",
     "The cash book", "The trial balance", "A",
     "Surplus or deficit replaces profit or loss."),
    (T_NP, "Medium", "Subscriptions in arrears at the year end of a club are treated as",
     "an asset (amounts receivable)", "a liability",
     "income of the next year only", "a loss written off always", "A",
     "Members still owe the club."),

    # ------------------------------------------------ errors and suspense
    (T_ERR, "Medium", "An error of original entry occurs when",
     "a wrong figure is first recorded", "the ledger is lost",
     "the trial balance agrees", "cash is stolen", "A",
     "The wrong figure travels through."),
    (T_ERR, "Medium", "An error of commission occurs when an entry is posted to",
     "the wrong person's account", "the wrong class of account",
     "no account at all", "both sides at once", "A",
     "Right amount, wrong account of the same type."),
    (T_ERR, "Hard", "An error of principle occurs when, for example,",
     "a motor van is debited to purchases", "rent is posted twice",
     "cash is correctly entered", "a debtor pays his debt", "A",
     "Capital and revenue items are mixed."),
    (T_ERR, "Medium", "The account opened with a trial balance difference pending correction of errors is the",
     "suspense account", "savings account",
     "current account", "capital account", "A",
     "It holds the gap until errors are found."),
]

build_batch(
    S,
    "batch_072_neco_accounting.json",
    "072",
    "NECO Financial Accounting Paper III round 1: the SSCE syllabus - nature "
    "and purpose, the accounting equation (with calculations), double entry "
    "and ledgers, books of prime entry, trial balance, final accounts "
    "(gross/net profit calculations), adjustments (straight-line "
    "depreciation machine-verified, accruals, bad debts), bank "
    "reconciliation, control accounts, manufacturing accounts, non-profit "
    "accounts, and errors/suspense. Near-dup scanned against the JAMB, WAEC "
    "and existing NECO banks.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
