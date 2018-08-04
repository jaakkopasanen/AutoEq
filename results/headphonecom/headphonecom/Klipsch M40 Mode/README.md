# Klipsch M40 Mode

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.5; 22 -4.9; 23 -5.0; 25 -5.3; 26 -5.4; 28 -5.5; 30 -5.6; 32 -5.6; 35 -5.6; 37 -5.5; 40 -5.4; 42 -5.4; 45 -5.3; 49 -5.1; 52 -5.0; 56 -4.9; 59 -4.7; 64 -4.6; 68 -4.4; 73 -4.3; 78 -4.1; 83 -4.0; 89 -3.8; 95 -3.7; 102 -3.5; 109 -3.4; 117 -3.2; 125 -3.2; 134 -3.1; 143 -2.9; 153 -2.8; 164 -2.7; 175 -2.4; 188 -2.4; 201 -2.4; 215 -2.1; 230 -2.3; 246 -2.1; 263 -1.9; 282 -1.7; 301 -1.3; 323 -0.7; 345 -0.7; 369 -0.7; 395 -0.7; 423 -0.5; 452 -0.4; 484 -0.3; 518 0.1; 554 0.5; 593 0.6; 635 0.9; 679 1.1; 726 1.0; 777 1.0; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -1.6; 1429 -2.1; 1529 -2.6; 1636 -2.6; 1751 -1.0; 1873 0.4; 2004 3.1; 2145 5.5; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch M40 Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.11 | -5.2 dB |
| Peaking | 691 Hz   | 2.4  | 1.3 dB  |
| Peaking | 1609 Hz  | 1.76 | -7.5 dB |
| Peaking | 2396 Hz  | 1.01 | 8.3 dB  |
| Peaking | 5235 Hz  | 1.97 | 4.9 dB  |
| Peaking | 34 Hz    | 2.2  | -0.4 dB |
| Peaking | 10272 Hz | 1.46 | -0.4 dB |
| Peaking | 6407 Hz  | 5.93 | 2.4 dB  |
| Peaking | 6917 Hz  | 3.82 | 0.9 dB  |
| Peaking | 7485 Hz  | 2.7  | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Klipsch%20M40%20Mode/Klipsch%20M40%20Mode.png)