# Denon AH-C351K

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.6; 23 -1.6; 25 -1.7; 26 -1.7; 28 -1.8; 30 -1.8; 32 -1.8; 35 -1.7; 37 -1.7; 40 -1.7; 42 -1.7; 45 -1.7; 49 -1.8; 52 -1.8; 56 -1.8; 59 -1.8; 64 -1.9; 68 -2.0; 73 -2.0; 78 -2.2; 83 -2.4; 89 -2.7; 95 -3.1; 102 -3.6; 109 -4.1; 117 -4.6; 125 -5.2; 134 -5.7; 143 -6.0; 153 -6.2; 164 -6.2; 175 -6.3; 188 -6.4; 201 -6.2; 215 -6.1; 230 -5.9; 246 -5.8; 263 -5.6; 282 -5.5; 301 -5.8; 323 -5.6; 345 -5.2; 369 -4.9; 395 -4.6; 423 -4.3; 452 -4.0; 484 -3.8; 518 -3.4; 554 -2.9; 593 -2.4; 635 -2.0; 679 -1.8; 726 -1.4; 777 -0.9; 832 -0.6; 890 -0.4; 952 -0.2; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.8; 1336 1.0; 1429 1.0; 1529 0.9; 1636 0.8; 1751 1.0; 1873 1.9; 2004 2.8; 2145 3.8; 2295 5.1; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.0; 4830 3.3; 5168 1.7; 5530 -1.5; 5917 -5.1; 6331 -3.2; 6775 0.2; 7249 1.2; 7756 0.3; 8299 -1.1; 8880 -3.8; 9502 -3.8; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -2.9; 16326 -1.7; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C351K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.26 | -1.5 dB |
| Peaking | 216 Hz   | 0.52 | -6.5 dB |
| Peaking | 3249 Hz  | 1.06 | 7.1 dB  |
| Peaking | 5961 Hz  | 5.89 | -7.8 dB |
| Peaking | 15551 Hz | 3.96 | -3.2 dB |
| Peaking | 3107 Hz  | 5.51 | -2.0 dB |
| Peaking | 3530 Hz  | 2.06 | 2.2 dB  |
| Peaking | 3551 Hz  | 5.45 | -2.2 dB |
| Peaking | 8896 Hz  | 1.55 | 1.5 dB  |
| Peaking | 9223 Hz  | 4.63 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C351K/Denon%20AH-C351K.png)