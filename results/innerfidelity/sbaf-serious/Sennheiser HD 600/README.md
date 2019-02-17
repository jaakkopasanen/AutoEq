# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.3; 41 -2.2; 45 -2.9; 49 -3.5; 54 -4.1; 60 -4.8; 66 -5.4; 72 -5.7; 79 -6.5; 87 -7.5; 96 -8.2; 106 -8.6; 116 -9.0; 128 -9.3; 141 -9.6; 155 -9.6; 170 -9.4; 187 -9.6; 206 -9.5; 227 -9.3; 249 -9.1; 274 -8.9; 302 -8.6; 332 -8.4; 365 -8.1; 402 -8.0; 442 -7.7; 486 -7.7; 535 -7.4; 588 -7.0; 647 -7.0; 712 -7.1; 783 -6.9; 861 -7.1; 947 -7.0; 1042 -6.6; 1146 -7.1; 1261 -7.5; 1387 -7.8; 1526 -8.4; 1678 -8.8; 1846 -8.4; 2031 -7.8; 2234 -7.9; 2457 -7.3; 2703 -7.7; 2973 -7.6; 3270 -8.1; 3597 -8.1; 3957 -7.2; 4353 -7.8; 4788 -8.0; 5267 -4.4; 5793 -2.4; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.9; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.5  | 6.6 dB  |
| Peaking | 143 Hz  | 0.53 | -4.0 dB |
| Peaking | 1690 Hz | 2.8  | -2.0 dB |
| Peaking | 5208 Hz | 1    | -4.2 dB |
| Peaking | 6001 Hz | 2.33 | 8.5 dB  |
| Peaking | 8800 Hz | 3.85 | -1.4 dB |
| Peaking | 9542 Hz | 1.51 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)