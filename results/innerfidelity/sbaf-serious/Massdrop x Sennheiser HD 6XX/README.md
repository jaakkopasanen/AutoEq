# Massdrop x Sennheiser HD 6XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.6; 45 5.0; 49 4.5; 54 4.1; 60 3.8; 66 2.9; 72 2.7; 79 1.9; 87 0.6; 96 -0.3; 106 -0.9; 116 -1.3; 128 -1.8; 141 -2.1; 155 -2.4; 170 -2.3; 187 -2.5; 206 -2.7; 227 -2.5; 249 -2.3; 274 -2.0; 302 -1.8; 332 -1.8; 365 -1.6; 402 -1.5; 442 -1.2; 486 -1.2; 535 -1.0; 588 -0.7; 647 -0.6; 712 -0.4; 783 -0.1; 861 -0.4; 947 -0.6; 1042 -0.0; 1146 -0.9; 1261 -1.1; 1387 -1.3; 1526 -1.7; 1678 -2.0; 1846 -1.7; 2031 -1.0; 2234 -0.7; 2457 -0.3; 2703 0.1; 2973 -0.1; 3270 -0.1; 3597 -0.4; 3957 0.2; 4353 0.5; 4788 0.9; 5267 3.1; 5793 4.7; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Sennheiser HD 6XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 6XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.28 | 6.5 dB  |
| Peaking | 118 Hz  | 0.8  | -4.2 dB |
| Peaking | 234 Hz  | 0.89 | -2.0 dB |
| Peaking | 2873 Hz | 0.26 | -0.9 dB |
| Peaking | 6049 Hz | 2.99 | 6.4 dB  |
| Peaking | 939 Hz  | 1.84 | 0.6 dB  |
| Peaking | 1666 Hz | 2.19 | -1.4 dB |
| Peaking | 2625 Hz | 2.21 | 1.0 dB  |
| Peaking | 7752 Hz | 7.52 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Sennheiser%20HD%206XX/Massdrop%20x%20Sennheiser%20HD%206XX.png)