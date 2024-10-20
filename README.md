## ArkChain: OpenD/I 2023 December Hackathon Submission

ArkChain was a project and team that tackled the OpenD/I Hackathon's Challenge 3, the Data Verification challenge. The hackathon ran over multiple weeks out of the Sydney Startup Hub where the Arkchain team worked to develop a solution for verifying data integrity and authenticity.

### Design
Arkchain was designed with decentralization in mind, intending for independent nodes to validate data by reaching consensus on it's unique hash. Only the metadata including claimed source and file hash are communicated through the network, we namespace and identify data based on it's source and the topics that were collected.

### Next steps for the prototype
If the prototype were developed further, some topics of interest could include federated byzantine consensus and zero knowledge proofs.

## Running the demonstration
To run a solution demonstration, use the following commands in the root directory of this repository:


```
pip install -r requirements.txt
python3 rundemo.py
```
