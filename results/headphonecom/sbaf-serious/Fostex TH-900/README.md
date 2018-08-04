# Fostex TH-900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -4.5; 22 -4.8; 23 -4.9; 25 -5.0; 26 -5.1; 28 -5.1; 30 -5.2; 32 -5.2; 35 -5.2; 37 -5.2; 40 -5.1; 42 -5.1; 45 -5.0; 49 -4.3; 52 -3.8; 56 -4.1; 59 -4.7; 64 -5.2; 68 -5.3; 73 -5.2; 78 -5.2; 83 -5.1; 89 -5.0; 95 -5.2; 102 -5.5; 109 -5.5; 117 -5.6; 125 -6.0; 134 -6.1; 143 -6.2; 153 -6.0; 164 -5.6; 175 -5.5; 188 -5.3; 201 -5.0; 215 -4.8; 230 -4.4; 246 -4.1; 263 -3.8; 282 -3.3; 301 -2.9; 323 -2.4; 345 -1.8; 369 -1.3; 395 -0.6; 423 0.3; 452 1.3; 484 2.4; 518 3.8; 554 5.0; 593 5.0; 635 3.7; 679 2.2; 726 2.3; 777 2.3; 832 1.1; 890 0.4; 952 0.2; 1019 0.0; 1090 0.0; 1167 0.0; 1248 0.2; 1336 0.4; 1429 0.3; 1529 -0.1; 1636 -0.7; 1751 -1.1; 1873 -0.6; 2004 1.1; 2145 3.1; 2295 3.5; 2455 2.6; 2627 2.4; 2811 1.7; 3008 1.3; 3219 1.4; 3444 1.8; 3685 2.2; 3943 2.4; 4219 0.8; 4514 -0.9; 4830 -1.7; 5168 -1.9; 5530 -2.7; 5917 -3.4; 6331 -2.3; 6775 -2.0; 7249 -2.1; 7756 -1.8; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -1.4; 11640 -1.8; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 -1.2; 16326 -2.6; 17469 -2.2; 18692 -3.7; 20000 -9.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH-900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.81 | -2.9 dB |
| Peaking | 50 Hz    | 0.23 | -2.0 dB |
| Peaking | 158 Hz   | 0.55 | -4.4 dB |
| Peaking | 564 Hz   | 2.29 | 6.4 dB  |
| Peaking | 2407 Hz  | 3.55 | 3.4 dB  |
| Peaking | 2144 Hz  | 9.75 | 1.6 dB  |
| Peaking | 1789 Hz  | 5.15 | -1.8 dB |
| Peaking | 3835 Hz  | 4.01 | 3.2 dB  |
| Peaking | 5731 Hz  | 1.86 | -3.2 dB |
| Peaking | 20312 Hz | 1.46 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Fostex%20TH-900/Fostex%20TH-900.png)