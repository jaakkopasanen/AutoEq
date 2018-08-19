# LG Quadbeat HSS-F420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.3; 23 -1.3; 25 -1.4; 26 -1.4; 28 -1.5; 30 -1.6; 32 -1.7; 35 -1.8; 37 -1.8; 40 -1.9; 42 -1.9; 45 -2.0; 49 -2.2; 52 -2.3; 56 -2.5; 59 -2.7; 64 -2.9; 68 -3.1; 73 -3.3; 78 -3.5; 83 -3.8; 89 -4.1; 95 -4.4; 102 -4.6; 109 -4.7; 117 -4.8; 125 -5.0; 134 -5.1; 143 -5.3; 153 -5.4; 164 -5.4; 175 -5.4; 188 -5.3; 201 -5.3; 215 -5.1; 230 -5.0; 246 -4.9; 263 -4.7; 282 -4.5; 301 -4.2; 323 -4.0; 345 -3.7; 369 -3.4; 395 -3.2; 423 -2.7; 452 -2.4; 484 -2.2; 518 -1.9; 554 -1.4; 593 -0.9; 635 -0.7; 679 -0.5; 726 -0.2; 777 0.2; 832 0.3; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.6; 1429 -1.0; 1529 -1.3; 1636 -1.5; 1751 -1.6; 1873 -1.4; 2004 -1.3; 2145 -1.3; 2295 -1.3; 2455 -1.0; 2627 -0.8; 2811 -0.4; 3008 0.5; 3219 1.4; 3444 2.4; 3685 2.5; 3943 2.2; 4219 1.2; 4514 0.5; 4830 0.6; 5168 1.3; 5530 1.2; 5917 0.8; 6331 0.8; 6775 0.8; 7249 0.5; 7756 -0.0; 8299 -0.8; 8880 -1.3; 9502 -1.2; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -2.0; 16326 -2.9; 17469 -0.6; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.598421874808779dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `LG Quadbeat HSS-F420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.52 | -4.3 dB |
| Peaking | 261 Hz   | 1.01 | -2.6 dB |
| Peaking | 2161 Hz  | 1.68 | -1.9 dB |
| Peaking | 3649 Hz  | 2.39 | 2.9 dB  |
| Peaking | 16186 Hz | 4.42 | -3.4 dB |
| Peaking | 23 Hz    | 1.56 | -0.8 dB |
| Peaking | 847 Hz   | 1.39 | 2.5 dB  |
| Peaking | 850 Hz   | 0.76 | -1.5 dB |
| Peaking | 6314 Hz  | 2.67 | 0.9 dB  |
| Peaking | 8945 Hz  | 4.94 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/LG%20Quadbeat%20HSS-F420/LG%20Quadbeat%20HSS-F420.png)