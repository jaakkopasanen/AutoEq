# Stax SR-009 SZ9-1278

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.6; 64 5.0; 68 5.2; 73 5.6; 78 5.7; 83 5.7; 89 5.5; 95 5.3; 102 5.0; 109 4.8; 117 4.4; 125 4.0; 134 3.8; 143 3.5; 153 3.4; 164 3.2; 175 3.1; 188 3.0; 201 3.0; 215 3.0; 230 3.0; 246 2.9; 263 2.9; 282 3.0; 301 2.9; 323 2.9; 345 2.8; 369 2.8; 395 2.7; 423 2.6; 452 2.5; 484 2.1; 518 2.0; 554 2.1; 593 2.1; 635 2.0; 679 1.7; 726 1.5; 777 1.6; 832 1.6; 890 1.2; 952 0.6; 1019 -0.0; 1090 0.1; 1167 -0.2; 1248 -0.2; 1336 -0.1; 1429 -0.1; 1529 -0.1; 1636 -0.5; 1751 0.2; 1873 1.5; 2004 2.6; 2145 3.4; 2295 3.2; 2455 4.1; 2627 4.3; 2811 3.8; 3008 3.4; 3219 3.1; 3444 4.0; 3685 4.0; 3943 2.9; 4219 1.7; 4514 0.8; 4830 -0.2; 5168 1.5; 5530 5.5; 5917 5.9; 6331 5.5; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.21 | 4.8 dB  |
| Peaking | 126 Hz  | 0.22 | 2.8 dB  |
| Peaking | 2829 Hz | 1.83 | 4.2 dB  |
| Peaking | 6037 Hz | 4.81 | 6.3 dB  |
| Peaking | 1907 Hz | 1.45 | -2.9 dB |
| Peaking | 2071 Hz | 3.35 | 3.7 dB  |
| Peaking | 4661 Hz | 1.72 | 2.8 dB  |
| Peaking | 4770 Hz | 5.12 | -4.7 dB |
| Peaking | 8234 Hz | 2.51 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278/Stax%20SR-009%20SZ9-1278.png)