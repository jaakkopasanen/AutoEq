# Polk Utrafit 3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -9.2; 22 -9.2; 23 -9.2; 25 -9.2; 26 -9.2; 28 -9.2; 30 -9.2; 32 -9.2; 35 -9.2; 37 -9.2; 40 -9.1; 42 -9.1; 45 -9.1; 49 -9.0; 52 -9.0; 56 -8.9; 59 -8.8; 64 -8.8; 68 -8.8; 73 -8.8; 78 -8.9; 83 -9.0; 89 -9.2; 95 -9.5; 102 -9.9; 109 -10.1; 117 -10.5; 125 -10.8; 134 -11.0; 143 -11.1; 153 -11.1; 164 -11.0; 175 -10.7; 188 -10.4; 201 -10.1; 215 -9.7; 230 -9.3; 246 -9.0; 263 -8.5; 282 -8.0; 301 -7.6; 323 -7.1; 345 -6.6; 369 -6.1; 395 -5.6; 423 -5.0; 452 -4.5; 484 -4.1; 518 -3.6; 554 -2.9; 593 -2.2; 635 -1.7; 679 -1.3; 726 -0.9; 777 -0.5; 832 -0.4; 890 -0.4; 952 -0.2; 1019 0.2; 1090 0.3; 1167 0.4; 1248 0.5; 1336 0.3; 1429 -0.0; 1529 -0.3; 1636 -0.5; 1751 -0.4; 1873 -0.1; 2004 0.2; 2145 0.6; 2295 1.4; 2455 2.6; 2627 3.6; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.1; 4514 1.7; 4830 0.8; 5168 2.8; 5530 5.6; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Utrafit 3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.25 | -8.9 dB |
| Peaking | 160 Hz  | 0.78 | -8.0 dB |
| Peaking | 331 Hz  | 1.23 | -3.2 dB |
| Peaking | 3332 Hz | 2.2  | 6.7 dB  |
| Peaking | 6035 Hz | 4.6  | 6.0 dB  |
| Peaking | 1210 Hz | 1.49 | 1.7 dB  |
| Peaking | 1648 Hz | 1.3  | -1.7 dB |
| Peaking | 2667 Hz | 4.48 | 1.1 dB  |
| Peaking | 9973 Hz | 2.7  | -0.3 dB |
| Peaking | 8028 Hz | 6.5  | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Utrafit%203000/Polk%20Utrafit%203000.png)