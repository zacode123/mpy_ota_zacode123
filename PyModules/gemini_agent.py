import network
import time
import urequests
import ujson
import gc
from Config.config import STA_SSID, STA_PASS, AI_MODEL, GEMINI_API_KEY

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/" + AI_MODEL + ":generateContent?key=" + GEMINI_API_KEY

def connectWIFI():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.connect(STA_SSID, STA_PASS)
        while not sta_if.isconnected():
            time.sleep(0.5)
    print("Connected:", sta_if.ifconfig())

def askGemini(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{
                    "text": "You are Arc, an AI assistant created by Zahid Arman that gives helpful explanations and complete MicroPython code wrapped in triple backticks like ```python ... ```. Remember my board is ESP8266 12E and running micropython v1.25.0. you can also search for solutions. But don't crash my esp with unknown codes!"
                }]
            },
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        res = urequests.post(GEMINI_URL, headers=headers, json=payload)
        data = res.json()
        res.close()

        if "candidates" in data:
            full_text = data["candidates"][0]["content"]["parts"][0]["text"]

            start = full_text.find("```")
            end = full_text.find("```", start + 3)

            if start != -1 and end != -1:
                code = full_text[start + 3:end].strip()

                if code.startswith("python"):
                    code = code[6:].strip()

                explanation = full_text[:start].strip()
                return code, explanation

            else:
                return None, full_text

        elif "error" in data:
            return None, "Gemini API Error: " + data["error"]["message"]

        else:
            return None, "Unknown Gemini response format."

    except Exception as e:
        return None, "Exception: " + str(e)

def execCode(code):
    try:
        exec(code, globals())
        return "[EXECUTED]"
    except Exception as e:
        return "Exception: " + str(e)

def begin():
    while True:
        try:
            prompt = input("\nAsk Gemini (type 'exit' to quit):\n> ")
            if prompt.strip().lower() == "exit":
               print("Exited Gemini Agent")
               return

            code, explanation = askGemini(prompt)

            if explanation:
                print("\n" + explanation)

            if code:
                print("\nCode from Gemini:\n" + code)
                print("\nExecuting...\n")
                result = execCode(code)
                print("\nResult: " + result)
          
            gc.collect()

        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Main loop error:", e)
