# Intelligent_Agent
This project analysis the effect of diversity of professions in a team.
## Agent
in Agent.ipynb first a set of individuals will be generated with normal distributions (mus), then their attribute will be assessed by generating a signal for each indivual
with normal distribution (theta = np.random.normal(0, ru)):
```
np.random.normal(theta, np.sqrt(np.abs(theta - m) + 1)) for m in mus
```
### Result
<img src="https://github.com/aicam/Intelligent_Agent/blob/master/result.png?raw=true" />

## DOE
This generates a sample dataset indicates how many users have clicked on a sample advertisement with attributes with uniform distribution of:
````
attributes_p = [.8, .3, .5]
````
You can specify conditions you prefer to have by
```
conditions_constraints = [
    [3, [0, 1, 0]],
    [2, [1, 0, 1]]]
```
First the estimated time the user has spent will be calculated:
```
np.random.uniform(-1, 0) if attr[i] == (i%3 == 0) else np.random.uniform(0, 1)
```
Then the ad is clicked by the chance of:
```
1 if np.random.uniform(0, .8) < (1 - np.e**(- int(es_time/3000)))
```
