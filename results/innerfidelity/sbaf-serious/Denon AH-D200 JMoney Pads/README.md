# Denon AH-D200 JMoney Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.4; 26 5.1; 28 4.6; 30 4.1; 32 3.8; 35 3.4; 37 3.3; 40 3.2; 42 3.1; 45 3.1; 49 3.0; 52 3.1; 56 3.3; 59 3.4; 64 3.4; 68 3.3; 73 3.1; 78 2.9; 83 2.7; 89 2.5; 95 2.3; 102 2.0; 109 2.0; 117 1.9; 125 1.7; 134 1.6; 143 1.6; 153 1.5; 164 1.6; 175 1.6; 188 1.5; 201 1.6; 215 1.8; 230 1.9; 246 1.9; 263 1.9; 282 1.9; 301 1.9; 323 1.9; 345 2.0; 369 2.1; 395 1.9; 423 1.9; 452 1.7; 484 1.2; 518 0.9; 554 0.7; 593 0.6; 635 0.1; 679 -0.6; 726 -0.2; 777 1.3; 832 0.2; 890 -0.3; 952 -0.2; 1019 0.1; 1090 0.5; 1167 1.1; 1248 1.4; 1336 1.4; 1429 1.3; 1529 0.9; 1636 0.7; 1751 0.6; 1873 0.9; 2004 1.1; 2145 1.3; 2295 1.3; 2455 1.0; 2627 1.0; 2811 1.1; 3008 2.1; 3219 1.7; 3444 0.3; 3685 -1.0; 3943 -1.6; 4219 -2.0; 4514 -1.3; 4830 -0.7; 5168 -2.4; 5530 -2.4; 5917 0.2; 6331 1.2; 6775 -1.0; 7249 -2.2; 7756 -2.2; 8299 -1.3; 8880 -0.1; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D200 JMoney Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 21 Hz   |  1.11 | 5.8 dB  |
| Peaking | 66 Hz   |  0.92 | 2.6 dB  |
| Peaking | 308 Hz  |  0.75 | 1.8 dB  |
| Peaking | 5037 Hz |  3.47 | -2.1 dB |
| Peaking | 675 Hz  |  6.72 | -1.5 dB |
| Peaking | 2982 Hz |  0.86 | 1.8 dB  |
| Peaking | 3992 Hz |  4.47 | -2.8 dB |
| Peaking | 6318 Hz | 10.18 | 2.6 dB  |
| Peaking | 7344 Hz |  3.6  | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D200%20JMoney%20Pads/Denon%20AH-D200%20JMoney%20Pads.png)