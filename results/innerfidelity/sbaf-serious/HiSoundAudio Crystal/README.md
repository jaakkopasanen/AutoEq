# HiSoundAudio Crystal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -0.9; 22 -1.1; 23 -1.2; 25 -1.3; 26 -1.4; 28 -1.4; 30 -1.5; 32 -1.5; 35 -1.5; 37 -1.6; 40 -1.6; 42 -1.6; 45 -1.6; 49 -1.6; 52 -1.6; 56 -1.7; 59 -1.7; 64 -1.8; 68 -1.8; 73 -1.9; 78 -2.0; 83 -2.2; 89 -2.6; 95 -2.9; 102 -3.5; 109 -3.8; 117 -4.3; 125 -4.8; 134 -5.2; 143 -5.4; 153 -5.5; 164 -5.5; 175 -5.5; 188 -5.3; 201 -5.2; 215 -5.0; 230 -4.7; 246 -4.5; 263 -4.3; 282 -3.9; 301 -3.7; 323 -3.4; 345 -3.0; 369 -2.7; 395 -2.4; 423 -1.9; 452 -1.6; 484 -1.4; 518 -1.1; 554 -0.6; 593 -0.1; 635 0.1; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -1.5; 1336 -2.2; 1429 -3.0; 1529 -3.8; 1636 -4.4; 1751 -4.7; 1873 -4.6; 2004 -3.8; 2145 -2.6; 2295 -1.3; 2455 -0.1; 2627 5.0; 2811 5.7; 3008 2.0; 3219 -0.6; 3444 0.2; 3685 0.5; 3943 1.8; 4219 0.6; 4514 -0.9; 4830 -1.2; 5168 -1.3; 5530 -2.4; 5917 -4.3; 6331 -6.7; 6775 -5.9; 7249 -3.3; 7756 -0.6; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.7; 13327 -1.5; 14260 -1.6; 15258 -2.3; 16326 -3.1; 17469 -2.3; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiSoundAudio Crystal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 169 Hz   | 0.72 | -5.7 dB |
| Peaking | 1789 Hz  | 2.5  | -5.2 dB |
| Peaking | 2735 Hz  | 7.12 | 7.6 dB  |
| Peaking | 6446 Hz  | 4.97 | -7.3 dB |
| Peaking | 31791 Hz | 2.22 | -3.3 dB |
| Peaking | 30 Hz    | 1.26 | -1.3 dB |
| Peaking | 780 Hz   | 2.41 | 1.6 dB  |
| Peaking | 5916 Hz  | 0.45 | -0.8 dB |
| Peaking | 3943 Hz  | 7.28 | 2.7 dB  |
| Peaking | 8800 Hz  | 1.74 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiSoundAudio%20Crystal/HiSoundAudio%20Crystal.png)