# Sennheiser HD 599
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.5; 31 -2.1; 34 -2.5; 37 -2.9; 41 -3.4; 45 -3.7; 49 -4.1; 54 -4.6; 60 -5.2; 66 -5.8; 72 -6.3; 79 -6.7; 87 -7.3; 96 -7.8; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.5; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.2; 227 -8.9; 249 -8.6; 274 -8.5; 302 -8.3; 332 -8.1; 365 -7.8; 402 -7.6; 442 -7.3; 486 -7.2; 535 -6.9; 588 -6.7; 647 -6.0; 712 -5.5; 783 -5.1; 861 -4.9; 947 -4.8; 1042 -4.5; 1146 -4.2; 1261 -3.9; 1387 -3.4; 1526 -2.5; 1678 -2.4; 1846 -3.2; 2031 -4.6; 2234 -5.0; 2457 -4.2; 2703 -4.9; 2973 -6.5; 3270 -7.8; 3597 -7.4; 3957 -7.4; 4353 -8.9; 4788 -7.5; 5267 -5.9; 5793 -6.0; 6373 -4.5; 7010 -4.1; 7711 -6.2; 8482 -7.4; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -10.7; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 599 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 599 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.31 | 6.6 dB  |
| Peaking | 154 Hz   | 0.6  | -3.6 dB |
| Peaking | 938 Hz   | 1.53 | 1.6 dB  |
| Peaking | 1631 Hz  | 2.2  | 4.0 dB  |
| Peaking | 9067 Hz  | 3.62 | -0.6 dB |
| Peaking | 2552 Hz  | 6.39 | 2.0 dB  |
| Peaking | 4005 Hz  | 1.85 | -1.9 dB |
| Peaking | 6710 Hz  | 5.2  | 3.4 dB  |
| Peaking | 19376 Hz | 1.42 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20599/Sennheiser%20HD%20599.png)