# Cowin E8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.8; 34 -1.2; 37 -1.7; 41 -2.4; 45 -3.1; 49 -3.7; 54 -4.3; 60 -4.9; 66 -5.6; 72 -6.2; 79 -6.7; 87 -7.3; 96 -7.8; 106 -8.3; 116 -8.6; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.7; 187 -8.3; 206 -7.8; 227 -7.3; 249 -6.9; 274 -5.9; 302 -5.6; 332 -5.5; 365 -5.3; 402 -5.2; 442 -5.2; 486 -5.2; 535 -5.3; 588 -5.6; 647 -6.0; 712 -6.0; 783 -3.3; 861 -0.7; 947 -4.5; 1042 -6.4; 1146 -4.5; 1261 -2.1; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.0; 5267 -11.2; 5793 -10.9; 6373 -5.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.76 | 6.4 dB   |
| Peaking | 130 Hz  | 1.26 | -3.2 dB  |
| Peaking | 2043 Hz | 0.63 | 5.9 dB   |
| Peaking | 4588 Hz | 1.89 | 5.3 dB   |
| Peaking | 5453 Hz | 5.97 | -12.7 dB |
| Peaking | 425 Hz  | 1.5  | 1.5 dB   |
| Peaking | 793 Hz  | 1.61 | -3.3 dB  |
| Peaking | 856 Hz  | 4.81 | 7.6 dB   |
| Peaking | 1024 Hz | 4.33 | -3.7 dB  |
| Peaking | 1374 Hz | 4.02 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E8/Cowin%20E8.png)