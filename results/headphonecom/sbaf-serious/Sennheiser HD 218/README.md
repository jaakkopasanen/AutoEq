# Sennheiser HD 218
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.7; 72 -1.4; 79 -1.6; 87 -2.1; 96 -3.4; 106 -4.4; 116 -5.3; 128 -6.2; 141 -7.0; 155 -7.6; 170 -7.2; 187 -7.6; 206 -8.6; 227 -9.2; 249 -9.7; 274 -10.2; 302 -10.5; 332 -11.0; 365 -11.6; 402 -10.4; 442 -9.2; 486 -8.8; 535 -8.8; 588 -7.2; 647 -6.4; 712 -6.2; 783 -6.2; 861 -6.3; 947 -6.6; 1042 -6.7; 1146 -6.6; 1261 -6.2; 1387 -5.7; 1526 -5.2; 1678 -6.2; 1846 -6.1; 2031 -5.5; 2234 -4.4; 2457 -3.3; 2703 -2.8; 2973 -2.9; 3270 -2.3; 3597 -1.2; 3957 -0.5; 4353 -4.3; 4788 -9.1; 5267 -8.6; 5793 -7.1; 6373 -5.2; 7010 -4.1; 7711 -6.2; 8482 -7.1; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.9; 18182 -13.2; 20000 -13.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 218 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.48 | 6.8 dB  |
| Peaking | 299 Hz   | 1.02 | -5.0 dB |
| Peaking | 3303 Hz  | 1.86 | 5.3 dB  |
| Peaking | 14762 Hz | 1.01 | 5.1 dB  |
| Peaking | 18812 Hz | 0.38 | -8.4 dB |
| Peaking | 142 Hz   | 4.95 | -1.4 dB |
| Peaking | 714 Hz   | 3.45 | 1.3 dB  |
| Peaking | 4050 Hz  | 6.23 | 4.8 dB  |
| Peaking | 4860 Hz  | 3.38 | -4.9 dB |
| Peaking | 6755 Hz  | 6.67 | 3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)