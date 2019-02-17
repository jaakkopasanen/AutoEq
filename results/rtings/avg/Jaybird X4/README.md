# Jaybird X4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.5; 28 -3.4; 31 -3.3; 34 -3.2; 37 -3.2; 41 -3.2; 45 -3.2; 49 -3.1; 54 -3.1; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.8; 87 -4.0; 96 -4.1; 106 -4.4; 116 -5.2; 128 -6.3; 141 -7.2; 155 -7.5; 170 -7.3; 187 -7.1; 206 -6.9; 227 -6.6; 249 -6.1; 274 -5.6; 302 -5.1; 332 -4.6; 365 -4.1; 402 -3.7; 442 -3.2; 486 -2.6; 535 -2.1; 588 -1.6; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.5; 1042 -2.8; 1146 -3.9; 1261 -4.5; 1387 -4.8; 1526 -5.1; 1678 -5.4; 1846 -5.8; 2031 -6.5; 2234 -6.9; 2457 -7.3; 2703 -7.2; 2973 -5.9; 3270 -4.3; 3597 -3.1; 3957 -2.4; 4353 -2.4; 4788 -2.2; 5267 -2.9; 5793 -5.4; 6373 -11.8; 7010 -10.6; 7711 -3.8; 8482 -2.2; 9330 -2.2; 10263 -4.4; 11289 -9.2; 12418 -10.3; 13660 -9.5; 15026 -10.1; 16529 -7.6; 18182 -2.6; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 173 Hz   | 0.91 | -5.0 dB  |
| Peaking | 766 Hz   | 1.21 | 5.5 dB   |
| Peaking | 1645 Hz  | 0.31 | -4.3 dB  |
| Peaking | 12061 Hz | 3.53 | -5.9 dB  |
| Peaking | 15071 Hz | 1.54 | -7.6 dB  |
| Peaking | 23 Hz    | 1.09 | -1.3 dB  |
| Peaking | 2582 Hz  | 2.51 | -2.9 dB  |
| Peaking | 4559 Hz  | 1.13 | 4.1 dB   |
| Peaking | 6649 Hz  | 4.23 | -12.3 dB |
| Peaking | 8385 Hz  | 2.93 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X4/Jaybird%20X4.png)