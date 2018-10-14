# Denon AH-D7000 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.3; 28 4.0; 31 2.7; 34 1.7; 37 1.2; 41 1.1; 45 0.9; 49 0.3; 54 0.2; 60 0.5; 66 0.4; 72 0.3; 79 0.2; 87 0.2; 96 0.4; 106 0.6; 116 0.8; 128 0.8; 141 0.8; 155 0.9; 170 1.2; 187 1.2; 206 1.3; 227 1.6; 249 1.8; 274 2.2; 302 2.6; 332 3.0; 365 3.2; 402 3.4; 442 2.9; 486 2.2; 535 1.3; 588 0.6; 647 0.3; 712 -0.3; 783 -0.9; 861 -0.1; 947 0.5; 1042 -0.0; 1146 0.3; 1261 0.9; 1387 1.3; 1526 1.3; 1678 1.8; 1846 2.2; 2031 2.0; 2234 2.5; 2457 3.3; 2703 3.7; 2973 2.7; 3270 1.1; 3597 0.5; 3957 0.9; 4353 0.9; 4788 -1.7; 5267 -0.5; 5793 -1.4; 6373 -2.4; 7010 -2.0; 7711 -0.7; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.77 | 6.2 dB  |
| Peaking | 486 Hz  |  0.69 | 4.7 dB  |
| Peaking | 672 Hz  |  1.34 | -4.2 dB |
| Peaking | 2515 Hz |  1.79 | 3.3 dB  |
| Peaking | 6341 Hz |  2.81 | -2.7 dB |
| Peaking | 1075 Hz |  7.5  | -0.7 dB |
| Peaking | 1944 Hz |  2.18 | 1.0 dB  |
| Peaking | 2119 Hz |  4.75 | -1.5 dB |
| Peaking | 4787 Hz | 16.39 | -1.8 dB |
| Peaking | 8359 Hz |  7.11 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000%20(balanced)/Denon%20AH-D7000%20(balanced).png)