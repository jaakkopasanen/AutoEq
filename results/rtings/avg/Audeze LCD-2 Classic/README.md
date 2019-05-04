# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -1.8; 25 -2.0; 28 -2.3; 31 -2.8; 34 -3.2; 37 -3.6; 41 -3.9; 45 -4.0; 49 -4.1; 54 -4.1; 60 -4.3; 66 -4.4; 72 -4.6; 79 -4.9; 87 -5.2; 96 -5.6; 106 -5.9; 116 -6.3; 128 -6.6; 141 -7.0; 155 -7.2; 170 -7.4; 187 -7.5; 206 -7.6; 227 -7.7; 249 -7.8; 274 -8.0; 302 -8.1; 332 -8.2; 365 -8.3; 402 -8.5; 442 -8.4; 486 -8.2; 535 -8.2; 588 -8.7; 647 -9.3; 712 -9.7; 783 -10.1; 861 -10.4; 947 -9.2; 1042 -8.6; 1146 -8.8; 1261 -8.6; 1387 -8.1; 1526 -6.8; 1678 -7.1; 1846 -7.2; 2031 -7.2; 2234 -6.1; 2457 -6.4; 2703 -4.7; 2973 -3.8; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -1.3; 4788 -3.1; 5267 -3.2; 5793 -5.3; 6373 -6.3; 7010 -6.3; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.0; 15026 -7.1; 16529 -9.0; 18182 -10.6; 20000 -11.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  0.76 | 4.8 dB  |
| Peaking | 68 Hz    |  0.96 | 1.6 dB  |
| Peaking | 235 Hz   |  0.57 | -1.3 dB |
| Peaking | 852 Hz   |  0.99 | -3.1 dB |
| Peaking | 3823 Hz  |  2.1  | 6.8 dB  |
| Peaking | 858 Hz   |  6.08 | -0.8 dB |
| Peaking | 989 Hz   |  7.25 | 1.0 dB  |
| Peaking | 1972 Hz  |  7.04 | -0.8 dB |
| Peaking | 5238 Hz  | 11.86 | 1.4 dB  |
| Peaking | 19412 Hz |  0.75 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)