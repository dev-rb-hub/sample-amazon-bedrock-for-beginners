import boto3  

client = boto3.client("bedrock-runtime", region_name="ap-southeast-2")  

# modelId="au.anthropic.claude-haiku-4-5-20251001-v1:0", 
#"apac.amazon.nova-lite-v1:0",
response = client.converse( 
    modelId = "au.anthropic.claude-haiku-4-5-20251001-v1:0",
    messages=[ 
        { 
            "role": "user", 
            "content": [{"text": "Write a one-sentence bedtime story about a unicorn."}]
        } 
    ] 
)  

print(response["output"]["message"]["content"][0]["text"])