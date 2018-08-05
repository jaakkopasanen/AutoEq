# Phiaton PS 210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.9; 25 5.6; 26 5.4; 28 5.0; 30 4.7; 32 4.4; 35 4.0; 37 3.8; 40 3.5; 42 3.3; 45 3.1; 49 2.8; 52 2.6; 56 2.4; 59 2.3; 64 2.1; 68 1.8; 73 1.6; 78 1.3; 83 1.0; 89 0.5; 95 -0.0; 102 -0.6; 109 -1.1; 117 -1.7; 125 -2.4; 134 -3.0; 143 -3.3; 153 -3.6; 164 -3.8; 175 -3.8; 188 -3.8; 201 -3.9; 215 -3.9; 230 -3.9; 246 -3.8; 263 -3.8; 282 -3.8; 301 -3.7; 323 -3.7; 345 -3.5; 369 -3.3; 395 -3.4; 423 -4.1; 452 -3.9; 484 -3.4; 518 -3.3; 554 -3.2; 593 -3.1; 635 -3.0; 679 -2.9; 726 -2.4; 777 -1.8; 832 -1.3; 890 -0.8; 952 -0.4; 1019 0.1; 1090 0.5; 1167 0.7; 1248 0.8; 1336 0.5; 1429 -0.1; 1529 -0.9; 1636 -1.8; 1751 -2.7; 1873 -3.6; 2004 -4.5; 2145 -5.2; 2295 -5.2; 2455 -3.5; 2627 -1.2; 2811 1.2; 3008 3.8; 3219 5.4; 3444 6.0; 3685 5.6; 3943 3.8; 4219 0.9; 4514 -1.0; 4830 0.5; 5168 0.9; 5530 1.9; 5917 5.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 0.16 | 6.0 dB   |
| Peaking | 304 Hz  | 0.26 | -5.4 dB  |
| Peaking | 2176 Hz | 1.75 | -10.1 dB |
| Peaking | 3307 Hz | 4.11 | 5.8 dB   |
| Peaking | 1911 Hz | 0.42 | 5.6 dB   |
| Peaking | 147 Hz  | 4.85 | -0.8 dB  |
| Peaking | 1181 Hz | 6.11 | 0.8 dB   |
| Peaking | 4565 Hz | 7.58 | -3.7 dB  |
| Peaking | 6314 Hz | 5.17 | 5.4 dB   |
| Peaking | 8036 Hz | 1.58 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20210/Phiaton%20PS%20210.png)