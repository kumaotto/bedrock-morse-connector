import json
import boto3

MODEL_ID = 'anthropic.claude-3-sonnet-20240229-v1:0'
MAX_TOKENS = 1000


def generate_message(bedrock, system: str, messages: str) -> str:

    """
    Bedrockにリクエストを送信し、レスポンスを取得する

    :param bedrock: Bedrock APIのクライアント
    :param system: システムプロンプト
    :param messages: Bedrockに送信するメッセージ

    :return: Bedrockからのレスポンス
    """

    body: dict = json.dumps(
        {
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': MAX_TOKENS,
            'system': system,
            'messages': messages
        }
    )

    accept: str = 'application/json'
    contentType: str = 'application/json'
    response = bedrock.invoke_model(body=body, modelId=MODEL_ID, accept=accept, contentType=contentType)
    response_body: dict = json.loads(response.get('body').read())

    return response_body["content"][0]["text"]


def execute_bedrock_api(message: str) -> str:

    """
    Bedrock APIを実行する

    :param message: Bedrockに送信するメッセージ
    """

    try:
        
        # バージニアリージョンのBedrockランタイムクライアントを作成
        bedrock = boto3.client('bedrock-runtime', region_name = "us-east-1")

        system_prompt: str = '''
        
        あなたは通信士です。あなたは、モールス符号を使ってメッセージを送信する訓練を受けています。
        メッセージを自然言語に変換し、その内容に基づいて返信してください。
        但し、返信は和文モールス符号に変換可能なテキスト、かつ10文字以内である必要があります。

        There are the following restrictions.
        
        1. All must be in katakana.
        2. Must be in declarative form.
        3. Symbols are not allowed.
        4. If it exceeds 10 charaters, consider a shorter way to say it.
        5. No need to respond with "yes" or similar.
        6. Do not use 'desu/masu' form.

        <task>
        Respond with an appropriate replay to the recieve message.

        以下は出力例です。
        <example id="1">
        ケ゛ンキテ゛スカ
        </example>

        <example id="2">
        リヨウカイ
        </example>

        </task>
        '''

        # サンプルメッセージでBedrock APIを実行
        user_message: dict = {'role': 'user', 'content': message}
        messages: list[str] = [user_message]

        response: str = generate_message(bedrock, system_prompt, messages)
        
        return response

    except Exception as e:
        print('Error:', e)
        return
