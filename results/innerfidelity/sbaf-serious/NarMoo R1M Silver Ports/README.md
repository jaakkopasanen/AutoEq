# NarMoo R1M Silver Ports

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -5.5; 22 -5.5; 23 -5.6; 25 -5.6; 26 -5.6; 28 -5.6; 30 -5.7; 32 -5.7; 35 -5.8; 37 -5.8; 40 -5.8; 42 -5.9; 45 -6.0; 49 -6.1; 52 -6.2; 56 -6.3; 59 -6.4; 64 -6.6; 68 -6.8; 73 -7.0; 78 -7.2; 83 -7.4; 89 -7.6; 95 -7.8; 102 -8.0; 109 -8.0; 117 -8.1; 125 -8.2; 134 -8.3; 143 -8.4; 153 -8.3; 164 -8.3; 175 -8.2; 188 -8.1; 201 -8.0; 215 -7.7; 230 -7.5; 246 -7.3; 263 -7.0; 282 -6.6; 301 -6.3; 323 -6.0; 345 -5.6; 369 -5.2; 395 -4.8; 423 -4.3; 452 -3.8; 484 -3.5; 518 -3.1; 554 -2.6; 593 -1.9; 635 -1.6; 679 -1.3; 726 -1.0; 777 -0.5; 832 -0.5; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.8; 1751 -0.8; 1873 -0.6; 2004 -0.4; 2145 -0.4; 2295 -0.2; 2455 0.1; 2627 -0.0; 2811 -0.3; 3008 -0.5; 3219 -0.7; 3444 -1.0; 3685 -1.5; 3943 -2.5; 4219 -4.6; 4514 -6.6; 4830 -8.2; 5168 -7.8; 5530 -5.2; 5917 -1.7; 6331 0.9; 6775 2.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.8; 17469 -2.0; 18692 -0.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6161379408651504dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Silver Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.18 | -5.2 dB |
| Peaking | 155 Hz   | 0.67 | -5.1 dB |
| Peaking | 323 Hz   | 1.18 | -2.7 dB |
| Peaking | 4955 Hz  | 3.23 | -9.2 dB |
| Peaking | 6679 Hz  | 4.32 | 4.2 dB  |
| Peaking | 501 Hz   | 4.01 | -0.6 dB |
| Peaking | 1225 Hz  | 1.17 | 1.1 dB  |
| Peaking | 1628 Hz  | 1.82 | -1.2 dB |
| Peaking | 2548 Hz  | 2.73 | 0.6 dB  |
| Peaking | 17058 Hz | 4.26 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Silver%20Ports/NarMoo%20R1M%20Silver%20Ports.png)