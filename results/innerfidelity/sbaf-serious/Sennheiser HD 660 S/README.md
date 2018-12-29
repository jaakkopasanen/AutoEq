# Sennheiser HD 660 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.2; 49 4.7; 54 4.2; 60 3.7; 66 3.2; 72 3.3; 79 3.3; 87 1.9; 96 1.1; 106 0.6; 116 0.3; 128 -0.1; 141 -0.6; 155 -0.8; 170 -0.7; 187 -1.0; 206 -1.0; 227 -1.0; 249 -0.9; 274 -0.9; 302 -0.8; 332 -0.6; 365 -0.5; 402 -0.4; 442 -0.2; 486 -0.2; 535 0.0; 588 0.4; 647 0.5; 712 0.6; 783 0.9; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.4; 1261 -0.5; 1387 -0.7; 1526 -0.7; 1678 -1.0; 1846 -0.6; 2031 0.2; 2234 0.8; 2457 1.5; 2703 1.9; 2973 1.7; 3270 1.2; 3597 1.3; 3957 1.8; 4353 2.0; 4788 3.1; 5267 3.1; 5793 4.0; 6373 3.7; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 660 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 29 Hz   |  0.3  | 6.4 dB  |
| Peaking | 146 Hz  |  0.55 | -2.8 dB |
| Peaking | 1565 Hz |  1.17 | -4.7 dB |
| Peaking | 1731 Hz |  0.56 | 3.8 dB  |
| Peaking | 5855 Hz |  2.72 | 3.6 dB  |
| Peaking | 78 Hz   |  6.67 | 0.7 dB  |
| Peaking | 2597 Hz |  2.43 | -0.5 dB |
| Peaking | 2624 Hz |  5.19 | 1.2 dB  |
| Peaking | 6745 Hz | 11.5  | 2.2 dB  |
| Peaking | 8031 Hz |  2.34 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)