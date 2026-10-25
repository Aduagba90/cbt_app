"""Batch 186 - NECO Financial Accounting round 6 (NECO top-up, R36).

Grows NECO Accounting from 208 toward ~238 with angles not yet in
the bank: accounting as the language of business; input and output
tax; VAT at 7.5%; the ledger is NOT a book of prime entry; the
bank overdraft as a current liability; net purchases; stock-taking;
leasehold worn down by time; the departmental accounts' purpose;
the paying-in slip; the cash discount calculation; the compound
journal entry; the petty cash voucher; the provision calculation;
the partner's current account; the audit fee as an expense;
internal check; turnover; the final accounts umbrella; the
long-term loan; paid-up capital; cheque endorsement; the stale
cheque; the crossed cheque; the provision deducted from debtors;
net book value; the source document; cash sales into the cash
book; the sum insured family. Scanned against NECO rounds 1-5,
WAEC Accounting (all rounds) and the JAMB pool.

    python3 scripts/build_neco_batch186.py -> content/batch_186_neco_accounting6.json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from batch_common import build_batch  # noqa: E402

S = "Financial Accounting"

T_NAT = "Nature and Purpose of Accounting"
T_VAT = "VAT and Departmental Accounts"
T_BPE = "Books of Prime Entry"
T_CB = "The Cash Book"
T_LED = "The Ledger and Double Entry"
T_BAL = "Final Accounts"
T_ADJ = "Adjustments"
T_CON = "Control Accounts"
T_PAR = "Partnership Accounts"
T_CO = "Capital and Revenue Expenditure"
T_PUB = "Public Sector Accounting"
T_RAT = "Further Ratios"
T_NPO = "Accounts of Non-Profit Bodies"

PASSAGES = []
PQ = []

Q = [
    (T_NAT, "Easy", "Accounting is popularly called the language of",
     "business", "the courts",
     "government alone", "the medical world", "A",
     "Its figures speak to everyone who reads them."),
    (T_VAT, "Medium", "The VAT a trader pays on goods he buys for his business is called his",
     "input tax", "output tax",
     "value added", "excise duty", "A",
     "Tax paid on purchases waits to be recovered."),
    (T_VAT, "Medium", "The VAT a trader charges on the goods he sells is known as his",
     "output tax", "input tax",
     "trading surplus", "customs levy", "A",
     "Tax collected on sales goes to the revenue service."),
    (T_VAT, "Easy", "The current rate of value added tax in Nigeria is",
     "7.5%", "5%",
     "10%", "15%", "A",
     "Seven and a half kobo on every naira.", "7.5"),
    (T_VAT, "Medium", "A large store keeps separate accounts for its textile and food sections chiefly to know",
     "each department's profit", "the manager's birthday",
     "the weight of each item", "the rent of the whole building", "A",
     "Each counter must earn its own keep."),
    (T_BPE, "Medium", "Which of these is NOT a book of prime entry?",
     "The ledger", "The sales day book",
     "The purchases day book", "The petty cash book", "A",
     "The ledger receives postings; it does not originate them."),
    (T_BPE, "Easy", "The first written record of a transaction, from which the books are later written up, is a",
     "source document", "trial balance",
     "balance sheet", "final account", "A",
     "The invoice and the receipt begin every entry."),
    (T_BPE, "Medium", "Goods sold for cash are first recorded in the",
     "cash book", "sales day book",
     "petty cash book", "returns inwards book", "A",
     "Cash sales never pass through the day book."),
    (T_CB, "Easy", "The slip a customer fills and signs when paying money into his bank account is the",
     "paying-in slip", "cheque leaf",
     "credit transfer form", "bank statement", "A",
     "Its counterfoil remains with the depositor."),
    (T_CB, "Medium", "An invoice of N50,000 offers a cash discount of 5% for payment within the month. Paying in time, the customer parts with",
     "N47,500", "N45,000",
     "N52,500", "N50,000", "A",
     "The discount lifts two thousand five hundred off.", "47500"),
    (T_CB, "Medium", "A cheque presented at the bank six months after its date will be rejected as",
     "stale", "post-dated",
     "crossed", "open", "A",
     "Cheques die after six months of waiting."),
    (T_CB, "Medium", "Crossing a cheque with two parallel lines chiefly ensures that it can only be paid into a",
     "bank account", "cash till over the counter",
     "post office", "government purse", "A",
     "The crossing bars the ready cash."),
    (T_CB, "Hard", "A cheque may be passed on to somebody else by the holder signing his name on its back. This signing is the",
     "endorsement", "crossing",
     "counter-signing of officers", "allocation", "A",
     "The back signature passes the paper on."),
    (T_LED, "Hard", "A journal entry that debits two accounts and credits one at the same time is called a",
     "compound entry", "simple entry",
     "opening entry", "closing entry", "A",
     "Several accounts ride in one journal line-up."),
    (T_LED, "Medium", "Purchases less returns outwards give the figure known as",
     "net purchases", "gross purchases",
     "cost of sales", "goods available", "A",
     "What remains after the sent-back goods leave."),
    (T_LED, "Medium", "The amount a company's shareholders have actually paid in on their shares is the",
     "paid-up capital", "authorised capital",
     "called-up capital", "reserve capital", "A",
     "Promises aside, this is the cash that came."),
    (T_BAL, "Medium", "The trading account, the profit and loss account and the balance sheet prepared together at the year end are collectively called the",
     "final accounts", "control accounts",
     "adjustment accounts", "appropriation accounts", "A",
     "Three statements close the year's story."),
    (T_BAL, "Medium", "A bank overdraft appears in the balance sheet among",
     "current liabilities", "current assets",
     "fixed assets", "long-term capital", "A",
     "The bank is owed, and soon."),
    (T_BAL, "Medium", "A loan repayable in five years stands in the balance sheet under",
     "long-term liabilities", "current liabilities",
     "current assets", "trading account", "A",
     "Years away from repayment, it sits below the line."),
    (T_BAL, "Easy", "In the balance sheet, fixed assets are shown at cost less",
     "accumulated depreciation", "bad debts",
     "opening stock", "accrued expenses", "A",
     "What remains is the net book value."),
    (T_BAL, "Medium", "The total sales made in a trading year is simply called the",
     "turnover", "gross profit",
     "surplus", " takings at cost", "A",
     "The wheel of trade turned that much."),
    (T_ADJ, "Easy", "The physical counting of goods on hand at the year end is called",
     "stock-taking", "stock valuation",
     "stocktaking discount", "auditing", "A",
     "Hands count what the cards claim."),
    (T_ADJ, "Hard", "A leasehold building is depreciated over the years of the lease chiefly because its value falls with the passage of",
     "time", "use alone",
     "market prices", "repairs done", "A",
     "Each year of the lease spends itself."),
    (T_ADJ, "Medium", "Debtors stand at N40,000 and the firm keeps a provision for doubtful debts of 5%. The provision figure is",
     "N2,000", "N4,000",
     "N38,000", "N1,600", "A",
     "Five per cent of forty thousand.", "2000"),
    (T_CB, "Medium", "Every payment made out of the petty cash float must be backed by a duly signed",
     "voucher", "cheque leaf",
     "certificate", "receipt from the bank", "A",
     "The voucher tells the float where its money went."),
    (T_CON, "Hard", "Sharing accounting duties among staff so that one person's work automatically checks another's is called",
     "internal check", "internal audit",
     "external audit", "internal control of cash only", "A",
     "No single hand finishes a transaction alone."),
    (T_PAR, "Medium", "A partner's current account may show either a credit or a debit balance depending on whether his share of profit",
     "exceeds his drawings or not", "is taxed or not",
     "is paid in cash or kind", "was earned monthly or yearly", "A",
     "The running account swings both ways."),
    (T_NAT, "Medium", "The fee paid to the firm's auditors appears in the profit and loss account as",
     "an expense", "an income",
     "an asset", "an appropriation of profit", "A",
     "Professional service is a cost of the year."),
    (T_PUB, "Easy", "Money voted for a ministry's spending in a coming year is contained in its",
     "estimate or budget", "balance sheet",
     "receipts book", "vote ledger of accounts", "A",
     "The National Assembly must first agree."),
    (T_RAT, "Hard", "A trader's capital is N200,000 and his net profit for the year is N50,000. His return on capital is",
     "25%", "20%",
     "50%", "4%", "A",
     "Fifty thousand on two hundred thousand.", "25"),
    (T_NPO, "Medium", "A club's statement of affairs shows the accumulated fund standing between its assets and its",
     "liabilities", "members' subscriptions",
     "bar purchases", "entrance fees", "A",
     "What is left over belongs to the members together."),
]

build_batch(
    S,
    "batch_186_neco_accounting6.json",
    "186",
    "NECO Accounting round 6 (R36 top-up): accounting as the "
    "language of business; input and output tax; VAT 7.5%; the "
    "ledger is no book of prime entry; source document; cash sales "
    "into the cash book; paying-in slip; cash discount N47,500; "
    "stale and crossed cheques; endorsement; compound entry; net "
    "purchases; paid-up capital; the final accounts umbrella; bank "
    "overdraft and five-year loan classifications; net book value; "
    "turnover; stock-taking; leasehold and time; provision "
    "calculation N2,000; provision deducted from debtors; internal "
    "check; the partner's current account; audit fee as expense; "
    "the ministry's estimate; return on capital 25%; the club's "
    "statement of affairs. Scanned against NECO rounds 1-5, WAEC "
    "Accounting (all rounds) and the JAMB pool.",
    PASSAGES,
    PQ,
    Q,
    exam_type="NECO",
)
