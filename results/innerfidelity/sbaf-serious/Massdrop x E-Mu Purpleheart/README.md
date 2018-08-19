# Massdrop x E-Mu Purpleheart

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.5; 23 -2.7; 25 -3.0; 26 -3.1; 28 -3.4; 30 -3.6; 32 -3.8; 35 -4.0; 37 -4.1; 40 -4.3; 42 -4.5; 45 -4.6; 49 -4.8; 52 -4.9; 56 -5.1; 59 -5.1; 64 -5.3; 68 -5.4; 73 -5.5; 78 -5.7; 83 -5.8; 89 -6.0; 95 -6.2; 102 -6.3; 109 -6.4; 117 -6.5; 125 -6.6; 134 -6.6; 143 -6.5; 153 -6.5; 164 -6.3; 175 -6.1; 188 -6.1; 201 -5.9; 215 -5.6; 230 -5.3; 246 -5.0; 263 -4.7; 282 -4.3; 301 -4.2; 323 -3.9; 345 -3.6; 369 -3.2; 395 -2.9; 423 -2.5; 452 -2.4; 484 -2.4; 518 -2.2; 554 -1.8; 593 -1.4; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.9; 832 -1.1; 890 -0.6; 952 0.0; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.9; 1429 -1.2; 1529 -1.3; 1636 -1.3; 1751 -1.0; 1873 -0.6; 2004 -0.2; 2145 0.4; 2295 0.9; 2455 1.5; 2627 1.3; 2811 -0.0; 3008 -0.9; 3219 -1.1; 3444 -0.3; 3685 1.5; 3943 1.7; 4219 -1.5; 4514 -1.0; 4830 1.0; 5168 2.4; 5530 4.7; 5917 5.6; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.0; 8880 -2.4; 9502 -2.6; 10167 -1.8; 10879 -0.3; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.819298206665973dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x E-Mu Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.57 | -2.5 dB |
| Peaking | 146 Hz  | 0.45 | -6.1 dB |
| Peaking | 6072 Hz | 3.64 | 6.3 dB  |
| Peaking | 9213 Hz | 3.82 | -3.4 dB |
| Peaking | 885 Hz  | 3.21 | -0.4 dB |
| Peaking | 975 Hz  | 4.1  | 1.1 dB  |
| Peaking | 1593 Hz | 2.47 | -1.3 dB |
| Peaking | 2515 Hz | 3.63 | 2.1 dB  |
| Peaking | 3059 Hz | 5.58 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20E-Mu%20Purpleheart/Massdrop%20x%20E-Mu%20Purpleheart.png)