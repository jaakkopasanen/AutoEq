# Sennheiser Urbanite XL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 -0.0; 25 -0.6; 28 -1.2; 31 -1.7; 34 -2.2; 37 -2.6; 41 -3.1; 45 -3.5; 49 -3.8; 54 -4.2; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.6; 87 -6.1; 96 -6.5; 106 -6.5; 116 -6.3; 128 -6.1; 141 -6.6; 155 -7.1; 170 -5.9; 187 -6.2; 206 -6.0; 227 -5.2; 249 -4.8; 274 -4.9; 302 -5.4; 332 -5.5; 365 -5.0; 402 -4.0; 442 -3.2; 486 -3.1; 535 -2.3; 588 -1.4; 647 -1.2; 712 -1.2; 783 -0.7; 861 -0.6; 947 -0.2; 1042 0.2; 1146 -0.1; 1261 -0.4; 1387 -0.9; 1526 -1.5; 1678 -1.9; 1846 -2.2; 2031 -2.2; 2234 -1.1; 2457 0.4; 2703 1.0; 2973 2.4; 3270 2.6; 3597 3.7; 3957 5.5; 4353 6.1; 4788 1.0; 5267 -0.2; 5793 4.1; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Urbanite XL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 74 Hz    |  0.68 | -2.0 dB |
| Peaking | 155 Hz   |  0.45 | -5.4 dB |
| Peaking | 350 Hz   |  2.91 | -1.9 dB |
| Peaking | 4073 Hz  |  2.6  | 5.8 dB  |
| Peaking | 21464 Hz |  2.52 | 1.9 dB  |
| Peaking | 20 Hz    |  2.46 | 1.6 dB  |
| Peaking | 1878 Hz  |  1.69 | -5.3 dB |
| Peaking | 1891 Hz  |  0.83 | 2.8 dB  |
| Peaking | 5026 Hz  | 10.51 | -5.6 dB |
| Peaking | 6228 Hz  |  5.08 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite%20XL/Sennheiser%20Urbanite%20XL.png)