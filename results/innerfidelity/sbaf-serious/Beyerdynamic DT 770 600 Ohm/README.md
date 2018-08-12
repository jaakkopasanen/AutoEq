# Beyerdynamic DT 770 600 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.6; 23 -1.8; 25 -2.3; 26 -2.5; 28 -2.9; 30 -3.2; 32 -3.5; 35 -3.9; 37 -4.0; 40 -4.2; 42 -4.3; 45 -4.5; 49 -4.5; 52 -4.4; 56 -4.1; 59 -3.7; 64 -2.4; 68 -1.1; 73 0.8; 78 1.0; 83 -0.6; 89 -3.1; 95 -4.9; 102 -5.8; 109 -5.9; 117 -5.8; 125 -5.5; 134 -5.0; 143 -4.3; 153 -3.0; 164 -2.1; 175 -2.0; 188 -1.1; 201 -0.6; 215 -0.4; 230 -0.4; 246 -0.9; 263 -1.2; 282 -1.5; 301 -1.7; 323 -1.9; 345 -1.9; 369 -2.0; 395 -2.0; 423 -1.8; 452 -1.7; 484 -1.7; 518 -1.6; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.6; 726 -0.4; 777 -0.2; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.2; 1248 -0.0; 1336 -0.4; 1429 -0.8; 1529 -1.1; 1636 -1.5; 1751 -1.9; 1873 -1.8; 2004 -1.3; 2145 -1.4; 2295 -2.0; 2455 -1.9; 2627 -1.3; 2811 -0.4; 3008 0.8; 3219 1.9; 3444 3.3; 3685 4.5; 3943 4.5; 4219 3.9; 4514 5.6; 4830 4.7; 5168 -3.1; 5530 -7.2; 5917 -7.1; 6331 -7.6; 6775 -6.5; 7249 -5.8; 7756 -7.5; 8299 -9.6; 8880 -10.2; 9502 -7.9; 10167 -3.8; 10879 -1.0; 11640 -1.6; 12455 -4.2; 13327 -5.7; 14260 -4.7; 15258 -3.0; 16326 -3.7; 17469 -6.6; 18692 -8.3; 20000 -6.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 116 Hz   | 1.36 | -5.6 dB  |
| Peaking | 4608 Hz  | 1.68 | 23.2 dB  |
| Peaking | 5437 Hz  | 1.05 | -20.8 dB |
| Peaking | 8734 Hz  | 5.89 | -6.6 dB  |
| Peaking | 43 Hz    | 1.1  | -4.4 dB  |
| Peaking | 77 Hz    | 4.75 | 5.6 dB   |
| Peaking | 412 Hz   | 2.23 | -1.8 dB  |
| Peaking | 15965 Hz | 4.88 | 1.6 dB   |
| Peaking | 18762 Hz | 1.12 | -8.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)