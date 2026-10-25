import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)

cube = rng.random((6, 8, 4))

print(cube.shape)

band_three = cube[:, :, 2]

print(band_three.shape)

spectrum = cube[2, 3, :]
print(spectrum)

plt.imshow(band_three)
plt.colorbar(label="Simulated reflectance")
plt.title("Simulated HSI — Band 3")
plt.xlabel("Column (pixel index)")
plt.ylabel("Row (pixel index)")
plt.savefig("reports/figures/band_three.png")

plt.figure()
plt.plot(spectrum, marker="o")
plt.title("Simulated spectrum — Pixel (2, 3)")
plt.xlabel("Spectral band index")
plt.ylabel("Simulated reflectance")
plt.savefig("reports/figures/pixel_spectrum.png")

plt.show()
