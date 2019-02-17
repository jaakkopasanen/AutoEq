# Sennheiser HD 202
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.7; 34 -2.7; 37 -3.5; 41 -4.4; 45 -5.3; 49 -5.8; 54 -6.2; 60 -6.8; 66 -7.5; 72 -7.5; 79 -8.0; 87 -8.2; 96 -8.3; 106 -8.3; 116 -8.1; 128 -8.0; 141 -7.7; 155 -7.3; 170 -6.5; 187 -5.1; 206 -2.4; 227 -1.4; 249 -2.0; 274 -2.2; 302 -2.3; 332 -2.8; 365 -3.5; 402 -3.6; 442 -3.8; 486 -4.4; 535 -4.7; 588 -5.2; 647 -5.5; 712 -5.8; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.8; 1261 -6.6; 1387 -6.9; 1526 -7.2; 1678 -6.7; 1846 -5.6; 2031 -4.1; 2234 -2.3; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -5.4; 4788 -4.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 202 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.07 | 6.6 dB  |
| Peaking | 153 Hz  | 0.61 | -5.6 dB |
| Peaking | 242 Hz  | 0.96 | 9.1 dB  |
| Peaking | 3017 Hz | 1.81 | 6.7 dB  |
| Peaking | 5849 Hz | 3.59 | 5.9 dB  |
| Peaking | 2377 Hz | 2.47 | 6.4 dB  |
| Peaking | 2629 Hz | 0.99 | -5.8 dB |
| Peaking | 4222 Hz | 2.03 | 6.6 dB  |
| Peaking | 4496 Hz | 7.62 | -8.1 dB |
| Peaking | 8217 Hz | 3.5  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 5.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)