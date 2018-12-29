# Sennheiser HD 414
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.3; 79 4.1; 87 3.3; 96 2.4; 106 1.6; 116 1.1; 128 0.4; 141 -0.2; 155 -0.6; 170 -1.0; 187 -1.0; 206 -1.2; 227 -1.2; 249 -1.1; 274 -0.9; 302 -0.7; 332 -0.8; 365 -0.6; 402 -0.4; 442 -0.2; 486 -0.2; 535 -0.1; 588 0.3; 647 0.3; 712 0.2; 783 0.4; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.2; 1526 -1.9; 1678 -2.4; 1846 -2.3; 2031 -1.6; 2234 -2.0; 2457 -4.1; 2703 -6.3; 2973 -4.2; 3270 -1.7; 3597 -0.5; 3957 0.9; 4353 2.6; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 414 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 414 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.25 | 7.5 dB  |
| Peaking | 157 Hz  | 0.67 | -6.0 dB |
| Peaking | 1668 Hz | 3.67 | -2.3 dB |
| Peaking | 2742 Hz | 3.54 | -6.7 dB |
| Peaking | 5462 Hz | 2.37 | 7.1 dB  |
| Peaking | 63 Hz   | 1.03 | -0.9 dB |
| Peaking | 66 Hz   | 2.91 | 1.7 dB  |
| Peaking | 776 Hz  | 2.62 | 0.5 dB  |
| Peaking | 6559 Hz | 6.78 | 2.6 dB  |
| Peaking | 7627 Hz | 2.13 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20414/Sennheiser%20HD%20414.png)