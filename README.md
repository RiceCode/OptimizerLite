# OptimizerLite
In the logistics world, one of the most important KPI is the container utilization. This means that we will need to pick the correct container size to fit all of the cargos. The OptimizerLite helps by telling the user which container mix they should use given the volume of their cargo (CBM). 


## Steps to run OptimizerLite
1) Clone this repo
2) Enter the CBM in the readLite.xlsx in column A. 
3) install package needed: 
  - pulp
  - openpyxl
4) runs the ContainerOptimizerLite.py script
5) answer the questions in the prompt, and get the results in updatedLite.xlsx.


## Discussion
OptimizerLite determines the container mix useage by using linear programming. Each of these container type has a cost assigned to it. 20' container being the smallest is the cheapest but the least cost efficient. The 45' container is the most expensive but most cost efficient. 

### Objective Function
The objective function is to minimize the cost of containers. 

### Variables
The variables are the different container sizes - 20' container, 40' container, 40H container, 45' container. 

### Constraints 
- All cargos must be filled. Example- if there's 35 CBM, all 35 CBMs must go into one or more container. 




