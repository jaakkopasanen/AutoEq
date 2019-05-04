# Jaybird X2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -5.9; 25 -5.9; 28 -5.9; 31 -6.0; 34 -6.0; 37 -6.0; 41 -6.1; 45 -6.1; 49 -6.2; 54 -6.2; 60 -6.3; 66 -6.5; 72 -6.6; 79 -6.8; 87 -7.0; 96 -7.1; 106 -7.2; 116 -7.3; 128 -7.3; 141 -7.2; 155 -7.1; 170 -7.1; 187 -6.9; 206 -6.7; 227 -6.3; 249 -6.1; 274 -5.8; 302 -5.4; 332 -4.9; 365 -4.5; 402 -4.0; 442 -3.5; 486 -3.0; 535 -2.4; 588 -1.9; 647 -1.3; 712 -1.0; 783 -1.1; 861 -1.6; 947 -2.5; 1042 -3.3; 1146 -4.0; 1261 -4.4; 1387 -4.4; 1526 -4.5; 1678 -4.7; 1846 -4.7; 2031 -4.7; 2234 -4.5; 2457 -4.2; 2703 -3.9; 2973 -3.5; 3270 -3.1; 3597 -2.9; 3957 -3.0; 4353 -3.0; 4788 -3.0; 5267 -2.1; 5793 -1.0; 6373 -0.5; 7010 -2.3; 7711 -6.4; 8482 -7.8; 9330 -6.8; 10263 -9.2; 11289 -13.4; 12418 -12.2; 13660 -7.0; 15026 -5.2; 16529 -9.0; 18182 -13.7; 20000 -13.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 0.37 | -3.0 dB  |
| Peaking | 671 Hz   | 1.52 | 3.9 dB   |
| Peaking | 5998 Hz  | 2.94 | 4.5 dB   |
| Peaking | 11421 Hz | 2.54 | -9.1 dB  |
| Peaking | 19126 Hz | 1.01 | -11.3 dB |
| Peaking | 19 Hz    | 1.93 | -1.0 dB  |
| Peaking | 3595 Hz  | 3.54 | 1.3 dB   |
| Peaking | 8135 Hz  | 8.22 | -3.1 dB  |
| Peaking | 14863 Hz | 3.92 | 2.9 dB   |
| Peaking | 17471 Hz | 3.44 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X2/Jaybird%20X2.png)