# Sennheiser HE 60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.9; 40 5.8; 42 5.8; 45 5.8; 49 5.9; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 5.8; 73 5.2; 78 3.9; 83 3.1; 89 2.9; 95 2.9; 102 2.7; 109 2.5; 117 2.3; 125 1.9; 134 1.7; 143 1.5; 153 1.4; 164 1.2; 175 1.2; 188 1.2; 201 1.1; 215 1.0; 230 1.1; 246 1.0; 263 1.0; 282 1.1; 301 1.1; 323 1.1; 345 1.1; 369 1.0; 395 1.0; 423 0.9; 452 0.9; 484 0.9; 518 1.1; 554 1.6; 593 2.2; 635 2.2; 679 1.5; 726 1.4; 777 1.8; 832 1.9; 890 1.5; 952 0.4; 1019 0.0; 1090 0.3; 1167 0.2; 1248 0.4; 1336 0.3; 1429 -0.1; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -1.0; 2004 -0.8; 2145 -0.1; 2295 0.0; 2455 0.6; 2627 0.8; 2811 0.6; 3008 0.8; 3219 0.6; 3444 1.8; 3685 2.1; 3943 2.0; 4219 1.2; 4514 0.7; 4830 -0.6; 5168 -2.3; 5530 -3.2; 5917 -3.9; 6331 -1.8; 6775 1.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.8; 9502 -2.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.2; 20000 -4.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HE 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.44 | 6.5 dB  |
| Peaking | 641 Hz   | 1.72 | 1.9 dB  |
| Peaking | 3787 Hz  | 3.56 | 2.5 dB  |
| Peaking | 5681 Hz  | 5.41 | -4.4 dB |
| Peaking | 28244 Hz | 3.29 | -4.5 dB |
| Peaking | 79 Hz    | 2.22 | -1.7 dB |
| Peaking | 68 Hz    | 3.39 | 2.6 dB  |
| Peaking | 1773 Hz  | 4.06 | -1.3 dB |
| Peaking | 7079 Hz  | 9.89 | 2.5 dB  |
| Peaking | 9276 Hz  | 9.51 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HE%2060/Sennheiser%20HE%2060.png)