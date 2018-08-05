# AudioFly AF140

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.4; 23 -3.5; 25 -3.7; 26 -3.8; 28 -3.9; 30 -4.1; 32 -4.2; 35 -4.3; 37 -4.4; 40 -4.5; 42 -4.5; 45 -4.6; 49 -4.6; 52 -4.7; 56 -4.8; 59 -4.8; 64 -4.8; 68 -4.8; 73 -5.0; 78 -5.1; 83 -5.2; 89 -5.6; 95 -6.0; 102 -6.5; 109 -6.9; 117 -7.3; 125 -7.8; 134 -8.2; 143 -8.4; 153 -8.5; 164 -8.5; 175 -8.3; 188 -8.1; 201 -8.0; 215 -7.7; 230 -7.4; 246 -7.1; 263 -6.8; 282 -6.4; 301 -6.0; 323 -5.5; 345 -5.1; 369 -4.7; 395 -4.2; 423 -3.5; 452 -3.1; 484 -3.0; 518 -2.4; 554 -1.8; 593 -1.0; 635 -0.4; 679 -0.1; 726 1.1; 777 1.5; 832 1.4; 890 1.1; 952 0.8; 1019 0.0; 1090 -0.5; 1167 -1.1; 1248 -1.7; 1336 -2.5; 1429 -3.3; 1529 -4.0; 1636 -4.6; 1751 -5.1; 1873 -5.4; 2004 -5.3; 2145 -5.1; 2295 -5.0; 2455 -4.0; 2627 -2.6; 2811 -1.0; 3008 1.3; 3219 3.2; 3444 4.6; 3685 4.9; 3943 5.9; 4219 6.0; 4514 6.0; 4830 4.4; 5168 0.6; 5530 -1.1; 5917 2.3; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -2.5; 10879 -2.8; 11640 -1.0; 12455 -0.0; 13327 -0.8; 14260 -3.1; 15258 -4.0; 16326 -1.8; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AudioFly AF140 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.24 | -3.8 dB |
| Peaking | 189 Hz   | 0.78 | -6.8 dB |
| Peaking | 2095 Hz  | 1.73 | -6.9 dB |
| Peaking | 3704 Hz  | 1.87 | 6.1 dB  |
| Peaking | 4447 Hz  | 5.28 | 2.9 dB  |
| Peaking | 809 Hz   | 1.56 | 5.9 dB  |
| Peaking | 801 Hz   | 0.72 | -3.1 dB |
| Peaking | 6517 Hz  | 9.56 | 5.1 dB  |
| Peaking | 10601 Hz | 6.19 | -3.3 dB |
| Peaking | 15067 Hz | 3.86 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AudioFly%20AF140/AudioFly%20AF140.png)