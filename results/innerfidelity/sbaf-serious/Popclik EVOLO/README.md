# Popclik EVOLO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 10 -84; 20 -10.0; 22 -10.1; 23 -10.1; 25 -10.2; 26 -10.3; 28 -10.3; 30 -10.4; 32 -10.4; 35 -10.5; 37 -10.5; 40 -10.4; 42 -10.3; 45 -10.2; 49 -10.1; 52 -10.0; 56 -9.9; 59 -9.8; 64 -9.6; 68 -9.5; 73 -9.4; 78 -9.3; 83 -9.3; 89 -9.4; 95 -9.6; 102 -9.8; 109 -9.9; 117 -10.1; 125 -10.4; 134 -10.5; 143 -10.4; 153 -10.3; 164 -10.1; 175 -9.7; 188 -9.4; 201 -9.0; 215 -8.5; 230 -8.0; 246 -7.6; 263 -7.1; 282 -6.6; 301 -6.1; 323 -5.6; 345 -5.1; 369 -4.6; 395 -4.1; 423 -3.5; 452 -3.1; 484 -2.7; 518 -2.3; 554 -1.7; 593 -1.1; 635 -0.7; 679 -0.6; 726 -0.3; 777 0.1; 832 0.1; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.6; 1336 -1.1; 1429 -1.6; 1529 -2.4; 1636 -3.2; 1751 -3.8; 1873 -4.0; 2004 -4.2; 2145 -4.5; 2295 -4.7; 2455 -4.5; 2627 -4.3; 2811 -3.7; 3008 -2.0; 3219 -0.3; 3444 1.5; 3685 2.1; 3943 1.7; 4219 0.2; 4514 -1.3; 4830 -2.3; 5168 -3.5; 5530 -5.9; 5917 -8.5; 6331 -7.2; 6775 -3.3; 7249 -0.4; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.7dB` and instead set Global volume in the UI for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclik EVOLO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.22 | -10.0 dB |
| Peaking | 179 Hz  | 0.74 | -6.7 dB  |
| Peaking | 2308 Hz | 1.7  | -5.2 dB  |
| Peaking | 3642 Hz | 4.12 | 4.2 dB   |
| Peaking | 5934 Hz | 4.86 | -9.1 dB  |
| Peaking | 202 Hz  | 2.43 | 0.9 dB   |
| Peaking | 395 Hz  | 0.69 | -1.1 dB  |
| Peaking | 807 Hz  | 1.08 | 1.9 dB   |
| Peaking | 1652 Hz | 4.7  | -1.5 dB  |
| Peaking | 7730 Hz | 7.47 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclik%20EVOLO/Popclik%20EVOLO.png)