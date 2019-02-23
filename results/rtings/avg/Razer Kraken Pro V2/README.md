# Razer Kraken Pro V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -1.4; 31 -2.3; 34 -3.1; 37 -3.8; 41 -4.8; 45 -5.7; 49 -6.6; 54 -7.6; 60 -8.6; 66 -9.5; 72 -10.1; 79 -10.7; 87 -11.2; 96 -11.5; 106 -11.8; 116 -12.0; 128 -12.2; 141 -12.2; 155 -12.2; 170 -12.1; 187 -11.8; 206 -11.4; 227 -10.9; 249 -10.0; 274 -9.4; 302 -11.9; 332 -12.0; 365 -11.1; 402 -10.3; 442 -9.7; 486 -9.5; 535 -9.4; 588 -8.6; 647 -8.4; 712 -7.3; 783 -7.0; 861 -7.4; 947 -6.5; 1042 -5.4; 1146 -4.0; 1261 -2.7; 1387 -2.0; 1526 -2.5; 1678 -2.3; 1846 -2.4; 2031 -3.3; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.4; 3597 -2.7; 3957 -2.0; 4353 -0.5; 4788 -0.9; 5267 -1.1; 5793 -2.1; 6373 -1.6; 7010 -4.0; 7711 -6.3; 8482 -9.7; 9330 -10.4; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.9; 16529 -6.8; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken Pro V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken Pro V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.75 | 6.9 dB  |
| Peaking | 111 Hz  | 0.55 | -5.9 dB |
| Peaking | 411 Hz  | 0.84 | -3.2 dB |
| Peaking | 2207 Hz | 0.71 | 5.3 dB  |
| Peaking | 4999 Hz | 2.33 | 4.2 dB  |
| Peaking | 1337 Hz | 5.89 | 1.8 dB  |
| Peaking | 2065 Hz | 4.95 | -2.4 dB |
| Peaking | 2685 Hz | 3.08 | 1.4 dB  |
| Peaking | 6556 Hz | 6.65 | 2.9 dB  |
| Peaking | 8954 Hz | 3.82 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20Pro%20V2/Razer%20Kraken%20Pro%20V2.png)