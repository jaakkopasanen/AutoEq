# Soul Jet Pro ANC On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 -1.1; 22 -2.9; 23 -3.7; 25 -5.2; 26 -5.9; 28 -7.0; 30 -7.9; 32 -8.3; 35 -8.3; 37 -8.0; 40 -7.5; 42 -7.2; 45 -6.9; 49 -6.7; 52 -6.5; 56 -6.3; 59 -6.3; 64 -6.2; 68 -6.1; 73 -6.1; 78 -6.1; 83 -6.2; 89 -6.3; 95 -6.5; 102 -6.6; 109 -6.6; 117 -6.8; 125 -7.2; 134 -7.6; 143 -8.0; 153 -8.2; 164 -8.4; 175 -8.4; 188 -8.7; 201 -8.9; 215 -9.0; 230 -9.1; 246 -9.3; 263 -9.3; 282 -9.4; 301 -9.6; 323 -9.8; 345 -9.8; 369 -9.7; 395 -9.6; 423 -9.1; 452 -7.8; 484 -5.2; 518 -1.5; 554 2.0; 593 3.3; 635 4.7; 679 4.6; 726 4.0; 777 3.9; 832 3.3; 890 1.9; 952 0.8; 1019 -0.2; 1090 -1.1; 1167 -2.1; 1248 -3.1; 1336 -4.1; 1429 -5.9; 1529 -8.2; 1636 -10.1; 1751 -11.8; 1873 -13.6; 2004 -15.2; 2145 -15.8; 2295 -14.8; 2455 -12.7; 2627 -10.5; 2811 -8.4; 3008 -5.8; 3219 -4.4; 3444 -3.8; 3685 -5.3; 3943 -7.2; 4219 -11.0; 4514 -10.0; 4830 -7.6; 5168 -4.6; 5530 -1.8; 5917 1.4; 6331 3.2; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.9744735983631dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 66 Hz   | 0.15 | -6.2 dB  |
| Peaking | 418 Hz  | 0.84 | -13.6 dB |
| Peaking | 632 Hz  | 1.16 | 16.6 dB  |
| Peaking | 2065 Hz | 1.78 | -17.1 dB |
| Peaking | 4378 Hz | 5.92 | -9.6 dB  |
| Peaking | 34 Hz   | 4.01 | -2.7 dB  |
| Peaking | 2601 Hz | 4.31 | -1.6 dB  |
| Peaking | 3266 Hz | 5.95 | 2.0 dB   |
| Peaking | 5031 Hz | 5.23 | -2.6 dB  |
| Peaking | 6501 Hz | 4.18 | 5.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20On/Soul%20Jet%20Pro%20ANC%20On.png)