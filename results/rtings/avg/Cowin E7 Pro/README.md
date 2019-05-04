# Cowin E7 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.9; 41 -3.8; 45 -5.3; 49 -6.4; 54 -7.4; 60 -8.5; 66 -9.6; 72 -9.8; 79 -8.9; 87 -8.0; 96 -7.5; 106 -7.3; 116 -7.2; 128 -7.2; 141 -7.1; 155 -6.9; 170 -6.7; 187 -6.4; 206 -6.0; 227 -5.7; 249 -5.3; 274 -4.9; 302 -4.3; 332 -3.0; 365 -1.6; 402 -0.5; 442 -1.5; 486 -2.9; 535 -3.6; 588 -3.5; 647 -3.3; 712 -3.7; 783 -4.0; 861 -4.9; 947 -6.4; 1042 -8.0; 1146 -9.7; 1261 -11.9; 1387 -13.4; 1526 -14.1; 1678 -13.5; 1846 -11.5; 2031 -9.8; 2234 -7.9; 2457 -5.5; 2703 -3.2; 2973 -1.8; 3270 -1.5; 3597 -2.1; 3957 -3.4; 4353 -5.5; 4788 -8.0; 5267 -9.2; 5793 -7.2; 6373 -7.7; 7010 -10.6; 7711 -10.8; 8482 -10.5; 9330 -10.6; 10263 -11.1; 11289 -10.4; 12418 -8.3; 13660 -9.4; 15026 -14.0; 16529 -14.4; 18182 -11.7; 20000 -14.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 2.19 | 7.3 dB  |
| Peaking | 472 Hz   | 1.09 | 5.2 dB  |
| Peaking | 1544 Hz  | 1.9  | -9.0 dB |
| Peaking | 3214 Hz  | 1.94 | 7.6 dB  |
| Peaking | 20046 Hz | 0.07 | -5.8 dB |
| Peaking | 38 Hz    | 2.13 | 3.3 dB  |
| Peaking | 67 Hz    | 1.16 | -3.6 dB |
| Peaking | 386 Hz   | 7.94 | 2.0 dB  |
| Peaking | 12949 Hz | 3.64 | 4.4 dB  |
| Peaking | 15733 Hz | 2.53 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.7 dB  |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 5.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)