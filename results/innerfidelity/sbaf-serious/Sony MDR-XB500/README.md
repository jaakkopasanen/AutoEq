# Sony MDR-XB500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.8; 22 -5.3; 23 -5.5; 25 -5.9; 26 -6.0; 28 -6.3; 30 -6.5; 32 -6.7; 35 -6.9; 37 -7.1; 40 -7.2; 42 -7.3; 45 -7.4; 49 -7.5; 52 -7.6; 56 -7.5; 59 -7.4; 64 -7.2; 68 -7.2; 73 -7.5; 78 -7.9; 83 -8.2; 89 -8.5; 95 -8.7; 102 -9.4; 109 -10.0; 117 -10.6; 125 -11.2; 134 -11.7; 143 -12.3; 153 -12.6; 164 -12.3; 175 -12.6; 188 -12.7; 201 -12.8; 215 -13.2; 230 -13.2; 246 -13.0; 263 -12.6; 282 -12.1; 301 -11.9; 323 -11.3; 345 -10.6; 369 -10.0; 395 -9.6; 423 -9.0; 452 -8.4; 484 -7.7; 518 -6.8; 554 -5.7; 593 -4.4; 635 -3.2; 679 -2.3; 726 -1.1; 777 0.0; 832 0.7; 890 0.9; 952 0.5; 1019 -0.0; 1090 -0.5; 1167 -1.4; 1248 -2.8; 1336 -4.1; 1429 -5.0; 1529 -5.4; 1636 -5.5; 1751 -5.3; 1873 -4.8; 2004 -4.1; 2145 -3.2; 2295 -2.1; 2455 -0.8; 2627 0.8; 2811 2.1; 3008 3.7; 3219 5.4; 3444 6.0; 3685 6.0; 3943 4.3; 4219 1.0; 4514 -1.4; 4830 -4.2; 5168 -4.8; 5530 -4.3; 5917 -2.2; 6331 -1.8; 6775 -0.8; 7249 0.5; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.5; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 4 Hz    | 1.62 | -3.9 dB  |
| Peaking | 60 Hz   | 0.22 | -6.6 dB  |
| Peaking | 242 Hz  | 0.75 | -9.7 dB  |
| Peaking | 1721 Hz | 2.68 | -5.7 dB  |
| Peaking | 3399 Hz | 4.53 | 7.6 dB   |
| Peaking | 141 Hz  | 3.09 | -1.8 dB  |
| Peaking | 503 Hz  | 0.91 | -9.0 dB  |
| Peaking | 888 Hz  | 0.48 | 13.8 dB  |
| Peaking | 1343 Hz | 0.81 | -10.1 dB |
| Peaking | 5188 Hz | 3.91 | -6.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB500/Sony%20MDR-XB500.png)