def f_G(G, m1, m2, r):
    return G*m1*m2*(r**-2)

G = 6.67408 * 10**(-11)
m_M = 7.34767309 * 10**22
m_H = 80

r_l = 356400000

r_h = 406700000

min_force = f_G(G, m_H, m_M, r_h)
max_force = f_G(G, m_H, m_M, r_l)
diff_force = max_force - min_force
diff_kg = diff_force / 9.81

print("Min: ", min_force)
print("Max: ", max_force)
print("Diff: ", diff_force)
print("Diff in kg: ", diff_kg)
print("Diff in mg: ", diff_kg*10**6)