import numpy as np
import matplotlib.pyplot as plt

# A LiDAR point 2 m ahead and 1 m to the left of the sensor

p = np.array([2.0, 1.0])

# Rotate it by 30 degrees (the sensor is mounted at an angle)
theta = np.deg2rad(30)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])

p_rot = R @ p  # @ is a matrix multiplicaiton

print("original:", p, "length:", np.linalg.norm(p))
print("rotated: ", p_rot, "length:", np.linalg.norm(p_rot))
print("det(R) =", np.linalg.det(R))  # what does this number mean?

plt.quiver([0,0], [0,0], [p[0], p_rot[0]], [p[1], p_rot[1]], angles='xy', scale_units='xy', scale=1, color=["tab:blue", "tab:orange"], label='original')
plt.xlim(-1, 3); plt.ylim(-1,3); plt.gca().set_aspect("equal"); plt.grid(True)
plt.title("rotation preserves length")
plt.show()