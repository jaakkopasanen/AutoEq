# FLC Technologies FLC8 CCY Voca

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.8; 40 5.7; 42 5.7; 45 5.6; 49 5.5; 52 5.4; 56 5.3; 59 5.2; 64 5.0; 68 4.9; 73 4.7; 78 4.4; 83 4.1; 89 3.7; 95 3.1; 102 2.5; 109 2.0; 117 1.4; 125 0.7; 134 0.2; 143 -0.2; 153 -0.4; 164 -0.6; 175 -0.7; 188 -0.8; 201 -0.9; 215 -0.9; 230 -0.7; 246 -0.8; 263 -0.8; 282 -0.6; 301 -0.5; 323 -0.4; 345 -0.3; 369 -0.1; 395 -0.1; 423 0.2; 452 0.4; 484 0.4; 518 0.5; 554 0.7; 593 1.1; 635 1.2; 679 1.1; 726 1.0; 777 1.2; 832 1.3; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.5; 1248 -2.3; 1336 -3.5; 1429 -4.8; 1529 -6.2; 1636 -7.0; 1751 -6.7; 1873 -5.6; 2004 -3.9; 2145 -2.7; 2295 -1.9; 2455 -1.0; 2627 -0.7; 2811 -0.5; 3008 -0.5; 3219 2.5; 3444 5.8; 3685 6.0; 3943 6.0; 4219 5.4; 4514 5.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.6; 10167 -2.4; 10879 -2.3; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 CCY Voca ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.6  | 6.7 dB  |
| Peaking | 933 Hz  | 1.35 | 3.3 dB  |
| Peaking | 1682 Hz | 1.19 | -8.8 dB |
| Peaking | 4879 Hz | 0.79 | 8.1 dB  |
| Peaking | 9380 Hz | 1.45 | -4.8 dB |
| Peaking | 40 Hz   | 2.37 | -1.2 dB |
| Peaking | 82 Hz   | 1.45 | 1.8 dB  |
| Peaking | 171 Hz  | 1.11 | -1.9 dB |
| Peaking | 3015 Hz | 7.36 | -3.0 dB |
| Peaking | 3455 Hz | 7    | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20CCY%20Voca/FLC%20Technologies%20FLC8%20CCY%20Voca.png)