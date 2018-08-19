# Radius HP-TWF41

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.3; 22 3.8; 23 3.5; 25 3.1; 26 2.9; 28 2.5; 30 2.2; 32 2.0; 35 1.6; 37 1.4; 40 1.1; 42 0.9; 45 0.6; 49 0.3; 52 0.1; 56 -0.2; 59 -0.5; 64 -0.8; 68 -1.1; 73 -1.5; 78 -1.8; 83 -2.1; 89 -2.4; 95 -2.9; 102 -3.2; 109 -3.3; 117 -3.5; 125 -3.8; 134 -4.0; 143 -4.2; 153 -4.4; 164 -4.5; 175 -4.6; 188 -4.8; 201 -4.8; 215 -4.8; 230 -4.8; 246 -4.8; 263 -4.8; 282 -4.7; 301 -4.6; 323 -4.5; 345 -4.4; 369 -4.3; 395 -4.2; 423 -3.9; 452 -3.7; 484 -3.5; 518 -3.3; 554 -2.9; 593 -2.4; 635 -2.0; 679 -1.8; 726 -1.0; 777 -0.6; 832 -0.3; 890 -0.2; 952 -0.0; 1019 0.0; 1090 0.2; 1167 0.3; 1248 0.3; 1336 0.3; 1429 0.2; 1529 0.1; 1636 0.1; 1751 0.3; 1873 0.6; 2004 1.0; 2145 1.3; 2295 1.5; 2455 2.1; 2627 2.4; 2811 2.8; 3008 4.0; 3219 4.9; 3444 5.5; 3685 5.2; 3943 4.5; 4219 3.3; 4514 3.0; 4830 4.2; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -2.0; 10167 -1.5; 10879 -1.0; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.4; 16326 -3.2; 17469 -1.2; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096989832632929dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-TWF41 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.63 | 4.6 dB  |
| Peaking | 217 Hz   | 0.48 | -5.2 dB |
| Peaking | 3363 Hz  | 1.81 | 4.8 dB  |
| Peaking | 5969 Hz  | 2.18 | 7.2 dB  |
| Peaking | 8486 Hz  | 1.03 | -2.8 dB |
| Peaking | 526 Hz   | 1.23 | -2.1 dB |
| Peaking | 804 Hz   | 0.58 | 2.2 dB  |
| Peaking | 1545 Hz  | 0.68 | -0.9 dB |
| Peaking | 13629 Hz | 2.21 | 1.1 dB  |
| Peaking | 16335 Hz | 3.75 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-TWF41/Radius%20HP-TWF41.png)