# NarMoo R1M Black Ports

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 10 -84; 20 -12.8; 22 -12.8; 23 -12.8; 25 -12.8; 26 -12.8; 28 -12.7; 30 -12.7; 32 -12.6; 35 -12.5; 37 -12.5; 40 -12.4; 42 -12.4; 45 -12.3; 49 -12.3; 52 -12.2; 56 -12.2; 59 -12.2; 64 -12.2; 68 -12.1; 73 -12.1; 78 -12.1; 83 -12.1; 89 -12.1; 95 -12.1; 102 -11.9; 109 -11.7; 117 -11.5; 125 -11.4; 134 -11.2; 143 -11.0; 153 -10.7; 164 -10.4; 175 -10.0; 188 -9.6; 201 -9.3; 215 -8.8; 230 -8.3; 246 -7.9; 263 -7.5; 282 -6.9; 301 -6.3; 323 -5.8; 345 -5.2; 369 -4.6; 395 -4.1; 423 -3.4; 452 -2.8; 484 -2.3; 518 -1.7; 554 -0.9; 593 -0.3; 635 0.2; 679 0.3; 726 0.4; 777 0.6; 832 0.3; 890 0.0; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.8; 1529 -1.1; 1636 -1.2; 1751 -1.3; 1873 -1.1; 2004 -0.9; 2145 -0.8; 2295 -0.6; 2455 -0.3; 2627 -0.4; 2811 -0.8; 3008 -0.9; 3219 -1.0; 3444 -1.1; 3685 -1.6; 3943 -2.5; 4219 -4.6; 4514 -6.6; 4830 -8.2; 5168 -8.0; 5530 -5.6; 5917 -2.0; 6331 0.6; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -2.1; 17469 -2.8; 18692 -0.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.5151692581448875dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Black Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.2  | -12.5 dB |
| Peaking | 170 Hz   | 0.7  | -5.2 dB  |
| Peaking | 5059 Hz  | 2.75 | -10.2 dB |
| Peaking | 6529 Hz  | 2.46 | 4.5 dB   |
| Peaking | 17253 Hz | 3.56 | -3.3 dB  |
| Peaking | 40 Hz    | 2.25 | 0.3 dB   |
| Peaking | 351 Hz   | 1.86 | -1.1 dB  |
| Peaking | 690 Hz   | 1.54 | 1.9 dB   |
| Peaking | 1677 Hz  | 2.9  | -1.1 dB  |
| Peaking | 3559 Hz  | 6.37 | 0.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Black%20Ports/NarMoo%20R1M%20Black%20Ports.png)