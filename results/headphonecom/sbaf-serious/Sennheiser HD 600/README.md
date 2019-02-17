# Sennheiser HD 600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -1.8; 45 -2.4; 49 -2.9; 54 -2.9; 60 -3.1; 66 -4.6; 72 -5.5; 79 -6.0; 87 -6.6; 96 -7.0; 106 -7.4; 116 -7.6; 128 -8.0; 141 -7.9; 155 -8.2; 170 -8.3; 187 -8.1; 206 -8.1; 227 -7.9; 249 -7.9; 274 -7.6; 302 -7.3; 332 -7.1; 365 -6.8; 402 -6.5; 442 -6.2; 486 -6.1; 535 -6.2; 588 -6.0; 647 -5.8; 712 -5.6; 783 -5.7; 861 -6.0; 947 -6.3; 1042 -6.2; 1146 -6.2; 1261 -6.4; 1387 -6.8; 1526 -7.1; 1678 -7.1; 1846 -7.2; 2031 -7.2; 2234 -7.7; 2457 -8.0; 2703 -8.4; 2973 -9.0; 3270 -10.2; 3597 -10.8; 3957 -10.7; 4353 -11.0; 4788 -10.7; 5267 -7.9; 5793 -4.0; 6373 -4.8; 7010 -5.3; 7711 -6.2; 8482 -6.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -10.9; 15026 -11.9; 16529 -7.8; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.52 | 6.4 dB  |
| Peaking | 134 Hz   | 0.82 | -2.7 dB |
| Peaking | 4428 Hz  | 1.38 | -6.5 dB |
| Peaking | 5939 Hz  | 2.4  | 5.9 dB  |
| Peaking | 14673 Hz | 2.99 | -6.3 dB |
| Peaking | 268 Hz   | 1.41 | -1.2 dB |
| Peaking | 349 Hz   | 0.67 | 0.8 dB  |
| Peaking | 735 Hz   | 2.32 | 0.8 dB  |
| Peaking | 3226 Hz  | 5.91 | -0.6 dB |
| Peaking | 11545 Hz | 4.16 | 1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -4.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)