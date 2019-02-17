# Sennheiser HD 419
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.8; 23 -13.0; 25 -13.3; 28 -13.5; 31 -13.7; 34 -13.9; 37 -14.0; 41 -14.1; 45 -14.2; 49 -14.3; 54 -14.4; 60 -14.4; 66 -14.4; 72 -14.6; 79 -14.1; 87 -11.9; 96 -12.2; 106 -15.4; 116 -16.2; 128 -16.1; 141 -16.4; 155 -16.4; 170 -16.2; 187 -16.8; 206 -16.6; 227 -16.5; 249 -15.5; 274 -14.4; 302 -13.1; 332 -12.1; 365 -10.8; 402 -9.2; 442 -8.6; 486 -8.6; 535 -9.4; 588 -9.3; 647 -8.3; 712 -7.6; 783 -7.7; 861 -7.1; 947 -6.8; 1042 -6.5; 1146 -7.4; 1261 -6.9; 1387 -7.9; 1526 -8.4; 1678 -8.4; 1846 -8.8; 2031 -7.9; 2234 -6.0; 2457 -4.9; 2703 -4.9; 2973 -4.3; 3270 -4.4; 3597 -4.6; 3957 -2.7; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -0.9; 6373 -1.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 419 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.78 | -6.2 dB |
| Peaking | 56 Hz   | 1.72 | -3.3 dB |
| Peaking | 164 Hz  | 0.68 | -9.3 dB |
| Peaking | 244 Hz  | 2.5  | -2.3 dB |
| Peaking | 4945 Hz | 1.74 | 6.4 dB  |
| Peaking | 92 Hz   | 6.55 | 5.8 dB  |
| Peaking | 95 Hz   | 2.68 | -2.9 dB |
| Peaking | 1872 Hz | 2.35 | -3.9 dB |
| Peaking | 2319 Hz | 1.99 | 2.4 dB  |
| Peaking | 8443 Hz | 4.3  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)