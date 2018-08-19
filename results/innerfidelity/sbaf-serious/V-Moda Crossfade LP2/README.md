# V-Moda Crossfade LP2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.0; 23 -1.1; 25 -1.4; 26 -1.5; 28 -1.7; 30 -1.8; 32 -2.0; 35 -2.2; 37 -2.3; 40 -2.4; 42 -2.5; 45 -2.6; 49 -2.7; 52 -2.8; 56 -2.8; 59 -2.8; 64 -2.8; 68 -2.8; 73 -2.9; 78 -3.2; 83 -3.5; 89 -4.0; 95 -4.4; 102 -4.8; 109 -5.1; 117 -5.4; 125 -5.5; 134 -5.7; 143 -5.7; 153 -5.7; 164 -5.4; 175 -5.3; 188 -5.2; 201 -4.8; 215 -4.1; 230 -3.4; 246 -2.9; 263 -2.1; 282 -1.2; 301 -0.2; 323 0.7; 345 1.8; 369 2.7; 395 3.5; 423 4.2; 452 4.7; 484 4.8; 518 4.8; 554 4.6; 593 4.3; 635 3.5; 679 2.4; 726 1.6; 777 1.0; 832 0.5; 890 0.2; 952 0.0; 1019 -0.0; 1090 -0.1; 1167 0.0; 1248 0.2; 1336 -0.2; 1429 -0.4; 1529 0.0; 1636 0.6; 1751 1.5; 1873 2.9; 2004 5.3; 2145 5.0; 2295 4.9; 2455 5.0; 2627 5.0; 2811 4.3; 3008 0.8; 3219 -1.7; 3444 -1.1; 3685 1.2; 3943 3.7; 4219 4.8; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099952559277957dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.98 | -1.6 dB |
| Peaking | 152 Hz  | 0.71 | -6.1 dB |
| Peaking | 462 Hz  | 1.53 | 6.6 dB  |
| Peaking | 2260 Hz | 3.37 | 5.5 dB  |
| Peaking | 5304 Hz | 2.27 | 6.9 dB  |
| Peaking | 1234 Hz | 1.98 | -0.9 dB |
| Peaking | 2789 Hz | 5.76 | 3.8 dB  |
| Peaking | 3266 Hz | 4.24 | -5.0 dB |
| Peaking | 4147 Hz | 4.59 | 2.5 dB  |
| Peaking | 8368 Hz | 4.5  | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP2/V-Moda%20Crossfade%20LP2.png)