# PureSound Clarity One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.1dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.4; 23 -4.6; 25 -5.0; 26 -5.2; 28 -5.7; 30 -6.0; 32 -6.4; 35 -6.7; 37 -7.0; 40 -7.3; 42 -7.5; 45 -7.8; 49 -8.1; 52 -8.3; 56 -8.6; 59 -8.9; 64 -9.1; 68 -9.4; 73 -9.7; 78 -9.8; 83 -10.1; 89 -10.3; 95 -10.5; 102 -10.6; 109 -10.6; 117 -10.6; 125 -10.7; 134 -10.7; 143 -10.6; 153 -10.5; 164 -10.4; 175 -10.2; 188 -9.9; 201 -9.7; 215 -9.4; 230 -9.0; 246 -8.7; 263 -8.3; 282 -7.9; 301 -7.4; 323 -7.0; 345 -6.5; 369 -6.0; 395 -5.6; 423 -4.9; 452 -4.4; 484 -4.1; 518 -3.6; 554 -2.9; 593 -2.3; 635 -1.7; 679 -1.5; 726 -1.0; 777 -0.6; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 -0.0; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -2.0; 1636 -2.5; 1751 -2.6; 1873 -2.6; 2004 -2.3; 2145 -2.1; 2295 -1.8; 2455 -1.5; 2627 -1.6; 2811 -2.0; 3008 -2.3; 3219 -2.8; 3444 -3.1; 3685 -3.3; 3943 -3.4; 4219 -4.4; 4514 -5.3; 4830 -5.6; 5168 -5.9; 5530 -7.4; 5917 -11.0; 6331 -13.7; 6775 -10.4; 7249 -7.1; 7756 -4.5; 8299 -3.2; 8880 -3.4; 9502 -4.2; 10167 -4.3; 10879 -2.6; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.2; 16326 -3.4; 17469 -3.1; 18692 -1.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.1181271787434306dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PureSound Clarity One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 53 Hz    | 0.39 | -6.4 dB  |
| Peaking | 144 Hz   | 0.63 | -6.4 dB  |
| Peaking | 302 Hz   | 1.01 | -3.3 dB  |
| Peaking | 6214 Hz  | 1.81 | -11.7 dB |
| Peaking | 16952 Hz | 3.47 | -3.8 dB  |
| Peaking | 1865 Hz  | 2.85 | -2.1 dB  |
| Peaking | 8084 Hz  | 5.31 | 2.4 dB   |
| Peaking | 10194 Hz | 3.22 | -3.5 dB  |
| Peaking | 11874 Hz | 2.35 | 2.4 dB   |
| Peaking | 21944 Hz | 1.34 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PureSound%20Clarity%20One/PureSound%20Clarity%20One.png)