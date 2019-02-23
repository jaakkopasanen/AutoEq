# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -8.0; 25 -8.3; 28 -8.8; 31 -9.1; 34 -9.4; 37 -9.6; 41 -9.9; 45 -10.2; 49 -10.4; 54 -10.6; 60 -10.9; 66 -11.1; 72 -11.3; 79 -11.5; 87 -11.7; 96 -11.6; 106 -11.2; 116 -11.4; 128 -11.8; 141 -11.8; 155 -11.8; 170 -11.8; 187 -11.7; 206 -11.5; 227 -11.2; 249 -10.9; 274 -10.4; 302 -10.0; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.4; 535 -8.0; 588 -7.7; 647 -7.5; 712 -7.3; 783 -7.1; 861 -7.0; 947 -7.0; 1042 -7.2; 1146 -7.1; 1261 -7.5; 1387 -7.1; 1526 -7.5; 1678 -7.1; 1846 -5.9; 2031 -3.4; 2234 -1.3; 2457 -0.5; 2703 -0.6; 2973 -2.1; 3270 -3.4; 3597 -0.8; 3957 -0.9; 4353 -5.3; 4788 -4.8; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.62 | -2.4 dB |
| Peaking | 164 Hz   | 0.45 | -4.7 dB |
| Peaking | 2737 Hz  | 1.8  | 6.0 dB  |
| Peaking | 5946 Hz  | 3.62 | 6.0 dB  |
| Peaking | 22050 Hz | 2.4  | 3.7 dB  |
| Peaking | 1685 Hz  | 2.21 | -2.4 dB |
| Peaking | 2259 Hz  | 2.82 | 3.0 dB  |
| Peaking | 3400 Hz  | 1.88 | -3.2 dB |
| Peaking | 3753 Hz  | 5.75 | 6.4 dB  |
| Peaking | 8253 Hz  | 4.98 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)