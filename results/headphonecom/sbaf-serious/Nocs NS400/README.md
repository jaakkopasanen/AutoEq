# Nocs NS400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.7; 23 -15.6; 25 -15.6; 28 -15.5; 31 -15.4; 34 -15.3; 37 -15.3; 41 -15.2; 45 -15.1; 49 -15.0; 54 -15.0; 60 -14.9; 66 -14.8; 72 -14.7; 79 -14.7; 87 -14.5; 96 -14.3; 106 -14.1; 116 -13.8; 128 -13.5; 141 -13.2; 155 -12.9; 170 -12.5; 187 -12.0; 206 -11.4; 227 -10.8; 249 -10.2; 274 -9.6; 302 -8.9; 332 -8.2; 365 -7.4; 402 -6.8; 442 -6.2; 486 -5.6; 535 -4.9; 588 -4.3; 647 -3.7; 712 -3.3; 783 -3.2; 861 -3.1; 947 -3.3; 1042 -3.7; 1146 -4.0; 1261 -4.5; 1387 -5.1; 1526 -5.7; 1678 -6.2; 1846 -6.6; 2031 -7.4; 2234 -8.1; 2457 -8.3; 2703 -7.5; 2973 -5.6; 3270 -2.7; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -3.5; 5267 -4.1; 5793 -6.5; 6373 -10.5; 7010 -8.9; 7711 -6.2; 8482 -4.2; 9330 -4.7; 10263 -6.1; 11289 -3.7; 12418 -3.6; 13660 -3.6; 15026 -3.6; 16529 -3.6; 18182 -3.6; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.21 | -11.8 dB |
| Peaking | 170 Hz   | 0.73 | -4.3 dB  |
| Peaking | 2434 Hz  | 1.76 | -5.7 dB  |
| Peaking | 3722 Hz  | 2.62 | 5.4 dB   |
| Peaking | 6588 Hz  | 3.68 | -7.3 dB  |
| Peaking | 85 Hz    | 3.35 | -0.5 dB  |
| Peaking | 324 Hz   | 1.89 | -0.8 dB  |
| Peaking | 791 Hz   | 1.51 | 1.6 dB   |
| Peaking | 1564 Hz  | 3.28 | -1.0 dB  |
| Peaking | 10212 Hz | 8.31 | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -12.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.0 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS400/Nocs%20NS400.png)