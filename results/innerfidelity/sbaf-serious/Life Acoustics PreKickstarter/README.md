# Life Acoustics PreKickstarter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.1; 22 0.9; 23 0.8; 25 0.7; 26 0.7; 28 0.6; 30 0.5; 32 0.4; 35 0.3; 37 0.3; 40 0.2; 42 0.2; 45 0.2; 49 0.1; 52 0.0; 56 -0.0; 59 -0.0; 64 -0.1; 68 -0.2; 73 -0.4; 78 -0.6; 83 -0.9; 89 -1.3; 95 -1.6; 102 -2.2; 109 -2.7; 117 -3.1; 125 -3.8; 134 -4.3; 143 -4.6; 153 -4.7; 164 -4.9; 175 -4.9; 188 -4.8; 201 -4.9; 215 -4.7; 230 -4.6; 246 -4.5; 263 -4.4; 282 -4.2; 301 -4.0; 323 -3.8; 345 -3.6; 369 -3.4; 395 -3.2; 423 -2.8; 452 -2.6; 484 -2.4; 518 -2.1; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.7; 726 -0.4; 777 -0.0; 832 -0.0; 890 -0.0; 952 -0.0; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.1; 1429 0.1; 1529 0.0; 1636 0.0; 1751 0.1; 1873 0.2; 2004 0.3; 2145 0.3; 2295 0.6; 2455 1.6; 2627 2.8; 2811 3.9; 3008 5.3; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.3; 4219 3.1; 4514 2.2; 4830 2.8; 5168 4.1; 5530 4.9; 5917 5.5; 6331 4.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Life Acoustics PreKickstarter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.58 | 2.1 dB  |
| Peaking | 177 Hz  | 0.57 | -6.0 dB |
| Peaking | 3373 Hz | 2.49 | 6.4 dB  |
| Peaking | 6069 Hz | 2.79 | 5.7 dB  |
| Peaking | 8022 Hz | 1.93 | -1.5 dB |
| Peaking | 17 Hz   | 1.61 | 0.8 dB  |
| Peaking | 455 Hz  | 1.97 | -0.7 dB |
| Peaking | 775 Hz  | 1.5  | 0.8 dB  |
| Peaking | 2163 Hz | 5.47 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Life%20Acoustics%20PreKickstarter/Life%20Acoustics%20PreKickstarter.png)