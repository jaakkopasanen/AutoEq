# Stax Lambda Nova Signature

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.6; 25 3.9; 28 3.1; 31 2.6; 34 2.5; 37 2.5; 41 2.6; 45 2.8; 49 3.0; 54 3.3; 60 3.4; 66 3.4; 72 3.4; 79 3.3; 87 3.0; 96 2.5; 106 2.4; 116 2.5; 128 2.3; 141 2.2; 155 2.2; 170 2.1; 187 2.0; 206 2.0; 227 2.0; 249 1.9; 274 1.9; 302 1.9; 332 1.8; 365 1.9; 402 1.8; 442 2.1; 486 1.9; 535 1.8; 588 2.0; 647 1.7; 712 1.4; 783 1.4; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.6; 1261 -1.6; 1387 -3.0; 1526 -3.1; 1678 -3.7; 1846 -2.8; 2031 -0.0; 2234 3.1; 2457 3.6; 2703 1.8; 2973 0.5; 3270 0.4; 3597 1.2; 3957 2.1; 4353 1.9; 4788 2.0; 5267 4.6; 5793 1.9; 6373 1.6; 7010 2.5; 7711 0.3; 8482 -2.4; 9330 -3.4; 10263 -0.6; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax Lambda Nova Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  1.19 | 6.3 dB  |
| Peaking | 86 Hz    |  0.06 | 2.4 dB  |
| Peaking | 1666 Hz  |  1.57 | -5.6 dB |
| Peaking | 2337 Hz  |  3.61 | 5.9 dB  |
| Peaking | 5268 Hz  |  3.24 | 4.0 dB  |
| Peaking | 32 Hz    |  2.13 | -0.9 dB |
| Peaking | 65 Hz    |  2.42 | 1.1 dB  |
| Peaking | 6890 Hz  | 10.18 | 2.9 dB  |
| Peaking | 9177 Hz  |  4.58 | -4.3 dB |
| Peaking | 10698 Hz |  4.11 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20Lambda%20Nova%20Signature/Stax%20Lambda%20Nova%20Signature.png)