# Sennheiser HD 428
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.3; 66 -2.2; 72 -0.7; 79 -1.2; 87 -3.6; 96 -5.4; 106 -6.8; 116 -7.6; 128 -8.1; 141 -8.4; 155 -8.5; 170 -8.1; 187 -7.8; 206 -7.6; 227 -7.0; 249 -7.0; 274 -7.5; 302 -7.2; 332 -7.5; 365 -7.5; 402 -7.4; 442 -7.4; 486 -7.3; 535 -7.0; 588 -6.8; 647 -7.3; 712 -8.0; 783 -8.7; 861 -9.1; 947 -9.2; 1042 -8.7; 1146 -7.1; 1261 -9.2; 1387 -9.9; 1526 -10.3; 1678 -11.0; 1846 -11.0; 2031 -10.2; 2234 -8.0; 2457 -6.5; 2703 -6.4; 2973 -6.1; 3270 -5.9; 3597 -6.5; 3957 -5.6; 4353 -0.5; 4788 -0.5; 5267 -5.5; 5793 -4.8; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 428 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.53 | 9.3 dB  |
| Peaking | 391 Hz  | 0.14 | -6.8 dB |
| Peaking | 967 Hz  | 0.19 | 6.2 dB  |
| Peaking | 1697 Hz | 1.34 | -5.3 dB |
| Peaking | 4577 Hz | 5.9  | 5.7 dB  |
| Peaking | 19 Hz   | 3.13 | 1.5 dB  |
| Peaking | 77 Hz   | 8.22 | 3.1 dB  |
| Peaking | 862 Hz  | 5.85 | -1.7 dB |
| Peaking | 6482 Hz | 6.63 | 5.3 dB  |
| Peaking | 8147 Hz | 0.96 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)