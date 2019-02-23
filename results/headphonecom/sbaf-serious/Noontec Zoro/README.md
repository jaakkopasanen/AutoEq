# Noontec Zoro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.7; 25 -9.0; 28 -9.3; 31 -9.5; 34 -9.7; 37 -9.9; 41 -10.0; 45 -10.2; 49 -10.3; 54 -10.4; 60 -10.7; 66 -11.0; 72 -11.1; 79 -11.4; 87 -11.4; 96 -11.8; 106 -11.9; 116 -11.9; 128 -12.0; 141 -12.2; 155 -12.6; 170 -12.3; 187 -12.5; 206 -12.6; 227 -12.3; 249 -12.1; 274 -11.7; 302 -11.2; 332 -11.3; 365 -11.1; 402 -10.7; 442 -10.6; 486 -10.5; 535 -10.4; 588 -9.9; 647 -9.3; 712 -8.7; 783 -8.1; 861 -7.6; 947 -7.3; 1042 -7.3; 1146 -7.4; 1261 -7.4; 1387 -8.3; 1526 -8.9; 1678 -8.8; 1846 -7.6; 2031 -5.8; 2234 -3.7; 2457 -1.3; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.4; 6373 -2.9; 7010 -4.4; 7711 -8.3; 8482 -11.8; 9330 -11.8; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.25 | -2.7 dB |
| Peaking | 309 Hz   | 0.27 | -4.6 dB |
| Peaking | 1673 Hz  | 1.79 | -7.1 dB |
| Peaking | 3195 Hz  | 0.39 | 8.1 dB  |
| Peaking | 8803 Hz  | 2.54 | -9.9 dB |
| Peaking | 200 Hz   | 5.51 | -0.3 dB |
| Peaking | 2604 Hz  | 6.61 | 1.4 dB  |
| Peaking | 3681 Hz  | 1.4  | -0.7 dB |
| Peaking | 5477 Hz  | 4.33 | 1.2 dB  |
| Peaking | 14576 Hz | 1.87 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-9.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 9.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)