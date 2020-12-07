from dog import Dog

Rex = Dog("Golden", 8)      # Make a Dog instance, Rex.
Spot = Dog("Pit Bull", 12)  # Make another Dog instance, Spot.
Rex.addTrick("roll over")   # Add a trick to Rex.
Spot.addTrick("sit")        # Add a trick to Spot.
Spot.addTrick("play dead")  # Add another trick to Spot.

print(Rex.kind)             # Print kind, which is inherited by all Dogs.
print(Spot.kind)
print(Rex.breed)            # Breed is specified at instantiation.
print(Rex.age)              # Age is specified at instantiation.
print(Spot.breed)
print(Spot.age)
print(Rex.tricks)           # All dogs have a tricks array.
print(Spot.tricks)

Spot.age += 1   # You can modify Dog properties
Spot.weight = 70
# Just added a property to
# spot from outside the class.
# This is bad form.

print(Spot.age)             # See the age has been modified
print(Spot.weight)          # You're allowed to do this, but ew.
print(Spot.bark())          # The bark method returns "arf."