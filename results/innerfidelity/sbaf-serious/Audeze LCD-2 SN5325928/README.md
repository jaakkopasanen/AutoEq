# Audeze LCD-2 sn5325928

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.4; 22 4.4; 23 4.4; 25 4.4; 26 4.4; 28 4.4; 30 4.4; 32 4.3; 35 4.2; 37 4.2; 40 4.1; 42 4.1; 45 4.0; 49 3.8; 52 3.7; 56 3.4; 59 3.3; 64 3.2; 68 3.1; 73 2.9; 78 2.7; 83 2.5; 89 2.2; 95 2.0; 102 1.8; 109 1.7; 117 1.5; 125 1.3; 134 1.1; 143 1.0; 153 0.8; 164 0.7; 175 0.6; 188 0.5; 201 0.4; 215 0.4; 230 0.5; 246 0.3; 263 0.3; 282 0.4; 301 0.4; 323 0.4; 345 0.3; 369 0.3; 395 0.2; 423 0.2; 452 0.1; 484 -0.0; 518 -0.0; 554 -0.1; 593 -0.2; 635 -0.3; 679 -0.3; 726 -0.2; 777 -0.1; 832 -0.3; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.2; 1167 0.0; 1248 0.1; 1336 -0.2; 1429 -0.6; 1529 -1.0; 1636 -1.2; 1751 -0.8; 1873 -0.0; 2004 0.3; 2145 0.4; 2295 1.4; 2455 1.9; 2627 2.5; 2811 3.0; 3008 3.5; 3219 4.4; 3444 5.7; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.3; 4830 4.1; 5168 5.1; 5530 5.9; 5917 5.9; 6331 5.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.9; 17469 -2.2; 18692 -2.8; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999857591355dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5325928 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.38 | 4.5 dB  |
| Peaking | 1634 Hz  | 3.11 | -1.7 dB |
| Peaking | 3686 Hz  | 1.76 | 5.7 dB  |
| Peaking | 6096 Hz  | 2.55 | 6.6 dB  |
| Peaking | 7410 Hz  | 1.5  | -2.3 dB |
| Peaking | 748 Hz   | 1.64 | -0.4 dB |
| Peaking | 1161 Hz  | 3.28 | 0.3 dB  |
| Peaking | 18811 Hz | 1.79 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5325928/Audeze%20LCD-2%20sn5325928.png)