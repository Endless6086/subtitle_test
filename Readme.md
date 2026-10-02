# subtitle_test

一個將 WebVTT (`.vtt`) 字幕轉換為 LRC (`.lrc`) 格式的 Python 小工具。

## Baseline

目前版本為原始手寫版本，主要用途為日常字幕格式轉換。

目前功能：

- 掃描指定資料夾中的 `.vtt` 檔案
- 讀取 WebVTT 字幕
- 將字幕開始時間轉換為 LRC 時間標記
- 輸出 UTF-8 `.lrc` 檔案

## Environment

- Python
- webvtt-py

## Future Work

後續將以此版本作為基準，加入單元測試與邊界條件驗證。