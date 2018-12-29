# Sennheiser HD 428
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.5; 96 3.7; 106 2.4; 116 1.5; 128 1.0; 141 0.8; 155 0.6; 170 1.0; 187 1.3; 206 1.5; 227 2.1; 249 2.1; 274 1.6; 302 1.9; 332 1.6; 365 1.6; 402 1.8; 442 1.7; 486 1.9; 535 2.1; 588 2.3; 647 1.9; 712 1.1; 783 0.4; 861 0.1; 947 -0.1; 1042 0.4; 1146 2.0; 1261 -0.1; 1387 -0.7; 1526 -1.2; 1678 -1.9; 1846 -1.9; 2031 -1.1; 2234 1.1; 2457 2.6; 2703 2.7; 2973 3.0; 3270 3.2; 3597 2.6; 3957 3.5; 4353 6.0; 4788 6.0; 5267 3.7; 5793 4.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 428 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.5  | 6.8 dB  |
| Peaking | 462 Hz   | 1.28 | 1.9 dB  |
| Peaking | 2864 Hz  | 4.24 | 2.0 dB  |
| Peaking | 4881 Hz  | 1.75 | 5.9 dB  |
| Peaking | 24000 Hz | 2.34 | 3.0 dB  |
| Peaking | 21 Hz    | 2.37 | 1.7 dB  |
| Peaking | 83 Hz    | 3.89 | 2.2 dB  |
| Peaking | 127 Hz   | 2.26 | -1.9 dB |
| Peaking | 726 Hz   | 0.16 | 0.3 dB  |
| Peaking | 1736 Hz  | 3.43 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)