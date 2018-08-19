# Audeze LCD-2 Rev 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 2.5; 22 2.5; 23 2.5; 25 2.5; 26 2.5; 28 2.5; 30 2.5; 32 2.5; 35 2.4; 37 2.4; 40 2.3; 42 2.3; 45 2.4; 49 2.4; 52 2.3; 56 1.7; 59 1.3; 64 1.1; 68 1.0; 73 0.9; 78 0.8; 83 0.5; 89 0.3; 95 0.0; 102 -0.2; 109 -0.3; 117 -0.4; 125 -0.7; 134 -0.9; 143 -1.2; 153 -1.3; 164 -1.4; 175 -1.6; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.7; 246 -1.5; 263 -1.5; 282 -1.4; 301 -1.5; 323 -1.5; 345 -1.5; 369 -1.5; 395 -1.4; 423 -1.3; 452 -1.3; 484 -1.5; 518 -1.4; 554 -1.3; 593 -1.1; 635 -1.5; 679 -1.9; 726 -1.9; 777 -1.6; 832 -1.5; 890 -1.1; 952 -0.5; 1019 0.2; 1090 1.1; 1167 1.8; 1248 1.6; 1336 1.2; 1429 0.4; 1529 -0.5; 1636 -0.6; 1751 -0.2; 1873 0.7; 2004 0.8; 2145 1.2; 2295 1.2; 2455 1.7; 2627 1.7; 2811 2.2; 3008 3.2; 3219 2.7; 3444 3.2; 3685 5.0; 3943 5.8; 4219 5.0; 4514 4.1; 4830 2.2; 5168 1.2; 5530 1.7; 5917 2.1; 6331 1.3; 6775 1.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -2.4; 18692 -4.6; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.939527629478357dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Rev 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.6  | 2.9 dB  |
| Peaking | 1171 Hz  | 4.57 | 2.7 dB  |
| Peaking | 3922 Hz  | 3.1  | 4.6 dB  |
| Peaking | 4515 Hz  | 0.27 | 3.7 dB  |
| Peaking | 4526 Hz  | 0.03 | -2.5 dB |
| Peaking | 779 Hz   | 5.06 | -0.6 dB |
| Peaking | 1624 Hz  | 8.22 | -1.2 dB |
| Peaking | 8602 Hz  | 4.15 | -0.9 dB |
| Peaking | 15264 Hz | 3.8  | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20Rev%202/Audeze%20LCD-2%20Rev%202.png)