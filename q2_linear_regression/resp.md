# 2
## d
### What happens as we keep the number of training samples being used constant and we increase the maximum degree of the polynomial being fitted?
#### The model will start being overfitted, because the model will fit the noise produced by each point, so for new points after training it tends to perform poor predictions. The training error will goes to 0 while the degree goes to N-1, but the validation error will increase.

### How does increasing λ for ridge regression affect the results? Intuitively, what do you expect will happen as λ → ∞? Do the resulting plots validate your intuition as you increase ridge_lamdba?

#### Increasing the lambda will penalize more vectors w with big lenght, so the model will have less freedom for big parameters that sometimes fit the noise. Lambda tends to infinite so the model will be a straight line with the smallest size, because w values tend to 0, only remaining the bias w0. Validate, but I observed that the inclination looks to be 0, but i dont know if it always happen.

### Experiment with varying the number of training samples being used. What do you observe with respect to the relationship between the “optimal” model complexity and the number of training samples?

#### With more datapoints the model supports high degrees and high lambdas, with a few points this complexity reduces too.