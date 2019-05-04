# Jaybird Freedom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.3; 25 -8.3; 28 -8.3; 31 -8.3; 34 -8.3; 37 -8.3; 41 -8.3; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.3; 66 -8.4; 72 -8.5; 79 -8.5; 87 -8.6; 96 -8.6; 106 -8.6; 116 -8.6; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.7; 187 -7.3; 206 -6.9; 227 -6.8; 249 -7.2; 274 -7.1; 302 -6.5; 332 -6.0; 365 -5.4; 402 -4.9; 442 -4.5; 486 -4.0; 535 -3.4; 588 -2.9; 647 -2.3; 712 -1.7; 783 -1.3; 861 -1.3; 947 -1.7; 1042 -2.4; 1146 -3.5; 1261 -4.5; 1387 -5.3; 1526 -5.7; 1678 -6.1; 1846 -6.5; 2031 -7.1; 2234 -7.8; 2457 -8.3; 2703 -8.6; 2973 -7.2; 3270 -5.1; 3597 -3.5; 3957 -2.5; 4353 -1.8; 4788 -1.6; 5267 -0.9; 5793 -0.5; 6373 -1.4; 7010 -5.2; 7711 -8.7; 8482 -7.1; 9330 -5.1; 10263 -5.1; 11289 -8.0; 12418 -8.5; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 0.21 | -3.6 dB  |
| Peaking | 770 Hz   | 1.26 | 4.4 dB   |
| Peaking | 2457 Hz  | 1.53 | -5.3 dB  |
| Peaking | 6159 Hz  | 0.99 | 16.7 dB  |
| Peaking | 7267 Hz  | 1.04 | -14.9 dB |
| Peaking | 1189 Hz  | 1.95 | 0.9 dB   |
| Peaking | 1341 Hz  | 2.99 | -1.5 dB  |
| Peaking | 7864 Hz  | 5.44 | -2.8 dB  |
| Peaking | 9425 Hz  | 1.83 | 2.7 dB   |
| Peaking | 11891 Hz | 4.7  | -4.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom/Jaybird%20Freedom.png)