# Philips Fidelio M1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.7; 22 3.2; 23 3.0; 25 2.7; 26 2.5; 28 2.2; 30 1.9; 32 1.7; 35 1.3; 37 1.1; 40 0.9; 42 0.8; 45 0.6; 49 0.3; 52 0.2; 56 0.0; 59 -0.1; 64 -0.3; 68 -0.5; 73 -0.8; 78 -1.0; 83 -1.2; 89 -1.5; 95 -1.9; 102 -2.1; 109 -2.4; 117 -2.7; 125 -3.2; 134 -3.7; 143 -4.2; 153 -4.5; 164 -4.3; 175 -4.0; 188 -3.9; 201 -3.6; 215 -3.1; 230 -2.5; 246 -1.8; 263 -1.1; 282 -0.4; 301 0.1; 323 0.6; 345 1.2; 369 1.7; 395 2.1; 423 2.4; 452 2.6; 484 2.5; 518 2.4; 554 2.4; 593 2.3; 635 1.9; 679 1.3; 726 0.9; 777 0.8; 832 0.6; 890 0.1; 952 -0.0; 1019 -0.0; 1090 0.3; 1167 0.9; 1248 1.6; 1336 2.2; 1429 1.8; 1529 1.2; 1636 1.4; 1751 2.0; 1873 2.1; 2004 2.2; 2145 2.3; 2295 2.7; 2455 3.1; 2627 2.2; 2811 1.1; 3008 1.5; 3219 1.4; 3444 1.2; 3685 0.9; 3943 0.8; 4219 0.5; 4514 0.9; 4830 1.8; 5168 4.0; 5530 5.7; 5917 5.9; 6331 4.2; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.1; 18692 -2.1; 20000 -0.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio M1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.88 | 3.7 dB  |
| Peaking | 166 Hz   | 1.01 | -4.8 dB |
| Peaking | 437 Hz   | 1.28 | 3.4 dB  |
| Peaking | 2158 Hz  | 1.5  | 2.5 dB  |
| Peaking | 5787 Hz  | 4.15 | 6.3 dB  |
| Peaking | 994 Hz   | 3.92 | -1.0 dB |
| Peaking | 1359 Hz  | 3.99 | 2.0 dB  |
| Peaking | 1493 Hz  | 3.62 | -1.1 dB |
| Peaking | 19576 Hz | 2.31 | -0.6 dB |
| Peaking | 29434 Hz | 2.93 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20M1/Philips%20Fidelio%20M1.png)