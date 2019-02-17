# Sleek SA1- Normal Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.1; 34 -12.2; 37 -12.2; 41 -12.3; 45 -12.4; 49 -12.6; 54 -12.8; 60 -13.1; 66 -13.4; 72 -13.7; 79 -14.0; 87 -14.3; 96 -14.4; 106 -14.7; 116 -14.7; 128 -15.0; 141 -15.0; 155 -15.1; 170 -15.0; 187 -15.0; 206 -14.7; 227 -14.5; 249 -14.2; 274 -13.8; 302 -13.3; 332 -12.7; 365 -12.1; 402 -11.4; 442 -10.9; 486 -10.4; 535 -9.7; 588 -9.0; 647 -8.3; 712 -7.6; 783 -7.1; 861 -6.7; 947 -6.6; 1042 -6.4; 1146 -6.3; 1261 -6.3; 1387 -6.2; 1526 -6.2; 1678 -6.0; 1846 -5.3; 2031 -4.6; 2234 -3.8; 2457 -3.0; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.9; 4353 -4.9; 4788 -7.4; 5267 -9.6; 5793 -8.7; 6373 -4.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sleek SA1- Normal Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA1- Normal Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.18 | -5.0 dB |
| Peaking | 141 Hz  | 0.63 | -4.5 dB |
| Peaking | 297 Hz  | 0.85 | -3.8 dB |
| Peaking | 3392 Hz | 1.25 | 6.6 dB  |
| Peaking | 5146 Hz | 4.12 | -6.2 dB |
| Peaking | 520 Hz  | 2.44 | -0.9 dB |
| Peaking | 1353 Hz | 0.55 | 1.5 dB  |
| Peaking | 1579 Hz | 1.22 | -1.9 dB |
| Peaking | 6522 Hz | 1.98 | -2.4 dB |
| Peaking | 6618 Hz | 5.72 | 5.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -6.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA1-%20Normal%20Filter/Sleek%20SA1-%20Normal%20Filter.png)