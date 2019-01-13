# Sennheiser HD 439
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.3; 28 0.9; 31 0.5; 34 0.2; 37 0.0; 41 -0.3; 45 -0.5; 49 -0.7; 54 -0.9; 60 -1.1; 66 -1.1; 72 -1.0; 79 -1.4; 87 -1.7; 96 -0.4; 106 0.8; 116 -1.1; 128 -2.4; 141 -2.7; 155 -3.0; 170 -2.9; 187 -3.1; 206 -3.1; 227 -3.2; 249 -3.2; 274 -2.7; 302 -1.6; 332 -0.8; 365 -0.2; 402 -0.3; 442 0.1; 486 0.3; 535 0.3; 588 0.5; 647 0.4; 712 0.3; 783 0.2; 861 -0.1; 947 -0.0; 1042 0.3; 1146 0.3; 1261 0.2; 1387 -1.2; 1526 -1.6; 1678 -1.6; 1846 -0.5; 2031 0.6; 2234 2.0; 2457 3.9; 2703 4.4; 2973 4.8; 3270 4.9; 3597 4.8; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 439 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.35 | 2.2 dB  |
| Peaking | 60 Hz   | 1.62 | -1.1 dB |
| Peaking | 197 Hz  | 1.35 | -3.6 dB |
| Peaking | 1627 Hz | 3.28 | -3.3 dB |
| Peaking | 4120 Hz | 0.93 | 6.5 dB  |
| Peaking | 105 Hz  | 9.16 | 2.3 dB  |
| Peaking | 128 Hz  | 4.4  | -1.0 dB |
| Peaking | 2573 Hz | 6.46 | 1.7 dB  |
| Peaking | 6178 Hz | 2.55 | 6.2 dB  |
| Peaking | 6875 Hz | 1.21 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)