# Sterling TE-400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.3; 64 3.8; 68 2.7; 73 1.3; 78 0.1; 83 -0.7; 89 -1.6; 95 -2.7; 102 -3.7; 109 -4.1; 117 -4.2; 125 -4.4; 134 -4.4; 143 -4.3; 153 -4.2; 164 -3.9; 175 -3.6; 188 -3.5; 201 -3.3; 215 -3.2; 230 -3.1; 246 -3.0; 263 -2.8; 282 -2.4; 301 -1.9; 323 -1.9; 345 -1.8; 369 -1.8; 395 -1.8; 423 -1.5; 452 -1.5; 484 -1.6; 518 -1.4; 554 -1.3; 593 0.4; 635 3.5; 679 5.9; 726 6.0; 777 6.0; 832 5.1; 890 2.9; 952 1.2; 1019 -0.4; 1090 -1.0; 1167 -1.2; 1248 -0.8; 1336 0.0; 1429 0.3; 1529 1.4; 1636 2.0; 1751 2.9; 1873 3.7; 2004 4.7; 2145 5.0; 2295 4.9; 2455 4.8; 2627 4.0; 2811 3.5; 3008 2.9; 3219 2.9; 3444 4.5; 3685 5.8; 3943 2.8; 4219 -3.0; 4514 -3.4; 4830 -1.9; 5168 1.9; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.5; 8299 -1.8; 8880 -0.6; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sterling TE-400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 62 Hz   | 0.23 | 26.5 dB  |
| Peaking | 99 Hz   | 0.28 | -26.6 dB |
| Peaking | 736 Hz  | 3.27 | 8.9 dB   |
| Peaking | 2305 Hz | 1.65 | 5.9 dB   |
| Peaking | 6034 Hz | 5.59 | 6.7 dB   |
| Peaking | 2989 Hz | 3    | -0.8 dB  |
| Peaking | 3739 Hz | 4.62 | 7.6 dB   |
| Peaking | 4345 Hz | 3.9  | -7.7 dB  |
| Peaking | 5427 Hz | 9.71 | 3.9 dB   |
| Peaking | 8242 Hz | 9.13 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sterling%20TE-400/Sterling%20TE-400.png)