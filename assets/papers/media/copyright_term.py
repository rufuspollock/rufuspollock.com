import os
import math

import matplotlib.pyplot as pylab

class CopyrightTradeoff(object):
    cache_path = 'copyright_term'
    
    # config for plots
    amount = 10.0
    # slightly exaggerated decay rates to make things clearer
    cdrate = 0.9
    drate = 0.9
    num_years = 10
    years = range(0, 2*num_years, 2)
    past = [ -ii for ii in years ]
    production = [ amount ] * num_years
    today = [ amount * cdrate**ii for ii in years ]
    rtoday = list(today)
    rtoday.reverse()
    fullwidth = 0.8
    dw_width = fullwidth * 0.5
    barparams = { 'fc': 'blue', 'width': fullwidth, 'align': 'center',
            'alpha': '0.5'}

    ymax = 1.5 * amount

    def _xticks(self):
        tlabels =  ['Today'] + [''] * 3 + ['<------------- The Past ------------------']
        pylab.xticks(self.past, tlabels)
        pylab.xlim(xmax=2, xmin=self.past[-1]-2)
        pylab.figtext(0.1, 0.4, '.....', size='xx-large')

    def over_time(self):
        pylab.bar(self.past, self.production, **self.barparams)
        self._xticks()

    def over_time_with_decay(self):
        pylab.bar(self.past, self.today, **self.barparams)
        self._xticks()

    past_dw_xxs = [ xx + barparams['width']/2 for xx in past ]
    def tradeoff(self, startterm=3):
        def _showpd(term):

            termyear = self.past[term] + 1.25
            pylab.plot([termyear,termyear], [0,self.ymax], 'k')
            pylab.annotate('Public Domain', (self.past[-1], self.amount),
                    (termyear-3.5,self.amount))
            pylab.arrow(termyear-4, self.amount+0.2, -3, 0, head_width=0.2,
            fc='black', head_starts_at_zero=True)

        def _dw(term):
            # add offset for width of bar
            pylab.bar(self.past_dw_xxs[term:], self.today[term:], width=self.dw_width,
                    fc='red', alpha=0.5)

        self.over_time_with_decay()
        _showpd(startterm)
        _dw(startterm)
        self._xticks()
        self._savefig('over_time_tradeoff-%s-%s.png' % (startterm, 1))

        pylab.clf()

        # now with longer term
        self.over_time_with_decay()
        _showpd(startterm+1)
        _dw(startterm+1)

        # show old term
        oldtermyear = self.past[startterm] + 1.25
        pylab.plot([oldtermyear,oldtermyear+0.01], [0,self.ymax], 'k--')

        # extra production
        extras = [ 0.25/startterm * x for x in self.today ]
        newparams = dict(self.barparams)
        newparams['fc'] = 'yellow'
        pylab.bar(self.past, extras, bottom=self.today, **newparams)
        pylab.bar(self.past_dw_xxs[startterm+1:], extras[startterm+1:],
                bottom=self.today[startterm+1:], width=self.dw_width,
                fc='yellow', alpha=0.5)

        # extra d/w loss
        lostdw = self.past[startterm]+self.barparams['width']/2
        pylab.bar([lostdw], self.today[startterm], fc='black',
                width=self.dw_width)

        self._xticks()
        self._savefig('over_time_tradeoff-%s-%s.png' % (startterm, 2))

        pylab.bar([-3], [2*25/startterm**2], bottom=10, width=1, fc='yellow', alpha=0.5)
        pylab.bar([-4.5], [1.5*5/startterm], bottom=10, width=1, fc='black')
        self._savefig('over_time_tradeoff-%s-%s.png' % (startterm, 3))

    def revenue(self):
        pylab.bar(self.years, self.today , **self.barparams)

        def _xticks():
            tlabels =  ['Today'] + [''] * 3 + ['------------- The Future ------------------>']
            pylab.xticks(self.years, tlabels)
            pylab.xlim(xmin=-2, xmax=self.years[-1]+2)
            pylab.figtext(0.9, 0.4, '.....', size='xx-large')

        _xticks()
        self._savefig('over_time_for_revenue.png')

        rtoday_discounted =  [ xx*self.drate**ii for (ii,xx) in enumerate(self.today)
                ]
        newparams = dict(self.barparams)
        newparams['fc'] = 'red'
        pylab.bar(self.years, rtoday_discounted, **newparams)
        self._savefig('over_time_for_revenue_discounted.png')

        pylab.clf()
    
    fontsize = 'large'
    def works_to_welfare(self):
        import math
        xxs = range(0,100)
        vals = map(lambda x: math.log(x+1.0), xxs)
        pylab.bar(xxs, vals, 'k')
        pylab.xlabel('No. of Works', fontsize=self.fontsize)
        pylab.ylabel('Welfare', fontsize=self.fontsize)
        pylab.xticks([], [])
        pylab.yticks([], [])
        fn = 'works_to_welfare.png'
        fp = os.path.join(self.cache_path, fn)
        # pylab.savefig(fp, dpi=75)
        self._savefig(fn)

    def all(self):
        self.over_time()
        self._savefig('over_time.png')
        pylab.clf()

        self.over_time_with_decay()
        self._savefig('over_time_with_decay.png')
        pylab.clf()

        self.tradeoff(startterm=3)
        pylab.clf()
        self.tradeoff(startterm=6)
        pylab.clf()

        self.revenue()
        pylab.clf()
        self.works_to_welfare()
        pylab.clf()

    def _savefig(self, fn):
        if not os.path.exists(self.cache_path):
            os.makedirs(self.cache_path)
        fp = os.path.join(self.cache_path, fn)
        pylab.ylim(ymax=self.ymax)
        pylab.yticks([],[])

        # hack to get rid of axes ...
        ax = pylab.gca()
        ax.set_frame_on(False)
        # if you draw at 0 it does not work ??!
        pylab.axhline(0.01, color='k')

        # pylab.grid()
        fig = pylab.figure(1)
        fig.set_size_inches(10, 6)
        pylab.savefig(fp, dpi=75)

import optparse
import inspect
if __name__ == '__main__':
    methods = inspect.getmembers(CopyrightTradeoff, inspect.ismethod)
    methods = filter(lambda (name,y): not name.startswith('_'), methods)
    methods = dict(methods)

    usage = '''%prog {action}

action:
    '''
    usage += '\n    '.join(methods.keys())
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    action = args[0]
    if not action in methods:
        print 'Invalid action: %s' % action
        parser.print_help()
        sys.exit(1)
    
    a = CopyrightTradeoff()
    getattr(a, action)()

