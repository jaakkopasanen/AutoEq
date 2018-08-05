# AudioFly AF180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.0; 22 2.8; 23 2.7; 25 2.5; 26 2.5; 28 2.3; 30 2.2; 32 2.2; 35 2.0; 37 2.0; 40 1.9; 42 1.9; 45 1.8; 49 1.6; 52 1.6; 56 1.5; 59 1.5; 64 1.4; 68 1.3; 73 1.2; 78 1.0; 83 0.7; 89 0.2; 95 -0.2; 102 -0.8; 109 -1.3; 117 -1.9; 125 -2.4; 134 -2.8; 143 -3.1; 153 -3.4; 164 -3.6; 175 -3.6; 188 -3.5; 201 -3.7; 215 -3.5; 230 -3.4; 246 -3.4; 263 -3.3; 282 -3.1; 301 -3.0; 323 -2.8; 345 -2.7; 369 -2.5; 395 -2.4; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.5; 554 -1.1; 593 -0.7; 635 -0.5; 679 -0.4; 726 -0.2; 777 0.1; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.1; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.2; 1429 -0.2; 1529 -0.3; 1636 -0.1; 1751 0.3; 1873 0.8; 2004 1.6; 2145 2.2; 2295 3.0; 2455 4.1; 2627 4.9; 2811 5.5; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.8; 10167 -3.3; 10879 -2.4; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.26 | 3.0 dB  |
| Peaking | 81 Hz    | 1.07 | 3.0 dB  |
| Peaking | 153 Hz   | 0.44 | -4.8 dB |
| Peaking | 4281 Hz  | 0.84 | 6.9 dB  |
| Peaking | 10080 Hz | 2.62 | -4.2 dB |
| Peaking | 1640 Hz  | 2.55 | -1.6 dB |
| Peaking | 2864 Hz  | 2.56 | 2.0 dB  |
| Peaking | 4292 Hz  | 1.67 | -1.9 dB |
| Peaking | 6507 Hz  | 1.71 | 3.1 dB  |
| Peaking | 7601 Hz  | 4.13 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF180/AudioFly%20AF180.png)