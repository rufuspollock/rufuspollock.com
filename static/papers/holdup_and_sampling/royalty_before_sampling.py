import pylab

import scipy.optimize
class DiscreteCostTransactionCostModel(object):
    """For meaning of variables see associated paper"""
    
    # variables for defining search space when using numerical optimization
    kMin = 0.0
    kMax = 3.0
    rMin = 0.0
    rMax = 1.0
    
    def __init__(self, value, costHigh, costLow, probFunction, tau):
        self.value = value
        self.costHigh = costHigh
        self.costLow = costLow
        self.probFunction = probFunction
        self.tau = tau
        
        self.royaltyLow = (self.value - self.costHigh)/self.value
        self.royaltyHigh = (self.value - self.costLow)/self.value
        self.kForRoyaltyLow = self.getKl()
    
    def stage2ProfitCase1(self, kk):
        """
        Get stage 2 profits as function of kk when both innovators participate.
        NB: ignore factor of rv
        """
        return -1 * self.probFunction(kk) * (self.costHigh - self.costLow) - kk * self.tau
    
    def stage2ProfitCase2(self, kk, royalty):
        return (1-self.probFunction(kk))*((1-royalty)*self.value - self.costLow) - kk * self.tau
    
    def getKl(self):
        def tmp(kk):
            return self.stage2ProfitCase1(kk) * -1
        return scipy.optimize.fminbound(tmp, self.kMin, self.kMax)
    
    def kStar(self, royalty):
        def tmp2(kk):
            return self.stage2ProfitCase2(kk, royalty) * -1
        if royalty < self.royaltyLow:
            raise 'It does not make sense to calculate kStar for a royalty %s, since it is less than royaltyLow' % royalty
        elif royalty <= self.royaltyHigh:
            result = scipy.optimize.fminbound(tmp2, self.kMin, self.kMax)
            # because we have kMin = 0 when we have a set a royalty such that kStar
            # < 0 result will simply be very small due to numerical solving
            if result < 0.00001: return 0
            else: return result
        else:
            return 0
    
    def stage1ProfitFunctionRestricted(self, royalty):
        if royalty >= self.royaltyLow and royalty <= self.royaltyHigh:
            kValue = self.kStar(royalty)
            return self.value * royalty * (1-self.probFunction(kValue))
        else:
            return 0
    
    def stage1ProfitFunction(self, royalty):
        if royalty <= self.royaltyLow:
            return self.value * royalty
        else:
            return self.stage1ProfitFunctionRestricted(royalty)
    
    def getOptimalRestrictedRoyalty(self):
        def tmp3(royalty):
            return -1 * self.stage1ProfitFunctionRestricted(royalty)
        # because the function has long 0 sections (below royaltyLow and above royaltyHigh
        # we have to be careful with bounds or the numerical solver will go wrong
        result = scipy.optimize.fminbound(tmp3, self.rMin, self.royaltyHigh)
        return result
    
    def getOptimalRoyalty(self):
        restrictedOptimum = self.getOptimalRestrictedRoyalty()
        relatedProfits = self.stage1ProfitFunction(restrictedOptimum)
        if self.value * self.royaltyLow > relatedProfits:
            return self.royaltyLow
        else:
            return restrictedOptimum
    
    def _helper(self, kk):
        return self.costHigh - self.probFunction(kk) * (self.costHigh - self.costLow)
    
    def getWelfare(self, monopolyRights = True, royalty = None):
        if royalty == None:
            royalty = self.getOptimalRoyalty()
        return 0
    
    def getIndifferentQ(self):
        """
        Get q, the probability of high cost first stage innovation such that
        indifferent between monopoly and no monopoly rights
        Assumes that optimal royalty is greater than royaltyLow
        """
        royalty = self.getOptimalRoyalty()
        if royalty <= self.royaltyLow: # we are in the rL case so q = 0
            return 0
        kstar = self.kStar(royalty)
        largeSurplus = self.value - self.costLow
        numerator = (1 - self.probFunction(kstar)) * largeSurplus - kstar * self.tau
        denominator = self.value - self._helper(self.kForRoyaltyLow) - self.kForRoyaltyLow * self.tau
        return 1 - numerator/denominator
    
