# Sennheiser HD 448
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.5; 60 4.8; 66 4.4; 72 3.8; 79 3.0; 87 1.8; 96 1.9; 106 2.9; 116 2.5; 128 0.8; 141 -0.9; 155 -1.6; 170 -1.6; 187 -2.1; 206 -1.8; 227 -1.5; 249 -0.9; 274 -0.3; 302 0.5; 332 1.1; 365 1.0; 402 0.8; 442 0.8; 486 0.5; 535 0.2; 588 0.2; 647 -0.1; 712 -0.5; 783 -0.3; 861 -0.2; 947 -0.0; 1042 -0.3; 1146 -0.6; 1261 -1.5; 1387 -2.4; 1526 -3.4; 1678 -4.2; 1846 -4.0; 2031 -2.8; 2234 -1.1; 2457 2.0; 2703 1.4; 2973 2.2; 3270 2.4; 3597 3.3; 3957 5.1; 4353 6.0; 4788 6.0; 5267 3.2; 5793 5.2; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 448 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.92 | 5.6 dB  |
| Peaking | 53 Hz   | 1.35 | 4.2 dB  |
| Peaking | 1710 Hz | 2.67 | -5.0 dB |
| Peaking | 4315 Hz | 1.82 | 6.0 dB  |
| Peaking | 6201 Hz | 6.23 | 4.3 dB  |
| Peaking | 112 Hz  | 3.96 | 3.0 dB  |
| Peaking | 183 Hz  | 1.24 | -2.8 dB |
| Peaking | 351 Hz  | 1.76 | 1.7 dB  |
| Peaking | 2512 Hz | 8.3  | 2.2 dB  |
| Peaking | 5730 Hz | 0.19 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)