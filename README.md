# Using Neural Network-based Approximation to Improve Performance of HPC Applications 

In this project, we use neural network models to approximate computation of an HPC application to improve performance (reducing execution time) of the application. The neural network should use the same input and output variables as the HPC application.

To use a neural network model to approximate computation, we face multiple research challenges.First, we must make sure that our neural network models can bring a performance benefit. This means the execution time (inference time) of the neural network model should be shorter than that of the original HPC application. To address this issue, we will try different neural network models based on the performance (execution time) of the original code to decide which model should be used. Using such a performance-driven approach to select the model separates us from the existing work where the model accuracy is often used as the only metric to select the model.  

Secondly, we must determine appropriate input and output variables for the neural network models. Those variables are also the input and output variables of the approximated application. 

We  will  study  a  specific  HPC  application,  openFuelCell  in  this  project.  The  openFuelCell is  a  popular code for computational fluid dynamics (CFD) to model fuel cells (http://openfuelcell.sourceforge.net/project).  We  want  to  improve  performance  of  openFuelCell without losing simulation accuracy.

In  the  openFuelCell  project ,  you  can  find  and  run  the  sofcFoam  model  using  the  instructions  in “http://openfuelcell.sourceforge.net/doc/quick-start”.  Use  scripts  under  “/openfuelcell/run/ crossFlow”  to run your openFuelCell code. To use this scrip to run crossFlow, you will need to OpenFOAM version 6. See https://openfoam.org/download/6-ubuntu/ for details.
