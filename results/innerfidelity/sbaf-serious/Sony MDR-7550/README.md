# Sony MDR-7550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.2; 22 4.9; 23 4.8; 25 4.6; 26 4.5; 28 4.3; 30 4.1; 32 4.0; 35 3.8; 37 3.7; 40 3.6; 42 3.6; 45 3.5; 49 3.4; 52 3.3; 56 3.3; 59 3.2; 64 3.0; 68 2.9; 73 2.8; 78 2.6; 83 2.3; 89 1.9; 95 1.5; 102 0.9; 109 0.4; 117 -0.2; 125 -0.8; 134 -1.3; 143 -1.7; 153 -1.9; 164 -2.0; 175 -2.1; 188 -2.2; 201 -2.1; 215 -2.0; 230 -2.0; 246 -2.0; 263 -1.9; 282 -1.7; 301 -1.6; 323 -1.5; 345 -1.3; 369 -1.2; 395 -1.0; 423 -0.7; 452 -0.5; 484 -0.5; 518 -0.3; 554 -0.0; 593 0.3; 635 0.5; 679 0.5; 726 0.7; 777 0.8; 832 0.7; 890 0.4; 952 0.2; 1019 -0.0; 1090 0.0; 1167 -0.2; 1248 -0.9; 1336 -1.6; 1429 -2.4; 1529 -3.1; 1636 -3.5; 1751 -3.6; 1873 -3.2; 2004 -2.6; 2145 -1.6; 2295 -0.3; 2455 1.5; 2627 3.2; 2811 4.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.0; 4514 0.7; 4830 -2.1; 5168 -2.6; 5530 0.7; 5917 4.4; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.05 | 4.9 dB  |
| Peaking | 61 Hz   | 2.22 | 2.7 dB  |
| Peaking | 1772 Hz | 2.29 | -4.6 dB |
| Peaking | 3241 Hz | 2.41 | 7.5 dB  |
| Peaking | 6353 Hz | 7.86 | 5.8 dB  |
| Peaking | 91 Hz   | 1.83 | 2.1 dB  |
| Peaking | 183 Hz  | 0.67 | -2.6 dB |
| Peaking | 748 Hz  | 1.81 | 1.3 dB  |
| Peaking | 4008 Hz | 8    | 3.0 dB  |
| Peaking | 4964 Hz | 7.54 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7550/Sony%20MDR-7550.png)