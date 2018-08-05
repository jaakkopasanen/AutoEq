# Massdrop x Fostex TH-X00

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 2.4; 22 1.5; 23 1.1; 25 0.4; 26 0.1; 28 -0.4; 30 -0.7; 32 -1.0; 35 -1.2; 37 -1.3; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.4; 52 -1.3; 56 -1.3; 59 -1.2; 64 -1.2; 68 -1.2; 73 -1.3; 78 -1.4; 83 -1.4; 89 -1.7; 95 -1.8; 102 -2.1; 109 -2.2; 117 -2.4; 125 -2.7; 134 -2.8; 143 -2.9; 153 -2.9; 164 -2.8; 175 -2.6; 188 -2.5; 201 -2.3; 215 -1.7; 230 -1.2; 246 -1.0; 263 -0.9; 282 -0.6; 301 -0.5; 323 -0.2; 345 0.0; 369 0.3; 395 0.5; 423 0.8; 452 1.1; 484 1.0; 518 0.9; 554 1.0; 593 1.1; 635 2.0; 679 2.4; 726 1.9; 777 1.5; 832 1.3; 890 0.9; 952 0.3; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.0; 1336 -0.3; 1429 -0.6; 1529 -1.0; 1636 -1.2; 1751 -0.9; 1873 -0.9; 2004 -0.5; 2145 -0.0; 2295 0.5; 2455 1.2; 2627 1.7; 2811 1.8; 3008 2.1; 3219 2.6; 3444 5.7; 3685 5.1; 3943 3.9; 4219 3.1; 4514 2.4; 4830 2.3; 5168 1.3; 5530 0.6; 5917 0.6; 6331 1.5; 6775 2.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -1.4; 10879 -1.5; 11640 -0.6; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 3.3  | 1.9 dB  |
| Peaking | 134 Hz   | 0.84 | -2.9 dB |
| Peaking | 645 Hz   | 2    | 2.2 dB  |
| Peaking | 3679 Hz  | 2.67 | 5.2 dB  |
| Peaking | 10607 Hz | 5.51 | -1.8 dB |
| Peaking | 15 Hz    | 1.02 | 2.9 dB  |
| Peaking | 36 Hz    | 1.59 | -1.7 dB |
| Peaking | 408 Hz   | 3.51 | 0.7 dB  |
| Peaking | 1656 Hz  | 2.85 | -1.6 dB |
| Peaking | 6794 Hz  | 7.77 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00/Massdrop%20x%20Fostex%20TH-X00.png)