# Sennheiser HD 239
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.7; 28 -8.2; 31 -8.5; 34 -8.8; 37 -9.0; 41 -9.3; 45 -9.5; 49 -9.8; 54 -10.0; 60 -10.3; 66 -10.5; 72 -10.6; 79 -10.8; 87 -11.0; 96 -11.0; 106 -10.6; 116 -10.7; 128 -11.1; 141 -11.2; 155 -11.2; 170 -11.2; 187 -11.0; 206 -10.9; 227 -10.6; 249 -10.3; 274 -9.8; 302 -9.3; 332 -9.0; 365 -8.6; 402 -8.2; 442 -7.9; 486 -7.8; 535 -7.3; 588 -7.1; 647 -6.9; 712 -6.7; 783 -6.5; 861 -6.4; 947 -6.3; 1042 -6.6; 1146 -6.5; 1261 -6.8; 1387 -6.4; 1526 -6.9; 1678 -6.5; 1846 -5.3; 2031 -2.8; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -1.5; 3270 -2.8; 3597 -0.6; 3957 -0.7; 4353 -4.7; 4788 -4.2; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 239 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 65 Hz    | 0.6  | -3.2 dB |
| Peaking | 190 Hz   | 0.69 | -3.6 dB |
| Peaking | 2792 Hz  | 1.54 | 6.1 dB  |
| Peaking | 5906 Hz  | 3.53 | 5.8 dB  |
| Peaking | 22050 Hz | 2.55 | 3.6 dB  |
| Peaking | 1699 Hz  | 2.55 | -2.2 dB |
| Peaking | 2209 Hz  | 2.94 | 2.8 dB  |
| Peaking | 3352 Hz  | 1.96 | -2.4 dB |
| Peaking | 3764 Hz  | 6.16 | 4.8 dB  |
| Peaking | 8278 Hz  | 4.51 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)