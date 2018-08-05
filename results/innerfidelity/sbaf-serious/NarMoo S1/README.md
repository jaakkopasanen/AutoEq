# NarMoo S1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.5; 23 -11.5; 25 -11.5; 26 -11.6; 28 -11.6; 30 -11.6; 32 -11.5; 35 -11.5; 37 -11.4; 40 -11.4; 42 -11.3; 45 -11.3; 49 -11.1; 52 -11.0; 56 -10.9; 59 -10.9; 64 -10.7; 68 -10.6; 73 -10.6; 78 -10.6; 83 -10.6; 89 -10.7; 95 -11.0; 102 -11.3; 109 -11.5; 117 -11.7; 125 -12.0; 134 -12.1; 143 -12.2; 153 -12.1; 164 -11.9; 175 -11.5; 188 -11.3; 201 -10.9; 215 -10.4; 230 -10.0; 246 -9.5; 263 -9.1; 282 -8.5; 301 -8.1; 323 -7.5; 345 -6.9; 369 -6.4; 395 -5.8; 423 -5.1; 452 -4.5; 484 -4.0; 518 -3.4; 554 -2.7; 593 -1.9; 635 -1.4; 679 -1.1; 726 -0.7; 777 -0.3; 832 -0.1; 890 -0.0; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.1; 1248 -0.4; 1336 -0.9; 1429 -1.7; 1529 -2.4; 1636 -2.9; 1751 -3.3; 1873 -3.7; 2004 -3.8; 2145 -4.2; 2295 -4.9; 2455 -5.6; 2627 -6.8; 2811 -8.6; 3008 -9.3; 3219 -6.6; 3444 -3.3; 3685 -2.8; 3943 -4.0; 4219 -6.1; 4514 -9.4; 4830 -10.7; 5168 -7.3; 5530 -2.8; 5917 0.6; 6331 2.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 -1.0; 8880 -3.9; 9502 -5.9; 10167 -6.2; 10879 -3.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.2; 18692 -3.0; 20000 -2.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 0.13 | -11.2 dB |
| Peaking | 194 Hz   | 0.69 | -7.5 dB  |
| Peaking | 2786 Hz  | 2.22 | -8.1 dB  |
| Peaking | 4768 Hz  | 6.2  | -10.5 dB |
| Peaking | 19344 Hz | 1.42 | -3.1 dB  |
| Peaking | 907 Hz   | 2.04 | 1.6 dB   |
| Peaking | 1725 Hz  | 3.76 | -1.9 dB  |
| Peaking | 5289 Hz  | 3.77 | -3.2 dB  |
| Peaking | 6386 Hz  | 2.64 | 5.6 dB   |
| Peaking | 9727 Hz  | 4.07 | -7.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20S1/NarMoo%20S1.png)