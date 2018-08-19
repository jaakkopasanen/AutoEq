# Klipsch XR8i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.1; 22 -7.2; 23 -7.2; 25 -7.3; 26 -7.3; 28 -7.4; 30 -7.3; 32 -7.3; 35 -7.3; 37 -7.3; 40 -7.2; 42 -7.2; 45 -7.1; 49 -7.1; 52 -7.1; 56 -7.0; 59 -7.0; 64 -7.0; 68 -6.9; 73 -6.9; 78 -6.9; 83 -6.9; 89 -6.9; 95 -6.9; 102 -6.8; 109 -6.6; 117 -6.4; 125 -6.3; 134 -6.2; 143 -6.0; 153 -5.8; 164 -5.6; 175 -5.3; 188 -5.0; 201 -4.8; 215 -4.4; 230 -4.2; 246 -4.0; 263 -3.7; 282 -3.5; 301 -3.2; 323 -2.9; 345 -2.6; 369 -2.3; 395 -2.0; 423 -1.7; 452 -1.3; 484 -1.2; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.1; 1529 -1.4; 1636 -1.5; 1751 -1.5; 1873 -1.3; 2004 -1.2; 2145 -1.1; 2295 -1.1; 2455 -0.6; 2627 -0.2; 2811 0.5; 3008 2.0; 3219 3.7; 3444 5.2; 3685 5.5; 3943 5.2; 4219 3.9; 4514 3.4; 4830 4.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.097714767088151dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch XR8i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.13 | -7.3 dB |
| Peaking | 803 Hz  | 0.76 | 2.6 dB  |
| Peaking | 2783 Hz | 0.36 | -3.2 dB |
| Peaking | 3583 Hz | 2.37 | 7.2 dB  |
| Peaking | 5728 Hz | 2.23 | 7.8 dB  |
| Peaking | 6654 Hz | 7.28 | 2.2 dB  |
| Peaking | 7174 Hz | 2.08 | -1.8 dB |
| Peaking | 8933 Hz | 0.69 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20XR8i/Klipsch%20XR8i.png)