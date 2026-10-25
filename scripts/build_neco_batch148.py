"""Batch 148 - NECO Financial Accounting round 5 (NECO top-up, R28).

Grows NECO Accounting from 172 toward ~208 with angles not yet in the
bank: the accounting equation by numbers; double-entry destinations
for credit purchases and cash sales; books of original entry
(purchases returns day book, journal proper, petty cash); the cash
book (contra entries, discount allowed, three columns); bank
statement items (standing orders, credit transfers, unpresented
cheques); capital vs revenue expenditure; trading account arithmetic
(net purchases, cost of goods sold); year-end adjustments (prepaid,
accrued, accrued income); current ratio and gross margin arithmetic;
reducing-balance book value; subscriptions in advance; interest on
drawings; balance c/d placement; one-sided posting and the trial
balance; carriage outwards; bad debts recovered; provision treatment
in the balance sheet; the imprest system; source documents; trade vs
cash discount; the purchases ledger. Scanned against NECO rounds
1-4, WAEC Accounting (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch148.py -> content/batch_148_neco_accounting5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_EQ = "The Accounting Equation"
T_BOOKS = "Books of Original Entry"
T_CASH = "The Cash Book"
T_BANK = "Bank Statement Items"
T_CAPREV = "Capital and Revenue Expenditure"
T_TR = "The Trading Account"
T_ADJ = "Year-End Adjustments"
T_RATIO = "Simple Ratios"
T_DEP = "Depreciation Further"
T_CLUB = "Club Accounts Further"
T_PART = "Partnership Further"
T_LEDGER = "Ledger and Trial Balance"
T_BT = "Bad and Doubtful Debts"
T_PETTY = "Petty Cash and Source Documents"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- equation
    (T_EQ, "Hard", "Mama Ngozi's boutique shows assets of N90,000 and debts of N40,000. Her net worth in the business is",
     "N50,000", "N130,000", "N40,000", "N90,000", "A",
     "Assets minus liabilities give capital.", "50000"),
    (T_EQ, "Medium", "When a trader pays cash for a delivery van, the accounting equation shows that",
     "one asset rises as another falls", "capital falls at once", "liabilities rise at once", "assets vanish", "A",
     "Total assets stand still; only the mix moves."),
    (T_EQ, "Medium", "Goods bought on credit from Ade Njoku are recorded by debiting purchases and crediting",
     "Ade Njoku's account", "cash book", "sales account", "capital account", "A",
     "The supplier's account carries the debt."),

    # ------------------------------------------------------------- books
    (T_BOOKS, "Medium", "Goods returned to a supplier because of defects first pass through the",
     "purchases returns day book", "sales day book", "cash book", "petty cash book", "A",
     "Return-outwards begins its journey there."),
    (T_BOOKS, "Medium", "Opening entries, corrections and other unusual items are recorded in the",
     "journal proper", "cash book", "sales day book", "stock card", "A",
     "The book of first and last resort."),
    (T_BOOKS, "Medium", "Stamps, bus fares and cleaning items are best paid from the",
     "petty cash book", "bank account", "capital account", "purchases ledger", "A",
     "Small change for small needs."),
    (T_BOOKS, "Hard", "Cash sales are first recorded in the",
     "cash book", "sales day book", "purchases day book", "returns book", "A",
     "Money movement lives in the cash book."),

    # ------------------------------------------------------------- cash book
    (T_CASH, "Hard", "Cash withdrawn from the bank for office use enters the cash book as a contra entry, meaning",
     "both columns of one book", "no entry is needed", "only the bank column moves", "only the cash column moves", "A",
     "One book, two columns, both ticked."),
    (T_CASH, "Medium", "Discount allowed to a prompt-paying customer is treated in the final accounts as",
     "an expense", "an income", "an asset", "a liability", "A",
     "The seller pays for speedy cash."),
    (T_CASH, "Medium", "A three-column cash book carries columns for cash, bank and",
     "discount", "stock", "wages", "capital", "A",
     "Two money columns and one courtesy column."),

    # ------------------------------------------------------------- bank statement
    (T_BANK, "Medium", "A fixed sum the bank pays out regularly for a customer, say monthly insurance, is a",
     "standing order", "credit transfer", "dishonoured cheque", "dividend warrant", "A",
     "The instruction stands and repeats."),
    (T_BANK, "Medium", "Money paid straight into a customer's bank account by a debtor shows on the statement as a",
     "credit transfer", "standing order", "bank charge", "unpresented cheque", "A",
     "The balance swells without a counter visit."),
    (T_BANK, "Hard", "Cheques the trader has issued and recorded but which have not yet cleared will make the bank statement show a balance",
     "higher than the cash book's", "lower than the cash book's", "equal to the cash book's", "twice the cash book's", "A",
     "The bank has not yet paid out."),

    # ------------------------------------------------------------- capital vs revenue
    (T_CAPREV, "Medium", "Repainting the shop's walls each year is an example of",
     "revenue expenditure", "capital expenditure", "capital receipt", "deferred income", "A",
     "Upkeep never builds an asset."),
    (T_CAPREV, "Hard", "The cost of a new warehouse together with the legal fees on its purchase belong to",
     "capital expenditure", "revenue expenditure", "current assets", "trading expenses", "A",
     "All costs of acquiring the asset join it."),

    # ------------------------------------------------------------- trading account
    (T_TR, "Medium", "In the trading account, net purchases means purchases",
     "less returns outwards", "plus returns outwards", "less returns inwards", "plus carriage outwards", "A",
     "Send-backs shrink what we bought."),
    (T_TR, "Hard", "A grocer began the year with stock of N8,000, bought N64,000 worth of goods, sent back N3,000, and ended with N11,000 on the shelves. Goods actually sold cost him",
     "N58,000", "N61,000", "N64,000", "N47,000", "A",
     "Available stock less what remains.", "58000"),

    # ------------------------------------------------------------- adjustments
    (T_ADJ, "Hard", "Rent paid partly in advance of the year end appears in the balance sheet as a",
     "current asset", "current liability", "fixed asset", "capital loss", "A",
     "The unused months are money parked."),
    (T_ADJ, "Medium", "Commission earned but not yet received at the year end is",
     "accrued income", "deferred income", "prepaid expense", "bad debt", "A",
     "Earned today, collected tomorrow."),
    (T_ADJ, "Hard", "Electricity consumed but unpaid at the year end is charged in full and the unpaid part shown as a",
     "current liability", "current asset", "fixed asset", "capital reserve", "A",
     "Owed light is a debt to be paid."),

    # ------------------------------------------------------------- ratios
    (T_RATIO, "Hard", "A firm's balance sheet shows current assets of N75,000 and current liabilities of N25,000. Its current ratio reads",
     "3 to 1", "1 to 3", "2 to 1", "4 to 1", "A",
     "Divide the one by the other.", "3"),
    (T_RATIO, "Hard", "For every N100 of takings, a trader pays N60 for the goods themselves. His gross profit margin is",
     "40%", "60%", "25%", "75%", "A",
     "Gross profit over sales, in percent.", "40"),

    # ------------------------------------------------------------- depreciation
    (T_DEP, "Hard", "A machine costing N50,000 is depreciated at 20% on reducing balance. Its book value after two years is",
     "N32,000", "N30,000", "N20,000", "N36,000", "A",
     "Eighty per cent, twice over.", "32000"),

    # ------------------------------------------------------------- clubs
    (T_CLUB, "Hard", "Subscriptions received by a club for months not yet enjoyed appear as",
     "a current liability", "a current asset", "accumulated fund", "entrance fees", "A",
     "Next year's money sits in this year's hands."),

    # ------------------------------------------------------------- partnership
    (T_PART, "Medium", "Interest charged on partners' drawings is credited to the",
     "the appropriation account", "trading account", "balance sheet", "partners' capital only", "A",
     "It claws back into shared profit."),
    (T_PART, "Hard", "A partner's current account shows a credit balance when his share of profits",
     "exceeds his drawings", "equals his drawings", "falls below his drawings", "is withheld by the bank", "A",
     "Undrawn earnings pile up to his credit."),

    # ------------------------------------------------------------- ledger & TB
    (T_LEDGER, "Medium", "In a balanced account at the year end, 'balance c/d' is written on the side with the",
     "smaller total", "larger total", "equal totals", "blank side", "A",
     "It tops up the light side to match."),
    (T_LEDGER, "Hard", "Which mistake would make a trial balance disagree?",
     "posting an amount to one side only", "omitting a whole transaction", "a complete reversal of entries", "an error of principle", "A",
     "One-legged entries tilt the scales."),
    (T_LEDGER, "Medium", "The trial balance is prepared chiefly to check the",
     "arithmetic of the ledger", "honesty of the cashier", "value of closing stock", "goodwill of the firm", "A",
     "Columns must agree, or a slip shows."),
    (T_LEDGER, "Medium", "Carriage on goods sold, borne by the seller, is charged to the",
     "profit and loss account", "trading account", "balance sheet", "manufacturing account", "A",
     "Selling costs never touch cost of goods."),

    # ------------------------------------------------------------- bad debts
    (T_BT, "Medium", "A debt written off in an earlier year but recovered now is credited to",
     "bad debts recovered", "sales account", "capital account", "cash book only", "A",
     "Lost hope returns as income."),
    (T_BT, "Hard", "In the balance sheet, the provision for doubtful debts appears as",
     "a deduction from debtors", "an addition to debtors", "a current liability", "capital", "A",
     "Hope's discount trims the debtors."),

    # ------------------------------------------------------------- petty cash & documents
    (T_PETTY, "Medium", "Under the imprest system, the petty cashier is reimbursed",
     "exactly what was spent", "a fixed sum regardless", "double the float", "nothing at all", "A",
     "The float returns to its set level."),
    (T_PETTY, "Medium", "The source document for a credit purchase in the buyer's books is the",
     "supplier's invoice", "receipt voucher", "credit note", "debit note", "A",
     "The bill that came with the goods."),
    (T_PETTY, "Hard", "Of trade and cash discounts, the one actually recorded in the ledger accounts is",
     "cash discount", "trade discount", "both of them", "neither of them", "A",
     "Trade discount is netted off silently."),
    (T_PETTY, "Medium", "The purchases ledger holds the accounts of",
     "suppliers", "customers", "workers", "debtors", "A",
     "Those we owe live there in rows."),
]

build_batch(
    S,
    "batch_148_neco_accounting5.json",
    "148",
    "NECO Financial Accounting round 5 (R28 top-up): equation arithmetic "
    "85,000, van-for-cash mix, credit purchase double entry; purchases "
    "returns day book, journal proper, petty cash, cash sales in the "
    "cash book; contra entry, discount allowed as expense, three "
    "columns; standing order, credit transfer, unpresented cheques "
    "raising the statement balance; repainting as revenue, warehouse "
    "plus legal fees as capital; net purchases, COGS 75,000; prepaid "
    "rent asset, accrued commission, accrued electricity liability; "
    "current ratio 2:1, gross margin 30%; reducing-balance book value "
    "32,000; subscriptions in advance; interest on drawings credited to "
    "appropriation; current account credit balance; balance c/d on the "
    "smaller side; one-sided posting breaks the trial balance; TB "
    "purpose; carriage outwards in P&L; bad debts recovered; provision "
    "as debtors' deduction; imprest reimbursement; supplier's invoice; "
    "cash discount recorded; purchases ledger. Scanned against NECO "
    "rounds 1-4, WAEC Accounting (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
