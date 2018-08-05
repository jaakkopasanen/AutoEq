# NarMoo R1M Silver Ports

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 -5.5; 22 -5.5; 23 -5.5; 25 -5.5; 26 -5.5; 28 -5.5; 30 -5.5; 32 -5.5; 35 -5.5; 37 -5.4; 40 -5.4; 42 -5.4; 45 -5.4; 49 -5.4; 52 -5.4; 56 -5.3; 59 -5.3; 64 -5.3; 68 -5.4; 73 -5.5; 78 -5.6; 83 -5.8; 89 -6.1; 95 -6.4; 102 -6.9; 109 -7.3; 117 -7.8; 125 -8.2; 134 -8.6; 143 -8.8; 153 -8.9; 164 -8.8; 175 -8.7; 188 -8.6; 201 -8.4; 215 -8.1; 230 -7.8; 246 -7.6; 263 -7.2; 282 -6.8; 301 -6.5; 323 -6.1; 345 -5.7; 369 -5.3; 395 -4.9; 423 -4.3; 452 -3.9; 484 -3.6; 518 -3.2; 554 -2.6; 593 -1.9; 635 -1.6; 679 -1.3; 726 -1.0; 777 -0.6; 832 -0.5; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.8; 1751 -0.8; 1873 -0.6; 2004 -0.4; 2145 -0.4; 2295 -0.2; 2455 0.1; 2627 -0.0; 2811 -0.3; 3008 -0.5; 3219 -0.7; 3444 -1.0; 3685 -1.5; 3943 -2.5; 4219 -4.6; 4514 -6.6; 4830 -8.2; 5168 -7.8; 5530 -5.2; 5917 -1.7; 6331 0.9; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.8; 17469 -2.0; 18692 -0.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Silver Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.4  | -5.0 dB |
| Peaking | 181 Hz   | 0.59 | -8.5 dB |
| Peaking | 4955 Hz  | 3.25 | -9.3 dB |
| Peaking | 6650 Hz  | 3.98 | 4.1 dB  |
| Peaking | 31099 Hz | 4.23 | -2.6 dB |
| Peaking | 215 Hz   | 2.16 | 0.9 dB  |
| Peaking | 883 Hz   | 0.36 | -2.4 dB |
| Peaking | 907 Hz   | 0.78 | 3.2 dB  |
| Peaking | 2720 Hz  | 1.69 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Silver%20Ports/NarMoo%20R1M%20Silver%20Ports.png)