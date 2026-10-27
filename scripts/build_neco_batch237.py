"""Batch 237 - NECO Financial Accounting round 5 (NECO top-up, R48).

Grows NECO Financial Accounting from 260 toward ~285 with angles
verified absent from the whole Accounting pool (1,019 items across
JAMB, WAEC and NECO) and cleared of cross-subject twins (dropped:
corporation tax — econ company-income-tax family banked; merchant/
development bank, unit trust, primary/secondary market — Commerce;
bonus/rights issues — econ; merger/holding company — Commerce).
Fresh angles: profit-sharing ratio; contingent liability; proforma
invoice; increase in provision for doubtful debts calc; vertical vs
horizontal balance sheet formats; withholding tax; credit balance
in the sales ledger; goods distributed as free samples; carriage on
a new machine; details on an invoice; sacrificing ratio on
admission; income and expenditure account ≈ trading account of a
club; obsolete stock; payslip; shares issued at a discount; the
accounting cycle sequence; dissolution expenses; the debit side as
the left-hand side; 'To' and 'By' in ledger accounts; trial balance
agreement not conclusive; debtors shown net of provision; net
profit transferred to capital; goods transferred at market value
(manufacturing); import duty as part of cost; bank credit and debit
advice. Avoided as banked: the full standard families (cash book
139, trial balance 60, suspense 53, control accounts 43, bank
reconciliation 60, trading/P&L 83, balance sheet 79, depreciation
76, errors and transposition/undercast/reversal, bad debts 36,
stock valuation 34, concepts 50, partnership deed/interest/admission/
dissolution, departmental, branch, bills, PAYE, gross/net pay,
petty cash, marshalling, invoice/credit-note items, share
certificate, dividend warrant, mortgage, carriage placements both,
import-adjacent items, trade discount not recorded ×2, opening/
compound entries, narration, principal book, cash-book nature,
petty-cash advantage, sale-or-return, goods-in-transit/branch,
royalty in prime cost, obsolete-depreciation vs stock, guaranteed
profit, partner loans, interim dividend ×2, cumulative preference,
capital redemption reserve, EPS, FIFO-in-inflation ×3, average
stock/cost per unit, shortage calc, leveraged ratios, audit 40,
stewardship, historical cost, materiality, objectivity, ICT 13.

    python3 scripts/build_neco_batch237.py -> content/batch_237_neco_acct5.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_PART = "Partnership Arithmetic"
T_PCH = "Partnership Changes"
T_PCO = "Partnership, Company and Other Accounts"
T_ADJ = "Final Accounts and Adjustments"
T_FA = "Final Accounts"
T_BS = "The Balance Sheet"
T_SRC = "Source Documents and Books"
T_BAD = "Depreciation, Accruals and Bad Debts"
T_CTRL = "Control Accounts and Reconciliation"
T_LEDGER = "The Ledger"
T_LDE = "The Ledger and Double Entry"
T_NP = "Non-Profit-Making Organisations"
T_STOCK = "Stock Valuation"
T_PAY = "Wages and Payroll"
T_CO = "Company Accounts"
T_NAT = "Nature and Purpose of Accounting"
T_BANK = "Bank Reconciliation and Cash"
T_MAN = "Manufacturing Accounts"

PASSAGES = []
PQ = []

Q = [
    (T_PART, "Medium", "Two partners, Ada and Bola, agreed in their deed to share profits in the ratio 3 : 2. Of a profit of ₦500,000, Bola receives",
     "₦200,000", "₦250,000",
     "₦300,000", "₦150,000", "A",
     "Two shares of five parts fall to Bola."),
    (T_FA, "Hard", "A pending court case against a company, whose outcome is not yet known, may create an obligation in future. Such a possible obligation is reported in the accounts as a",
     "contingent liability", "current liability at once",
     "long-term loan", "capital reserve", "A",
     "It waits upon the judge before it becomes a debt."),
    (T_SRC, "Medium", "An invoice marked 'pro forma' sent to a prospective buyer is one that",
     "shows prices and terms but is not a demand for payment", "must be paid within seven days",
     "is issued only after goods are returned", "replaces the debit note", "A",
     "It says: here is what it would cost — nothing more."),
    (T_BAD, "Hard", "To provide for the cash discounts that debtors are expected to earn when they settle their accounts promptly, a trader creates a",
     "provision for discounts on debtors", "provision for bad debts",
     "discount received account", "suspense account for discounts", "A",
     "Prompt payers will be rewarded; the books prepare for it."),
    (T_BS, "Medium", "A balance sheet that runs from top to bottom as one continuous column of items, instead of having two sides, is prepared in the",
     "vertical format", "horizontal format",
     "diagonal format", "narrative format", "A",
     "The modern statement reads like a page, not a scale."),
    (T_PAY, "Hard", "A tax deducted at source from payments such as rent, interest, directors' fees and professional charges, and remitted to government on behalf of the recipient, is",
     "withholding tax", "withheld salary",
     "wealth tax", "welfare levy", "A",
     "The payer collects the tax before the money moves on."),
    (T_CTRL, "Medium", "A credit balance on a customer's account in the sales ledger means that",
     "the customer has paid in more than he owes", "the customer owes the business money",
     "the account must be written off", "the customer has returned all goods", "A",
     "Rare, but real — the debt now runs the other way."),
    (T_LDE, "Medium", "When a trader gives away goods from his store as free samples to advertise his business, the goods are debited to the",
     "advertisement account", "sales account",
     "purchases returns account", "capital account", "A",
     "The gift is a cost of winning customers."),
    (T_ADJ, "Medium", "The carriage paid on a newly bought machine, together with its installation charges, is treated as",
     "part of the cost of the machine", "an expense in the profit and loss account",
     "an item of revenue expenditure", "a loss on purchase", "A",
     "Every cost of bringing the asset to work joins its cost."),
    (T_SRC, "Medium", "Among other details, a properly prepared invoice normally shows the",
     "quantity, description, price and terms", "names of the firm's external auditors",
     "the director's private home address", "the staff payroll numbers used", "A",
     "The bill of sale tells the whole trade in few lines."),
    (T_PCH, "Hard", "On the admission of a new partner, the ratio in which the old partners give up portions of their profit shares in favour of the newcomer is the",
     "sacrificing ratio", "dissolution ratio",
     "gearing ratio", "realisation ratio", "A",
     "The old hands yield ground by this measure."),
    (T_NP, "Medium", "In the final accounts of a social club, the income and expenditure account serves the same purpose as the",
     "trading and profit and loss account", "the receipts and payments account",
     "the statement of affairs of a trader", "the cash book of the club", "A",
     "The club's surplus plays the profit's part."),
    (T_STOCK, "Medium", "Stock of an old design that can no longer be sold at its normal price should be valued in the accounts at",
     "the reduced amount it can now fetch", "its original cost price as bought",
     "the price of the newest stock", "twice its cost for safety", "A",
     "The shelf remembers old prices; the books must not."),
    (T_PAY, "Easy", "The document prepared for each employee at the end of a pay period, showing gross pay, all deductions and the net pay, is the",
     "payslip", "receipt",
     "voucher", "invoice", "A",
     "One small paper tells the worker his wage's whole story."),
    (T_CO, "Medium", "When a company allots its ₦1 ordinary shares to subscribers at 90 kobo per share, the shares are said to be issued",
     "at a discount", "at a premium",
     "at par", "at a profit", "A",
     "Below the face value is a discount by law."),
    (T_NAT, "Medium", "The complete sequence — transaction, source document, books of prime entry, ledger, trial balance and final accounts — is together called the",
     "accounting cycle", "trading cycle",
     "credit cycle", "cash cycle", "A",
     "Every naira's journey through the books, in order."),
    (T_PCO, "Medium", "On the dissolution of a partnership, the expenses incurred in selling off the assets, such as auctioneer's fees, are debited to the",
     "realisation account", "revaluation account",
     "capital account of the partner who paid", "profit and loss account", "A",
     "The costs of unwinding the firm enter at the realisation door."),
    (T_LEDGER, "Easy", "In every ledger account, the debit side is the",
     "left-hand side", "right-hand side",
     "outer side only", "side chosen by the accountant", "A",
     "Debit keeps to the left, as bookkeepers say."),
    (T_LEDGER, "Medium", "In the traditional wording of ledger accounts, the word used on the debit side of an account is",
     "'To', as in 'To Bank'", "'By', as in 'By Bank'",
     "'From', as in 'From Bank'", "'At', as in 'At Bank'", "A",
     "Old ledgers still speak this little language."),
    (T_CTRL, "Medium", "The agreement of the two sides of the trial balance is",
     "not conclusive proof that the books are free of errors", "final proof that no error exists",
     "proof that all entries are complete", "proof that the balance sheet is correct", "A",
     "Some errors are too polite to disturb the totals."),
    (T_FA, "Medium", "In the balance sheet, the amount shown for debtors is the total debtors",
     "less the provision for doubtful debts", "plus the provision for doubtful debts",
     "before any provision", "plus bad debts written off", "A",
     "The doubtful part is shaved off before the figure is shown."),
    (T_LDE, "Medium", "At the end of the trading year, the net profit shown by the profit and loss account is transferred to the",
     "capital account", "drawing account",
     "suspense account", "trading account", "A",
     "The year's gain swells the owner's stake."),
    (T_MAN, "Hard", "Some firms transfer the cost of finished goods to the trading account at the market price of those goods rather than at cost, so as to reveal a notional profit on manufacture. The market price is credited to the",
     "manufacturing account", "profit and loss account",
     "sales account", "balance sheet", "A",
     "The factory's silent gain is credited where it was made."),
    (T_ADJ, "Medium", "Import duty paid on goods bought for resale is accounted for as",
     "part of the cost of the goods purchased", "a revenue expense of the office",
     "an item of carriage outwards", "a deduction from sales", "A",
     "The tax at the port belongs to the cost of the stock."),
    (T_BANK, "Medium", "When the bank sends a credit advice to a customer, it means that",
     "money has been paid into the customer's account", "the customer's account has been charged",
     "a cheque has been dishonoured", "the account has been closed", "A",
     "Good news travels by credit advice."),
]

build_batch(
    S,
    "batch_237_neco_acct5.json",
    "237",
    "NECO Financial Accounting round 5 (R48 top-up): profit-sharing "
    "ratio; contingent liability; proforma invoice; increase in "
    "provision calc; vertical format; withholding tax; credit balance "
    "in sales ledger; free samples; carriage on a new machine; "
    "invoice details; sacrificing ratio; income and expenditure "
    "account of a club; obsolete stock; payslip; shares at a "
    "discount; accounting cycle; dissolution expenses; debit side; "
    "'To' and 'By'; trial balance not conclusive; debtors net of "
    "provision; net profit to capital; market value of goods "
    "transferred; import duty; bank credit advice. Scanned against "
    "the whole Accounting pool (JAMB, WAEC and NECO stems).",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
