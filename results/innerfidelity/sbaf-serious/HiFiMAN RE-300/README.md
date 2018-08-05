# HiFiMAN RE-300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.0; 23 -0.1; 25 -0.2; 26 -0.2; 28 -0.2; 30 -0.3; 32 -0.4; 35 -0.4; 37 -0.4; 40 -0.4; 42 -0.4; 45 -0.4; 49 -0.5; 52 -0.5; 56 -0.6; 59 -0.6; 64 -0.7; 68 -0.8; 73 -0.9; 78 -1.0; 83 -1.2; 89 -1.5; 95 -2.0; 102 -2.6; 109 -3.0; 117 -3.5; 125 -4.0; 134 -4.5; 143 -4.7; 153 -4.8; 164 -4.9; 175 -4.8; 188 -4.8; 201 -4.7; 215 -4.5; 230 -4.3; 246 -4.1; 263 -3.9; 282 -3.6; 301 -3.3; 323 -3.0; 345 -2.7; 369 -2.4; 395 -2.1; 423 -1.6; 452 -1.3; 484 -1.1; 518 -0.7; 554 -0.2; 593 0.3; 635 0.5; 679 0.7; 726 0.8; 777 1.1; 832 0.9; 890 0.7; 952 0.3; 1019 -0.2; 1090 -0.8; 1167 -0.3; 1248 -0.6; 1336 -1.9; 1429 -2.8; 1529 -3.5; 1636 -3.5; 1751 -2.8; 1873 -1.3; 2004 0.9; 2145 3.2; 2295 5.6; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.5; 6331 2.6; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 1.18 | -0.2 dB |
| Peaking | 189 Hz  | 0.75 | -5.1 dB |
| Peaking | 714 Hz  | 2.54 | 1.3 dB  |
| Peaking | 1621 Hz | 2.26 | -7.5 dB |
| Peaking | 3110 Hz | 0.73 | 7.6 dB  |
| Peaking | 77 Hz   | 3.66 | 0.6 dB  |
| Peaking | 2383 Hz | 5.54 | 2.4 dB  |
| Peaking | 2934 Hz | 1.25 | -1.0 dB |
| Peaking | 5501 Hz | 2.47 | 3.9 dB  |
| Peaking | 7453 Hz | 1.09 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-300/HiFiMAN%20RE-300.png)