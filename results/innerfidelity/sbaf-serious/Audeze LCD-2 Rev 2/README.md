# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 2.5; 22 2.5; 23 2.5; 25 2.5; 26 2.5; 28 2.5; 30 2.6; 32 2.6; 35 2.5; 37 2.5; 40 2.5; 42 2.5; 45 2.5; 49 2.7; 52 2.6; 56 2.1; 59 1.7; 64 1.6; 68 1.6; 73 1.6; 78 1.5; 83 1.3; 89 1.1; 95 0.8; 102 0.4; 109 0.1; 117 -0.2; 125 -0.7; 134 -1.0; 143 -1.4; 153 -1.6; 164 -1.7; 175 -1.8; 188 -1.9; 201 -1.9; 215 -1.9; 230 -1.8; 246 -1.6; 263 -1.6; 282 -1.5; 301 -1.6; 323 -1.6; 345 -1.5; 369 -1.5; 395 -1.5; 423 -1.3; 452 -1.3; 484 -1.5; 518 -1.4; 554 -1.3; 593 -1.1; 635 -1.5; 679 -1.9; 726 -1.9; 777 -1.6; 832 -1.5; 890 -1.1; 952 -0.5; 1019 0.2; 1090 1.1; 1167 1.8; 1248 1.6; 1336 1.2; 1429 0.4; 1529 -0.5; 1636 -0.6; 1751 -0.2; 1873 0.7; 2004 0.8; 2145 1.2; 2295 1.2; 2455 1.7; 2627 1.7; 2811 2.2; 3008 3.2; 3219 2.7; 3444 3.2; 3685 5.0; 3943 5.8; 4219 5.0; 4514 4.1; 4830 2.2; 5168 1.2; 5530 1.7; 5917 2.1; 6331 1.3; 6775 1.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -2.4; 18692 -4.6; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.26 | 3.1 dB  |
| Peaking | 182 Hz   | 0.59 | -3.5 dB |
| Peaking | 709 Hz   | 3.49 | -1.7 dB |
| Peaking | 3893 Hz  | 1.74 | 5.1 dB  |
| Peaking | 10940 Hz | 1.95 | -0.3 dB |
| Peaking | 1167 Hz  | 2.6  | 2.4 dB  |
| Peaking | 932 Hz   | 2.71 | -1.2 dB |
| Peaking | 1573 Hz  | 5.93 | -1.6 dB |
| Peaking | 5144 Hz  | 6.38 | -2.5 dB |
| Peaking | 5478 Hz  | 2.46 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)