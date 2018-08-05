# PureSound Clarity One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -3.9; 22 -4.3; 23 -4.5; 25 -4.9; 26 -5.1; 28 -5.5; 30 -5.9; 32 -6.1; 35 -6.4; 37 -6.6; 40 -6.9; 42 -7.1; 45 -7.2; 49 -7.4; 52 -7.5; 56 -7.7; 59 -7.8; 64 -7.9; 68 -8.0; 73 -8.1; 78 -8.2; 83 -8.4; 89 -8.7; 95 -9.1; 102 -9.5; 109 -9.9; 117 -10.2; 125 -10.7; 134 -10.9; 143 -11.0; 153 -11.0; 164 -10.9; 175 -10.7; 188 -10.4; 201 -10.2; 215 -9.8; 230 -9.3; 246 -9.0; 263 -8.6; 282 -8.0; 301 -7.6; 323 -7.1; 345 -6.6; 369 -6.1; 395 -5.6; 423 -4.9; 452 -4.5; 484 -4.1; 518 -3.6; 554 -2.9; 593 -2.3; 635 -1.7; 679 -1.5; 726 -1.0; 777 -0.6; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -2.0; 1636 -2.5; 1751 -2.6; 1873 -2.6; 2004 -2.3; 2145 -2.2; 2295 -1.8; 2455 -1.5; 2627 -1.6; 2811 -2.0; 3008 -2.3; 3219 -2.8; 3444 -3.1; 3685 -3.3; 3943 -3.4; 4219 -4.4; 4514 -5.3; 4830 -5.6; 5168 -5.9; 5530 -7.4; 5917 -11.0; 6331 -13.7; 6775 -10.4; 7249 -7.1; 7756 -4.5; 8299 -3.2; 8880 -3.4; 9502 -4.2; 10167 -4.3; 10879 -2.6; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.2; 16326 -3.4; 17469 -3.1; 18692 -1.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PureSound Clarity One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 3 Hz     | 1.97 | -2.9 dB  |
| Peaking | 48 Hz    | 0.32 | -5.6 dB  |
| Peaking | 187 Hz   | 0.6  | -8.3 dB  |
| Peaking | 6219 Hz  | 1.83 | -11.8 dB |
| Peaking | 31188 Hz | 3.43 | -3.8 dB  |
| Peaking | 993 Hz   | 1.09 | 5.6 dB   |
| Peaking | 1164 Hz  | 0.65 | -4.4 dB  |
| Peaking | 8042 Hz  | 5.09 | 2.3 dB   |
| Peaking | 10186 Hz | 3.7  | -3.8 dB  |
| Peaking | 11720 Hz | 1.87 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PureSound%20Clarity%20One/PureSound%20Clarity%20One.png)