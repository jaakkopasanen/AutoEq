# Pioneer SE-M290
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.1; 31 4.0; 34 3.0; 37 2.2; 41 1.2; 45 0.5; 49 -0.1; 54 -0.6; 60 -1.2; 66 -1.6; 72 -0.9; 79 0.4; 87 -1.0; 96 -2.6; 106 -3.0; 116 -3.3; 128 -3.6; 141 -3.8; 155 -3.7; 170 -3.5; 187 -3.7; 206 -3.7; 227 -3.5; 249 -3.2; 274 -2.6; 302 -2.5; 332 -2.3; 365 -1.8; 402 -1.2; 442 -0.5; 486 -0.3; 535 -0.1; 588 -0.1; 647 -0.4; 712 -0.8; 783 -1.2; 861 -0.9; 947 -0.3; 1042 0.3; 1146 1.5; 1261 3.3; 1387 4.4; 1526 5.3; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 4.8; 5793 5.5; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-M290 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-M290 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.69 | 6.4 dB  |
| Peaking | 48 Hz   | 2.05 | -1.9 dB |
| Peaking | 173 Hz  | 0.64 | -4.3 dB |
| Peaking | 892 Hz  | 1.89 | -3.7 dB |
| Peaking | 2492 Hz | 0.46 | 6.9 dB  |
| Peaking | 1618 Hz | 4.61 | 0.9 dB  |
| Peaking | 2573 Hz | 2.11 | -0.9 dB |
| Peaking | 6347 Hz | 1.66 | 5.3 dB  |
| Peaking | 7623 Hz | 1.42 | -5.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-M290/Pioneer%20SE-M290.png)