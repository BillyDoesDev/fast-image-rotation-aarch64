import re
import subprocess
from os import path, listdir
from time import perf_counter_ns
import matplotlib.pyplot as plt

# Gather input images
input_imgs = [path.join("./assets/", _) for _ in listdir("./assets/") if "00.png" in _]
input_imgs.sort(key=lambda x: int(re.findall(r"\d+", x)[0]))

# Gather targets
targets = [
    x
    for _ in listdir("./build/")
    if "make" not in _.lower() and
    not re.findall(r"\.", _) and path.isfile(x := path.join("./build/", _))
]
print(f"{targets = }")

angle = 30
trials = 5

# Initialize data collection
data = {target: {img: [] for img in input_imgs} for target in targets}

for input_img in input_imgs:
    print(f"\n\n[operating on {input_img}]...")
    
    for target in targets:
        timestamps = []
        
        for trial in range(trials):
            start = perf_counter_ns()
            r = subprocess.run(
                [
                    "qemu-aarch64-static",
                    target,
                    input_img,
                    path.join("./outputs/", f"{target.split('/')[-1]}_{input_img.split('/')[-1]}"),
                    str(angle),
                ],
                capture_output=True,
            )
            time_elapsed = perf_counter_ns() - start
            if not r.stderr:
                print(f"{target} took {time_elapsed} ns to process {input_img}")
                timestamps.append(time_elapsed)
        
        # Store data for plotting
        data[target][input_img] = timestamps
        
        try:
            print(f"[{target} took about {round((sum(timestamps) / len(timestamps)) / 1e+9, 3)} s on average]\n")
        except ZeroDivisionError:
            pass

fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('#000')
ax.set_facecolor('#000')

for target in targets:
    for input_img in input_imgs:
        times = data[target][input_img]
        if times:
            x = range(1, trials + 1)
            y = [t / 1e+9 for t in times]
            ax.plot(x, y)
            ax.text(x[-1], y[-1], f"{target} on {path.basename(input_img)}", fontsize='small', color='white', ha='left', va='center')

ax.set_title('Processing Time for Targets over Multiple Trials', color='white')
ax.set_xlabel('Trial', color='white')
ax.set_ylabel('Time (s)', color='white')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
ax.tick_params(axis='both', colors='white')

plt.tight_layout()
plt.show()
