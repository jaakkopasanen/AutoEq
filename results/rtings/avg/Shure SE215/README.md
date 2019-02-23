# Shure SE215
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.0; 25 -1.1; 28 -1.3; 31 -1.4; 34 -1.5; 37 -1.7; 41 -1.8; 45 -2.0; 49 -2.2; 54 -2.5; 60 -3.1; 66 -3.7; 72 -4.1; 79 -4.7; 87 -5.4; 96 -6.1; 106 -6.8; 116 -7.6; 128 -8.3; 141 -8.9; 155 -9.3; 170 -9.6; 187 -9.8; 206 -9.9; 227 -9.9; 249 -9.7; 274 -9.6; 302 -9.4; 332 -9.0; 365 -8.6; 402 -8.2; 442 -7.6; 486 -7.1; 535 -6.4; 588 -5.8; 647 -5.0; 712 -4.3; 783 -3.6; 861 -3.3; 947 -3.4; 1042 -4.1; 1146 -5.3; 1261 -5.6; 1387 -6.1; 1526 -6.4; 1678 -6.9; 1846 -7.5; 2031 -8.0; 2234 -7.3; 2457 -5.7; 2703 -4.0; 2973 -2.9; 3270 -2.8; 3597 -3.7; 3957 -5.5; 4353 -8.8; 4788 -11.5; 5267 -7.9; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -7.8; 11289 -7.7; 12418 -6.2; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE215 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.44 | 5.1 dB  |
| Peaking | 193 Hz   | 0.89 | -4.9 dB |
| Peaking | 3294 Hz  | 3.34 | 4.1 dB  |
| Peaking | 4830 Hz  | 3.91 | -7.3 dB |
| Peaking | 6155 Hz  | 4.41 | 7.4 dB  |
| Peaking | 372 Hz   | 2.17 | -1.2 dB |
| Peaking | 851 Hz   | 1.87 | 3.3 dB  |
| Peaking | 2032 Hz  | 2.16 | -2.6 dB |
| Peaking | 2722 Hz  | 4.58 | 1.8 dB  |
| Peaking | 10771 Hz | 4.24 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Shure%20SE215/Shure%20SE215.png)