import uncertainpy as un
import chaospy as cp

from valderrama import valderrama

if __name__ == '__main__': 
    # Initialize the model
    model = un.Model(run=valderrama,
                    labels=["Time (ms)", "Membrane potential (mV)"])

    # Define a parameter dictionary
    parameters = {  "V_0": -10,
                    "C_m": 1,
                    "m_0": 0.0011,
                    "n_0": 0.0003,
                    "h_0": 0.9998,
                    "gbar_Na": 120,
                    "gbar_K": 36,
                    "gbar_L": 0.3,
                    "E_Na": 112,
                    "E_K": -12,
                    "E_l": 10.613}

    # Create the parameters
    parameters = un.Parameters(parameters)

    # Set all parameters to have a uniform distribution
    # within a 20% interval around their fixed value
    parameters.set_all_distributions(un.uniform(0.2))

    # Perform the uncertainty quantification
    UQ = un.UncertaintyQuantification(model,
                                    parameters=parameters)
    # We set the seed to easier be able to reproduce the result
    data = UQ.quantify(seed=10)

    # Plot first total Sobol' indices
    un.plotting.PlotUncertainty(filename="data/valderrama.h5", folder=u'sobol_total/', figureformat=u'.png', logger_level=u'info').plot_condensed(sensitivity="sobol_total")