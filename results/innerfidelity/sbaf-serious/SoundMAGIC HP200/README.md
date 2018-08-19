# SoundMAGIC HP200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 10 -84; 20 -3.0; 22 -3.0; 23 -3.0; 25 -3.0; 26 -2.9; 28 -2.8; 30 -2.7; 32 -2.5; 35 -2.2; 37 -2.0; 40 -1.6; 42 -1.3; 45 -0.9; 49 -0.3; 52 0.2; 56 1.1; 59 1.7; 64 1.5; 68 0.0; 73 -2.2; 78 -3.4; 83 -3.4; 89 -3.3; 95 -4.2; 102 -5.3; 109 -5.7; 117 -5.8; 125 -6.1; 134 -6.1; 143 -6.1; 153 -5.6; 164 -4.5; 175 -5.6; 188 -5.5; 201 -5.2; 215 -4.9; 230 -4.3; 246 -4.0; 263 -3.6; 282 -3.0; 301 -2.5; 323 -2.0; 345 -1.4; 369 -0.8; 395 -0.3; 423 0.4; 452 0.8; 484 1.1; 518 1.3; 554 1.7; 593 2.1; 635 2.0; 679 1.8; 726 1.7; 777 1.7; 832 1.5; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.1; 1336 -1.7; 1429 -2.6; 1529 -3.6; 1636 -4.6; 1751 -5.6; 1873 -6.6; 2004 -7.6; 2145 -8.7; 2295 -9.5; 2455 -9.3; 2627 -8.8; 2811 -8.2; 3008 -7.0; 3219 -6.7; 3444 -6.5; 3685 -6.6; 3943 -6.5; 4219 -6.5; 4514 -5.8; 4830 -3.8; 5168 -1.6; 5530 -2.6; 5917 0.2; 6331 2.0; 6775 0.6; 7249 -1.8; 7756 -5.9; 8299 -10.9; 8880 -14.4; 9502 -14.9; 10167 -12.2; 10879 -7.2; 11640 -2.1; 12455 -0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.0; 20000 -7.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.2147357611948704dB` and instead set Global volume in the UI for both channels to **-22**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC HP200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 121 Hz  | 1.6  | -5.9 dB  |
| Peaking | 209 Hz  | 2.12 | -4.1 dB  |
| Peaking | 2335 Hz | 1.92 | -9.6 dB  |
| Peaking | 3892 Hz | 3.02 | -4.9 dB  |
| Peaking | 9344 Hz | 3.86 | -16.7 dB |
| Peaking | 15 Hz   | 0.3  | -3.1 dB  |
| Peaking | 60 Hz   | 3.74 | 4.2 dB   |
| Peaking | 653 Hz  | 1.82 | 2.8 dB   |
| Peaking | 6493 Hz | 5.43 | 5.1 dB   |
| Peaking | 8338 Hz | 7.58 | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20HP200/SoundMAGIC%20HP200.png)