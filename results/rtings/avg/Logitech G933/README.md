# Logitech G933
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.5; 25 -7.2; 28 -8.0; 31 -8.5; 34 -8.8; 37 -8.7; 41 -8.4; 45 -8.2; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.8; 72 -8.9; 79 -8.8; 87 -8.6; 96 -8.3; 106 -7.6; 116 -7.0; 128 -6.6; 141 -6.8; 155 -6.9; 170 -6.7; 187 -5.9; 206 -4.9; 227 -3.8; 249 -2.7; 274 -1.7; 302 -0.9; 332 -0.7; 365 -0.8; 402 -1.0; 442 -0.8; 486 -0.7; 535 -1.2; 588 -1.4; 647 -1.4; 712 -1.6; 783 -1.5; 861 -1.3; 947 -1.2; 1042 -1.7; 1146 -1.2; 1261 -1.3; 1387 -1.7; 1526 -2.0; 1678 -1.9; 1846 -1.4; 2031 -1.0; 2234 -0.8; 2457 -0.5; 2703 -1.7; 2973 -4.3; 3270 -5.8; 3597 -6.2; 3957 -8.1; 4353 -7.3; 4788 -4.4; 5267 -2.0; 5793 -1.5; 6373 -0.9; 7010 -2.6; 7711 -5.1; 8482 -8.7; 9330 -9.2; 10263 -5.4; 11289 -3.3; 12418 -3.4; 13660 -5.6; 15026 -5.0; 16529 -3.8; 18182 -7.6; 20000 -16.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G933 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G933 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 0.46 | -6.5 dB  |
| Peaking | 167 Hz   | 2.45 | -2.8 dB  |
| Peaking | 497 Hz   | 0.19 | 2.8 dB   |
| Peaking | 3936 Hz  | 3.61 | -5.9 dB  |
| Peaking | 20115 Hz | 0.87 | -13.0 dB |
| Peaking | 316 Hz   | 4.54 | 1.3 dB   |
| Peaking | 6358 Hz  | 2.72 | 4.0 dB   |
| Peaking | 9064 Hz  | 2.29 | -7.5 dB  |
| Peaking | 10900 Hz | 3.53 | 3.2 dB   |
| Peaking | 16859 Hz | 3.51 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G933/Logitech%20G933.png)