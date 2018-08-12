# Beyerdynamic DT 880 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.6; 32 5.4; 35 5.0; 37 4.8; 40 4.4; 42 4.2; 45 4.0; 49 3.6; 52 3.3; 56 2.9; 59 2.7; 64 2.7; 68 2.9; 73 2.6; 78 1.9; 83 1.3; 89 0.9; 95 0.5; 102 0.1; 109 -0.1; 117 -0.3; 125 -0.6; 134 -0.9; 143 -1.1; 153 -1.3; 164 -1.2; 175 -1.4; 188 -1.5; 201 -1.7; 215 -1.7; 230 -1.7; 246 -1.7; 263 -1.7; 282 -1.6; 301 -1.5; 323 -1.6; 345 -1.5; 369 -1.5; 395 -1.4; 423 -1.1; 452 -0.7; 484 -0.7; 518 -0.8; 554 -0.7; 593 -0.5; 635 -0.4; 679 -0.4; 726 -0.3; 777 -0.1; 832 -0.3; 890 -0.5; 952 -0.2; 1019 0.0; 1090 0.3; 1167 0.3; 1248 0.7; 1336 0.7; 1429 0.5; 1529 0.2; 1636 0.0; 1751 -0.4; 1873 -0.3; 2004 -0.0; 2145 0.4; 2295 1.0; 2455 1.6; 2627 2.0; 2811 2.0; 3008 1.7; 3219 1.0; 3444 0.3; 3685 -0.4; 3943 -0.2; 4219 -0.4; 4514 -0.2; 4830 -0.1; 5168 -1.0; 5530 -2.1; 5917 -2.5; 6331 -2.2; 6775 -2.0; 7249 -3.7; 7756 -5.6; 8299 -7.3; 8880 -7.5; 9502 -5.8; 10167 -2.8; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -0.9; 15258 -0.7; 16326 -0.5; 17469 -1.5; 18692 -3.4; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.57 | 6.1 dB  |
| Peaking | 71 Hz    | 3.25 | 1.2 dB  |
| Peaking | 210 Hz   | 0.62 | -2.0 dB |
| Peaking | 2719 Hz  | 3.57 | 2.4 dB  |
| Peaking | 8510 Hz  | 2.76 | -8.0 dB |
| Peaking | 1299 Hz  | 3.77 | 0.9 dB  |
| Peaking | 1822 Hz  | 6.25 | -0.7 dB |
| Peaking | 5746 Hz  | 7.75 | -1.6 dB |
| Peaking | 11237 Hz | 6.23 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT%20880%20250%20Ohm.png)