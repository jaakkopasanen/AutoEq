# Audeze LCD-4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 4.7; 23 4.7; 25 4.6; 26 4.5; 28 4.4; 30 4.3; 32 4.2; 35 4.2; 37 4.2; 40 4.1; 42 4.0; 45 3.9; 49 3.8; 52 3.7; 56 3.5; 59 3.4; 64 3.3; 68 3.2; 73 3.0; 78 2.8; 83 2.6; 89 2.3; 95 2.1; 102 1.9; 109 1.8; 117 1.6; 125 1.4; 134 1.2; 143 1.0; 153 0.9; 164 0.8; 175 0.7; 188 0.7; 201 0.6; 215 0.6; 230 0.7; 246 0.6; 263 0.5; 282 0.5; 301 0.4; 323 0.3; 345 0.4; 369 0.4; 395 0.3; 423 0.2; 452 0.1; 484 -0.0; 518 0.0; 554 0.1; 593 0.2; 635 0.2; 679 0.0; 726 0.2; 777 0.2; 832 0.0; 890 0.1; 952 0.1; 1019 0.1; 1090 0.0; 1167 -0.2; 1248 -0.2; 1336 -0.3; 1429 -0.6; 1529 -1.2; 1636 -1.3; 1751 -0.9; 1873 -0.5; 2004 -0.4; 2145 -0.5; 2295 0.2; 2455 1.4; 2627 2.1; 2811 2.3; 3008 3.4; 3219 4.9; 3444 5.1; 3685 5.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.8; 5917 4.8; 6331 3.9; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.7; 18692 -4.9; 20000 -7.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734476dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.59 | 4.2 dB  |
| Peaking | 59 Hz    | 0.67 | 2.3 dB  |
| Peaking | 280 Hz   | 1.7  | 0.2 dB  |
| Peaking | 1767 Hz  | 1.94 | -2.0 dB |
| Peaking | 4356 Hz  | 1.27 | 6.8 dB  |
| Peaking | 3244 Hz  | 6.83 | 1.4 dB  |
| Peaking | 4515 Hz  | 1.63 | -1.9 dB |
| Peaking | 6010 Hz  | 1.47 | 3.2 dB  |
| Peaking | 7945 Hz  | 2.02 | -2.7 dB |
| Peaking | 19520 Hz | 2.01 | -7.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-4/Audeze%20LCD-4.png)