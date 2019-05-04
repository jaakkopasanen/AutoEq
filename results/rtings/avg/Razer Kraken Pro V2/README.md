# Razer Kraken Pro V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.1; 34 -2.9; 37 -3.6; 41 -4.6; 45 -5.5; 49 -6.4; 54 -7.4; 60 -8.5; 66 -9.3; 72 -9.9; 79 -10.4; 87 -10.9; 96 -11.3; 106 -11.6; 116 -11.8; 128 -11.9; 141 -12.0; 155 -12.0; 170 -11.9; 187 -11.6; 206 -11.3; 227 -10.8; 249 -9.9; 274 -9.5; 302 -11.9; 332 -12.0; 365 -11.0; 402 -10.3; 442 -9.7; 486 -9.6; 535 -9.4; 588 -8.7; 647 -8.5; 712 -7.4; 783 -7.1; 861 -7.5; 947 -6.6; 1042 -5.5; 1146 -4.1; 1261 -2.8; 1387 -2.2; 1526 -2.7; 1678 -2.5; 1846 -2.8; 2031 -3.8; 2234 -2.7; 2457 -1.2; 2703 -0.6; 2973 -0.5; 3270 -1.0; 3597 -2.5; 3957 -1.5; 4353 -0.5; 4788 -1.3; 5267 -1.6; 5793 -2.0; 6373 -1.1; 7010 -4.0; 7711 -6.7; 8482 -9.4; 9330 -8.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.75 | 6.9 dB  |
| Peaking | 109 Hz   | 0.56 | -5.6 dB |
| Peaking | 423 Hz   | 0.73 | -3.3 dB |
| Peaking | 2140 Hz  | 0.63 | 4.8 dB  |
| Peaking | 4858 Hz  | 1.85 | 4.0 dB  |
| Peaking | 1330 Hz  | 6.22 | 1.7 dB  |
| Peaking | 2043 Hz  | 8.3  | -2.3 dB |
| Peaking | 6482 Hz  | 5.93 | 3.5 dB  |
| Peaking | 8701 Hz  | 2.95 | -4.4 dB |
| Peaking | 10310 Hz | 3.73 | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)