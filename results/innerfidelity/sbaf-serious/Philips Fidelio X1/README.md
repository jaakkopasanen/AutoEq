# Philips Fidelio X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 4.6; 22 3.5; 23 3.0; 25 2.0; 26 1.5; 28 0.7; 30 -0.1; 32 -0.9; 35 -1.9; 37 -2.5; 40 -3.4; 42 -3.9; 45 -4.6; 49 -5.4; 52 -5.9; 56 -6.4; 59 -6.6; 64 -6.8; 68 -6.8; 73 -6.8; 78 -6.7; 83 -6.6; 89 -6.6; 95 -6.7; 102 -6.6; 109 -6.4; 117 -6.3; 125 -6.4; 134 -6.3; 143 -6.3; 153 -6.1; 164 -5.8; 175 -5.8; 188 -6.4; 201 -6.1; 215 -5.5; 230 -5.1; 246 -4.7; 263 -4.5; 282 -4.1; 301 -3.9; 323 -3.6; 345 -3.3; 369 -3.1; 395 -2.9; 423 -2.6; 452 -2.4; 484 -2.5; 518 -2.4; 554 -2.0; 593 -1.8; 635 -1.8; 679 -1.7; 726 -1.7; 777 -1.4; 832 -1.2; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.1; 1167 0.5; 1248 0.6; 1336 -0.6; 1429 -1.8; 1529 -2.7; 1636 -3.2; 1751 -3.2; 1873 -3.0; 2004 -3.2; 2145 -2.9; 2295 -2.8; 2455 -2.7; 2627 -1.8; 2811 0.7; 3008 0.9; 3219 -0.5; 3444 -1.4; 3685 -1.8; 3943 -1.8; 4219 -2.7; 4514 -3.3; 4830 -3.2; 5168 -2.8; 5530 -3.5; 5917 -3.7; 6331 -2.4; 6775 -1.3; 7249 -2.4; 7756 -3.8; 8299 -5.8; 8880 -6.8; 9502 -5.1; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.1dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.9  | 6.3 dB  |
| Peaking | 58 Hz    | 0.76 | -5.6 dB |
| Peaking | 175 Hz   | 0.52 | -5.0 dB |
| Peaking | 1960 Hz  | 2.09 | -3.3 dB |
| Peaking | 8396 Hz  | 1.99 | -5.6 dB |
| Peaking | 1179 Hz  | 5.06 | 1.9 dB  |
| Peaking | 2946 Hz  | 6.93 | 3.4 dB  |
| Peaking | 7140 Hz  | 0.87 | -5.4 dB |
| Peaking | 7120 Hz  | 2.92 | 6.7 dB  |
| Peaking | 36886 Hz | 1.86 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X1/Philips%20Fidelio%20X1.png)