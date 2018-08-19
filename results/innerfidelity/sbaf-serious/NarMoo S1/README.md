# NarMoo S1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -11.5; 22 -11.6; 23 -11.6; 25 -11.7; 26 -11.7; 28 -11.7; 30 -11.7; 32 -11.8; 35 -11.8; 37 -11.8; 40 -11.8; 42 -11.8; 45 -11.8; 49 -11.8; 52 -11.9; 56 -11.9; 59 -12.0; 64 -12.0; 68 -12.1; 73 -12.1; 78 -12.2; 83 -12.2; 89 -12.3; 95 -12.4; 102 -12.3; 109 -12.2; 117 -12.1; 125 -12.0; 134 -11.8; 143 -11.8; 153 -11.6; 164 -11.4; 175 -11.0; 188 -10.8; 201 -10.5; 215 -10.1; 230 -9.7; 246 -9.3; 263 -8.9; 282 -8.4; 301 -7.9; 323 -7.4; 345 -6.8; 369 -6.3; 395 -5.8; 423 -5.0; 452 -4.4; 484 -4.0; 518 -3.4; 554 -2.7; 593 -1.9; 635 -1.4; 679 -1.1; 726 -0.7; 777 -0.2; 832 -0.1; 890 -0.0; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.1; 1248 -0.4; 1336 -0.9; 1429 -1.7; 1529 -2.4; 1636 -2.9; 1751 -3.3; 1873 -3.7; 2004 -3.8; 2145 -4.2; 2295 -4.9; 2455 -5.6; 2627 -6.8; 2811 -8.6; 3008 -9.3; 3219 -6.6; 3444 -3.3; 3685 -2.8; 3943 -4.0; 4219 -6.1; 4514 -9.4; 4830 -10.7; 5168 -7.3; 5530 -2.8; 5917 0.6; 6331 2.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 -1.0; 8880 -3.9; 9502 -5.9; 10167 -6.2; 10879 -3.5; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.2; 18692 -3.0; 20000 -2.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6031166255069773dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.19 | -11.6 dB |
| Peaking | 194 Hz   | 0.65 | -5.4 dB  |
| Peaking | 2791 Hz  | 2.24 | -8.2 dB  |
| Peaking | 4728 Hz  | 6.3  | -10.6 dB |
| Peaking | 19434 Hz | 1.29 | -3.0 dB  |
| Peaking | 899 Hz   | 1.91 | 1.7 dB   |
| Peaking | 1728 Hz  | 3.66 | -1.9 dB  |
| Peaking | 5266 Hz  | 5.94 | -3.5 dB  |
| Peaking | 6503 Hz  | 2.68 | 5.0 dB   |
| Peaking | 9750 Hz  | 4.08 | -7.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20S1/NarMoo%20S1.png)