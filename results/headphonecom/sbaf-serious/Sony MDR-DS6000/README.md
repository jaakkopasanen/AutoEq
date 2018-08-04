# Sony MDR-DS6000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.5; 42 4.9; 45 3.9; 49 2.6; 52 1.8; 56 1.0; 59 0.6; 64 -0.2; 68 -1.1; 73 -2.1; 78 -2.7; 83 -3.2; 89 -3.6; 95 -3.9; 102 -4.0; 109 -4.1; 117 -4.0; 125 -4.0; 134 -3.7; 143 -3.5; 153 -3.3; 164 -2.9; 175 -2.4; 188 -2.6; 201 -2.3; 215 -1.4; 230 -1.7; 246 -1.6; 263 -1.4; 282 -1.1; 301 -0.9; 323 -0.7; 345 -0.5; 369 -0.4; 395 -0.3; 423 0.3; 452 0.3; 484 -0.1; 518 -0.3; 554 -0.5; 593 -0.5; 635 -0.7; 679 -1.3; 726 -1.5; 777 -1.5; 832 -1.4; 890 -0.9; 952 0.1; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.6; 1336 -2.8; 1429 -3.1; 1529 -3.7; 1636 -4.4; 1751 -4.9; 1873 -5.3; 2004 -5.7; 2145 -5.3; 2295 -4.3; 2455 -2.7; 2627 -1.2; 2811 0.4; 3008 1.7; 3219 3.0; 3444 4.1; 3685 5.8; 3943 6.0; 4219 5.1; 4514 3.7; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.59 | 7.6 dB  |
| Peaking | 96 Hz   | 0.74 | -6.2 dB |
| Peaking | 1986 Hz | 1.45 | -6.6 dB |
| Peaking | 3698 Hz | 1.95 | 6.5 dB  |
| Peaking | 5752 Hz | 3.04 | 5.7 dB  |
| Peaking | 2 Hz    | 1.51 | 0.3 dB  |
| Peaking | 444 Hz  | 3.85 | 1.1 dB  |
| Peaking | 871 Hz  | 1.91 | -1.6 dB |
| Peaking | 965 Hz  | 4.93 | 2.6 dB  |
| Peaking | 8221 Hz | 4.72 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)