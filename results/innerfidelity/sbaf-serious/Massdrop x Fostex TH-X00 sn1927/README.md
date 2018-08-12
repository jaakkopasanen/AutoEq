# Massdrop x Fostex TH-X00 sn1927

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.8; 23 -0.9; 25 -1.2; 26 -1.3; 28 -1.4; 30 -1.5; 32 -1.5; 35 -1.5; 37 -1.5; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.3; 52 -1.3; 56 -1.2; 59 -1.2; 64 -1.1; 68 -1.1; 73 -1.2; 78 -1.4; 83 -1.6; 89 -1.8; 95 -1.9; 102 -2.1; 109 -2.2; 117 -2.2; 125 -2.3; 134 -2.4; 143 -2.4; 153 -2.5; 164 -2.3; 175 -2.2; 188 -2.2; 201 -2.1; 215 -1.8; 230 -1.6; 246 -1.3; 263 -1.0; 282 -0.8; 301 -0.6; 323 -0.5; 345 -0.3; 369 -0.1; 395 0.1; 423 0.4; 452 0.7; 484 0.6; 518 0.6; 554 0.6; 593 0.8; 635 0.6; 679 0.2; 726 0.0; 777 0.9; 832 1.0; 890 0.4; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 -0.2; 1429 -0.5; 1529 -0.9; 1636 -1.0; 1751 -0.8; 1873 -0.5; 2004 0.0; 2145 0.5; 2295 0.9; 2455 1.8; 2627 2.6; 2811 3.2; 3008 4.8; 3219 4.8; 3444 4.9; 3685 4.2; 3943 4.1; 4219 3.3; 4514 2.8; 4830 2.7; 5168 1.5; 5530 1.4; 5917 1.9; 6331 2.0; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.0; 10167 -0.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 -0.0; 14260 -0.4; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sn1927 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.55 | -1.3 dB |
| Peaking | 148 Hz  | 1.17 | -2.4 dB |
| Peaking | 1762 Hz | 2.63 | -1.8 dB |
| Peaking | 3394 Hz | 1.6  | 5.1 dB  |
| Peaking | 6657 Hz | 5.65 | 1.8 dB  |
| Peaking | 227 Hz  | 3.06 | -0.5 dB |
| Peaking | 533 Hz  | 1.36 | 0.8 dB  |
| Peaking | 9607 Hz | 2.3  | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sn1927/Massdrop%20x%20Fostex%20TH-X00%20sn1927.png)