# Cowin E7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -9.8; 25 -9.3; 28 -8.8; 31 -8.4; 34 -8.1; 37 -7.9; 41 -7.7; 45 -7.6; 49 -7.6; 54 -7.7; 60 -7.9; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.2; 96 -9.6; 106 -10.0; 116 -10.4; 128 -10.8; 141 -11.2; 155 -11.5; 170 -11.8; 187 -12.0; 206 -12.2; 227 -12.4; 249 -12.5; 274 -12.4; 302 -12.8; 332 -12.8; 365 -12.6; 402 -12.4; 442 -12.3; 486 -12.1; 535 -11.8; 588 -11.5; 647 -11.3; 712 -11.2; 783 -10.8; 861 -9.3; 947 -8.8; 1042 -9.7; 1146 -9.3; 1261 -7.1; 1387 -5.1; 1526 -3.4; 1678 -1.6; 1846 -0.6; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -5.7; 5267 -5.4; 5793 -3.7; 6373 -4.3; 7010 -6.7; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -10.8; 13660 -10.1; 15026 -6.7; 16529 -6.5; 18182 -10.1; 20000 -14.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.83 | -3.6 dB |
| Peaking | 394 Hz   | 0.29 | -6.9 dB |
| Peaking | 1128 Hz  | 3.65 | -3.2 dB |
| Peaking | 2227 Hz  | 0.64 | 8.7 dB  |
| Peaking | 21137 Hz | 0.12 | -4.3 dB |
| Peaking | 2523 Hz  | 4.38 | -1.0 dB |
| Peaking | 4171 Hz  | 3.16 | 2.9 dB  |
| Peaking | 4790 Hz  | 5.4  | -4.1 dB |
| Peaking | 12924 Hz | 4.37 | -4.4 dB |
| Peaking | 16122 Hz | 2.3  | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.7 dB |
| Peaking | 1000 Hz  | 1.41 | -3.6 dB |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7/Cowin%20E7.png)