# Behringer HPS5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 5.6; 128 5.0; 141 4.7; 155 4.3; 170 4.2; 187 4.1; 206 3.8; 227 3.8; 249 3.8; 274 4.1; 302 4.6; 332 4.5; 365 4.5; 402 4.4; 442 3.4; 486 3.3; 535 3.3; 588 3.5; 647 3.3; 712 2.9; 783 2.4; 861 1.3; 947 0.4; 1042 -0.2; 1146 -0.8; 1261 -0.6; 1387 -1.9; 1526 -3.7; 1678 -3.6; 1846 -2.5; 2031 0.1; 2234 2.7; 2457 5.6; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Behringer HPS5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Behringer HPS5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.21 | 6.3 dB  |
| Peaking | 358 Hz  | 1.76 | 2.6 dB  |
| Peaking | 635 Hz  | 2.49 | 2.3 dB  |
| Peaking | 1656 Hz | 1.95 | -7.7 dB |
| Peaking | 3284 Hz | 0.72 | 7.6 dB  |
| Peaking | 1044 Hz | 6.74 | -0.8 dB |
| Peaking | 2506 Hz | 7.2  | 1.8 dB  |
| Peaking | 3470 Hz | 2.61 | -1.0 dB |
| Peaking | 6261 Hz | 2.31 | 5.6 dB  |
| Peaking | 7337 Hz | 1.44 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Behringer%20HPS5000/Behringer%20HPS5000.png)