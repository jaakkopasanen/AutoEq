# Sennheiser IE 800 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.7; 22 -4.8; 23 -4.9; 25 -4.9; 26 -5.0; 28 -5.0; 30 -5.0; 32 -5.0; 35 -5.0; 37 -4.9; 40 -4.8; 42 -4.8; 45 -4.7; 49 -4.5; 52 -4.4; 56 -4.3; 59 -4.2; 64 -4.0; 68 -3.9; 73 -3.8; 78 -3.8; 83 -3.8; 89 -3.9; 95 -4.1; 102 -4.4; 109 -4.5; 117 -4.8; 125 -5.1; 134 -5.3; 143 -5.3; 153 -5.2; 164 -5.1; 175 -4.8; 188 -4.5; 201 -4.3; 215 -3.9; 230 -3.6; 246 -3.3; 263 -3.0; 282 -2.6; 301 -2.4; 323 -2.0; 345 -1.7; 369 -1.5; 395 -1.3; 423 -0.9; 452 -0.7; 484 -0.5; 518 -0.3; 554 0.0; 593 0.4; 635 0.5; 679 0.6; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.6; 1429 -0.8; 1529 -0.9; 1636 -0.8; 1751 -0.4; 1873 0.3; 2004 1.1; 2145 2.2; 2295 3.4; 2455 4.8; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 3.5; 4830 2.0; 5168 1.5; 5530 1.0; 5917 3.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -2.7; 10167 -3.1; 10879 -1.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.44 | -4.9 dB |
| Peaking | 159 Hz  | 0.88 | -4.5 dB |
| Peaking | 3287 Hz | 1.65 | 7.0 dB  |
| Peaking | 6417 Hz | 7.11 | 5.0 dB  |
| Peaking | 9888 Hz | 4.31 | -3.7 dB |
| Peaking | 729 Hz  | 2.12 | 1.1 dB  |
| Peaking | 1586 Hz | 2.06 | -1.9 dB |
| Peaking | 2552 Hz | 3.96 | 2.6 dB  |
| Peaking | 4130 Hz | 5.06 | 3.7 dB  |
| Peaking | 3772 Hz | 1.63 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%202013/Sennheiser%20IE%20800%202013.png)