# Jaybird X4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.5; 28 -3.4; 31 -3.3; 34 -3.2; 37 -3.2; 41 -3.2; 45 -3.2; 49 -3.1; 54 -3.1; 60 -3.3; 66 -3.5; 72 -3.6; 79 -3.8; 87 -4.0; 96 -4.1; 106 -4.4; 116 -5.2; 128 -6.3; 141 -7.2; 155 -7.5; 170 -7.3; 187 -7.1; 206 -6.9; 227 -6.6; 249 -6.1; 274 -5.6; 302 -5.1; 332 -4.6; 365 -4.1; 402 -3.7; 442 -3.2; 486 -2.6; 535 -2.1; 588 -1.6; 647 -1.1; 712 -0.7; 783 -0.5; 861 -0.7; 947 -1.5; 1042 -2.8; 1146 -3.9; 1261 -4.5; 1387 -4.8; 1526 -5.1; 1678 -5.4; 1846 -5.8; 2031 -6.5; 2234 -6.9; 2457 -7.3; 2703 -7.2; 2973 -5.9; 3270 -4.3; 3597 -3.1; 3957 -2.4; 4353 -2.4; 4788 -2.2; 5267 -2.9; 5793 -5.4; 6373 -11.8; 7010 -10.6; 7711 -4.7; 8482 -4.5; 9330 -4.5; 10263 -4.8; 11289 -9.2; 12418 -10.3; 13660 -9.5; 15026 -10.1; 16529 -7.6; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 180 Hz   | 1.71 | -3.3 dB  |
| Peaking | 725 Hz   | 1.52 | 4.3 dB   |
| Peaking | 2262 Hz  | 2.53 | -3.1 dB  |
| Peaking | 13811 Hz | 1.12 | -6.0 dB  |
| Peaking | 22050 Hz | 1.81 | -4.8 dB  |
| Peaking | 32 Hz    | 1.03 | 1.2 dB   |
| Peaking | 63 Hz    | 1.68 | 1.0 dB   |
| Peaking | 4780 Hz  | 2.18 | 3.6 dB   |
| Peaking | 6619 Hz  | 5.11 | -10.3 dB |
| Peaking | 8394 Hz  | 2.38 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | -5.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X4/Jaybird%20X4.png)