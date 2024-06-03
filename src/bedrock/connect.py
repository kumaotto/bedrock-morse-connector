import json
import boto3

MODEL_ID = 'anthropic.claude-3-sonnet-20240229-v1:0'
MAX_TOKENS = 1000


def generate_message(bedrock, system_prompt: str, messages: str) -> str:

    """
    Bedrockにリクエストを送信し、レスポンスを取得する

    :param bedrock: Bedrock APIのクライアント
    :param system_prompt: システムプロンプト
    :param messages: Bedrockに送信するメッセージ

    :return: Bedrockからのレスポンス
    """

    body = json.dumps(
        {
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': MAX_TOKENS,
            # 'system_prompt': system_prompt, # システムプロンプトを指定する場合はコメントアウトを解除
            'messages': messages
        }
    )

    accept = 'application/json'
    contentType = 'application/json'
    response = bedrock.invoke_model(body=body, modelId=MODEL_ID, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())

    return response_body["content"][0]["text"]


def execute_bedrock_api(message: str = None) -> None:

    """
    Bedrock APIを実行する

    :param message: Bedrockに送信するメッセージ
    """

    try:
        
        # バージニアリージョンのBedrockランタイムクライアントを作成
        bedrock = boto3.client('bedrock-runtime', region_name = "us-east-1")

        system_prompt: str = ''

        # サンプルメッセージでBedrock APIを実行
        user_message: dict = {'role': 'user', 'content': '味噌汁の作り方を説明してください'}
        messages: list[str] = [user_message]

        response = generate_message(bedrock, system_prompt, messages)
        print(response)


    except Exception as e:
        print('Error:', e)
        return


if __name__ == "__main__":
    execute_bedrock_api()
    