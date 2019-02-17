# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.7; 28 -2.4; 31 -3.1; 34 -3.6; 37 -4.1; 41 -4.6; 45 -5.0; 49 -5.4; 54 -5.8; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.2; 87 -7.6; 96 -8.2; 106 -8.8; 116 -9.0; 128 -9.3; 141 -9.8; 155 -10.0; 170 -10.0; 187 -10.2; 206 -10.1; 227 -10.1; 249 -10.1; 274 -9.9; 302 -9.7; 332 -9.5; 365 -9.3; 402 -9.0; 442 -8.6; 486 -8.5; 535 -8.2; 588 -7.7; 647 -7.5; 712 -7.3; 783 -6.7; 861 -6.6; 947 -6.1; 1042 -5.5; 1146 -5.2; 1261 -4.3; 1387 -3.8; 1526 -2.9; 1678 -2.6; 1846 -1.8; 2031 -1.4; 2234 -1.8; 2457 -2.4; 2703 -3.0; 2973 -3.3; 3270 -3.1; 3597 -2.2; 3957 -3.7; 4353 -7.1; 4788 -9.6; 5267 -10.9; 5793 -12.2; 6373 -15.4; 7010 -10.6; 7711 -7.1; 8482 -7.4; 9330 -8.3; 10263 -7.7; 11289 -5.9; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -6.5; 18182 -10.0; 20000 -15.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.54 | 6.9 dB  |
| Peaking | 211 Hz   | 0.41 | -4.5 dB |
| Peaking | 2019 Hz  | 1.2  | 4.8 dB  |
| Peaking | 3682 Hz  | 5.39 | 3.9 dB  |
| Peaking | 6068 Hz  | 2.23 | -8.8 dB |
| Peaking | 7850 Hz  | 4.33 | 4.3 dB  |
| Peaking | 8675 Hz  | 1.42 | -3.2 dB |
| Peaking | 14951 Hz | 0.5  | 2.3 dB  |
| Peaking | 19852 Hz | 0.67 | -9.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)