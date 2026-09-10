import boto3

client = boto3.client("bedrock-runtime", region_name="ap-southeast-2")  

# Load image from file 
with open("GitHub_Button.jpg", "rb") as f: 
    image_bytes = f.read()  

response = client.converse( 
    modelId="au.anthropic.claude-haiku-4-5-20251001-v1:0", 
    messages=[{ 
        "role": "user", 
        "content": [ 
            { "image": { 
                  "format": "jpeg", 
                  "source": {"bytes": image_bytes} 
               } 
            }, 
            {"text": "What is in this image?"}
        ] 
    }] 
)  
print(response["output"]["message"]["content"][0]["text"])