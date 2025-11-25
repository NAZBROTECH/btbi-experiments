# Brain-to-Brain Interface (BTBI) Experiments

Welcome! 👋  
This repository documents my personal journey exploring **Brain-to-Brain Interfaces (BTBI)**.  

I am **Elon Paul Anozie Nnamdi**, based in Nigeria, and I am deeply interested in how humans might one day communicate thoughts directly — beyond traditional modes of speech or text. While I am starting small with open resources, my long-term vision is to contribute meaningfully to this exciting frontier of neuroscience and technology.  

---

## 📌 Goals
- Learn the foundations of **Brain-Computer Interfaces (BCI)**.  
- Run simple experiments with accessible hardware (EEG, Arduino, biosignal kits).  
- Explore pathways toward **direct brain-to-brain communication**.  
- Share all progress openly for collaboration and learning.  

---

## 🌍 Why This Project?
I believe BTBI has the potential to:
- Transform how humans connect and understand each other.  
- Support people with disabilities through new communication channels.  
- Open up new frontiers in neuroscience, AI, and human collaboration.  

---

## 🛠 Current Focus
- Collecting resources and learning materials.  
- Connecting with global BCI/BTBI communities (OpenBCI, NeuroTechX).  
- Planning small, proof-of-concept projects as stepping stones.  

---

## 📖 Future Plans
- Document experiments (e.g., simple EEG → computer outputs).  
- Progress toward remote brain-to-brain demonstrations.  
- Collaborate with researchers, hobbyists, and labs worldwide.  

---

## 📚 Resources
Some beginner-friendly resources I am using:  
- [OpenBCI Documentation](https://docs.openbci.com/) – Learn about open-source EEG hardware and software.  
- [NeuroTechX Community](https://neurotechx.com/) – A global community for neurotechnology enthusiasts.  
- [Introduction to Brain–Computer Interfaces (Coursera)](https://www.coursera.org/learn/brain-computer-interface) – Free/paid course on BCI basics.  
- [Awesome BCI GitHub Repo](https://github.com/NeuroTechX/awesome-bci) – Curated list of BCI projects, tools, and research.  
- [EEGLearn](http://eeglearn.org/) – Tutorials for EEG and brain-signal processing.  

---

## 🤝 Contributions & Collaboration
I welcome ideas, suggestions, and collaboration opportunities.  
If you’re working on BCI or BTBI and would like to connect, please feel free to open an issue or reach out.  

---

## 📬 Contact
- GitHub: [NAZBROTECH](https://github.com/NAZBROTECH)  
- Location: Nigeria  

---

✨ *This repo is both a learning diary and an open call for collaboration on the future of direct human communication.*  
📄 For the detailed project vision, see [PROJECT_PLAN.md](PROJECT_PLAN.md)
## 🧩 Lessons from DIY EEG Projects  
Real EEG hardware faces major limitations:
- Very low signal strength  
- High noise and electrical interference  
- Latency jitter  
- Unstable electrodes  
- Amplifier saturation  

Synapse does **not** capture real brain signals.  
To reflect real-world constraints, we include simulated “failure modes” that show how signals degrade in practice.



🎮 Neurogame Simulation Module (EEG-Driven Game Logic)

This project now includes a Neurogame Simulation module inspired by real EEG-based games such as those built using Muse, OpenBCI, and research-grade headsets.

Because Synapse does not use real EEG signals, we provide a realistic simulation of two common neurogame metrics:

Attention

Relaxation

These values are commonly mapped to:

Focus-based movement

Meditation-based calm mechanics

Neurofeedback visualizations

Brain-controlled difficulty scaling

🧠 Simulated Brain Signals

modules/neurogame_sim.py generates continuous EEG-like values with:

Smooth signal drift

Random biological noise

Occasional signal dropout (like electrode loss)

Optional amplifier saturation events

This helps users understand why real neurotech is highly unstable, especially in DIY projects.

Example generated output:

ATT=0.62  REL=0.41
ATT=0.58  REL=0.47
Signal dropout! (simulated electrode failure)

🕹 Example Neurogame Connection

We include a small demo script (run_neurogame_sim.py) showing how a game object can respond to brain-style input:

Attention → Move Left

Relaxation → Move Right

Dropout → Pause movement

This structure mirrors real neurogaming techniques used with Muse2, Neurosity Crown, and OpenBCI devices.

💡 Why This Matters

DIY EEG and neurogaming systems face serious constraints:

Very low signal strength

High external noise

Unstable electrodes

Latency jitter

Random dropouts

Amplifier saturation

Difficulty extracting clean mental-state features

Including these failure modes teaches users why real brain-computer interfaces are challenging and why noise-handling is essential for any serious experiment.