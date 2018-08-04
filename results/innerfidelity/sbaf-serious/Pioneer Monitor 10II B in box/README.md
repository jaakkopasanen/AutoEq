# Pioneer Monitor 10II B in box

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -8.9; 22 -9.0; 23 -9.0; 25 -9.1; 26 -9.1; 28 -9.1; 30 -9.1; 32 -9.1; 35 -9.1; 37 -9.1; 40 -9.0; 42 -8.9; 45 -8.9; 49 -8.8; 52 -8.8; 56 -8.7; 59 -8.6; 64 -8.5; 68 -8.4; 73 -8.3; 78 -8.2; 83 -8.0; 89 -7.8; 95 -7.5; 102 -6.9; 109 -6.2; 117 -5.2; 125 -5.1; 134 -7.5; 143 -10.6; 153 -11.8; 164 -9.5; 175 -8.0; 188 -11.3; 201 -11.4; 215 -11.6; 230 -11.5; 246 -11.2; 263 -10.6; 282 -10.1; 301 -9.5; 323 -8.8; 345 -8.1; 369 -7.3; 395 -6.4; 423 -5.4; 452 -4.4; 484 -3.6; 518 -2.5; 554 -1.3; 593 -0.0; 635 0.9; 679 1.4; 726 1.7; 777 1.4; 832 0.8; 890 0.1; 952 0.2; 1019 -0.0; 1090 0.5; 1167 1.3; 1248 -0.0; 1336 -2.4; 1429 -5.4; 1529 -8.9; 1636 -11.9; 1751 -14.4; 1873 -13.5; 2004 -9.6; 2145 -4.9; 2295 -1.6; 2455 -0.3; 2627 -1.8; 2811 -2.3; 3008 0.4; 3219 3.0; 3444 2.5; 3685 2.2; 3943 5.6; 4219 6.0; 4514 6.0; 4830 5.1; 5168 4.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.7; 10879 -1.7; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -0.9; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 -1.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10II B in box ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 1.22 | -7.7 dB  |
| Peaking | 40 Hz   | 0.35 | -8.3 dB  |
| Peaking | 237 Hz  | 1.19 | -10.4 dB |
| Peaking | 1787 Hz | 4.15 | -16.4 dB |
| Peaking | 4796 Hz | 1.47 | 6.5 dB   |
| Peaking | 392 Hz  | 2.63 | -2.1 dB  |
| Peaking | 1518 Hz | 5.07 | -3.2 dB  |
| Peaking | 1193 Hz | 4.22 | 3.2 dB   |
| Peaking | 695 Hz  | 2.49 | 3.5 dB   |
| Peaking | 4035 Hz | 6.19 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20Monitor%2010II%20B%20in%20box/Pioneer%20Monitor%2010II%20B%20in%20box.png)