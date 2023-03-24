# HH_PR_uncertainpy  
### Uncertainty quantification and sensitivity analysis for a two-compartments neuron model with Uncertainpy
GitHub repository for my project about Uncertainpy : https://github.com/simetenn/uncertainpy 

I've carried out three main analysis:
1. Hodgkin-Huxley model as in Valderrama paper (from Uncertainpy's examples)
2. Pinsky-Rinzel model: a two-compartments model for neurons
3. Pinsky-Rinzel model in the long run

## Folders and files description
In each folder you'll find:
- `model.py` : complete model setup with all the parameters (I've never run this complete model)
- `uq_model.py` : uncertainty quantification and sensitivity analysis for `model.py`. This is the only file that should be run
- a set of sub-folders with the sub-models that I analyzed

In each sub-folder you'll find:
- `model_*.py` : model setup with the chosen subset of parameters (*)
- `uq_model_*.py` : uncertainty quantification and sensitivity analysis for `model_*.py`
- `data/` : output data of `uq_model_*.py`
- `figures/` : output plots for the first order Sobol' indices
- `sobol_total/` : output plots for the first order total Sobol' indices


## Note for [PR_long/](https://github.com/letiziasignorelli/HH_PR_uncertainpy/tree/master/PR_long)
In this folder there are two sub-folders:
- `model_run/` : implementation of PR model with figures examples (taken from : https://github.com/CINPLA/PRmodel)
- `uq_sa/` : uncertainty quantification and sensitivity analysis for PR_long
