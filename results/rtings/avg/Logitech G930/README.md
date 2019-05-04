# Logitech G930
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.4; 25 -6.9; 28 -7.5; 31 -7.9; 34 -8.1; 37 -8.1; 41 -8.0; 45 -7.9; 49 -7.7; 54 -7.5; 60 -7.2; 66 -7.1; 72 -7.2; 79 -7.6; 87 -8.1; 96 -8.6; 106 -9.1; 116 -9.3; 128 -9.2; 141 -9.1; 155 -8.6; 170 -7.8; 187 -6.8; 206 -5.4; 227 -3.5; 249 -1.6; 274 -0.6; 302 -2.5; 332 -5.2; 365 -7.0; 402 -8.2; 442 -8.8; 486 -9.4; 535 -9.8; 588 -10.0; 647 -10.0; 712 -9.9; 783 -9.8; 861 -9.6; 947 -9.3; 1042 -9.0; 1146 -8.3; 1261 -7.4; 1387 -6.7; 1526 -7.4; 1678 -7.7; 1846 -7.7; 2031 -7.5; 2234 -7.0; 2457 -5.9; 2703 -4.2; 2973 -2.2; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -8.5; 4788 -11.2; 5267 -9.0; 5793 -8.3; 6373 -10.9; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.2; 13660 -7.6; 15026 -7.1; 16529 -7.4; 18182 -9.6; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Logitech G930 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Logitech G930 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 126 Hz   |  1.23 | -2.0 dB  |
| Peaking | 269 Hz   |  1.85 | 10.6 dB  |
| Peaking | 415 Hz   |  0.4  | -4.9 dB  |
| Peaking | 3784 Hz  |  2.08 | 13.1 dB  |
| Peaking | 4631 Hz  |  2.12 | -11.0 dB |
| Peaking | 36 Hz    |  2.61 | -1.4 dB  |
| Peaking | 2159 Hz  |  2.07 | -4.4 dB  |
| Peaking | 2314 Hz  |  1.15 | 3.2 dB   |
| Peaking | 3640 Hz  | 10.16 | -1.9 dB  |
| Peaking | 19761 Hz |  0.86 | -5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | 6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -4.1 dB |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Logitech%20G930/Logitech%20G930.png)