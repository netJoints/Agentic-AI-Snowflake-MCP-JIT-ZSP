# Make sure this file has exec permissions in Linux/MacOS

from fastmcp import FastMCP
import requests
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os
import sys

tenant = "demo"
API_URL = f"https://{tenant}.britive-app.com/api/access"

# Get API key from environment variable
TOKEN = os.environ.get("BRITIVE_API_KEY")
mcp = FastMCP("Britive API MCP")

@mcp.tool()
def list_s3_profiles() -> dict:
    """List all profiles/environments that support programmatic S3 access."""
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    try:
        response = requests.get(API_URL, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
        # Filter for AWS Standalone or S3-supporting profiles with programmaticAccess
        aws_profiles = []
        for app in data:
            if app.get("appName", "").lower().startswith("aws"):
                for profile in app.get("profiles", []):
                    if profile.get("programmaticAccess", False):
                        for env in profile.get("environments", []):
                            aws_profiles.append({
                                "profile_id": profile.get("profileId"),
                                "profile_name": profile.get("profileName"),
                                "environment_id": env.get("environmentId"),
                                "environment_name": env.get("environmentName"),
                            })
        return {"aws_profiles": aws_profiles}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def checkout_s3_profile(profile_id: str, environment_id: str) -> dict:
    """Checkout the given profile/environment and return the tx_id."""
    url = f"{API_URL}/{profile_id}/environments/{environment_id}?accessType=PROGRAMMATIC"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    try:
        resp = requests.post(url, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        tx_id = data.get("txId") or data.get("txID") or data.get("transactionId")
        if not tx_id:
            return {"error": "No transaction ID returned from checkout.", "response": data}
        return {"tx_id": tx_id, "checkout_response": data}
    except Exception as e:
        return {"error": f"Checkout failed: {str(e)}"}

@mcp.tool()
def get_s3_tokens(tx_id: str) -> dict:
    """Get AWS tokens for a checked-out profile using the tx_id."""
    token_url = f"{API_URL}/{tx_id}/tokens"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    try:
        resp = requests.get(token_url, headers=headers, timeout=30)
        resp.raise_for_status()
        tokens = resp.json()
        return tokens  # This will include accessKeyID, secretAccessKey, sessionToken, etc.
    except Exception as e:
        return {"error": f"Token fetch failed: {str(e)}"}

@mcp.tool()
def summarize_s3(access_key: str, secret_key: str, session_token: str) -> dict:
    """List and summarize S3 buckets using the provided AWS credentials (boto3)."""
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token,
        )
        response = s3.list_buckets()
        buckets = [bucket["Name"] for bucket in response.get("Buckets", [])]
        return {"bucket_count": len(buckets), "buckets": buckets}
    except (BotoCoreError, ClientError) as e:
        return {"error": str(e)}

@mcp.tool()
def checkin_s3_profile_when_session_done(tx_id: str) -> dict:
    """Check in the given profile at end of session using the transaction ID (txID)."""
    url = f"{API_URL}/{tx_id}?type=API"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    try:
        resp = requests.put(url, headers=headers, timeout=30)
        resp.raise_for_status()
        return {"status": "checked in", "response": resp.json()}
    except Exception as e:
        return {"error": f"Check-in failed: {str(e)}"}

if __name__ == "__main__":
    mcp.run()
