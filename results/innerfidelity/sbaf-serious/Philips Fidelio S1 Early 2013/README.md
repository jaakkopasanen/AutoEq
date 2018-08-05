# Philips Fidelio S1 Early 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.4; 23 -1.3; 25 -1.3; 26 -1.3; 28 -1.3; 30 -1.3; 32 -1.2; 35 -1.2; 37 -1.1; 40 -1.1; 42 -1.0; 45 -1.0; 49 -0.9; 52 -0.9; 56 -0.8; 59 -0.7; 64 -0.7; 68 -0.6; 73 -0.7; 78 -0.7; 83 -0.8; 89 -1.0; 95 -1.4; 102 -1.7; 109 -2.0; 117 -2.4; 125 -2.8; 134 -3.1; 143 -3.2; 153 -3.3; 164 -3.2; 175 -3.1; 188 -2.9; 201 -2.7; 215 -2.5; 230 -2.2; 246 -2.0; 263 -1.8; 282 -1.5; 301 -1.3; 323 -1.0; 345 -0.8; 369 -0.6; 395 -0.4; 423 -0.1; 452 0.2; 484 0.8; 518 0.5; 554 0.6; 593 1.0; 635 1.1; 679 1.0; 726 1.1; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.2; 1336 -1.7; 1429 -2.3; 1529 -2.8; 1636 -3.2; 1751 -3.4; 1873 -3.4; 2004 -3.2; 2145 -3.0; 2295 -2.6; 2455 -1.6; 2627 -0.8; 2811 0.0; 3008 1.1; 3219 1.8; 3444 2.3; 3685 1.8; 3943 0.4; 4219 -2.1; 4514 -4.1; 4830 -4.8; 5168 -3.3; 5530 -0.9; 5917 1.8; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.8dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio S1 Early 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 157 Hz  | 1.15 | -3.4 dB |
| Peaking | 1889 Hz | 2.03 | -3.9 dB |
| Peaking | 3524 Hz | 2.8  | 4.0 dB  |
| Peaking | 4734 Hz | 3.24 | -6.2 dB |
| Peaking | 6443 Hz | 4.62 | 5.2 dB  |
| Peaking | 25 Hz   | 1.1  | -1.4 dB |
| Peaking | 291 Hz  | 2.08 | -0.6 dB |
| Peaking | 688 Hz  | 1.19 | 1.5 dB  |
| Peaking | 1392 Hz | 3.03 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20S1%20Early%202013/Philips%20Fidelio%20S1%20Early%202013.png)