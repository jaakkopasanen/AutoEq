# Cowin E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.3; 25 -2.6; 28 -3.2; 31 -3.7; 34 -4.2; 37 -4.7; 41 -5.4; 45 -6.1; 49 -6.7; 54 -7.3; 60 -8.0; 66 -8.6; 72 -9.2; 79 -9.7; 87 -10.3; 96 -10.8; 106 -11.3; 116 -11.7; 128 -11.9; 141 -12.0; 155 -11.9; 170 -11.7; 187 -11.3; 206 -10.8; 227 -10.3; 249 -10.0; 274 -9.0; 302 -8.7; 332 -8.5; 365 -8.3; 402 -8.2; 442 -8.2; 486 -8.2; 535 -8.4; 588 -8.6; 647 -9.0; 712 -9.0; 783 -6.3; 861 -3.7; 947 -7.5; 1042 -9.4; 1146 -7.5; 1261 -5.1; 1387 -3.0; 1526 -1.1; 1678 -2.1; 1846 -1.7; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -0.9; 3957 -1.3; 4353 -2.4; 4788 -5.0; 5267 -14.2; 5793 -13.9; 6373 -8.3; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.74 | 4.9 dB   |
| Peaking | 133 Hz  | 0.65 | -5.7 dB  |
| Peaking | 973 Hz  | 0.74 | -3.8 dB  |
| Peaking | 2403 Hz | 0.54 | 7.9 dB   |
| Peaking | 5535 Hz | 5.43 | -14.0 dB |
| Peaking | 710 Hz  | 3.54 | -2.2 dB  |
| Peaking | 861 Hz  | 4.53 | 6.8 dB   |
| Peaking | 1002 Hz | 3.65 | -4.7 dB  |
| Peaking | 1468 Hz | 6.37 | 2.3 dB   |
| Peaking | 4309 Hz | 6.11 | 1.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E8/Cowin%20E8.png)