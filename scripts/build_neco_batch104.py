"""Batch 104 - WAEC Financial Accounting round 3 (WAEC top-up, Round 21).

Lifts WAEC Accounting from 103 toward ~150 with fresh, mostly numeric
angles: the accounting equation, double-entry rules, ledger classes, the
imprest system, bank reconciliation causes, depreciation calculations,
accruals and prepayments, bad debts, manufacturing-account structure,
ratio calculations, capital vs revenue expenditure, shares and
debentures, payroll deductions and spreadsheet use. Scanned against WAEC
rounds 1-2, NECO Accounting and the JAMB pool.

    python3 scripts/build_neco_batch104.py -> content/batch_104_waec_accounting3.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_FOUND = "Foundations and Double Entry"
T_BOOKS = "Books of Original Entry"
T_BANK = "Bank Reconciliation and Cash"
T_ADJ = "Depreciation, Accruals and Bad Debts"
T_FIN = "Final Accounts and Ratios"
T_MANU = "Manufacturing Accounts"
T_CAP = "Capital, Shares and Payroll"
T_ICT = "ICT and Ethics"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- foundations
    (T_FOUND, "Medium", "Under the fundamental accounting equation, assets are matched by",
     "capital plus liabilities", "income minus expenses", "sales minus returns", "debits minus credits", "A",
     "What the firm owns is funded by these."),
    (T_FOUND, "Hard", "If total assets stand at N120,000 while creditors are owed N45,000, the owner's stake is",
     "N75,000", "N165,000", "N95,000", "N45,000", "A",
     "Ownings minus owings give capital.", "120000-45000"),
    (T_FOUND, "Medium", "The dual aspect concept records every transaction in",
     "two accounts of equal value", "one account only", "three different books", "random order", "A",
     "Both sides of the entry balance."),
    (T_FOUND, "Medium", "Buying a delivery van on credit debits the",
     "motor van account", "cash account", "sales account", "drawings account", "A",
     "The asset received is debited."),
    (T_FOUND, "Medium", "In double entry, credits record increases in",
     "liabilities and capital", "assets and drawings", "expenses and losses", "purchases and vans", "A",
     "Credit the growing owe-and-own side."),
    (T_FOUND, "Hard", "Nominal accounts are closed off at year end to the",
     "profit and loss account", "statement of financial position only", "sales ledger", "cash book", "A",
     "Their balances feed the profit."),
    (T_FOUND, "Medium", "The personal accounts of customers live in the",
     "sales ledger", "purchases ledger", "general ledger", "private ledger", "A",
     "Debtors fill up its pages."),
    (T_FOUND, "Medium", "Suppliers' personal accounts are kept in the",
     "purchases ledger", "sales ledger", "cash book", "petty cash book", "A",
     "Creditors are listed there."),
    (T_FOUND, "Hard", "The concept that draws a line between the owner's purse and the firm's books is",
     "business entity", "going concern", "prudence", "consistency", "A",
     "The firm stands apart from its owner."),
    (T_FOUND, "Hard", "Recording an asset at its cost, ignoring rises in market value, follows the",
     "historical cost concept", "realisation concept", "matching concept", "dual aspect", "A",
     "Cost price stays in the books."),

    # ------------------------------------------------------------- books
    (T_BOOKS, "Medium", "The imprest system mainly governs the",
     "petty cash book", "sales day book", "cash account", "bank statement", "A",
     "A fixed float is restored each period."),
    (T_BOOKS, "Hard", "A petty cash float of N20,000 ends the month at N3,500; to restore the imprest the cashier receives",
     "N16,500", "N20,000", "N3,500", "N23,500", "A",
     "Spend the float, then top it up.", "20000-3500"),
    (T_BOOKS, "Medium", "Goods sold on credit are first entered in the",
     "sales day book", "cash book", "purchases day book", "returns outwards book", "A",
     "Invoices feed this book first."),
    (T_BOOKS, "Medium", "Goods returned by customers go first to the",
     "returns inwards book", "returns outwards book", "sales day book", "journal proper", "A",
     "They come back towards the seller."),
    (T_BOOKS, "Hard", "Opening entries, corrections and unusual items pass through the",
     "journal proper", "petty cash book", "sales day book", "stock card", "A",
     "It is the odd items' doorway."),
    (T_BOOKS, "Medium", "A cheque received and paid into the bank is recorded on the",
     "debit side of the cash book", "credit side of the cash book", "sales day book", "petty cash book", "A",
     "Cash and bank sit on the debit side."),

    # ------------------------------------------------------------- bank
    (T_BANK, "Medium", "A cheque issued but not yet presented appears in the cash book but not on the",
     "bank statement", "sales invoice", "stock sheet", "wage sheet", "A",
     "The bank knows nothing of it yet."),
    (T_BANK, "Medium", "Lodgments not yet credited cause the bank statement balance to be",
     "lower than the cash book", "higher than the cash book", "equal always", "doubled", "A",
     "The bank has not counted them."),
    (T_BANK, "Hard", "Bank charges on a statement call for an entry that",
     "debits bank charges and credits bank", "debits bank and credits charges", "credits both accounts", "debits both accounts", "A",
     "The charge reduces the balance."),
    (T_BANK, "Medium", "A standing order is a payment made",
     "regularly by the bank on instruction", "once by the customer in person", "by a debtor to a creditor only", "to open an account", "A",
     "The bank pays it every month."),
    (T_BANK, "Hard", "A dishonoured cheque is one that the bank",
     "refuses to pay", "pays twice", "issues itself", "stamps as cleared", "A",
     "The cheque bounces back unpaid."),
    (T_BANK, "Medium", "A credit transfer on a bank statement is",
     "money paid into the account", "money withdrawn by cheque", "a bank loan", "an overdraft fee", "A",
     "The bank balance grows by it."),

    # ------------------------------------------------------------- adjustments
    (T_ADJ, "Medium", "Depreciation is best described as the",
     "spreading an asset's cost over life", "loss of cash through theft", "appreciation of the asset", "the cost of goods bought", "A",
     "Use eats the value year by year."),
    (T_ADJ, "Hard", "A machine costing N800,000 is depreciated at 10% straight line yearly. The yearly charge is",
     "N80,000", "N8,000", "N72,000", "N800,000", "A",
     "Ten per cent of cost each year.", "800000*0.10"),
    (T_ADJ, "Hard", "Under reducing balance at 20%, an asset worth N500,000 depreciates in year one by",
     "N100,000", "N50,000", "N400,000", "N125,000", "A",
     "The rate hits the falling balance.", "500000*0.20"),
    (T_ADJ, "Medium", "Rent owed but not yet paid at year end is a",
     "current liability called an accrual", "current asset called a prepayment", "fixed asset", "capital reserve", "A",
     "The debt hangs at year end."),
    (T_ADJ, "Medium", "Insurance paid in advance for next year is a",
     "prepayment and current asset", "accrual and liability", "long-term loan", "revenue expense only", "A",
     "Next year's cover already bought."),
    (T_ADJ, "Hard", "A debt written off as bad is debited to the",
     "bad debts account", "debtors' account only", "sales account", "provision account", "A",
     "The loss account carries it."),
    (T_ADJ, "Hard", "Creating a provision for doubtful debts follows the accounting concept of",
     "prudence", "entity", "going concern", "money measurement", "A",
     "Caution anticipates losses."),

    # ------------------------------------------------------------- final accounts
    (T_FIN, "Medium", "Gross profit is the difference between sales and",
     "cost of goods sold", "total expenses", "net profit", "purchases only", "A",
     "Trading account finds it first."),
    (T_FIN, "Hard", "With purchases of N420,000, closing stock of N70,000 and no opening stock, cost of goods sold is",
     "N350,000", "N420,000", "N290,000", "N490,000", "A",
     "Purchases minus closing stock.", "420000-70000"),
    (T_FIN, "Medium", "Net profit equals gross profit minus",
     "operating expenses", "cost of sales", "opening stock", "share capital", "A",
     "Overheads chip away here."),
    (T_FIN, "Hard", "Current assets N250,000 and current liabilities N100,000 give a current ratio of",
     "2.5 to 1", "1 to 2.5", "3.5 to 1", "1.5 to 1", "A",
     "Divide assets by liabilities.", "250000/100000"),
    (T_FIN, "Hard", "Stock valued at N50,000 is removed from current assets of N250,000 with current liabilities of N100,000; the acid test ratio is",
     "2 to 1", "2.5 to 1", "3 to 1", "1 to 1", "A",
     "Quick assets over liabilities.", "(250000-50000)/100000"),
    (T_FIN, "Hard", "To compute working capital, current assets are reduced by",
     "current liabilities", "fixed assets", "long-term loans", "capital", "A",
     "It is the short-term cushion."),

    # ------------------------------------------------------------- manufacturing
    (T_MANU, "Medium", "Adding direct wages to direct materials, before any overheads, yields",
     "prime cost", "production cost", "factory cost", "conversion cost", "A",
     "The direct pair forms prime cost."),
    (T_MANU, "Hard", "Direct materials N300,000 and direct wages N150,000 give prime cost of",
     "N450,000", "N150,000", "N300,000", "N600,000", "A",
     "Simply add the direct pair.", "300000+150000"),
    (T_MANU, "Medium", "Factory overhead includes",
     "indirect wages and factory rent", "direct materials used", "sales commission earned", "head office salaries", "A",
     "Indirect factory costs only."),
    (T_MANU, "Hard", "In a manufacturing account, work in progress at the year end is",
     "added to production cost", "deducted from sales", "treated as a liability only", "ignored completely", "A",
     "Unfinished goods count as cost."),
    (T_MANU, "Medium", "The cost of transferring finished goods to the trading account is the",
     "cost of production", "prime cost alone", "selling price", "market value", "A",
     "It feeds the trading account."),

    # ------------------------------------------------------------- capital and payroll
    (T_CAP, "Medium", "Money spent acquiring a delivery truck is",
     "capital expenditure", "revenue expenditure", "deferred revenue", "drawings", "A",
     "Long-life assets come from it."),
    (T_CAP, "Medium", "Repainting the delivery truck is treated as",
     "revenue expenditure", "capital expenditure", "share capital", "goodwill", "A",
     "Upkeep costs are expensed."),
    (T_CAP, "Hard", "Ordinary shares differ from debentures because shareholders are",
     "owners, not lenders", "lenders, not owners", "employees of the firm", "auditors of the firm", "A",
     "Shareholding means ownership."),
    (T_CAP, "Hard", "A worker earning N600,000 a year under PAYE has tax deducted",
     "from salary by the employer", "voluntarily after payday", "by the customer", "by the bank only", "A",
     "The employer remits the tax."),
    (T_CAP, "Medium", "Pension contributions under Nigerian law are deducted",
     "from salary, matched by the employer", "yearly by the government alone", "never from wages", "by trade unions only", "A",
     "Both worker and employer fund it."),

    # ------------------------------------------------------------- ICT
    (T_ICT, "Medium", "In a spreadsheet, the formula to add cells A1 to A10 is written as",
     "=SUM(A1:A10)", "TOTAL(A1-A10)", "ADD A1 TO A10", "SUM=A1+A10", "A",
     "The range sits in brackets."),
    (T_ICT, "Medium", "Accounting software's biggest advantage over manual books is",
     "speed and fewer errors", "larger paper files", "more coffee breaks", "longer audits", "A",
     "Machines sum without slips."),
    (T_ICT, "Hard", "Regular backups of accounting data guard mainly against",
     "data loss from failure or attack", "high electricity bills", "staff promotions", "exchange-rate swings", "A",
     "A spare copy saves the firm."),
    (T_ICT, "Hard", "An accountant who keeps client records confidential observes",
     "professional ethics", "marketing mix", "prudence concept", "going concern", "A",
     "Silence is a duty of the job."),
]

build_batch(
    S,
    "batch_104_waec_accounting3.json",
    "104",
    "WAEC Financial Accounting round 3 (Round 21 top-up): accounting "
    "equation with numeric capital (N55,000), dual aspect, debit and "
    "credit rules, nominal accounts, sales and purchases ledgers, entity "
    "and historical cost concepts, imprest system with float top-up "
    "(N16,500), day books, journal proper, unpresented cheques and "
    "uncredited lodgments, bank charges, standing orders, credit "
    "transfers, dishonoured cheques, straight-line (N80,000) and reducing "
    "balance (N100,000) depreciation, accruals, prepayments, bad debts "
    "and prudence, gross profit, cost of goods sold (N300,000), current "
    "ratio 2.5, acid test 2, working capital, prime cost (N450,000), "
    "factory overhead, work in progress, cost of production, capital vs "
    "revenue expenditure, shares vs debentures, PAYE and pension "
    "deductions, spreadsheet SUM formula, backups and professional "
    "ethics. Scanned against WAEC rounds 1-2, NECO Accounting and the "
    "JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="WAEC",
)
