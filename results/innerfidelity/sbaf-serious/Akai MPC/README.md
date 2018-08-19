# Akai MPC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.7; 22 3.5; 23 3.4; 25 3.3; 26 3.2; 28 3.2; 30 3.1; 32 3.1; 35 3.0; 37 3.0; 40 3.0; 42 2.9; 45 2.9; 49 2.9; 52 2.9; 56 2.8; 59 2.7; 64 2.4; 68 2.3; 73 2.1; 78 2.1; 83 2.1; 89 2.0; 95 1.5; 102 0.4; 109 0.2; 117 0.4; 125 0.4; 134 0.1; 143 -0.3; 153 -0.7; 164 0.0; 175 0.4; 188 -0.2; 201 0.1; 215 0.2; 230 0.3; 246 0.8; 263 1.1; 282 1.4; 301 1.5; 323 1.6; 345 1.4; 369 1.6; 395 1.6; 423 1.5; 452 1.5; 484 1.2; 518 1.3; 554 1.3; 593 1.5; 635 1.5; 679 1.3; 726 1.0; 777 1.1; 832 0.7; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.9; 1429 -1.3; 1529 -0.6; 1636 -0.8; 1751 -1.2; 1873 1.0; 2004 1.9; 2145 2.1; 2295 1.4; 2455 1.5; 2627 2.2; 2811 3.6; 3008 3.5; 3219 1.9; 3444 0.6; 3685 1.2; 3943 2.4; 4219 3.0; 4514 4.1; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099245613600242dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akai MPC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.79 | 3.3 dB  |
| Peaking | 59 Hz   | 1.48 | 2.0 dB  |
| Peaking | 426 Hz  | 1.22 | 1.7 dB  |
| Peaking | 2828 Hz | 4.4  | 3.0 dB  |
| Peaking | 5455 Hz | 2.39 | 6.8 dB  |
| Peaking | 697 Hz  | 3.36 | 0.8 dB  |
| Peaking | 1703 Hz | 1.78 | -2.2 dB |
| Peaking | 2041 Hz | 4.24 | 3.2 dB  |
| Peaking | 6563 Hz | 6.83 | 2.5 dB  |
| Peaking | 7755 Hz | 2.26 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Akai%20MPC/Akai%20MPC.png)