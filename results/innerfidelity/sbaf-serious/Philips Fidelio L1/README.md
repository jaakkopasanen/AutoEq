# Philips Fidelio L1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -5.6; 22 -6.1; 23 -6.2; 25 -6.6; 26 -6.7; 28 -6.9; 30 -7.1; 32 -7.3; 35 -7.4; 37 -7.5; 40 -7.6; 42 -7.7; 45 -7.7; 49 -7.7; 52 -7.7; 56 -7.7; 59 -7.6; 64 -7.6; 68 -7.5; 73 -7.4; 78 -7.4; 83 -7.3; 89 -7.3; 95 -7.3; 102 -7.4; 109 -7.3; 117 -7.5; 125 -7.9; 134 -8.2; 143 -8.2; 153 -8.1; 164 -7.7; 175 -7.1; 188 -6.8; 201 -6.8; 215 -6.8; 230 -6.6; 246 -6.6; 263 -6.5; 282 -6.1; 301 -5.7; 323 -5.4; 345 -4.9; 369 -4.6; 395 -4.1; 423 -3.5; 452 -3.2; 484 -2.9; 518 -2.4; 554 -1.8; 593 -1.2; 635 -0.7; 679 -0.4; 726 -0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.4; 1248 -0.9; 1336 -2.2; 1429 -3.7; 1529 -5.2; 1636 -6.6; 1751 -7.4; 1873 -7.6; 2004 -7.5; 2145 -7.5; 2295 -8.5; 2455 -8.1; 2627 -7.4; 2811 -6.8; 3008 -5.4; 3219 -3.6; 3444 -1.9; 3685 -1.2; 3943 -0.3; 4219 0.6; 4514 1.8; 4830 3.2; 5168 4.7; 5530 5.0; 5917 4.6; 6331 3.4; 6775 -0.2; 7249 -3.1; 7756 -4.0; 8299 -4.2; 8880 -2.5; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -0.5; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio L1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 6 Hz    | 1.24 | -5.1 dB |
| Peaking | 48 Hz   | 0.28 | -7.3 dB |
| Peaking | 219 Hz  | 0.83 | -4.2 dB |
| Peaking | 2242 Hz | 1.56 | -9.0 dB |
| Peaking | 5320 Hz | 3.83 | 6.7 dB  |
| Peaking | 998 Hz  | 1.49 | 2.1 dB  |
| Peaking | 1623 Hz | 4.97 | -2.9 dB |
| Peaking | 6240 Hz | 5.8  | 3.6 dB  |
| Peaking | 9686 Hz | 2.65 | 1.7 dB  |
| Peaking | 7936 Hz | 2.74 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20L1/Philips%20Fidelio%20L1.png)