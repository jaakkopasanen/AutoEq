# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 0.5; 22 0.5; 23 0.5; 25 0.5; 26 0.5; 28 0.6; 30 0.6; 32 0.7; 35 0.6; 37 0.6; 40 0.5; 42 0.5; 45 0.5; 49 0.6; 52 0.8; 56 0.3; 59 -0.3; 64 -0.7; 68 -0.8; 73 -1.0; 78 -1.1; 83 -1.1; 89 -1.2; 95 -1.4; 102 -1.7; 109 -1.8; 117 -2.0; 125 -2.1; 134 -2.3; 143 -2.5; 153 -2.8; 164 -2.9; 175 -3.0; 188 -3.3; 201 -3.3; 215 -3.3; 230 -3.2; 246 -3.0; 263 -3.0; 282 -3.2; 301 -3.0; 323 -2.7; 345 -2.3; 369 -2.1; 395 -2.2; 423 -2.3; 452 -2.3; 484 -2.4; 518 -2.4; 554 -2.3; 593 -2.4; 635 -2.4; 679 -2.4; 726 -2.2; 777 -2.3; 832 -2.2; 890 -1.7; 952 -0.7; 1019 0.1; 1090 0.6; 1167 1.5; 1248 0.7; 1336 -0.1; 1429 -1.0; 1529 -1.9; 1636 -2.3; 1751 -2.5; 1873 -1.1; 2004 -0.3; 2145 -0.1; 2295 -1.4; 2455 -0.5; 2627 1.1; 2811 0.9; 3008 0.6; 3219 0.6; 3444 2.1; 3685 3.0; 3943 3.5; 4219 3.5; 4514 2.8; 4830 1.0; 5168 0.2; 5530 -0.0; 5917 -0.2; 6331 0.3; 6775 0.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -2.6; 18692 -3.9; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.601054363382767dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 214 Hz   | 0.7  | -3.3 dB |
| Peaking | 646 Hz   | 2.04 | -1.9 dB |
| Peaking | 1701 Hz  | 6.2  | -2.8 dB |
| Peaking | 4003 Hz  | 3.36 | 3.9 dB  |
| Peaking | 18865 Hz | 2.01 | -4.4 dB |
| Peaking | 35 Hz    | 1.4  | 1.1 dB  |
| Peaking | 1135 Hz  | 1.53 | -1.4 dB |
| Peaking | 1137 Hz  | 3.8  | 3.4 dB  |
| Peaking | 5597 Hz  | 5.2  | -0.8 dB |
| Peaking | 7143 Hz  | 9.21 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)