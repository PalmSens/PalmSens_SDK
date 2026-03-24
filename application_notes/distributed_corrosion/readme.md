# Distributed Polarization Resistance Using Python

The code here accompanies the application note: [Distributed Polarization Resistance Using Python](https://www.palmsens.com/knowledgebase-article/distributed-polarization-resistance-using-python/)

There are 2 scripts:
- [measure.py](./measure.py): This script runs the LSV measurement to collect LPS data. See the application note for instructions.
- [app.py](./app.py): An example [Streamlit](https://docs.streamlit.io) dashboard

## Running the dashboard locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Licence

The code for this notebook is licensed under the terms of the [MIT Licence](./LICENSE).
