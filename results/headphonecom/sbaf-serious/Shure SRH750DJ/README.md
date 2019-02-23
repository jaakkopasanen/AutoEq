# Shure SRH750DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.8; 25 -8.2; 28 -8.7; 31 -9.2; 34 -9.5; 37 -9.8; 41 -10.1; 45 -10.3; 49 -10.4; 54 -10.3; 60 -10.4; 66 -10.7; 72 -11.1; 79 -11.1; 87 -10.5; 96 -9.0; 106 -8.0; 116 -8.3; 128 -9.9; 141 -10.8; 155 -10.8; 170 -9.4; 187 -10.1; 206 -9.3; 227 -8.4; 249 -8.6; 274 -7.3; 302 -6.1; 332 -4.9; 365 -4.3; 402 -4.0; 442 -4.1; 486 -4.3; 535 -4.4; 588 -4.4; 647 -4.3; 712 -4.1; 783 -3.8; 861 -3.2; 947 -3.1; 1042 -4.1; 1146 -4.1; 1261 -4.0; 1387 -5.0; 1526 -6.3; 1678 -8.1; 1846 -10.0; 2031 -11.4; 2234 -11.7; 2457 -9.7; 2703 -6.8; 2973 -4.6; 3270 -3.0; 3597 -2.7; 3957 -4.0; 4353 -7.7; 4788 -4.7; 5267 -2.8; 5793 -0.5; 6373 -0.5; 7010 -3.5; 7711 -5.7; 8482 -9.2; 9330 -10.6; 10263 -7.7; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH750DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH750DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 55 Hz   | 0.69 | -4.7 dB  |
| Peaking | 177 Hz  | 1.45 | -3.9 dB  |
| Peaking | 2087 Hz | 1.83 | -10.5 dB |
| Peaking | 2395 Hz | 0.21 | 4.5 dB   |
| Peaking | 9212 Hz | 3.48 | -7.7 dB  |
| Peaking | 375 Hz  | 5.52 | 1.3 dB   |
| Peaking | 3441 Hz | 4.46 | 2.0 dB   |
| Peaking | 4395 Hz | 6.44 | -5.2 dB  |
| Peaking | 6115 Hz | 5.8  | 3.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH750DJ/Shure%20SRH750DJ.png)