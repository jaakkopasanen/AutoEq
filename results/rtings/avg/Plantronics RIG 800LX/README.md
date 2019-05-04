# Plantronics RIG 800LX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -2.1; 25 -3.1; 28 -4.1; 31 -4.9; 34 -5.3; 37 -5.5; 41 -5.6; 45 -5.5; 49 -5.2; 54 -4.9; 60 -4.5; 66 -4.2; 72 -4.1; 79 -4.0; 87 -4.0; 96 -4.0; 106 -4.0; 116 -4.0; 128 -4.0; 141 -4.0; 155 -3.8; 170 -3.5; 187 -3.1; 206 -2.5; 227 -2.1; 249 -1.7; 274 -1.4; 302 -1.5; 332 -1.5; 365 -1.5; 402 -1.5; 442 -1.6; 486 -1.8; 535 -1.7; 588 -1.7; 647 -1.8; 712 -2.1; 783 -2.5; 861 -3.0; 947 -3.4; 1042 -3.0; 1146 -2.6; 1261 -2.3; 1387 -1.1; 1526 -1.0; 1678 -1.5; 1846 -3.4; 2031 -5.1; 2234 -5.5; 2457 -5.3; 2703 -5.7; 2973 -7.1; 3270 -8.6; 3597 -9.2; 3957 -8.3; 4353 -6.8; 4788 -5.0; 5267 -3.8; 5793 -3.3; 6373 -0.5; 7010 -4.0; 7711 -5.6; 8482 -4.7; 9330 -3.5; 10263 -4.8; 11289 -6.7; 12418 -5.2; 13660 -4.9; 15026 -8.4; 16529 -9.4; 18182 -7.6; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics RIG 800LX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics RIG 800LX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.64 | 4.6 dB  |
| Peaking | 24 Hz    | 0.14 | -1.9 dB |
| Peaking | 391 Hz   | 0.36 | 2.2 dB  |
| Peaking | 3476 Hz  | 2.48 | -6.2 dB |
| Peaking | 17835 Hz | 0.58 | -5.6 dB |
| Peaking | 152 Hz   | 4.83 | -0.8 dB |
| Peaking | 948 Hz   | 3.03 | -1.4 dB |
| Peaking | 1555 Hz  | 2.88 | 2.7 dB  |
| Peaking | 2087 Hz  | 3.58 | -2.2 dB |
| Peaking | 6372 Hz  | 8.49 | 4.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -6.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20RIG%20800LX/Plantronics%20RIG%20800LX.png)