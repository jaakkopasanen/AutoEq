# Focal Utopia with Elear Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.0; 23 -1.1; 25 -1.2; 26 -1.3; 28 -1.4; 30 -1.4; 32 -1.5; 35 -1.6; 37 -1.7; 40 -1.8; 42 -1.8; 45 -2.0; 49 -2.1; 52 -2.3; 56 -2.5; 59 -2.7; 64 -2.9; 68 -3.1; 73 -3.3; 78 -3.5; 83 -3.7; 89 -3.9; 95 -4.2; 102 -4.3; 109 -4.3; 117 -4.5; 125 -4.6; 134 -4.7; 143 -4.7; 153 -4.7; 164 -4.6; 175 -4.6; 188 -4.5; 201 -4.4; 215 -4.3; 230 -4.0; 246 -3.9; 263 -3.7; 282 -3.3; 301 -3.1; 323 -2.8; 345 -2.5; 369 -2.2; 395 -1.9; 423 -1.6; 452 -1.4; 484 -1.3; 518 -1.3; 554 -0.9; 593 -0.5; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.1; 832 -0.0; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.1; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.4; 1529 -0.6; 1636 -0.9; 1751 -0.7; 1873 -0.3; 2004 -0.2; 2145 -0.4; 2295 -1.1; 2455 -2.2; 2627 -2.6; 2811 -1.6; 3008 -0.2; 3219 0.8; 3444 2.7; 3685 4.7; 3943 3.3; 4219 1.9; 4514 2.5; 4830 3.6; 5168 5.4; 5530 4.9; 5917 2.0; 6331 2.5; 6775 3.5; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -2.7; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.5; 18692 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.871619402640747dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Utopia with Elear Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 104 Hz   |  0.51 | -3.6 dB |
| Peaking | 219 Hz   |  0.92 | -2.2 dB |
| Peaking | 2606 Hz  |  4.1  | -3.0 dB |
| Peaking | 3672 Hz  |  5.69 | 4.5 dB  |
| Peaking | 5315 Hz  |  3.71 | 5.3 dB  |
| Peaking | 785 Hz   |  2.29 | 0.5 dB  |
| Peaking | 1635 Hz  |  6.89 | -0.8 dB |
| Peaking | 6786 Hz  | 10.11 | 2.7 dB  |
| Peaking | 8794 Hz  |  6.82 | -3.2 dB |
| Peaking | 18221 Hz |  4.57 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Utopia%20with%20Elear%20Pads/Focal%20Utopia%20with%20Elear%20Pads.png)