# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.6; 28 4.9; 31 3.9; 34 3.1; 37 2.4; 41 1.7; 45 1.0; 49 0.4; 54 -0.4; 60 -1.0; 66 -1.4; 72 -1.9; 79 -1.9; 87 -1.5; 96 -1.4; 106 -1.9; 116 -2.0; 128 -2.0; 141 -2.0; 155 -1.8; 170 -1.0; 187 -0.8; 206 -0.0; 227 1.8; 249 3.1; 274 2.9; 302 2.8; 332 3.2; 365 3.8; 402 3.9; 442 3.2; 486 2.6; 535 2.2; 588 1.9; 647 1.4; 712 1.0; 783 0.9; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.6; 1678 -1.7; 1846 -0.8; 2031 0.8; 2234 2.1; 2457 4.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.9; 4788 2.1; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 2.13 | 6.3 dB  |
| Peaking | 261 Hz  | 5.43 | 2.5 dB  |
| Peaking | 403 Hz  | 2.21 | 4.1 dB  |
| Peaking | 3249 Hz | 2.04 | 6.8 dB  |
| Peaking | 5877 Hz | 3.64 | 5.8 dB  |
| Peaking | 37 Hz   | 2.6  | 1.6 dB  |
| Peaking | 100 Hz  | 0.95 | -2.3 dB |
| Peaking | 1620 Hz | 2.78 | -2.8 dB |
| Peaking | 2570 Hz | 6.37 | 2.4 dB  |
| Peaking | 8279 Hz | 4.56 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)