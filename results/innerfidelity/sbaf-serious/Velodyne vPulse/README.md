# Velodyne vPulse

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -13.1; 22 -12.7; 23 -12.5; 25 -12.1; 26 -11.9; 28 -11.5; 30 -11.2; 32 -10.8; 35 -10.2; 37 -9.9; 40 -9.5; 42 -9.2; 45 -8.7; 49 -8.1; 52 -7.7; 56 -7.3; 59 -7.0; 64 -6.5; 68 -6.1; 73 -5.8; 78 -5.5; 83 -5.3; 89 -5.2; 95 -5.3; 102 -5.3; 109 -5.3; 117 -5.5; 125 -5.7; 134 -5.7; 143 -5.6; 153 -5.5; 164 -5.3; 175 -4.9; 188 -4.6; 201 -4.3; 215 -3.9; 230 -3.5; 246 -3.2; 263 -2.9; 282 -2.5; 301 -2.2; 323 -1.9; 345 -1.5; 369 -1.2; 395 -1.0; 423 -0.6; 452 -0.4; 484 -0.2; 518 -0.0; 554 0.4; 593 0.8; 635 1.0; 679 0.7; 726 0.7; 777 0.8; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.1; 1873 -3.2; 2004 -3.2; 2145 -3.3; 2295 -3.3; 2455 -3.0; 2627 -3.0; 2811 -3.2; 3008 -2.9; 3219 -2.7; 3444 -2.3; 3685 -2.4; 3943 -2.6; 4219 -2.7; 4514 -2.3; 4830 -0.6; 5168 1.5; 5530 3.9; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Velodyne vPulse ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 12 Hz   | 0.61 | -12.5 dB |
| Peaking | 33 Hz   | 0.47 | -6.4 dB  |
| Peaking | 157 Hz  | 1.08 | -4.2 dB  |
| Peaking | 2902 Hz | 0.79 | -3.6 dB  |
| Peaking | 6070 Hz | 3.7  | 7.7 dB   |
| Peaking | 299 Hz  | 1.88 | -0.7 dB  |
| Peaking | 723 Hz  | 1.1  | 1.6 dB   |
| Peaking | 1715 Hz | 2.25 | -1.5 dB  |
| Peaking | 3730 Hz | 1.42 | 1.0 dB   |
| Peaking | 4313 Hz | 4.85 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Velodyne%20vPulse/Velodyne%20vPulse.png)