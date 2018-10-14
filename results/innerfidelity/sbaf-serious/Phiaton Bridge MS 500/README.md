# Phiaton Bridge MS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.4; 28 1.9; 31 1.6; 34 1.2; 37 1.0; 41 0.7; 45 0.5; 49 0.3; 54 0.1; 60 0.0; 66 -0.1; 72 -0.3; 79 -0.5; 87 -0.3; 96 -0.1; 106 0.2; 116 0.0; 128 -0.2; 141 0.2; 155 0.9; 170 1.9; 187 2.4; 206 3.3; 227 4.4; 249 5.3; 274 5.9; 302 5.9; 332 5.7; 365 5.4; 402 4.9; 442 4.4; 486 3.5; 535 2.8; 588 2.5; 647 1.8; 712 1.4; 783 0.8; 861 0.5; 947 0.6; 1042 -0.3; 1146 -0.4; 1261 -0.3; 1387 -0.0; 1526 0.6; 1678 0.2; 1846 -0.3; 2031 1.5; 2234 3.5; 2457 5.7; 2703 6.0; 2973 5.5; 3270 3.8; 3597 2.5; 3957 1.8; 4353 3.6; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge MS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.86 | 3.1 dB  |
| Peaking | 318 Hz  | 1.21 | 6.4 dB  |
| Peaking | 2685 Hz | 3.36 | 6.1 dB  |
| Peaking | 5686 Hz | 1.83 | 7.0 dB  |
| Peaking | 7993 Hz | 2.1  | -2.2 dB |
| Peaking | 11 Hz   | 0.42 | 0.7 dB  |
| Peaking | 97 Hz   | 1.17 | -0.9 dB |
| Peaking | 534 Hz  | 2.41 | 0.6 dB  |
| Peaking | 1136 Hz | 3.44 | -1.2 dB |
| Peaking | 1831 Hz | 9.14 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Bridge%20MS%20500/Phiaton%20Bridge%20MS%20500.png)