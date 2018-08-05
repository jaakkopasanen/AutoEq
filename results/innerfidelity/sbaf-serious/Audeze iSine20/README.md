# Audeze iSine20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 5.8; 125 5.2; 134 4.7; 143 4.4; 153 4.1; 164 3.8; 175 3.7; 188 3.6; 201 3.6; 215 3.6; 230 3.6; 246 3.5; 263 3.4; 282 3.5; 301 3.4; 323 3.4; 345 3.3; 369 3.2; 395 3.1; 423 3.2; 452 3.1; 484 2.8; 518 2.6; 554 2.6; 593 2.6; 635 2.3; 679 1.9; 726 1.6; 777 1.5; 832 1.1; 890 0.6; 952 0.2; 1019 -0.2; 1090 -0.5; 1167 -0.8; 1248 -0.6; 1336 -0.3; 1429 -1.3; 1529 -2.1; 1636 -1.8; 1751 -0.6; 1873 1.0; 2004 2.7; 2145 4.3; 2295 5.9; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.07 | 5.8 dB  |
| Peaking | 1613 Hz | 1.97 | -4.9 dB |
| Peaking | 4191 Hz | 1.83 | 4.4 dB  |
| Peaking | 2434 Hz | 1.47 | 6.4 dB  |
| Peaking | 5895 Hz | 3.65 | 4.3 dB  |
| Peaking | 116 Hz  | 1.06 | 2.0 dB  |
| Peaking | 156 Hz  | 1.05 | -2.5 dB |
| Peaking | 573 Hz  | 0.75 | 0.9 dB  |
| Peaking | 1026 Hz | 3.19 | -1.2 dB |
| Peaking | 8339 Hz | 3.83 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20iSine20/Audeze%20iSine20.png)