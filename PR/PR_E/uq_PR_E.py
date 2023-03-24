import uncertainpy as un
import chaospy as cp

from PR_E import soma

# Function to return the second output (dendrite)
def dendrite(time, values, info):
    return time, info["dendrite"]

if __name__ == '__main__': 
    
    # Initialize the model
    model = un.Model(run=soma,
                    labels=["Time (ms)", "Membrane potential (mV)"])
    
    # Add second output
    feature_list = [dendrite]

    # Define a parameter dictionary
    parameters = {  "C_m" : 3. ,    # membrane capacitance [uF cm**-2]
                    "E_Na" : 60.  , # [mV]
                    "E_K" : -75.   ,# [mV]
                    "E_Ca" : 80.    # [mV]
                    }

    # Create the parameters
    parameters = un.Parameters(parameters)

    # Set all parameters to have a uniform distribution
    # within a 20% interval around their fixed value
    parameters.set_all_distributions(un.uniform(0.2))

    # Perform the uncertainty quantification
    UQ = un.UncertaintyQuantification(model,
                                    parameters=parameters,
                                    features=feature_list)
    # We set the seed to easier be able to reproduce the result
    data = UQ.quantify(seed=10)

    # Plot first total Sobol' indices
    un.plotting.PlotUncertainty(filename="data/soma.h5", folder=u'sobol_total/', figureformat=u'.png', logger_level=u'info').plot_condensed(sensitivity="sobol_total")