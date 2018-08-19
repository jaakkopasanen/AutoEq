# Brainwavz S1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 10 -84; 20 -9.0; 22 -9.1; 23 -9.1; 25 -9.2; 26 -9.3; 28 -9.3; 30 -9.4; 32 -9.4; 35 -9.5; 37 -9.5; 40 -9.6; 42 -9.7; 45 -9.8; 49 -9.9; 52 -9.9; 56 -10.0; 59 -10.1; 64 -10.2; 68 -10.4; 73 -10.5; 78 -10.6; 83 -10.8; 89 -10.9; 95 -11.1; 102 -11.1; 109 -11.0; 117 -11.0; 125 -11.0; 134 -10.9; 143 -10.8; 153 -10.7; 164 -10.5; 175 -10.2; 188 -10.0; 201 -9.7; 215 -9.4; 230 -9.0; 246 -8.7; 263 -8.3; 282 -7.8; 301 -7.4; 323 -6.9; 345 -6.4; 369 -6.0; 395 -5.5; 423 -4.9; 452 -4.4; 484 -4.0; 518 -3.5; 554 -2.8; 593 -2.2; 635 -1.7; 679 -1.4; 726 -1.0; 777 -0.5; 832 -0.3; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.4; 1429 -0.0; 1529 -1.1; 1636 -2.4; 1751 -2.9; 1873 -2.9; 2004 -2.6; 2145 -2.5; 2295 -2.4; 2455 -2.1; 2627 -2.0; 2811 -2.1; 3008 -2.1; 3219 -2.3; 3444 -2.5; 3685 -3.1; 3943 -4.2; 4219 -6.3; 4514 -8.4; 4830 -9.0; 5168 -9.4; 5530 -7.9; 5917 -4.2; 6331 -1.7; 6775 0.3; 7249 1.0; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -2.0; 10167 -4.9; 10879 -5.4; 11640 -2.9; 12455 -0.8; 13327 -2.6; 14260 -5.9; 15258 -5.9; 16326 -1.8; 17469 0.0; 18692 -0.2; 20000 -6.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.193150258664824dB` and instead set Global volume in the UI for both channels to **-11**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.21 | -8.8 dB |
| Peaking | 147 Hz   | 0.63 | -5.9 dB |
| Peaking | 310 Hz   | 1.15 | -2.9 dB |
| Peaking | 4823 Hz  | 2.6  | -9.8 dB |
| Peaking | 14656 Hz | 2.27 | -6.0 dB |
| Peaking | 1364 Hz  | 1.44 | 3.6 dB  |
| Peaking | 1746 Hz  | 1.58 | -4.6 dB |
| Peaking | 7252 Hz  | 3.84 | 3.2 dB  |
| Peaking | 10627 Hz | 5.11 | -5.3 dB |
| Peaking | 12632 Hz | 5.66 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S1/Brainwavz%20S1.png)