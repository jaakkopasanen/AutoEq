# NVX XPT100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.7; 25 5.4; 26 5.2; 28 4.9; 30 4.6; 32 4.4; 35 4.1; 37 3.9; 40 3.7; 42 3.6; 45 3.5; 49 3.4; 52 3.3; 56 3.1; 59 3.0; 64 2.9; 68 2.8; 73 2.6; 78 2.5; 83 2.3; 89 2.1; 95 1.8; 102 1.6; 109 1.4; 117 1.1; 125 0.4; 134 -0.4; 143 -0.9; 153 -1.3; 164 -0.8; 175 -0.6; 188 -1.1; 201 -1.0; 215 -0.7; 230 0.1; 246 1.3; 263 2.9; 282 4.8; 301 5.6; 323 5.1; 345 4.3; 369 3.5; 395 2.8; 423 2.5; 452 1.9; 484 1.3; 518 1.0; 554 1.0; 593 1.0; 635 0.8; 679 0.6; 726 0.6; 777 0.9; 832 1.1; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.5; 1429 -2.1; 1529 -2.6; 1636 -2.8; 1751 -2.8; 1873 -3.0; 2004 -2.9; 2145 -2.7; 2295 -2.3; 2455 -1.6; 2627 -1.2; 2811 -0.7; 3008 1.6; 3219 3.4; 3444 1.3; 3685 0.5; 3943 0.8; 4219 1.4; 4514 2.3; 4830 3.4; 5168 5.4; 5530 6.0; 5917 5.8; 6331 3.4; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -2.3; 20000 -4.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.83 | 5.7 dB  |
| Peaking | 67 Hz    | 1.88 | 2.0 dB  |
| Peaking | 322 Hz   | 2.89 | 5.6 dB  |
| Peaking | 1829 Hz  | 2.17 | -3.6 dB |
| Peaking | 5554 Hz  | 2.71 | 6.4 dB  |
| Peaking | 181 Hz   | 2.08 | -2.4 dB |
| Peaking | 2135 Hz  | 0.1  | 1.1 dB  |
| Peaking | 2789 Hz  | 1.6  | -1.4 dB |
| Peaking | 3199 Hz  | 5.79 | 4.3 dB  |
| Peaking | 18517 Hz | 0.02 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100/NVX%20XPT100.png)