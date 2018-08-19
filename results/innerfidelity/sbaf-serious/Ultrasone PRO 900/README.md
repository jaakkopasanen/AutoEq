# Ultrasone PRO 900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 -1.4; 22 -2.3; 23 -2.8; 25 -3.6; 26 -4.0; 28 -4.7; 30 -5.2; 32 -5.7; 35 -6.4; 37 -6.7; 40 -7.2; 42 -7.4; 45 -7.6; 49 -7.8; 52 -8.0; 56 -7.9; 59 -7.3; 64 -5.6; 68 -5.1; 73 -6.0; 78 -7.3; 83 -8.1; 89 -8.5; 95 -8.1; 102 -7.6; 109 -7.7; 117 -7.9; 125 -8.0; 134 -7.4; 143 -7.1; 153 -7.1; 164 -6.0; 175 -6.0; 188 -5.4; 201 -4.2; 215 -2.7; 230 -0.6; 246 1.7; 263 4.0; 282 4.5; 301 3.4; 323 1.8; 345 0.8; 369 0.1; 395 -0.5; 423 -0.8; 452 -0.8; 484 -0.8; 518 0.7; 554 4.7; 593 2.3; 635 0.5; 679 0.2; 726 0.2; 777 0.3; 832 0.0; 890 -0.3; 952 -0.1; 1019 0.2; 1090 0.7; 1167 1.3; 1248 1.4; 1336 0.7; 1429 -0.3; 1529 -1.0; 1636 -1.2; 1751 -1.1; 1873 0.0; 2004 1.1; 2145 0.6; 2295 0.7; 2455 -1.3; 2627 -5.1; 2811 -5.3; 3008 -4.3; 3219 -4.3; 3444 -4.4; 3685 -4.4; 3943 -4.5; 4219 -4.9; 4514 -3.4; 4830 0.9; 5168 4.4; 5530 0.1; 5917 -3.0; 6331 -8.6; 6775 -8.2; 7249 -3.9; 7756 -0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.3; 13327 -4.6; 14260 -7.8; 15258 -9.4; 16326 -9.0; 17469 -7.4; 18692 -5.7; 20000 -4.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.879654372919702dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.1dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 47 Hz    |  0.81 | -7.3 dB  |
| Peaking | 123 Hz   |  1.58 | -7.0 dB  |
| Peaking | 3423 Hz  |  1.87 | -5.1 dB  |
| Peaking | 15027 Hz |  2.91 | -6.8 dB  |
| Peaking | 17871 Hz |  1.14 | -6.4 dB  |
| Peaking | 188 Hz   |  3.58 | -3.1 dB  |
| Peaking | 275 Hz   |  4.05 | 6.5 dB   |
| Peaking | 564 Hz   | 10.58 | 5.0 dB   |
| Peaking | 6235 Hz  |  1.62 | 6.2 dB   |
| Peaking | 6515 Hz  |  5.06 | -15.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%20900/Ultrasone%20PRO%20900.png)