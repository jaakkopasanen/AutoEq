# Sony MDR-SA3000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.4; 83 4.9; 89 4.5; 95 4.2; 102 3.5; 109 2.8; 117 2.3; 125 1.8; 134 1.3; 143 1.0; 153 0.8; 164 1.0; 175 1.1; 188 1.0; 201 1.0; 215 1.1; 230 1.3; 246 1.2; 263 1.2; 282 1.2; 301 1.1; 323 0.9; 345 0.7; 369 0.4; 395 0.4; 423 0.3; 452 0.0; 484 -0.4; 518 -0.8; 554 -0.8; 593 -0.7; 635 -1.2; 679 -1.6; 726 -1.7; 777 -1.6; 832 -1.5; 890 -1.0; 952 -0.4; 1019 0.3; 1090 1.4; 1167 2.1; 1248 3.2; 1336 3.9; 1429 4.1; 1529 4.2; 1636 4.5; 1751 3.9; 1873 3.4; 2004 2.5; 2145 0.9; 2295 -1.1; 2455 -1.5; 2627 -1.7; 2811 -1.5; 3008 -0.7; 3219 0.3; 3444 2.5; 3685 5.1; 3943 6.0; 4219 6.0; 4514 3.3; 4830 3.3; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.2; 7249 0.7; 7756 -0.7; 8299 -2.9; 8880 -4.5; 9502 -3.3; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.47 | 6.7 dB  |
| Peaking | 1530 Hz | 3.18 | 5.0 dB  |
| Peaking | 3977 Hz | 6.04 | 5.8 dB  |
| Peaking | 5807 Hz | 2.85 | 6.7 dB  |
| Peaking | 8796 Hz | 4.21 | -5.5 dB |
| Peaking | 143 Hz  | 5.03 | -1.1 dB |
| Peaking | 763 Hz  | 1.96 | -2.3 dB |
| Peaking | 1201 Hz | 5.5  | 1.3 dB  |
| Peaking | 2401 Hz | 1.22 | 3.0 dB  |
| Peaking | 2614 Hz | 2.56 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-SA3000/Sony%20MDR-SA3000.png)