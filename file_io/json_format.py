# coding = utf8

import json
import tokenize


def loads_semicolon_format(json_str):
    n_call = []
    def __gen():
        if n_call:
            raise StopIteration
        else:
            n_call.append(1)
            return json_str
    corrected = []
    for token in tokenize.generate_tokens(__gen):
        if token[0] == tokenize.OP and token[1] == ';':
            corrected.append(',')
        else:
            corrected.append(token[1])
    dic = json.loads(''.join(corrected))
    return dic


if __name__ == '__main__':
    json_str = '{"list":[{"list":[{"intent":{"intent":"天气服务-新.天气服务";"nodeName":"天气服务-新";"title":"天气服务"};"slots":[{"value":"今天";"name":"date"};{"value":"天气";"name":"weather_information"}]}];"score":0.9998877}]}'
    json_str = '{"intent": {"intent": "音乐.点歌播放"; "score": 0.9978817};"slots": [{"slotName": "歌曲名"; "text": "好听的音乐"; "begin": 6; "end": 16; "entityType": "unused_song_after_disam"; "entityNorm": "" 好听的音乐 ""}];"slotsOut": []}'
    dic = loads_semicolon_format(json_str)
    print(json.dumps(dic, ensure_ascii=False, indent=4))
