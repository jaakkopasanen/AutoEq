# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.5; 25 -11.5; 28 -11.5; 31 -11.6; 34 -11.6; 37 -11.7; 41 -11.8; 45 -11.9; 49 -12.1; 54 -12.3; 60 -12.5; 66 -12.6; 72 -12.9; 79 -13.0; 87 -13.2; 96 -13.4; 106 -13.4; 116 -13.4; 128 -13.5; 141 -13.5; 155 -13.4; 170 -13.2; 187 -13.0; 206 -12.8; 227 -12.3; 249 -12.0; 274 -11.4; 302 -10.9; 332 -10.3; 365 -9.6; 402 -9.1; 442 -8.5; 486 -7.9; 535 -7.3; 588 -6.7; 647 -6.2; 712 -5.8; 783 -5.5; 861 -5.5; 947 -5.7; 1042 -6.2; 1146 -6.4; 1261 -6.9; 1387 -8.4; 1526 -9.5; 1678 -10.3; 1846 -11.1; 2031 -11.5; 2234 -11.6; 2457 -10.3; 2703 -7.9; 2973 -5.0; 3270 -2.5; 3597 -1.5; 3957 -3.7; 4353 -8.7; 4788 -13.4; 5267 -8.2; 5793 -1.8; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.1; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.27 | -5.3 dB  |
| Peaking | 134 Hz   | 0.76 | -4.5 dB  |
| Peaking | 263 Hz   | 1.34 | -2.9 dB  |
| Peaking | 1978 Hz  | 2.72 | -6.3 dB  |
| Peaking | 22050 Hz | 2.6  | -3.0 dB  |
| Peaking | 802 Hz   | 3.23 | 1.4 dB   |
| Peaking | 2466 Hz  | 4.41 | -2.9 dB  |
| Peaking | 3573 Hz  | 2.74 | 6.7 dB   |
| Peaking | 4802 Hz  | 4.06 | -10.6 dB |
| Peaking | 6077 Hz  | 4    | 7.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE215/Shure%20SE215.png)