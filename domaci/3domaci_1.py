initial_height = 1.0 # the initial height of the ball (in meters)
bounce_coefficient = 0.8 # the coefficient of restitution (bounce factor) of the ball
bounces = [] # a list to store the height of the ball after each bounce
current_height = initial_height # initialize the current height to the initial height

while current_height > 0.01: # keep bouncing until the ball stops bouncing (stops at 1cm)
    bounces.append(current_height) # add the current height to the list of bounces
    current_height *= bounce_coefficient # calculate the height of the next bounce
    print("The ball bounced to a height of", round(current_height, 2), "meters.")
    
num_bounces = len(bounces) - 1 # calculate the total number of bounces (excluding the first drop)
max_heights = [] # a list to store the maximum height of each bounce

print("The ball bounced", num_bounces)

x0=1
x=x0
visine=[]
koef=0.8 #koeficijent odbijanja
while x > 0.01:
    x=koef*x
    print(round(x,3))
    visine.append(x)
print(visine, len(visine)-1)