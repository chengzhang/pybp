# coding = utf8
import logging

import requests
import os
from typing import List, Union


def api_key():
    key = os.getenv('GOOGLE_TRANS_API_KEY')
    if not key:
        raise KeyError('GOOGLE_TRANS_API_KEY not set')
    return key


def translate(text: Union[str, List[str]], src_lang: str='pt', dst_lang: str='zh-cn') -> Union[str, List[str]]:
    """
    Translate text from source language to destination language using Google Translate API.

    :param text: The text to be translated. Can be a string or a list of strings.
    :param src_lang: The source language of the text. Default is 'pt' (Portuguese).
    :param dst_lang: The destination language of the text. Default is 'zh-cn' (Simplified Chinese).
    :return: The translated text as a string or a list of strings, depending on the input type.
    :raises KeyError: If the environment variable 'GOOGLE_TRANS_API_KEY' is not set.

    Example usage:
    >>> translate('oi', 'pt', 'zh-cn')
    '嗨'
    >>> translate(['oi', 'bora'], 'pt')
    ['嗨', '去']
    """
    q = text 
    if isinstance(text, list):
        q = '\n'.join(text)
    url = "https://translation.googleapis.com/language/translate/v2"
    data = {
        'key': api_key(),
        'source': src_lang,
        'target': dst_lang,
        'q': q,
        'format': "text"
    }
    logging.debug(f'translate request data: {data}')
    resp= requests.post(url, data)
    logging.debug(f'translate response: {resp}')
    res = resp.json()
    result = res["data"]["translations"][0]["translatedText"]
    if isinstance(text, list): 
        result = result.split('\n') 
    return result


if __name__ == '__main__':
    res = translate(['oi', 'bora'], 'pt')
    print(res)
