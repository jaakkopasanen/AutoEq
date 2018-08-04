# Audeze LCD-2 sn53211704

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 2.4; 22 2.5; 23 2.5; 25 2.5; 26 2.5; 28 2.5; 30 2.6; 32 2.7; 35 2.8; 37 2.8; 40 2.5; 42 2.4; 45 2.3; 49 2.4; 52 2.4; 56 2.2; 59 2.0; 64 1.7; 68 1.6; 73 1.5; 78 1.4; 83 1.4; 89 1.1; 95 0.8; 102 0.4; 109 0.1; 117 -0.3; 125 -0.8; 134 -1.0; 143 -1.2; 153 -1.5; 164 -1.6; 175 -1.7; 188 -1.7; 201 -1.9; 215 -2.0; 230 -2.0; 246 -2.1; 263 -2.1; 282 -2.0; 301 -2.1; 323 -2.1; 345 -1.9; 369 -1.7; 395 -1.5; 423 -1.2; 452 -0.9; 484 -0.9; 518 -0.9; 554 -1.0; 593 -1.1; 635 -1.5; 679 -1.9; 726 -2.2; 777 -2.2; 832 -2.4; 890 -2.0; 952 -0.9; 1019 0.3; 1090 0.8; 1167 0.9; 1248 1.1; 1336 0.5; 1429 -0.4; 1529 -0.7; 1636 -0.4; 1751 0.2; 1873 0.8; 2004 1.2; 2145 1.2; 2295 1.7; 2455 2.0; 2627 2.5; 2811 2.3; 3008 2.5; 3219 2.8; 3444 3.6; 3685 4.5; 3943 5.3; 4219 4.9; 4514 4.4; 4830 3.9; 5168 3.1; 5530 2.2; 5917 1.6; 6331 4.0; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -0.1; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.5; 17469 -3.3; 18692 -5.1; 20000 -4.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn53211704 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.32 | 2.9 dB  |
| Peaking | 203 Hz   | 0.63 | -2.9 dB |
| Peaking | 781 Hz   | 3.9  | -2.3 dB |
| Peaking | 3969 Hz  | 1.58 | 5.0 dB  |
| Peaking | 6549 Hz  | 9.05 | 3.5 dB  |
| Peaking | 1215 Hz  | 2.75 | 3.2 dB  |
| Peaking | 1496 Hz  | 1.32 | -3.1 dB |
| Peaking | 1999 Hz  | 1.82 | 2.1 dB  |
| Peaking | 8363 Hz  | 6.66 | -1.0 dB |
| Peaking | 19153 Hz | 1.83 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn53211704/Audeze%20LCD-2%20sn53211704.png)