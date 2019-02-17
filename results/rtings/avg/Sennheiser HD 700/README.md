# Sennheiser HD 700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.6; 34 -2.9; 37 -3.2; 41 -3.6; 45 -4.0; 49 -4.4; 54 -4.8; 60 -5.4; 66 -6.0; 72 -6.5; 79 -7.0; 87 -7.6; 96 -8.1; 106 -8.6; 116 -9.1; 128 -9.5; 141 -9.8; 155 -10.0; 170 -10.1; 187 -10.0; 206 -9.8; 227 -9.7; 249 -9.6; 274 -9.5; 302 -9.4; 332 -9.3; 365 -9.2; 402 -9.0; 442 -8.9; 486 -8.7; 535 -8.6; 588 -8.3; 647 -8.0; 712 -7.6; 783 -7.1; 861 -6.7; 947 -6.4; 1042 -6.0; 1146 -5.5; 1261 -4.8; 1387 -4.3; 1526 -3.8; 1678 -3.5; 1846 -3.1; 2031 -3.4; 2234 -2.7; 2457 -3.0; 2703 -3.1; 2973 -3.9; 3270 -3.9; 3597 -4.2; 3957 -5.5; 4353 -6.2; 4788 -7.1; 5267 -10.1; 5793 -12.4; 6373 -16.6; 7010 -11.5; 7711 -9.3; 8482 -9.1; 9330 -6.4; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -9.1; 18182 -14.7; 20000 -17.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.89 | 1.1 dB   |
| Peaking | 20 Hz   | 0.31 | 5.4 dB   |
| Peaking | 178 Hz  | 0.31 | -4.3 dB  |
| Peaking | 2241 Hz | 0.74 | 3.9 dB   |
| Peaking | 6315 Hz | 3.03 | -10.5 dB |
| Peaking | 154 Hz  | 2.6  | -0.5 dB  |
| Peaking | 261 Hz  | 2.19 | 0.5 dB   |
| Peaking | 5236 Hz | 4.1  | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)