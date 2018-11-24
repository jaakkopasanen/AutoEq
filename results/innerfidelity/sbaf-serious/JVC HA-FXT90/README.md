# JVC HA-FXT90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.6; 28 -0.1; 31 -0.9; 34 -1.5; 37 -1.9; 41 -2.5; 45 -2.9; 49 -3.4; 54 -3.9; 60 -4.5; 66 -5.0; 72 -5.4; 79 -5.8; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.2; 128 -7.3; 141 -7.5; 155 -7.4; 170 -7.3; 187 -7.1; 206 -6.9; 227 -6.5; 249 -6.1; 274 -5.7; 302 -5.1; 332 -4.8; 365 -4.2; 402 -3.6; 442 -2.9; 486 -2.4; 535 -1.9; 588 -1.1; 647 -0.6; 712 -0.2; 783 0.2; 861 0.1; 947 0.1; 1042 -0.2; 1146 -0.7; 1261 -0.7; 1387 -1.4; 1526 -0.5; 1678 -0.3; 1846 -1.1; 2031 -1.6; 2234 -1.9; 2457 -2.0; 2703 -2.1; 2973 -1.0; 3270 0.5; 3597 1.0; 3957 -0.3; 4353 -3.5; 4788 -6.0; 5267 -6.4; 5793 -4.0; 6373 -1.8; 7010 -2.4; 7711 -5.2; 8482 -6.2; 9330 -1.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JVC HA-FXT90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FXT90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 110 Hz   | 0.62 | -6.5 dB |
| Peaking | 252 Hz   | 0.97 | -3.5 dB |
| Peaking | 2279 Hz  | 4.21 | -1.5 dB |
| Peaking | 6048 Hz  | 1.16 | -4.6 dB |
| Peaking | 24000 Hz | 2.12 | -3.9 dB |
| Peaking | 22 Hz    | 2.31 | 2.3 dB  |
| Peaking | 3700 Hz  | 4.74 | 3.6 dB  |
| Peaking | 5004 Hz  | 2.43 | -6.0 dB |
| Peaking | 7114 Hz  | 1.24 | 6.9 dB  |
| Peaking | 8142 Hz  | 3.6  | -9.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-FXT90/JVC%20HA-FXT90.png)