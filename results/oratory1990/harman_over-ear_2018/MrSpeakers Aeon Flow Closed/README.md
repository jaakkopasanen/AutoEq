# MrSpeakers Aeon Flow Closed

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.4; 22 1.5; 23 1.5; 25 1.6; 26 1.7; 28 1.9; 30 2.1; 32 2.3; 35 2.5; 37 2.6; 40 2.8; 42 3.0; 45 3.2; 49 3.5; 52 3.8; 56 4.0; 59 4.1; 64 4.2; 68 4.0; 73 3.5; 78 3.3; 83 3.4; 89 3.6; 95 3.7; 102 3.7; 109 4.0; 117 4.3; 125 4.5; 134 4.6; 143 4.7; 153 4.9; 164 5.1; 175 5.0; 188 4.7; 201 4.5; 215 4.2; 230 4.0; 246 3.9; 263 3.9; 282 3.8; 301 3.7; 323 3.4; 345 3.1; 369 2.8; 395 2.4; 423 2.0; 452 2.0; 484 1.9; 518 1.7; 554 1.7; 593 1.8; 635 1.8; 679 1.4; 726 1.0; 777 0.8; 832 0.4; 890 -0.1; 952 -0.3; 1019 0.4; 1090 1.2; 1167 0.8; 1248 1.1; 1336 1.8; 1429 2.2; 1529 2.5; 1636 3.2; 1751 3.2; 1873 3.6; 2004 4.5; 2145 4.7; 2295 4.8; 2455 4.5; 2627 3.5; 2811 5.2; 3008 6.0; 3219 6.0; 3444 5.5; 3685 5.9; 3943 5.2; 4219 3.3; 4514 2.5; 4830 2.2; 5168 -0.1; 5530 -3.0; 5917 -1.2; 6331 1.4; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.8; 12455 -0.4; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.5; 17469 -2.2; 18692 -3.1; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678132dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Aeon Flow Closed ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.82 | 2.8 dB  |
| Peaking | 184 Hz   | 0.58 | 4.5 dB  |
| Peaking | 2085 Hz  | 1.81 | 3.8 dB  |
| Peaking | 3426 Hz  | 2.44 | 5.6 dB  |
| Peaking | 24000 Hz | 2.22 | 0.5 dB  |
| Peaking | 928 Hz   | 5.27 | -1.5 dB |
| Peaking | 1485 Hz  | 0.25 | 0.2 dB  |
| Peaking | 5612 Hz  | 8.25 | -4.6 dB |
| Peaking | 6720 Hz  | 9.63 | 4.0 dB  |
| Peaking | 19347 Hz | 1.46 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/MrSpeakers%20Aeon%20Flow%20Closed/MrSpeakers%20Aeon%20Flow%20Closed.png)