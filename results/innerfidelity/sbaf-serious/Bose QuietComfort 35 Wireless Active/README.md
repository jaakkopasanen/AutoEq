# Bose QuietComfort 35 Wireless Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -5.1; 23 -4.4; 25 -3.8; 28 -3.3; 31 -3.0; 34 -3.0; 37 -2.9; 41 -2.9; 45 -2.8; 49 -2.7; 54 -2.5; 60 -2.2; 66 -2.1; 72 -2.0; 79 -2.1; 87 -2.2; 96 -2.3; 106 -2.2; 116 -2.1; 128 -2.0; 141 -1.9; 155 -1.7; 170 -1.2; 187 -1.3; 206 -1.2; 227 -1.0; 249 -0.8; 274 -0.5; 302 -0.2; 332 0.0; 365 0.3; 402 0.5; 442 0.8; 486 0.7; 535 0.8; 588 1.0; 647 0.9; 712 0.5; 783 0.5; 861 0.1; 947 -0.1; 1042 0.2; 1146 1.0; 1261 2.1; 1387 2.3; 1526 3.1; 1678 1.9; 1846 1.6; 2031 -0.1; 2234 -1.2; 2457 -1.5; 2703 -2.7; 2973 -2.1; 3270 -0.2; 3597 -0.1; 3957 -2.4; 4353 -2.2; 4788 -0.4; 5267 4.6; 5793 1.8; 6373 -1.0; 7010 1.1; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 Wireless Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 116 Hz  |  1.03 | -1.7 dB |
| Peaking | 1627 Hz |  1.4  | 5.1 dB  |
| Peaking | 2326 Hz |  0.97 | -3.9 dB |
| Peaking | 5435 Hz | 11.1  | 7.0 dB  |
| Peaking | 18 Hz   |  1.47 | -5.5 dB |
| Peaking | 36 Hz   |  0.6  | -2.0 dB |
| Peaking | 506 Hz  |  2.3  | 1.0 dB  |
| Peaking | 3484 Hz |  8.72 | 2.8 dB  |
| Peaking | 4153 Hz |  5.01 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2035%20Wireless%20Active/Bose%20QuietComfort%2035%20Wireless%20Active.png)