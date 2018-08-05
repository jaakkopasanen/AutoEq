# Santa Cruz Audio SC1000 Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.7; 83 5.5; 89 5.1; 95 4.6; 102 4.0; 109 3.6; 117 3.1; 125 2.5; 134 2.0; 143 1.6; 153 1.3; 164 1.2; 175 1.2; 188 1.2; 201 1.1; 215 1.1; 230 1.2; 246 1.3; 263 1.2; 282 1.3; 301 1.3; 323 1.3; 345 1.4; 369 1.4; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.6; 554 1.7; 593 1.9; 635 1.8; 679 1.6; 726 1.5; 777 1.4; 832 1.1; 890 0.6; 952 0.3; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.6; 1336 -1.2; 1429 -1.9; 1529 -2.6; 1636 -3.2; 1751 -3.7; 1873 -4.1; 2004 -4.4; 2145 -4.9; 2295 -5.5; 2455 -6.0; 2627 -6.7; 2811 -7.3; 3008 -7.1; 3219 -6.7; 3444 -5.9; 3685 -6.0; 3943 -7.3; 4219 -10.2; 4514 -13.3; 4830 -15.3; 5168 -14.0; 5530 -11.0; 5917 -8.3; 6331 -7.3; 6775 -7.9; 7249 -10.1; 7756 -12.5; 8299 -14.0; 8880 -13.8; 9502 -12.0; 10167 -9.2; 10879 -5.3; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.43 | 6.7 dB   |
| Peaking | 629 Hz   | 1.02 | 2.0 dB   |
| Peaking | 2528 Hz  | 1.12 | -5.6 dB  |
| Peaking | 4876 Hz  | 3.13 | -12.8 dB |
| Peaking | 8605 Hz  | 2.52 | -14.2 dB |
| Peaking | 16 Hz    | 1.09 | 1.9 dB   |
| Peaking | 39 Hz    | 1.05 | -1.2 dB  |
| Peaking | 81 Hz    | 1.57 | 1.3 dB   |
| Peaking | 149 Hz   | 2.36 | -1.1 dB  |
| Peaking | 12472 Hz | 4.65 | 3.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Passive/Santa%20Cruz%20Audio%20SC1000%20Passive.png)