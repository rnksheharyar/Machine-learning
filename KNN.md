# K- nearest neibour
k = number of neibours
- k should not be lower
  - Noise
- K should not be heigher
  - Out of sample accuracy will decrease\
Predict the response value based on the neighbour which is nearest and more in numbers
- Minkowski distance

Can be used for numerical data/regression
- Number of rooms
- Years
- Maxumum ratio etc

Important:
- Jaccard index
- F1- score
- Log loss
- many more

**Prop:**
- Training phase is faster
- instance based learning algorithm
- can be used with non-linear data/
**Cons:**
- Testing phase is slower
- Costly for memory and computation
- Not suitable for large dimension\
**How to improve:**
- Data Wrangling and scaling
- Missing value
- Normalizarion on same scale for everything (-1,0-1)
- Reduce dimensions to improve performance