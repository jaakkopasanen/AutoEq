# Logitech UE 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.3; 22 1.2; 23 1.2; 25 1.2; 26 1.2; 28 1.2; 30 1.1; 32 1.1; 35 1.0; 37 1.0; 40 0.9; 42 1.0; 45 0.9; 49 0.9; 52 0.9; 56 0.8; 59 0.7; 64 0.6; 68 0.5; 73 0.4; 78 0.2; 83 -0.1; 89 -0.4; 95 -0.9; 102 -1.5; 109 -2.0; 117 -2.5; 125 -3.2; 134 -3.6; 143 -4.0; 153 -4.3; 164 -4.5; 175 -4.6; 188 -4.7; 201 -4.7; 215 -4.7; 230 -4.7; 246 -4.7; 263 -4.7; 282 -4.7; 301 -4.8; 323 -4.8; 345 -4.8; 369 -4.9; 395 -5.0; 423 -5.0; 452 -5.0; 484 -5.1; 518 -5.2; 554 -5.0; 593 -4.6; 635 -4.2; 679 -3.6; 726 -2.7; 777 -1.7; 832 -1.0; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.0; 1167 -0.0; 1248 -0.2; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.9; 1751 -2.2; 1873 -2.3; 2004 -2.4; 2145 -2.5; 2295 -2.2; 2455 -1.2; 2627 0.5; 2811 3.0; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 5.3; 4830 5.5; 5168 5.7; 5530 5.5; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.5; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech UE 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 57 Hz   | 0.58 | 2.3 dB  |
| Peaking | 257 Hz  | 0.43 | -5.7 dB |
| Peaking | 2288 Hz | 2.18 | -5.7 dB |
| Peaking | 3346 Hz | 1.38 | 7.7 dB  |
| Peaking | 5788 Hz | 3.31 | 4.5 dB  |
| Peaking | 16 Hz   | 1.54 | 0.7 dB  |
| Peaking | 592 Hz  | 1.46 | -4.3 dB |
| Peaking | 842 Hz  | 0.61 | 3.4 dB  |
| Peaking | 1617 Hz | 1.89 | -2.5 dB |
| Peaking | 9238 Hz | 3.78 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Logitech%20UE%20900/Logitech%20UE%20900.png)