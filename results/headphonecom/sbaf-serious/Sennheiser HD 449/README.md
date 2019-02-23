# Sennheiser HD 449
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.9; 25 -5.5; 28 -6.3; 31 -7.0; 34 -7.7; 37 -8.2; 41 -8.8; 45 -9.4; 49 -9.8; 54 -10.3; 60 -10.8; 66 -11.1; 72 -11.1; 79 -10.9; 87 -10.8; 96 -10.1; 106 -8.1; 116 -9.0; 128 -11.5; 141 -12.2; 155 -11.0; 170 -10.4; 187 -12.0; 206 -11.3; 227 -11.5; 249 -11.2; 274 -9.9; 302 -8.6; 332 -7.9; 365 -7.4; 402 -7.0; 442 -6.5; 486 -6.7; 535 -6.5; 588 -6.9; 647 -7.7; 712 -7.8; 783 -8.0; 861 -7.9; 947 -8.3; 1042 -8.2; 1146 -8.1; 1261 -8.9; 1387 -9.9; 1526 -10.5; 1678 -10.4; 1846 -9.8; 2031 -8.6; 2234 -6.9; 2457 -5.6; 2703 -5.2; 2973 -4.6; 3270 -4.6; 3597 -4.1; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 449 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 2.28 | -2.2 dB |
| Peaking | 73 Hz   | 1.95 | -3.5 dB |
| Peaking | 184 Hz  | 1.13 | -5.2 dB |
| Peaking | 1566 Hz | 1.77 | -4.5 dB |
| Peaking | 4853 Hz | 1.47 | 7.0 dB  |
| Peaking | 20 Hz   | 2.69 | 2.9 dB  |
| Peaking | 247 Hz  | 7.73 | -1.4 dB |
| Peaking | 425 Hz  | 3.2  | 1.1 dB  |
| Peaking | 6425 Hz | 4.41 | 3.6 dB  |
| Peaking | 7482 Hz | 1.73 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)