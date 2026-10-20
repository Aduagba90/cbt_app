"""Batch 125 - NECO Financial Accounting round 4 (NECO top-up, Round 24).

Lifts NECO Accounting from 137 toward ~180 with angles not yet in any
bank: control accounts, suspense accounts and error correction, stock
valuation (FIFO, LIFO, weighted average), depreciation disposal
accounts, provision for doubtful debts computation, VAT computation,
departmental accounts and petty cash analysis. Scanned against NECO
rounds 1-3, WAEC Accounting (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch125.py -> content/batch_125_neco_accounting4.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_CTRL = "Control and Suspense Accounts"
T_ERR = "Errors and Their Correction"
T_STOCK = "Stock Valuation"
T_DEP = "Depreciation and Disposal"
T_PROV = "Provisions and Adjustments"
T_VAT = "VAT and Departmental Accounts"

PASSAGES = []
PQ = []

Q = [
    # ------------------------------------------------------------- control accounts
    (T_CTRL, "Medium", "All the individual debtor accounts are mirrored in one summary called the",
     "debtors", "creditors", "shareholders", "employees", "A",
     "One account mirrors the whole ledger."),
    (T_CTRL, "Medium", "The purchases ledger control account collects the balances of",
     "creditors", "debtors", "customers", "directors", "A",
     "What the firm owes, in one place."),
    (T_CTRL, "Hard", "The total of a properly kept control account should agree with the",
     "schedule of balances", "bank statement", "trial balance always", "profit figure", "A",
     "The personal list proves the total."),
    (T_CTRL, "Hard", "Discounts allowed to customers appear on the",
     "debit side of the sales ledger control", "credit side of the purchases control", "sales day book only", "cash book never", "A",
     "They reduce what debtors owe."),
    (T_CTRL, "Medium", "Cheques received from customers are credited to the control account and debited to",
     "bank", "sales", "discounts", "purchases", "A",
     "Cash comes in and debt falls."),
    (T_CTRL, "Hard", "A contra entry between the sales and purchases ledgers of the same firm records",
     "offsetting debts", "a cash sale", "a bad debt written off", "a depreciation charge", "A",
     "Amounts owed both ways net off."),

    # ------------------------------------------------------------- errors
    (T_ERR, "Medium", "Errors of commission occur when an entry is posted to the",
     "wrong person's account", "wrong side of the account", "wrong class of account", "no account at all", "A",
     "The right amount, wrong person."),
    (T_ERR, "Hard", "Which of these is a classic error of principle?",
     "a motor van is debited to purchases", "a figure is misread", "the bookkeeper is absent", "two pages stick together", "A",
     "Capital item expensed wrongly."),
    (T_ERR, "Hard", "An error that makes the trial balance disagree is corrected through the",
     "suspense account", "sales account", "capital account", "trading account", "A",
     "It temporarily holds the difference."),
    (T_ERR, "Medium", "Error of complete reversal means an entry was posted to the",
     "wrong sides of the right accounts", "right side of the wrong account", "correct accounts correctly", "omitted books", "A",
     "Debit and credit switch seats."),
    (T_ERR, "Hard", "Errors that do NOT disturb the trial balance agreement are called",
     "omission and commission types", "errors of addition only", "single-entry errors", "bank errors always", "A",
     "Both sides miss the amount equally."),
    (T_ERR, "Medium", "The journal proper is used to correct errors because it",
     "shows the narration of each correction", "is faster than cash", "avoids the ledger", "replaces the trial balance", "A",
     "The story follows the entry."),

    # ------------------------------------------------------------- stock valuation
    (T_STOCK, "Medium", "Under FIFO, issues of stock are priced at the",
     "oldest purchase prices", "newest purchase prices", "average of the year", "selling price", "A",
     "The first goods in leave first."),
    (T_STOCK, "Medium", "Under LIFO, issues are valued at the",
     "most recent prices", "oldest prices", "standard price always", "market price", "A",
     "The last goods in leave first."),
    (T_STOCK, "Hard", "Buying 10 units at N20 and 10 at N30 gives a simple average cost per unit of",
     "N25", "N20", "N30", "N50", "A",
     "Add the prices and halve.", "(20+30)/2"),
    (T_STOCK, "Hard", "Stock of 200 units at N15 each has a value of",
     "N3,000", "N1,500", "N215", "N30,000", "A",
     "Multiply units by unit cost.", "200*15"),
    (T_STOCK, "Medium", "Stock is valued at the LOWER of cost and net realisable value because of the",
     "prudence concept", "entity concept", "matching concept", "consistency concept alone", "A",
     "Caution writes the price."),
    (T_STOCK, "Medium", "Closing stock appears in the balance sheet as a",
     "current asset", "current liability", "fixed asset", "long-term loan", "A",
     "It awaits sale next year."),

    # ------------------------------------------------------------- depreciation and disposal
    (T_DEP, "Medium", "The account that receives the profit or loss on selling a fixed asset is the",
     "disposal account", "trading account", "suspense account", "capital account only", "A",
     "It compares cost and sale."),
    (T_DEP, "Hard", "A machine cost N100,000 with accumulated depreciation of N60,000; its net book value is",
     "N40,000", "N160,000", "N60,000", "N100,000", "A",
     "Cost minus depreciation to date.", "100000-60000"),
    (T_DEP, "Hard", "Selling that machine (cost N100,000, depreciation N60,000) for N50,000 gives a disposal profit of",
     "N10,000", "N50,000", "N40,000", "N20,000", "A",
     "Sale price above book value.", "50000-(100000-60000)"),
    (T_DEP, "Medium", "Depreciation charged for a year is entered in the profit and loss account as an",
     "expense", "income", "asset", "appropriation", "A",
     "It reduces the year's profit."),
    (T_DEP, "Medium", "The double entry for annual depreciation debits depreciation and credits",
     "provision for depreciation", "bank", "sales", "capital", "A",
     "The provision grows each year."),
    (T_DEP, "Hard", "Part-exchange of an old van for a new one introduces into the disposal account the",
     "trade-in allowance", "full cash price", "road licence", "driver's wages", "A",
     "The allowance counts as sale proceeds."),

    # ------------------------------------------------------------- provisions and adjustments
    (T_PROV, "Hard", "Debtors total N80,000 and a 5% provision for doubtful debts is required; the provision is",
     "N4,000", "N76,000", "N84,000", "N8,000", "A",
     "Five per cent of the debtors.", "80000*0.05"),
    (T_PROV, "Hard", "If the existing provision is N3,000 and the new one required is N4,000, the profit and loss account is charged with",
     "N1,000", "N7,000", "N4,000", "N3,000", "A",
     "Only the increase goes to profit and loss.", "4000-3000"),
    (T_PROV, "Medium", "A debt previously written off and now recovered is credited to",
     "bad debts recovered", "sales", "cash only", "discounts", "A",
     "It restores the year's profit."),
    (T_PROV, "Medium", "Insurance of N24,000 paid for a year covers the year; three months fall into next year, so the prepayment is",
     "N6,000", "N18,000", "N24,000", "N2,000", "A",
     "Three-twelfths of the premium.", "24000*3/12"),
    (T_PROV, "Medium", "Electricity of N9,000 for a quarter is owed but unpaid at year end; the accrual charged to this year is",
     "N9,000", "N3,000", "N12,000", "nil", "A",
     "The bill belongs to this year.", "9000"),

    # ------------------------------------------------------------- VAT and departments
    (T_VAT, "Hard", "VAT at 5% on goods sold for N40,000 excluding VAT adds tax of",
     "N2,000", "N40,000", "N42,000", "N5,000", "A",
     "Five per cent of the price.", "40000*0.05"),
    (T_VAT, "Hard", "VAT charged on sales is owed to the tax authority and shown as a",
     "current liability", "current asset always", "sales revenue", "capital reserve", "A",
     "It is collected in trust, then remitted."),
    (T_VAT, "Medium", "Input VAT is the tax a business",
     "pays on its purchases", "charges on its sales", "owes as income tax", "receives as grant", "A",
     "It offsets the output VAT."),
    (T_VAT, "Hard", "Output VAT of N8,000 and input VAT of N5,000 leave the firm to remit",
     "N3,000", "N13,000", "N8,000", "N5,000", "A",
     "Output VAT minus input VAT.", "8000-5000"),
    (T_VAT, "Medium", "Departmental accounts are prepared mainly to reveal each department's",
     "profit or loss", "cash float", "staff list", "floor space", "A",
     "Poor departments stand exposed."),
    (T_VAT, "Medium", "A common basis for sharing rent among departments is",
     "floor space occupied", "staff birthdays", "sales commissions", "random choice", "A",
     "Square metres pay their share."),
]

build_batch(
    S,
    "batch_125_neco_accounting4.json",
    "125",
    "NECO Financial Accounting round 4 (Round 24 top-up): sales and "
    "purchases ledger control accounts, schedules of balances, discounts "
    "allowed, contra entries, errors of commission, principle, reversal "
    "and omission, suspense account corrections, journal narrations, "
    "FIFO and LIFO, average cost N25, stock value N3,000, lower of cost "
    "and NRV, disposal accounts, net book value N40,000, disposal profit "
    "N10,000, trade-in allowances, provision for doubtful debts N4,000 "
    "with N1,000 increase, bad debts recovered, prepayment N6,000, "
    "accrual N9,000, VAT at 5% (N2,000), input vs output VAT and N3,000 "
    "remit, departmental accounts and rent by floor space. Scanned "
    "against NECO rounds 1-3, WAEC Accounting (all rounds) and the JAMB "
    "pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
