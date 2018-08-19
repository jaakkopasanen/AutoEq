# Audeze LCD-X sample 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.2; 22 4.1; 23 4.0; 25 3.8; 26 3.7; 28 3.5; 30 3.3; 32 3.0; 35 2.1; 37 1.3; 40 0.3; 42 -0.0; 45 -0.1; 49 0.1; 52 0.2; 56 0.4; 59 0.5; 64 0.5; 68 0.4; 73 0.2; 78 0.1; 83 -0.0; 89 -0.3; 95 -0.5; 102 -0.7; 109 -0.8; 117 -1.0; 125 -1.2; 134 -1.4; 143 -1.6; 153 -1.7; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.1; 215 -2.1; 230 -2.1; 246 -2.2; 263 -2.2; 282 -2.1; 301 -2.0; 323 -1.8; 345 -1.6; 369 -1.4; 395 -1.2; 423 -1.1; 452 -1.3; 484 -1.6; 518 -1.6; 554 -1.2; 593 -0.9; 635 -1.1; 679 -1.3; 726 -1.3; 777 -0.9; 832 -0.8; 890 -0.2; 952 0.1; 1019 0.0; 1090 0.3; 1167 0.2; 1248 0.1; 1336 -0.4; 1429 -0.6; 1529 -0.6; 1636 -0.6; 1751 -0.3; 1873 -0.4; 2004 -0.6; 2145 -0.6; 2295 -0.4; 2455 0.4; 2627 1.8; 2811 3.1; 3008 4.5; 3219 5.3; 3444 5.8; 3685 6.0; 3943 5.6; 4219 3.2; 4514 -0.3; 4830 -0.5; 5168 4.5; 5530 6.0; 5917 5.5; 6331 3.9; 6775 2.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.7; 16326 -2.7; 17469 -4.0; 18692 -5.1; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999918362886dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.26 | 4.4 dB  |
| Peaking | 263 Hz   | 0.53 | -2.1 dB |
| Peaking | 3462 Hz  | 3.33 | 6.6 dB  |
| Peaking | 5807 Hz  | 4.68 | 6.1 dB  |
| Peaking | 19340 Hz | 1.25 | -6.2 dB |
| Peaking | 1085 Hz  | 3.76 | 0.9 dB  |
| Peaking | 2881 Hz  | 3.97 | 4.0 dB  |
| Peaking | 3170 Hz  | 1.24 | -4.5 dB |
| Peaking | 4258 Hz  | 1.88 | 5.4 dB  |
| Peaking | 4648 Hz  | 7.39 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X%20sample%203/Audeze%20LCD-X%20sample%203.png)