#### calculates repayment req, years to pay off, and interest charged
#### for a home loan paid off fortnightly.

## calculate repayment

P = 185000
Po = P
r = 4.2/100
yr = 30 #years
t = 24 #ftn

def Compinterest(Pzero, rate, repayments):
	a = (Pzero * rate * ((1+rate) ** repayments))
	b = (((1 + rate) ** repayments) -1)
	c = (a / b)
	global payment
	payment = (a / b)
	return "fortnight payment required: ${:0.2f}".format(c)

Compinterest(P, (r/t), yr*t) #repayments year*12wk or 24ftn

## calculate term, total paid and interest paid

interest_charged = 0
count = 0

#account for the two extra payments for ftn payments
ftn_month_adj = list(range(3,(26*(yr+1)),13))

## perform payments
while P > 0:
	P = (P - payment)
	if interest_charged > 0.5:
		if count not in ftn_month_adj: #brute force in two extra payments / year
			P = (P + (P*(r/12)))
		interest_charged = 0
	else:
		interest_charged = 1
	count = count + 1
#	if count < 26:
#		print '{:0.2f}'.format(P)
#		print '{:0.2f}'.format(P*(r/12))

print "Initial loan: $", Po, "@ ", r*100, "%"
print Compinterest(Po, (r/t), yr*t) #repayments year*12wk or 24ftn
print "years to pay off:", '{:0.2f}' .format(count / float(26))
print "interest charged $", '{:0.2f}'.format((count*payment-Po))


#cba says 25.9
#we calc 25.6
#not too bad.
