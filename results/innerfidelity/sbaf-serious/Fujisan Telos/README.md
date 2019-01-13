# Fujisan Telos
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.2; 31 4.6; 34 4.0; 37 3.4; 41 2.8; 45 2.3; 49 1.8; 54 1.2; 60 0.6; 66 -0.0; 72 -0.6; 79 -1.2; 87 -1.8; 96 -2.4; 106 -2.9; 116 -3.2; 128 -3.7; 141 -4.1; 155 -4.4; 170 -4.5; 187 -4.7; 206 -4.8; 227 -4.7; 249 -4.7; 274 -4.5; 302 -4.2; 332 -3.8; 365 -3.3; 402 -2.7; 442 -2.1; 486 -1.6; 535 -1.0; 588 -0.1; 647 0.3; 712 0.7; 783 0.9; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.9; 1387 -1.7; 1526 -2.4; 1678 -3.2; 1846 -3.5; 2031 -3.8; 2234 -3.8; 2457 -2.2; 2703 -0.0; 2973 3.0; 3270 5.8; 3597 6.0; 3957 5.8; 4353 3.3; 4788 0.6; 5267 -1.9; 5793 -3.5; 6373 0.2; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fujisan Telos GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fujisan Telos ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.82 | 6.2 dB  |
| Peaking | 186 Hz  | 0.7  | -5.3 dB |
| Peaking | 2218 Hz | 1.64 | -7.6 dB |
| Peaking | 3481 Hz | 1.25 | 8.7 dB  |
| Peaking | 5454 Hz | 4.01 | -6.3 dB |
| Peaking | 354 Hz  | 2.29 | -1.1 dB |
| Peaking | 749 Hz  | 1.83 | 1.8 dB  |
| Peaking | 1541 Hz | 4.3  | -1.1 dB |
| Peaking | 6860 Hz | 7.2  | 4.2 dB  |
| Peaking | 6865 Hz | 2.08 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fujisan%20Telos/Fujisan%20Telos.png)