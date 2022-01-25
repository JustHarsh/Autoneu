# Autoneu - Healthcare for the future
**Automatic Diagnosis of Penumonia using a CNN**

# Problem Definition
Make an automated system that can do end-to-end diagnosis of Pneumonia in seconds. 


# Reason for choosing the topic
Amidst the pandemic, there has been enormous pressure for hospitals and clinics alike to handle potential COVID-19 patients. The process of screening patients is largely manual and relies heavily on manpower. Nurses spend countless hours testing patients when a large part of the process can actually be automated. Apart from rapid tests, patients are often screened based on their Lung X-Rays and if they have Pneumonia or not. The reason being, if a person tests positive for Pneumonia then there is a high likelihood that he/she has COVID too, since both diseases target the lungs. Taking this problem into account, I have built an Artificially Intelligent system that can perform Pneumonia diagnosis automatically. My tool is mainly targeted towards helping accelerate the pace at which patients are tested while also not using a lot of nurses and doctors so that they can focus on treating the existing patients. 

# Objective
- Help clinics, hospitals and the healthcare system in general to accelerate the pace of COVID testing.
- Present a solution to not use a lot of manpower for the same.
Automatically diagnose Pneumonia off of Lung X-Rays.

# Hardware Requirements
- A PC
- Minimum of 8 GB of RAM 

# Software Requirements
- Tensorflow 2.x (latest version)
- Matplotlib
- Numpy
- Tkinter
- Sql Connector
- Numpy
- Pillow

# Guidelines -
- Clone the repository
- Make a virtual environment on your system by typing the following - 

        python3 -m venv /path/to/new/virtual/environment
        
- In the virtual environment (venv) type - 
    
        pip install -r /path/to/new/virtual/requirements.txt
- Visit tensorflow.org to view the installation guide on Tensorflow. 
- Run the gui.py by typing the below in your terminal/command prompt - 

        python gui.py

# Limitations
- If this project were to be implemented in real life, strict measures will have to be taken to prevent anyone from tampering with patient data. Hence, a clinic/hospital will need at least one person guarding the server room at all times.

- Training (workshop) will be required for both doctors and nurses

# Demo 
https://user-images.githubusercontent.com/33577077/151024632-77980471-ca32-4d45-b4c1-e686173b89f1.mp4

As you can see, in the last part of the video, the database was updated in the background. It had the file path and its correspoding label (0 for negative and 1 for positive). 


# References/Bibliography
- tensorflow.org for learning how to build the model
- docs.python.org for making ReadMe. 
- Stackoverflow.com for fixing bugs/errors
- Book - Computer Science with Python
