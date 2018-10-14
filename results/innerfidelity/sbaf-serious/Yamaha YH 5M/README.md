# Yamaha YH 5M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 5.5; 87 5.0; 96 4.4; 106 4.1; 116 3.8; 128 3.5; 141 2.8; 155 2.6; 170 2.4; 187 2.0; 206 1.9; 227 1.8; 249 1.6; 274 1.4; 302 1.3; 332 1.2; 365 1.0; 402 0.8; 442 0.7; 486 0.3; 535 -0.1; 588 -0.1; 647 -0.5; 712 -1.2; 783 -1.4; 861 -1.3; 947 -0.3; 1042 0.5; 1146 2.7; 1261 4.8; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.7; 4788 5.0; 5267 3.9; 5793 4.8; 6373 2.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH 5M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.28 | 6.3 dB  |
| Peaking | 872 Hz  | 1.68 | -3.3 dB |
| Peaking | 1393 Hz | 1.85 | 4.7 dB  |
| Peaking | 2372 Hz | 1.02 | 4.4 dB  |
| Peaking | 4301 Hz | 1.33 | 4.1 dB  |
| Peaking | 73 Hz   | 4.77 | 0.5 dB  |
| Peaking | 5150 Hz | 4.65 | -2.0 dB |
| Peaking | 5588 Hz | 2.92 | 2.3 dB  |
| Peaking | 8486 Hz | 1.95 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH%205M/Yamaha%20YH%205M.png)