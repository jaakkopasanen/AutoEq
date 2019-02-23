# Cowin E7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -9.9; 25 -9.5; 28 -8.9; 31 -8.6; 34 -8.3; 37 -8.0; 41 -7.8; 45 -7.7; 49 -7.8; 54 -7.8; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.4; 96 -9.8; 106 -10.2; 116 -10.6; 128 -11.0; 141 -11.4; 155 -11.7; 170 -12.0; 187 -12.2; 206 -12.3; 227 -12.5; 249 -12.6; 274 -12.5; 302 -12.8; 332 -12.9; 365 -12.6; 402 -12.5; 442 -12.3; 486 -12.0; 535 -11.7; 588 -11.4; 647 -11.2; 712 -11.1; 783 -10.7; 861 -9.2; 947 -8.7; 1042 -9.6; 1146 -9.1; 1261 -7.0; 1387 -5.0; 1526 -3.1; 1678 -1.3; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -5.4; 5267 -4.9; 5793 -3.8; 6373 -5.1; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -10.5; 13660 -11.0; 15026 -7.0; 16529 -6.5; 18182 -10.1; 20000 -14.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.74 | -3.7 dB |
| Peaking | 380 Hz   | 0.28 | -6.9 dB |
| Peaking | 1131 Hz  | 3.71 | -3.3 dB |
| Peaking | 2195 Hz  | 0.63 | 8.7 dB  |
| Peaking | 20992 Hz | 0.1  | -4.4 dB |
| Peaking | 4086 Hz  | 4.5  | 2.7 dB  |
| Peaking | 4752 Hz  | 5.71 | -2.8 dB |
| Peaking | 11262 Hz | 3.65 | 2.5 dB  |
| Peaking | 12976 Hz | 2.88 | -4.6 dB |
| Peaking | 16071 Hz | 2.09 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -4.7 dB |
| Peaking | 1000 Hz  | 1.41 | -3.4 dB |
| Peaking | 2000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7/Cowin%20E7.png)