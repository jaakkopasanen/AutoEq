# Sennheiser HD 471i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -6.0; 25 -6.3; 28 -6.5; 31 -6.7; 34 -6.9; 37 -6.9; 41 -6.9; 45 -6.9; 49 -6.8; 54 -6.7; 60 -6.5; 66 -6.2; 72 -6.0; 79 -5.8; 87 -5.6; 96 -5.6; 106 -4.8; 116 -4.0; 128 -5.2; 141 -8.0; 155 -8.1; 170 -7.7; 187 -9.1; 206 -8.8; 227 -9.0; 249 -9.0; 274 -8.6; 302 -8.2; 332 -7.7; 365 -6.9; 402 -6.7; 442 -6.9; 486 -6.9; 535 -6.9; 588 -6.9; 647 -7.0; 712 -7.2; 783 -6.8; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -6.6; 1261 -6.7; 1387 -7.0; 1526 -7.6; 1678 -7.5; 1846 -7.0; 2031 -5.7; 2234 -3.7; 2457 -3.4; 2703 -2.2; 2973 -1.6; 3270 -1.2; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 471i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 471i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.32 | 1.1 dB  |
| Peaking | 113 Hz  | 3.15 | 3.5 dB  |
| Peaking | 203 Hz  | 1.09 | -2.8 dB |
| Peaking | 1638 Hz | 2.85 | -2.6 dB |
| Peaking | 4118 Hz | 0.94 | 6.7 dB  |
| Peaking | 38 Hz   | 2.02 | -0.6 dB |
| Peaking | 2775 Hz | 2.84 | 1.2 dB  |
| Peaking | 3746 Hz | 1.91 | -0.9 dB |
| Peaking | 6310 Hz | 2.63 | 4.8 dB  |
| Peaking | 7360 Hz | 1.5  | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20471i/Sennheiser%20HD%20471i.png)