import pylab

def plotOptimalPolicyAsFunctionOfQandP():
    """
    Do plot of q = (1-p)/(1 - alpha p ) from paper
    """
    eps = 0.05
    vH = 1.0
    vL = 0.3
    alpha = 1 - vL/vH
    pValues = [ xx * eps for xx in range(alpha/eps) ] + [alpha]
    def qM(pp, beta):
        return pp * vL / ( (1-pp) * (1 - beta) + pp * vL )
    # draw lines for beta = 0, 0.5, 0.99
    qValues0 = [ qM(pp, 0) for pp in pValues]
    qValuesHalf = [ qM(pp, 0.5) for pp in pValues]
    qValues1 = [ qM(pp, 0.99) for pp in pValues]
    pylab.plot(pValues, qValues0, pValues, qValuesHalf, pValues, qValues1 )
    # also draw vertical line at alpha
    pylab.axvline(alpha, 0, 1)
    pylab.axis(xmax=1.0, ymax=1.0)
    pylab.xlabel('p')
    pylab.ylabel('q')
    pylab.text(0.1, 0.9, 'IP (RH)')
    pylab.text(alpha/1.3, 0.1, 'NIP (RH)')
    pylab.text((1+alpha)/2.0, 0.5, 'IP (RL)')
    pylab.title('Optimal Policy as Function of q and p\n(alpha = %s)' % alpha)
    fig = pylab.figure(1)
    fig.set_figsize_inches(6,5)
    fig.savefig('optimal_policy_as_function_of_q_and_p.png', dpi=75)

def plot2():
    """
    Plot of effect of discounting on innovation behaviour
    """
    delta = 0.9
    eps = 0.05
    rValues = [ xx * eps for xx in range(1.0/eps)]
    netIncomeValues = [ (1-rr)/(1- rr*delta) for rr in rValues]
    pylab.plot(rValues, netIncomeValues)

def plot3():
    """
    Choice of sampling level (k) as function of other variables
    """
    eps = 0.05
    pValues = [xx*eps for xx in range(1.0/eps)]
    pp = 0.9
    kvalues = [xx*eps for xx in range(5.0/eps)]
    vv = 0.5
    tau = 0.25
    payoffs = [ (1-pp**kk) * (vv - kk * tau) for kk in kvalues]
    pylab.plot(kvalues, payoffs)
    
def plotNashEquilibrium():
    """
    Normalize max k to 1
    """
    pylab.xlabel('k')
    pylab.ylabel('r')
    vv = 1.0
    ccL = 0.2
    ccH = 0.5
    tau = 0.5
    netValue = vv - ccL
    
    eps = 0.01
    kkValues =  [ xx * eps for xx in range(1.0/eps)]
    kk1 = 0.4
    rrLKkValues = [ xx * eps for xx in range(kk1/eps)] + [kk1]
    rrHKkValues = [ kk1 + xx * eps for xx in range((1-kk1)/eps)] + [1.0]
    rrL = [ vv - ccH - xx * tau for xx in rrLKkValues]
    rrH = [ vv - ccL - xx * tau for xx in rrHKkValues]
    pylab.plot(rrLKkValues, rrL, 'b')
    pylab.plot(rrHKkValues, rrH, 'b')
    kkFunction1 = [  max(0, -(xx - 0.3)*(xx + netValue/0.3)) for xx in kkValues]
    kkFunction2 = [  max(0, -(xx - 0.7)*(xx + netValue/0.7)) for xx in kkValues]
    kkFunction3 = [  max(0, - netValue *(xx - 0.95)*(xx + 1.0/0.95)) for xx in kkValues]
    pylab.plot(kkValues, kkFunction1)
    pylab.plot(kkValues, kkFunction2)
    pylab.plot(kkValues, kkFunction3)
    fig = pylab.figure(1)
    fig.set_figsize_inches(6,5)
    fig.savefig('reaction_functions_for_k_and_r.png', dpi=75)

def plotProfitsAsFunctionOfRoyaltyRate():
    """
    this is for discrete choice model with transaction costs and royalty rate
    
    p(r) as used here comes from an exponential model p(k) = exp(-ll ** k)
    """
    eps = 0.01
    
    vv = 1.0
    tau = 0.1
    costLow = 0.3
    rHigh = (vv - costLow) /vv
    rValues = [ xx * eps for xx in range(rHigh/eps)]
    def probHighCost(rr):
        """
        p(k(r))
        """
        return min(1, tau / ((1-rr) * vv - costLow))
    profitValues = [ (1-probHighCost(rr)) * rr for rr in rValues]
    probHighCostValues = [ probHighCost(rr) for rr in rValues]
    pylab.plot(rValues, profitValues)
    pylab.title('First Stage Innovator Income as Percentage of Value of an Innovation as a Function of Royalty Rate')

def plotSamplingAsFunctionOfRoyalty():
    """
    Draw graph ----
    """
    eps = 0.1
    sampling2 = 2.0
    rLow = 1.0
    royalty0 = 3.0
    rHigh = 4.0
    def func(xx):
        return (xx-royalty0)*(xx-4)/3.0
    rValues = [0, rLow] + [xx*eps + rLow for xx in range(2/eps)] + [royalty0, 4]
    kValues = [sampling2, sampling2] + [  func(rr) for rr in rValues[2:-2] ] + [0,0]
    pylab.plot(rValues, kValues)
    pylab.axis(ymax = 1.5*sampling2)
    pylab.xticks([0, rLow, royalty0, rHigh], ('0', 'rL', 'r0', 'rH'))
    pylab.yticks([0, sampling2], ('0', 'k2'))
    pylab.xlabel('Royalty Rate')
    pylab.ylabel('Sampling Level')
    pylab.figtext(0.5, 0.5, 'k1(r)')
    fig = pylab.figure(1)
    fig.set_figsize_inches(6,5)
    fig.savefig('sampling_as_function_of_royalty.png', dpi=75)

if __name__ == '__main__':
    plotOptimalPolicyAsFunctionOfQandP()
    # plotSamplingAsFunctionOfRoyalty()
    # pylab.show()
