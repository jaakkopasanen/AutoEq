# Audio Technical ATH-W5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.4; 60 4.5; 66 3.8; 72 3.2; 79 3.0; 87 2.6; 96 2.2; 106 1.7; 116 1.6; 128 1.3; 141 1.1; 155 0.9; 170 1.1; 187 0.9; 206 0.8; 227 1.0; 249 0.8; 274 0.8; 302 0.8; 332 1.2; 365 1.6; 402 1.8; 442 2.1; 486 2.3; 535 2.5; 588 2.6; 647 2.2; 712 1.2; 783 1.3; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.4; 1387 -1.9; 1526 -2.3; 1678 -2.6; 1846 -3.1; 2031 -3.7; 2234 -2.4; 2457 0.1; 2703 2.8; 2973 6.0; 3270 6.0; 3597 5.9; 3957 2.1; 4353 4.1; 4788 4.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.55 | 6.5 dB  |
| Peaking | 557 Hz  | 1.19 | 2.7 dB  |
| Peaking | 2102 Hz | 1.2  | -5.7 dB |
| Peaking | 3064 Hz | 2.23 | 8.9 dB  |
| Peaking | 5612 Hz | 2.67 | 6.4 dB  |
| Peaking | 45 Hz   | 1.27 | -0.9 dB |
| Peaking | 49 Hz   | 2.72 | 1.5 dB  |
| Peaking | 6588 Hz | 7.48 | 2.3 dB  |
| Peaking | 7693 Hz | 2.27 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-W5000/Audio%20Technical%20ATH-W5000.png)