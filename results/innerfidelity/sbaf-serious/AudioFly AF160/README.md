# AudioFly AF160

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.8; 22 4.7; 23 4.6; 25 4.6; 26 4.5; 28 4.4; 30 4.4; 32 4.3; 35 4.2; 37 4.2; 40 4.2; 42 4.2; 45 4.1; 49 4.0; 52 3.9; 56 3.9; 59 3.9; 64 3.8; 68 3.7; 73 3.6; 78 3.4; 83 3.2; 89 2.8; 95 2.3; 102 1.7; 109 1.2; 117 0.7; 125 0.0; 134 -0.5; 143 -0.8; 153 -1.1; 164 -1.3; 175 -1.3; 188 -1.3; 201 -1.3; 215 -1.3; 230 -1.3; 246 -1.2; 263 -1.2; 282 -1.1; 301 -1.0; 323 -0.9; 345 -0.8; 369 -0.7; 395 -0.6; 423 -0.3; 452 -0.2; 484 -0.3; 518 -0.1; 554 0.2; 593 0.5; 635 0.6; 679 0.6; 726 0.7; 777 0.8; 832 0.7; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.8; 1336 -1.1; 1429 -1.5; 1529 -1.8; 1636 -2.0; 1751 -2.0; 1873 -1.7; 2004 -1.3; 2145 -0.9; 2295 -0.3; 2455 0.7; 2627 1.5; 2811 2.2; 3008 3.3; 3219 3.7; 3444 3.6; 3685 3.2; 3943 3.8; 4219 4.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.29 | 4.6 dB  |
| Peaking | 78 Hz   | 1.12 | 2.1 dB  |
| Peaking | 169 Hz  | 0.93 | -2.5 dB |
| Peaking | 1716 Hz | 2.56 | -2.8 dB |
| Peaking | 4867 Hz | 1.4  | 6.5 dB  |
| Peaking | 737 Hz  | 1.79 | 1.3 dB  |
| Peaking | 3049 Hz | 4.67 | 2.1 dB  |
| Peaking | 1972 Hz | 0.16 | -0.4 dB |
| Peaking | 6396 Hz | 3.69 | 4.3 dB  |
| Peaking | 7168 Hz | 1.69 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF160/AudioFly%20AF160.png)