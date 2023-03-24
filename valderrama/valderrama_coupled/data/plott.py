import uncertainpy as un

#un.plotting.PlotUncertainty(filename="data\PR.h5", folder=u'figures/', figureformat=u'.png', logger_level=u'info').evaluations_2d()
#plot_condensed(sensitivity="sobol_first")(filename="data\PR.h5", folder=u'figures/', figureformat=u'.png', logger_level=u'info')

# pl = un.Data(filename="valderrama.h5").get_labels('valderrama')
# print(pl)

un.plotting.PlotUncertainty(filename="valderrama.h5", folder=u'figures/', figureformat=u'.png', logger_level=u'info').plot_condensed(sensitivity="sobol_total")

# pl = un.Data(filename="PR.h5").get_labels('PR')
# print(pl)

# un.plotting.PlotUncertainty(filename="PR.h5", folder=u'figures/', figureformat=u'.png', logger_level=u'info').plot_condensed(sensitivity="sobol_first")