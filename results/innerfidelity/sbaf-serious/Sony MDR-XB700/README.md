# Sony MDR-XB700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -7.1; 22 -7.3; 23 -7.3; 25 -7.5; 26 -7.6; 28 -7.8; 30 -7.9; 32 -8.0; 35 -8.1; 37 -8.0; 40 -7.7; 42 -7.5; 45 -7.4; 49 -7.3; 52 -7.1; 56 -7.2; 59 -7.6; 64 -8.3; 68 -8.9; 73 -9.3; 78 -9.8; 83 -10.1; 89 -10.4; 95 -10.8; 102 -11.1; 109 -11.4; 117 -11.5; 125 -11.6; 134 -11.7; 143 -11.8; 153 -11.4; 164 -11.2; 175 -11.3; 188 -10.8; 201 -10.3; 215 -9.8; 230 -9.1; 246 -8.3; 263 -7.4; 282 -6.4; 301 -5.6; 323 -4.7; 345 -4.0; 369 -3.5; 395 -3.0; 423 -2.2; 452 -1.5; 484 -0.8; 518 0.1; 554 0.7; 593 1.7; 635 2.9; 679 3.9; 726 4.6; 777 4.5; 832 3.4; 890 2.3; 952 1.2; 1019 -0.3; 1090 -1.6; 1167 -2.8; 1248 -4.0; 1336 -5.3; 1429 -6.3; 1529 -7.3; 1636 -7.9; 1751 -8.3; 1873 -8.5; 2004 -8.4; 2145 -7.7; 2295 -6.3; 2455 -4.2; 2627 -2.2; 2811 -0.1; 3008 2.2; 3219 3.8; 3444 3.2; 3685 -1.3; 3943 -2.2; 4219 -1.3; 4514 -1.2; 4830 -1.6; 5168 -1.5; 5530 -3.5; 5917 -7.7; 6331 -5.1; 6775 0.3; 7249 1.2; 7756 0.2; 8299 -3.3; 8880 -6.8; 9502 -6.9; 10167 -4.0; 10879 -0.7; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -0.6; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.27 | -7.3 dB |
| Peaking | 157 Hz   | 0.95 | -9.0 dB |
| Peaking | 1819 Hz  | 2.5  | -9.7 dB |
| Peaking | 9247 Hz  | 4.54 | -7.7 dB |
| Peaking | 24000 Hz | 2.21 | -4.3 dB |
| Peaking | 741 Hz   | 2.45 | 6.3 dB  |
| Peaking | 2268 Hz  | 7.52 | -2.7 dB |
| Peaking | 1333 Hz  | 3.95 | -3.0 dB |
| Peaking | 3214 Hz  | 6.95 | 5.9 dB  |
| Peaking | 5978 Hz  | 9.27 | -8.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB700/Sony%20MDR-XB700.png)