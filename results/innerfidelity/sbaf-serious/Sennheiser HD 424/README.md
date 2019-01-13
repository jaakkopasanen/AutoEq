# Sennheiser HD 424
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 4.7; 106 3.4; 116 2.2; 128 0.8; 141 -0.3; 155 -1.1; 170 -1.5; 187 -1.6; 206 -1.5; 227 -1.3; 249 -0.9; 274 -0.5; 302 -0.1; 332 0.2; 365 0.6; 402 0.8; 442 1.2; 486 1.3; 535 1.3; 588 1.5; 647 1.5; 712 1.2; 783 1.2; 861 0.8; 947 0.4; 1042 -0.0; 1146 -0.5; 1261 -1.1; 1387 -2.4; 1526 -3.6; 1678 -4.7; 1846 -5.3; 2031 -4.9; 2234 -3.8; 2457 -2.2; 2703 -1.1; 2973 -0.4; 3270 -0.3; 3597 -0.8; 3957 -0.7; 4353 -0.1; 4788 2.2; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.6; 9330 -0.9; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 424 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 424 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.27 | 7.3 dB  |
| Peaking | 176 Hz  | 1    | -6.7 dB |
| Peaking | 690 Hz  | 1.02 | 1.5 dB  |
| Peaking | 1827 Hz | 1.78 | -5.8 dB |
| Peaking | 5785 Hz | 3.39 | 7.1 dB  |
| Peaking | 18 Hz   | 1.1  | 1.7 dB  |
| Peaking | 42 Hz   | 0.69 | -0.9 dB |
| Peaking | 85 Hz   | 4.34 | 1.4 dB  |
| Peaking | 4090 Hz | 7.47 | -1.3 dB |
| Peaking | 9000 Hz | 6.03 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20424/Sennheiser%20HD%20424.png)