# JVC XX Elation HA FR100X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.1; 28 -0.4; 31 -0.8; 34 -1.3; 37 -1.6; 41 -2.1; 45 -2.6; 49 -3.0; 54 -3.6; 60 -4.0; 66 -4.5; 72 -5.0; 79 -5.5; 87 -6.1; 96 -6.6; 106 -6.9; 116 -7.1; 128 -7.3; 141 -7.8; 155 -8.0; 170 -8.0; 187 -8.1; 206 -8.0; 227 -7.9; 249 -7.7; 274 -7.4; 302 -7.2; 332 -6.7; 365 -6.2; 402 -5.7; 442 -4.9; 486 -4.4; 535 -3.7; 588 -2.7; 647 -2.0; 712 -1.4; 783 -0.6; 861 -0.3; 947 0.0; 1042 0.4; 1146 0.9; 1261 1.1; 1387 1.0; 1526 1.0; 1678 1.0; 1846 0.8; 2031 -0.0; 2234 -0.8; 2457 -1.0; 2703 -1.3; 2973 -0.4; 3270 0.5; 3597 0.6; 3957 -1.3; 4353 -5.0; 4788 -7.3; 5267 -4.4; 5793 1.1; 6373 4.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC XX Elation HA FR100X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC XX Elation HA FR100X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 2.15 | 2.9 dB  |
| Peaking | 130 Hz  | 0.55 | -7.0 dB |
| Peaking | 311 Hz  | 1.1  | -4.1 dB |
| Peaking | 4819 Hz | 4.64 | -8.6 dB |
| Peaking | 6402 Hz | 4.94 | 5.9 dB  |
| Peaking | 17 Hz   | 1.98 | 1.3 dB  |
| Peaking | 509 Hz  | 2.86 | -1.2 dB |
| Peaking | 1674 Hz | 0.8  | 2.9 dB  |
| Peaking | 2625 Hz | 1.04 | -3.3 dB |
| Peaking | 3416 Hz | 3.82 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20XX%20Elation%20HA%20FR100X/JVC%20XX%20Elation%20HA%20FR100X.png)