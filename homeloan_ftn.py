import numpy as np

#### calculates repayment req, years to pay off, and interest charged
#### for a home loan paid off fortnightly or monthly.

## calculate repayment

P = 200000
P0 = P
r = 4.2/100
yr = 30 #years
t = 24 #ftn=24, mth=12 #if want 30years for ftn, use 26
t0 = t

def Compinterest(Pzero, rate, repayments):
	a = (Pzero * rate * ((1+rate) ** repayments))
	b = (((1 + rate) ** repayments) -1)
	c = (a / b)
	global payment
	payment = (a / b)
	return "fortnight payment required: ${:0.2f}".format(c)

Compinterest(P, (r/t), yr*t) #repayments year*12wk or 24ftn

## calculate term, total paid and interest paid

if t == 24:
    t = 26
interest_charged = 0
int_paid = []
count = 0

#account for the two extra payments for ftn payments
ftn_month_adj = list(range(3,(26*(yr+1)),13))

## perform payments
while P > 0:
    if t is 12:
        P = (P + (P*(r/12)) - payment)
        int_paid = np.append(int_paid, P*(r/12))
    else:
        P = (P - payment)
        if interest_charged > 0.5:
            if t is 12:
                P = (P + (P*(r/12)))
                int_paid = np.append(int_paid, P*(r/12))
            else:
                if count not in ftn_month_adj: #brute force in two extra payments / year
                    P = (P + (P*(r/12)))
                    int_paid = np.append(int_paid, P*(r/12))
            interest_charged = 0
        else:
            interest_charged = 1
    count = count + 1

print "Initial loan: $", P0, "@ ", r*100, "%"
print Compinterest(P0, (r/t), yr*t0) #repayments year*12wk or 24ftn
print "years to pay off:", '{:0.2f}' .format(count / float(t))
print "interest charged $", '{:0.2f}'.format((count*payment-P0))

##print interest paid by year
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
a = 0
b = 12
yr = 1
for x in range(5):
	print "interest paid in year", yr , "  $ " + '{:0.2f}'.format(np.sum(int_paid[a:b]))
	yr = yr + 1
	a = a + 12
	b = b + 12
