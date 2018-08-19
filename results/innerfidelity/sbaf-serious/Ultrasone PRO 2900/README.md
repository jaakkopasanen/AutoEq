# Ultrasone PRO 2900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.7; 22 3.5; 23 2.9; 25 1.8; 26 1.3; 28 0.4; 30 -0.4; 32 -1.2; 35 -2.0; 37 -2.5; 40 -3.0; 42 -3.3; 45 -3.6; 49 -4.0; 52 -4.2; 56 -4.4; 59 -4.5; 64 -4.3; 68 -4.1; 73 -3.9; 78 -4.0; 83 -4.0; 89 -3.9; 95 -3.8; 102 -3.6; 109 -3.3; 117 -3.1; 125 -2.9; 134 -2.6; 143 -2.5; 153 -2.3; 164 -1.9; 175 -1.4; 188 -1.2; 201 -1.4; 215 -2.0; 230 -2.7; 246 -2.5; 263 -1.9; 282 -1.3; 301 -0.9; 323 -0.5; 345 -0.1; 369 0.2; 395 0.4; 423 0.6; 452 0.7; 484 0.8; 518 1.0; 554 1.5; 593 2.7; 635 2.6; 679 2.0; 726 1.8; 777 1.7; 832 1.3; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -0.9; 1429 -0.9; 1529 -1.3; 1636 -1.7; 1751 -1.5; 1873 -1.7; 2004 -2.1; 2145 4.4; 2295 4.5; 2455 0.4; 2627 -1.3; 2811 -2.3; 3008 -3.0; 3219 -4.0; 3444 -5.6; 3685 -6.2; 3943 -6.0; 4219 -4.6; 4514 0.9; 4830 5.9; 5168 4.3; 5530 -0.8; 5917 -3.6; 6331 -6.1; 6775 -4.9; 7249 0.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -1.3; 14260 -6.3; 15258 -8.9; 16326 -7.8; 17469 -4.7; 18692 -1.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642664dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 2900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.35 | 6.3 dB  |
| Peaking | 60 Hz    | 0.5  | -4.8 dB |
| Peaking | 3627 Hz  | 4.52 | -7.0 dB |
| Peaking | 15696 Hz | 2.48 | -9.8 dB |
| Peaking | 24000 Hz | 2.01 | -3.3 dB |
| Peaking | 644 Hz   | 2.08 | 2.9 dB  |
| Peaking | 2109 Hz  | 1.58 | -3.8 dB |
| Peaking | 2235 Hz  | 7.1  | 10.1 dB |
| Peaking | 4900 Hz  | 8.44 | 8.5 dB  |
| Peaking | 6329 Hz  | 7.09 | -6.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%202900/Ultrasone%20PRO%202900.png)