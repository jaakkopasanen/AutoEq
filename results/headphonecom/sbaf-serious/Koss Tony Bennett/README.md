# Koss Tony Bennett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.3; 25 -4.8; 28 -5.5; 31 -6.1; 34 -6.5; 37 -7.0; 41 -7.5; 45 -7.9; 49 -8.4; 54 -8.8; 60 -9.2; 66 -9.3; 72 -8.2; 79 -6.0; 87 -5.9; 96 -8.7; 106 -10.2; 116 -11.2; 128 -11.8; 141 -12.4; 155 -12.8; 170 -12.4; 187 -13.2; 206 -13.0; 227 -12.6; 249 -12.2; 274 -11.1; 302 -9.2; 332 -7.6; 365 -6.8; 402 -7.4; 442 -8.3; 486 -8.5; 535 -8.5; 588 -8.0; 647 -8.4; 712 -8.0; 783 -7.2; 861 -6.6; 947 -8.3; 1042 -7.7; 1146 -6.8; 1261 -6.0; 1387 -5.7; 1526 -5.8; 1678 -5.7; 1846 -5.4; 2031 -5.2; 2234 -5.3; 2457 -5.1; 2703 -4.5; 2973 -5.1; 3270 -5.1; 3597 -3.7; 3957 -1.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -9.3; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Tony Bennett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.86 | 3.2 dB  |
| Peaking | 54 Hz   | 3.43 | -2.3 dB |
| Peaking | 179 Hz  | 1.11 | -7.1 dB |
| Peaking | 643 Hz  | 2.43 | -1.4 dB |
| Peaking | 4883 Hz | 1.63 | 6.9 dB  |
| Peaking | 84 Hz   | 4.94 | 5.4 dB  |
| Peaking | 87 Hz   | 1.71 | -2.3 dB |
| Peaking | 356 Hz  | 6.99 | 2.0 dB  |
| Peaking | 6317 Hz | 7.68 | 2.5 dB  |
| Peaking | 9285 Hz | 3.9  | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)