# Sennheiser HD R 130
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -1.4; 72 -3.1; 79 -4.6; 87 -6.2; 96 -7.3; 106 -8.7; 116 -9.3; 128 -9.9; 141 -10.8; 155 -11.3; 170 -11.5; 187 -11.8; 206 -11.4; 227 -12.5; 249 -12.0; 274 -12.2; 302 -12.0; 332 -11.6; 365 -11.5; 402 -11.0; 442 -11.1; 486 -10.9; 535 -10.7; 588 -9.1; 647 -8.3; 712 -7.7; 783 -8.0; 861 -7.9; 947 -7.1; 1042 -6.2; 1146 -6.8; 1261 -8.9; 1387 -10.5; 1526 -12.0; 1678 -11.9; 1846 -12.4; 2031 -10.8; 2234 -8.7; 2457 -7.0; 2703 -10.9; 2973 -13.6; 3270 -12.7; 3597 -14.0; 3957 -10.7; 4353 -17.7; 4788 -14.7; 5267 -12.0; 5793 -12.6; 6373 -11.7; 7010 -4.5; 7711 -6.2; 8482 -11.7; 9330 -16.1; 10263 -12.6; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD R 130 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD R 130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 49 Hz    | 0.45 | 9.9 dB  |
| Peaking | 159 Hz   | 0.42 | -8.7 dB |
| Peaking | 1658 Hz  | 3.78 | -4.6 dB |
| Peaking | 4405 Hz  | 1.04 | -8.0 dB |
| Peaking | 21595 Hz | 2.2  | -6.0 dB |
| Peaking | 999 Hz   | 1.25 | 4.0 dB  |
| Peaking | 1176 Hz  | 0.5  | -2.6 dB |
| Peaking | 2406 Hz  | 8.24 | 4.6 dB  |
| Peaking | 7230 Hz  | 5.23 | 6.7 dB  |
| Peaking | 9381 Hz  | 4.85 | -9.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20R%20130/Sennheiser%20HD%20R%20130.png)