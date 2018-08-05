# Bowers & Wilkins C5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.1dB
GraphicEQ: 10 -84; 20 -13.9; 22 -13.7; 23 -13.7; 25 -13.5; 26 -13.4; 28 -13.2; 30 -13.0; 32 -12.8; 35 -12.4; 37 -12.2; 40 -11.9; 42 -11.7; 45 -11.4; 49 -11.0; 52 -10.7; 56 -10.3; 59 -10.0; 64 -9.7; 68 -9.4; 73 -9.1; 78 -8.9; 83 -8.7; 89 -8.7; 95 -8.8; 102 -8.8; 109 -8.9; 117 -8.9; 125 -9.0; 134 -9.1; 143 -9.0; 153 -8.8; 164 -8.5; 175 -8.1; 188 -7.7; 201 -7.3; 215 -6.8; 230 -6.3; 246 -5.9; 263 -5.5; 282 -5.0; 301 -4.5; 323 -4.0; 345 -3.6; 369 -3.2; 395 -2.8; 423 -2.2; 452 -1.8; 484 -1.6; 518 -1.2; 554 -0.8; 593 -0.2; 635 -0.0; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.4; 1336 -0.7; 1429 -1.2; 1529 -1.6; 1636 -2.0; 1751 -2.3; 1873 -2.3; 2004 -2.2; 2145 -2.3; 2295 -2.5; 2455 -2.5; 2627 -2.8; 2811 -3.3; 3008 -3.6; 3219 -3.7; 3444 -3.1; 3685 -2.9; 3943 -2.8; 4219 -3.8; 4514 -4.6; 4830 -4.7; 5168 -4.1; 5530 -3.6; 5917 -2.8; 6331 -2.0; 6775 -1.1; 7249 -0.3; 7756 -0.2; 8299 -0.4; 8880 -0.6; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.2; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.1dB` and instead set Global volume in the UI for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers and Wilkins C5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 0.81 | -13.7 dB |
| Peaking | 34 Hz   | 0.37 | -9.8 dB  |
| Peaking | 168 Hz  | 0.81 | -6.0 dB  |
| Peaking | 2741 Hz | 1.27 | -2.9 dB  |
| Peaking | 4903 Hz | 2.53 | -4.0 dB  |
| Peaking | 347 Hz  | 2.14 | -0.7 dB  |
| Peaking | 765 Hz  | 1.55 | 1.4 dB   |
| Peaking | 1688 Hz | 3.29 | -1.1 dB  |
| Peaking | 2456 Hz | 7.22 | 0.6 dB   |
| Peaking | 7442 Hz | 8.75 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20C5/Bowers%20&%20Wilkins%20C5.png)