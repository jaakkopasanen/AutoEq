# NarMoo R1M Silver Ports

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -5.5; 23 -5.6; 25 -5.6; 28 -5.6; 31 -5.7; 34 -5.7; 37 -5.8; 41 -5.8; 45 -6.0; 49 -6.1; 54 -6.2; 60 -6.4; 66 -6.7; 72 -7.0; 79 -7.2; 87 -7.6; 96 -7.9; 106 -8.0; 116 -8.1; 128 -8.3; 141 -8.4; 155 -8.3; 170 -8.2; 187 -8.1; 206 -7.9; 227 -7.5; 249 -7.2; 274 -6.8; 302 -6.3; 332 -5.8; 365 -5.2; 402 -4.7; 442 -4.0; 486 -3.5; 535 -2.9; 588 -2.0; 647 -1.5; 712 -1.1; 783 -0.5; 861 -0.5; 947 -0.3; 1042 0.1; 1146 0.1; 1261 0.1; 1387 -0.3; 1526 -0.6; 1678 -0.8; 1846 -0.6; 2031 -0.4; 2234 -0.3; 2457 0.1; 2703 -0.1; 2973 -0.4; 3270 -0.8; 3597 -1.3; 3957 -2.5; 4353 -5.6; 4788 -8.1; 5267 -7.2; 5793 -2.8; 6373 1.1; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.1; 18182 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo R1M Silver Ports ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.18 | -5.2 dB |
| Peaking | 155 Hz   | 0.67 | -5.1 dB |
| Peaking | 322 Hz   | 1.17 | -2.8 dB |
| Peaking | 4955 Hz  | 3.22 | -9.3 dB |
| Peaking | 6677 Hz  | 4.29 | 4.2 dB  |
| Peaking | 499 Hz   | 4.35 | -0.6 dB |
| Peaking | 1228 Hz  | 1.09 | 1.1 dB  |
| Peaking | 1645 Hz  | 1.87 | -1.3 dB |
| Peaking | 2558 Hz  | 2.85 | 0.6 dB  |
| Peaking | 17005 Hz | 4.26 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20R1M%20Silver%20Ports/NarMoo%20R1M%20Silver%20Ports.png)