import unittest
import math
import random
class DiscreteCostTransactionCostModelTest(unittest.TestCase):
    
    def setUp(self):
        self.ll = 1.0
        def p(k):
            return math.exp(-self.ll * k)
        self.value = 2.0
        self.costHigh = 1.5
        self.costLow = 1.0
        self.tau = 0.1
        self.probFunction = p
        self.model = DiscreteCostTransactionCostModel(self.value, self.costHigh, self.costLow, self.probFunction, self.tau)
        
        # analytic results used for testing
        # =================================
        largeSurplus = self.value - self.costLow
        
        self.royaltyLow = (self.value - self.costHigh)/self.value
        self.royaltyHigh = (self.value - self.costLow)/self.value
        # this depends on the specific p(k) we are using
        self.kForRoyaltyLow = -1/self.ll * math.log(self.tau/(self.costHigh - self.costLow))
        self.assertTrue(self.kForRoyaltyLow > 0, 
            'You have set values such that kForRoyaltyLow < 0 which => k must always be 0')
        
        self.optimalRestrictedRoyalty = (largeSurplus - math.sqrt((self.tau * largeSurplus)/self.ll)) /self.value
    
    def _kStar(self, royalty):
        return max(0, -1/self.ll * math.log(self.tau/((1-royalty)*self.value - self.costLow)))
    
    def _stage1ProfitFunction(self, royalty):
        prob = -1/self.ll * (self.tau/((1-royalty) * self.value - self.costLow))
        if royalty <= self.royaltyLow:
            return royalty * self.value
        elif royalty <= self.royaltyHigh:
            return royalty * self.value * (1 - prob)
        else:
            return 0
    
    def testRl(self):
        self.assertEquals(self.royaltyLow, self.model.royaltyLow)
     
    def testGetKl(self):
        self.assertAlmostEquals(self.kForRoyaltyLow, self.model.getKl(), 5)
    
    def testGetKStar(self):
        royalty = random.random() * (1-self.royaltyLow) + self.royaltyLow
        self.assertAlmostEquals(self._kStar(royalty), self.model.kStar(royalty), 5)
    
    def testStage1ProfitFunction(self):
        royalty = random.random() * (self.royaltyHigh + 1)
        profitFunction = self.model.stage1ProfitFunction
        self.assertAlmostEquals(self._stage1ProfitFunction(royalty), profitFunction(royalty),
            5, 'Royalty: %s' % royalty)
    
    def testGetOptimalRestrictedRoyalty(self):
        exp = self.optimalRestrictedRoyalty
        out = self.model.getOptimalRestrictedRoyalty()
        self.assertAlmostEquals(exp, out, 4)
    
    def testGetWelfare(self):
        pass
        

class Helper(object):
    
    def __init__(self, model):
        self.model = model
        self.eps = 0.01
        self.kValues = [ xx * self.eps for xx in range(self.model.kMax/self.eps)]
        self.rValues = [ xx * self.eps for xx in
            range(self.model.rMax/self.eps)] + [1.0]
    
    def plotFunctionOfKValues(self, function):
        out = [ function(kk) for kk in self.kValues]
        pylab.plot(self.kValues, out)
    
    def plotFunctionOfRoyalty(self, function):
        out = [ function(rr) for rr in self.rValues ]
        pylab.plot(self.rValues, out)
    
    def plotQ(self, variable, varMin, varMax):
        values = [ varMin + xx * self.eps for xx in range((varMax-varMin)/self.eps) ]
        out = []
        for value in values:
            self.model.__dict__[variable] = value
            out.append(self.model.getIndifferentQ())
        pylab.plot(values, out)

def defaultModel():
    ll = 1.0
    def p(k):
        return math.exp(-ll * k)
    value = 2.0
    costHigh = 1.75
    costLow = 0.25  
    tau = 0.2
    probFunction = p
    return DiscreteCostTransactionCostModel(value, costHigh, costLow, probFunction, tau)

def plotDiscreteModelStuff():
    helper = Helper(defaultModel())
    helper.plotFunctionOfRoyalty(helper.model.stage1ProfitFunction)
    # helper.plotQ('tau', 0.2, 0.6)
    # helper.plotstage2ProfitCase1()
    # helper.plotProbabilityFunction()
    pylab.show()

if __name__ == '__main__':
    # unittest.main()
    plotDiscreteModelStuff()
    
