import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Historical neuroscience milestones → mapped to Synapse modules
events = [
    ("460 BCE", "Hippocrates: Brain = seat of intelligence", "Foundation of scientific inquiry"),
    ("1897", "Cajal: Neuron Doctrine", "Discrete packets → SynapticPacket schema"),
    ("1952", "Hodgkin-Huxley model", "Realistic action potentials in signal generator"),
    ("1861-74", "Broca & Wernicke areas", "Future zone-specific encoding (Main Core)"),
    ("1848", "Phineas Gage accident", "Virtual lesion testing inspiration"),
    ("1953", "Patient H.M.", "Memory & privacy safeguards"),
    ("1990s", "Decade of the Brain (fMRI, PET)", "Multi-user signal validation"),
    ("2025", "Synapse BTBI (Nigeria)", "First African-led brain-to-brain simulation")
]

dates = [datetime.strptime(year.split()[0] if ' ' not in year else year.split('-')[0], "%Y") 
         if year.isdigit() or '-' in year else datetime.strptime("460", "%Y")] * len(events)
years = [e[0] for e in events]
descriptions = [e[1] for e in events]
synapse_links = [e[2] if len(e)>2 else "" for e in events]

fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(dates, range(len(events)), c='purple', s=100)
for i, (desc, link) in enumerate(zip(descriptions, synapse_links)):
    ax.text(dates[i], i, f"  {desc}\\n     → {link}", va='center', fontsize=10)

ax.set_yticks([])
ax.set_title("Neuroscience History → Synapse BTBI Roadmap", fontsize=16, pad=20)
ax.xaxis.set_major_locator(mdates.YearLocator(100))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.tight_layout()
plt.savefig("timeline/synapse_neuroscience_timeline.png", dpi=300)
plt.close()

print("Timeline image saved: timeline/synapse_neuroscience_timeline.png")
