# Audeze LCD-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -1.7; 25 -1.7; 28 -1.8; 31 -1.9; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.7; 49 -2.9; 54 -3.1; 60 -3.2; 66 -3.4; 72 -3.6; 79 -3.9; 87 -4.2; 96 -4.6; 106 -5.0; 116 -5.3; 128 -5.7; 141 -6.0; 155 -6.3; 170 -6.5; 187 -6.7; 206 -6.8; 227 -6.9; 249 -7.0; 274 -6.8; 302 -6.7; 332 -6.4; 365 -6.0; 402 -5.9; 442 -6.2; 486 -6.5; 535 -6.6; 588 -6.8; 647 -6.7; 712 -6.5; 783 -6.0; 861 -6.5; 947 -6.6; 1042 -6.4; 1146 -5.6; 1261 -4.8; 1387 -5.3; 1526 -5.5; 1678 -4.0; 1846 -3.2; 2031 -2.6; 2234 -2.5; 2457 -4.1; 2703 -4.2; 2973 -4.0; 3270 -2.5; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.4; 5793 -5.4; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -8.2; 13660 -7.8; 15026 -8.3; 16529 -11.0; 18182 -13.2; 20000 -14.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.24 | 4.8 dB  |
| Peaking | 189 Hz   |  1.24 | -1.1 dB |
| Peaking | 1736 Hz  |  2.43 | 0.7 dB  |
| Peaking | 2053 Hz  |  2.99 | 3.0 dB  |
| Peaking | 4170 Hz  |  1.86 | 6.5 dB  |
| Peaking | 395 Hz   |  3.09 | 1.5 dB  |
| Peaking | 420 Hz   |  1.37 | -0.8 dB |
| Peaking | 6744 Hz  | 10.37 | 3.0 dB  |
| Peaking | 14615 Hz |  3.45 | 1.4 dB  |
| Peaking | 19562 Hz |  0.49 | -8.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2/Audeze%20LCD-2.png)