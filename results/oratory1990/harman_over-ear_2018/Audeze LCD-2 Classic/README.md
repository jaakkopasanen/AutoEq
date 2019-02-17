# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.7; 41 -0.8; 45 -0.9; 49 -0.9; 54 -1.2; 60 -1.4; 66 -1.9; 72 -2.1; 79 -2.3; 87 -2.7; 96 -3.1; 106 -3.5; 116 -3.8; 128 -4.1; 141 -4.4; 155 -4.7; 170 -4.9; 187 -5.2; 206 -5.4; 227 -5.5; 249 -5.6; 274 -5.6; 302 -5.7; 332 -5.6; 365 -5.5; 402 -5.2; 442 -4.8; 486 -4.7; 535 -4.9; 588 -5.4; 647 -6.0; 712 -6.7; 783 -7.2; 861 -7.2; 947 -6.5; 1042 -6.8; 1146 -6.7; 1261 -6.4; 1387 -5.7; 1526 -4.5; 1678 -3.8; 1846 -2.9; 2031 -1.4; 2234 -2.3; 2457 -3.8; 2703 -3.1; 2973 -1.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.7; 6373 -4.2; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -10.9; 13660 -11.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -12.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.31 | 6.1 dB  |
| Peaking | 475 Hz   |  3.73 | 1.7 dB  |
| Peaking | 2005 Hz  |  3.94 | 3.6 dB  |
| Peaking | 4067 Hz  |  1.23 | 6.7 dB  |
| Peaking | 13123 Hz |  4.37 | -7.1 dB |
| Peaking | 985 Hz   |  1.63 | -1.0 dB |
| Peaking | 1587 Hz  |  5.81 | 0.9 dB  |
| Peaking | 5325 Hz  | 11.76 | 2.0 dB  |
| Peaking | 8271 Hz  |  3.6  | -1.1 dB |
| Peaking | 11416 Hz |  9.22 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 1.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)