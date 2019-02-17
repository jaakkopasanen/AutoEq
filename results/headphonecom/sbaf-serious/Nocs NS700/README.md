# Nocs NS700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.9; 25 -4.3; 28 -4.9; 31 -5.4; 34 -5.8; 37 -6.1; 41 -6.3; 45 -6.4; 49 -6.5; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.7; 79 -7.7; 87 -7.4; 96 -5.7; 106 -5.9; 116 -6.9; 128 -7.2; 141 -7.0; 155 -6.5; 170 -5.8; 187 -5.3; 206 -4.3; 227 -3.3; 249 -2.2; 274 -1.2; 302 -2.0; 332 -6.3; 365 -6.1; 402 -5.5; 442 -5.3; 486 -5.2; 535 -5.0; 588 -4.8; 647 -4.6; 712 -4.6; 783 -4.6; 861 -4.5; 947 -4.5; 1042 -4.4; 1146 -4.4; 1261 -4.4; 1387 -4.3; 1526 -4.9; 1678 -3.9; 1846 -3.7; 2031 -3.6; 2234 -3.7; 2457 -4.0; 2703 -4.6; 2973 -5.8; 3270 -5.7; 3597 -5.6; 3957 -3.0; 4353 -0.5; 4788 -1.7; 5267 -4.2; 5793 -2.2; 6373 -2.9; 7010 -9.3; 7711 -6.8; 8482 -4.4; 9330 -4.4; 10263 -4.4; 11289 -4.4; 12418 -4.4; 13660 -4.4; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 89 Hz   |  0.47 | -2.8 dB |
| Peaking | 284 Hz  |  2.46 | 6.9 dB  |
| Peaking | 339 Hz  |  2.97 | -5.0 dB |
| Peaking | 4502 Hz |  6.49 | 4.7 dB  |
| Peaking | 7138 Hz |  9.41 | -5.5 dB |
| Peaking | 20 Hz   |  2.41 | 1.8 dB  |
| Peaking | 144 Hz  |  6.36 | -0.6 dB |
| Peaking | 2120 Hz |  2.64 | 1.1 dB  |
| Peaking | 3195 Hz |  4.02 | -2.1 dB |
| Peaking | 6050 Hz | 11.42 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)