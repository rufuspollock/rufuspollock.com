import os
import matplotlib.pyplot as pylab

'''Simple linear demand curve.


WTP/Utility of someone purchasing here.

Price drops demand increases
'''
class DemandCurve(object):
    '''Linear demand curve q = const - p'''

    save_path = 'demand_curve'
    fontsize = 18
    const = 10.0
    xmax = const + 1.0
    ymax = xmax
    nice_red = '#A84542'

    def curve(self):
        pylab.plot([0,self.const], [self.const,0], color='k')
        pylab.xlabel('Quantity / Sales')
        pylab.ylabel('Price')
        # must set these to something or it goes weird
        # pylab.xticks([], [])
        pylab.xticks([self.const], ['$q^{max}$'], fontsize=self.fontsize)
        pylab.yticks([self.const], ['$p^{max}$'], fontsize=self.fontsize)

    def _addhline(self, y, xstart, xend):
        pylab.axhline(y, xstart/self.xmax, xend/self.xmax, color='k')

    def _addvline(self, x, ystart, yend):
        pylab.axvline(x, ystart/self.ymax, yend/self.ymax, color='k')

    def _addtick(self, ticks_func, pos, val):
        locs, labels = ticks_func()
        locs = list(locs)
        labels = [ lab.get_text() for lab in labels ]
        ticks_func(locs + [pos], labels + [val], fontsize=self.fontsize)

    def _figtext(self, xx, yy, text, **kwargs):
        pylab.figtext(xx/self.xmax, yy/self.ymax, text, **kwargs)

    def illustrate(self):
        xmax = self.const
        ymax = self.const

        self.curve()

        xx = 2.0 
        yy = ymax - xx
        basefn = 'demand_curve-%s.png'
        self._savefig(basefn % 0)

        self._figtext(xx+1.0, yy, 'High Price, Low Demand', ha='left', va='top')
        pylab.scatter([xx], [yy])
        self._savefig(basefn % 1)

        self._figtext(yy, xx+1.0, 'Low Price\nHigh Demand', ha='left', va='top')
        pylab.scatter([yy], [xx])
        self._savefig(basefn % 2)

        xhere = xmax/2 + 1.0
        yhere = 3*ymax/5
        msg = 'WTP of someone who buys\n(but only just) at this price\n(assumed equal to\n(money-metric) utility)'
        self._figtext(xhere, yhere, msg, ha='left', va='bottom')
        arrow_params={'length_includes_head':True, 'head_starts_at_zero':True,
                'fc': 'black', 'head_width': 0.2 }
        pylab.arrow(xhere, yhere, xx - xhere + 0.5, yy/2 - yhere, **arrow_params)
        pylab.arrow(xhere, yhere, yy - xhere - 0.1, yy/8 - yhere, **arrow_params)
        self._addvline(xx, 0, yy)
        self._addvline(yy, 0, xx)
        self._savefig(basefn % 3)

        self._figtext(2.25, yy/2, 'Total GROSS Welfare', rotation='vertical', va='center', ha='center')
        pylab.fill([0.0, 0.0, xx, xx], [0.0, ymax, yy, 0.0], 'y')
        self._savefig(basefn % 4)

        self._figtext(xmax/2, yy/3, 'Total GROSS Welfare', va='center', ha='center')
        pylab.fill([0.0, 0.0, yy, yy], [0.0, ymax, xx, 0.0], 'y')
        self._savefig(basefn % 5)

    def revenue_and_surplus(self):
        '''So we can use demand curve to calculate utility as well!'''
        xmax = self.const
        ymax = self.const
        xx = xmax / 2.0
        yy = ymax / 2.0
        basefn = 'revenue_and_surplus-%s.png'

        self.curve()

        def _rev():
            pylab.fill([0.0, xx, xx, 0.0], [0.0, 0.0, yy, yy], self.nice_red)
            pylab.xticks([xx], ['$q^{sold}$'], fontsize=self.fontsize)
            pylab.yticks([yy], ['$p^{set}$'], fontsize=self.fontsize)

        _rev()
        self._figtext(xx+0.5, yy/2+0.5, 'REVENUE', rotation='vertical', va='center',
                ha='center', size='x-large')
        self._savefig(basefn % 1)

        xcentre = 2*xx/3
        self._figtext(xcentre, 2*yy/5, 'COSTS', ha='center', va='center', color='white')
        pylab.fill([0.0, xx, xx, 0.0], [0.0, 0.0, yy/2, yy/2], 'black')
        self._savefig(basefn % 2)

        self._figtext(xcentre, 4*yy/5, 'PRODUCER SURPLUS', ha='center', va='center')
        pylab.fill([0.0, xx, xx, 0.0], [yy/2, yy/2, yy, yy], self.nice_red)
        self._savefig(basefn % 3)

        self._figtext(xx/2, 3*ymax/5, 'CONSUMER\nSURPLUS', ha='center')
        pylab.fill([0.0, 0.0, xx], [yy, ymax, yy], 'y', alpha=0.6)
        self._savefig(basefn % 4)

    def effect_of_ip(self):
        xmax = self.xmax
        ymax = self.ymax
        xx = 5.0
        yy = 5.0
        def do_ip():
            self._addhline(5.0, 0.0, 5.0)
            self._addvline(5.0, 0.0, 5.0)
            self._addtick(pylab.xticks, 5.0, '$q^{IP}$')
            self._addtick(pylab.yticks, 5.0, '$p^{IP}$')

        def do_pd():
            self._addhline(2.0, 0.0, 8.0)
            self._addvline(8.0, 0.0, 2.0)
            self._addtick(pylab.xticks, 8.0, '$q^{PD}$')
            self._addtick(pylab.yticks, 2.0, '$p^{PD}$')

        xcentre = 2*xx/3
        def shade_transfer():
            self._figtext(xcentre, 4*yy/5, 'TRANSFER', va='center', ha='center')
            pylab.fill([0.0, 5.0, 5.0, 0.0], [2.0, 2.0, 5.0, 5.0], 'red',
                    alpha=0.5)

        def shade_gain():
            self._figtext(5.5, 3.25, 'D/W\nLOSS')
            pylab.fill([5.0, 8.0, 5.0], [5.0, 2.0, 2.0], 'y', alpha=0.5)

        self.curve()
        do_pd()
        self._savefig('effect_of_ip-1.png')
        do_ip()
        self._savefig('effect_of_ip-2.png')
        shade_transfer()
        self._savefig('effect_of_ip-3.png')
        shade_gain()
        self._savefig('effect_of_ip-4.png')

        self._figtext(xcentre, 1.5, 'COSTS', va='center', ha='center', color='white')
        pylab.fill([0.0, 0.0, 5.0, 5.0], [0.0, 1.5, 1.5, 0.0], 'black')
        self._savefig('effect_of_ip-5.png')

        # overwrite
        self._figtext(xcentre, 1.5, 'COSTS', va='center', ha='center', color='black')
        self._figtext(xcentre, 2.5, 'COSTS', va='center', ha='center', color='white')
        pylab.fill([0.0, 0.0, 5.0, 5.0], [0.0, 3.0, 3.0, 0.0], 'black')
        self._savefig('effect_of_ip-6.png')


    def _savefig(self, fn):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        fn = os.path.join(self.save_path, fn)
        # have to do this last for some reason as o/w reset by other things
        pylab.axis(xmax=self.xmax, ymax=self.ymax)

        # big hack to get rid of axes all the way round
        # f = pylab.gcf()
        ax = pylab.gca()
        # f.set_frameon(False)
        ax.set_frame_on(False)
        # ax.set_axis_off()
        # if you draw at 0 it does not work ??!
        pylab.axhline(0.01, color='k')
        pylab.axvline(color='k')

        # resize
        # just will *not* work -- keeps cutting of parts of the figure
        # fig = pylab.figure(1)
        # fig.set_size_inches(10, 6)

        # adjust bottom so label not cut off
        pylab.subplots_adjust(bottom=0.1)
        dpi = 72.0
        pylab.savefig(fn, dpi=dpi)

    def all(self):
        print 'illustrate'
        self.illustrate()
        pylab.clf()
        print 'revenue_and_surplus'
        self.revenue_and_surplus()
        pylab.clf()
        print 'effect_of_ip'
        self.effect_of_ip()
        pylab.clf()


import optparse
import inspect
if __name__ == '__main__':
    methods = inspect.getmembers(DemandCurve, inspect.ismethod)
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
    
    a = DemandCurve()
    getattr(a, action)()

