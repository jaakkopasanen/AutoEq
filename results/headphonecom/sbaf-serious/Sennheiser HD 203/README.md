# Sennheiser HD 203
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.8; 25 -4.5; 28 -5.4; 31 -6.0; 34 -6.6; 37 -7.5; 41 -8.9; 45 -9.8; 49 -10.2; 54 -10.8; 60 -11.7; 66 -12.2; 72 -12.2; 79 -11.7; 87 -11.9; 96 -12.8; 106 -12.8; 116 -12.4; 128 -12.0; 141 -11.3; 155 -10.3; 170 -9.0; 187 -6.7; 206 -2.6; 227 -2.2; 249 -3.3; 274 -4.2; 302 -5.1; 332 -6.8; 365 -8.3; 402 -8.7; 442 -9.1; 486 -9.4; 535 -9.3; 588 -9.1; 647 -8.8; 712 -8.6; 783 -8.8; 861 -9.0; 947 -9.0; 1042 -9.4; 1146 -9.6; 1261 -9.8; 1387 -10.2; 1526 -10.2; 1678 -9.9; 1846 -8.3; 2031 -7.2; 2234 -5.7; 2457 -4.2; 2703 -3.2; 2973 -2.3; 3270 -2.2; 3597 -0.8; 3957 -0.5; 4353 -7.0; 4788 -7.5; 5267 -4.0; 5793 -1.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 203 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 203 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.63 | -6.1 dB |
| Peaking | 230 Hz   | 1.44 | 11.3 dB |
| Peaking | 528 Hz   | 0.16 | -3.9 dB |
| Peaking | 3397 Hz  | 1.2  | 6.9 dB  |
| Peaking | 21686 Hz | 2.39 | 3.3 dB  |
| Peaking | 11 Hz    | 0.53 | 6.0 dB  |
| Peaking | 51 Hz    | 1.75 | -2.2 dB |
| Peaking | 1570 Hz  | 4.73 | -2.1 dB |
| Peaking | 4613 Hz  | 9.52 | -6.5 dB |
| Peaking | 6178 Hz  | 4.6  | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -3.5 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20203/Sennheiser%20HD%20203.png)