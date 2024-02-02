# Polyglot

English speech to any language text in (sort of) real-time.

Little poem about it [here](https://simutisernestas.github.io/2024/02/01/parents.html).

## Usage

Install the `whisper.cpp` library:
```bash
git clone https://github.com/ggerganov/whisper.cpp.git
bash ./models/download-ggml-model.sh base.en
make
make stream
```

Transcribe English:
```bash
./stream -m ./models/ggml-base.en.bin -t 16 --step 0 --length 10000 -vth 0.8
```

To translate this, setup the Google Translation API with Google Cloud SDK and set ENV variable:
```bash
export PROJECT_ID="your-project-id"
```

Run:
```bash
python main.py
```

Happy speech translation!
