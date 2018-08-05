# HiFiMAN RE-272

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.1; 22 5.1; 23 5.1; 25 5.0; 26 5.0; 28 5.0; 30 4.9; 32 4.9; 35 4.9; 37 4.9; 40 4.9; 42 4.9; 45 4.8; 49 4.7; 52 4.7; 56 4.7; 59 4.6; 64 4.6; 68 4.5; 73 4.4; 78 4.2; 83 3.9; 89 3.4; 95 3.0; 102 2.4; 109 1.9; 117 1.3; 125 0.6; 134 0.1; 143 -0.3; 153 -0.5; 164 -0.7; 175 -0.8; 188 -0.9; 201 -1.1; 215 -1.0; 230 -1.0; 246 -1.1; 263 -1.1; 282 -1.0; 301 -1.0; 323 -0.9; 345 -1.0; 369 -1.0; 395 -0.9; 423 -0.7; 452 -0.6; 484 -0.5; 518 -0.3; 554 0.1; 593 0.6; 635 0.9; 679 1.0; 726 1.2; 777 1.5; 832 1.4; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -1.6; 1248 -2.6; 1336 -3.8; 1429 -5.0; 1529 -6.4; 1636 -7.5; 1751 -8.5; 1873 -8.5; 2004 -7.6; 2145 -5.8; 2295 -3.5; 2455 -0.7; 2627 1.9; 2811 4.8; 3008 5.8; 3219 6.0; 3444 6.0; 3685 5.9; 3943 4.6; 4219 2.6; 4514 2.0; 4830 3.2; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.3; 9502 -1.8; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-272 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.82 | 5.3 dB   |
| Peaking | 70 Hz   | 1.86 | 3.5 dB   |
| Peaking | 1853 Hz | 2.15 | -10.6 dB |
| Peaking | 3165 Hz | 2.12 | 8.1 dB   |
| Peaking | 5807 Hz | 3.55 | 6.2 dB   |
| Peaking | 98 Hz   | 2.59 | 1.4 dB   |
| Peaking | 231 Hz  | 0.57 | -1.5 dB  |
| Peaking | 795 Hz  | 1.75 | 2.5 dB   |
| Peaking | 1420 Hz | 4.41 | -1.4 dB  |
| Peaking | 9183 Hz | 6.18 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-272/HiFiMAN%20RE-272.png)