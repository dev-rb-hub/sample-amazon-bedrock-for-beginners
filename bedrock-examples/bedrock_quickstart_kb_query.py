import boto3

# Use the exact profile name you created in Step 2
session = boto3.Session(profile_name='your_profile_name')
s3 = session.client('s3')

# REPLACE THIS with your Knowledge Base ID
KNOWLEDGE_BASE_ID = ""  # Example: "ABCDEFGHIJ"

# REPLACE THIS with your model ID 
MODEL_ID = "apac.amazon.nova-lite-v1:0"

client = session.client("bedrock-agent-runtime", region_name="ap-southeast-2")

# Retrieve
retrieve = client.retrieve(
    knowledgeBaseId=KNOWLEDGE_BASE_ID,
    retrievalQuery={"text": "When is spring break this year?"},
)
print("Retrieve:", retrieve["retrievalResults"])

# RetrieveAndGenerate
rag = client.retrieve_and_generate(
    input={"text": "When is spring break this year?"},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KNOWLEDGE_BASE_ID,
            "modelArn": MODEL_ID,
        },
    },
)
print("RetrieveAndGenerate:", rag["output"]["text"])