# Audeze LCD-2 sn5312123

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 1.7; 22 1.6; 23 1.6; 25 1.6; 26 1.6; 28 1.7; 30 1.8; 32 1.8; 35 1.9; 37 2.0; 40 1.9; 42 1.8; 45 1.3; 49 0.9; 52 0.8; 56 0.8; 59 0.7; 64 0.5; 68 0.3; 73 0.1; 78 -0.0; 83 -0.2; 89 -0.5; 95 -0.8; 102 -1.0; 109 -1.1; 117 -1.3; 125 -1.6; 134 -1.8; 143 -2.0; 153 -2.1; 164 -2.3; 175 -2.2; 188 -2.2; 201 -2.4; 215 -2.5; 230 -2.6; 246 -2.8; 263 -2.9; 282 -2.9; 301 -2.7; 323 -2.6; 345 -2.6; 369 -2.6; 395 -2.5; 423 -2.1; 452 -2.1; 484 -2.1; 518 -1.8; 554 -1.4; 593 -1.3; 635 -1.4; 679 -1.8; 726 -1.7; 777 -1.4; 832 -1.5; 890 -1.1; 952 -0.4; 1019 0.1; 1090 0.8; 1167 1.2; 1248 1.0; 1336 0.9; 1429 0.4; 1529 0.2; 1636 0.6; 1751 1.0; 1873 1.6; 2004 1.6; 2145 1.3; 2295 1.1; 2455 1.7; 2627 1.4; 2811 1.5; 3008 2.2; 3219 2.1; 3444 2.3; 3685 3.6; 3943 4.1; 4219 3.7; 4514 3.6; 4830 1.8; 5168 0.9; 5530 0.4; 5917 1.4; 6331 2.1; 6775 0.8; 7249 0.7; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.5; 17469 -2.5; 18692 -4.4; 20000 -5.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.233067632699135dB` and instead set Global volume in the UI for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn5312123 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.63 | 2.1 dB  |
| Peaking | 304 Hz   | 0.41 | -3.4 dB |
| Peaking | 787 Hz   | 2.87 | -1.5 dB |
| Peaking | 1174 Hz  | 0.38 | 1.8 dB  |
| Peaking | 4029 Hz  | 2.75 | 3.5 dB  |
| Peaking | 1539 Hz  | 7.98 | -1.1 dB |
| Peaking | 5254 Hz  | 0.13 | 0.2 dB  |
| Peaking | 15828 Hz | 1.4  | 2.4 dB  |
| Peaking | 19666 Hz | 0.68 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn5312123/Audeze%20LCD-2%20sn5312123.png)