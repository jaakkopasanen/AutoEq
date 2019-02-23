# Jaybird Tarah
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.1; 25 -2.1; 28 -2.2; 31 -2.2; 34 -2.2; 37 -2.2; 41 -2.2; 45 -2.2; 49 -2.2; 54 -2.3; 60 -2.7; 66 -3.0; 72 -3.3; 79 -3.6; 87 -3.9; 96 -4.3; 106 -4.9; 116 -5.7; 128 -6.5; 141 -7.1; 155 -7.5; 170 -7.5; 187 -7.4; 206 -7.3; 227 -7.0; 249 -6.6; 274 -6.1; 302 -5.6; 332 -5.1; 365 -4.6; 402 -4.1; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.8; 647 -1.4; 712 -0.8; 783 -0.5; 861 -0.6; 947 -1.6; 1042 -3.1; 1146 -4.2; 1261 -4.7; 1387 -5.1; 1526 -5.6; 1678 -5.9; 1846 -6.3; 2031 -7.0; 2234 -7.5; 2457 -7.9; 2703 -7.8; 2973 -6.4; 3270 -4.8; 3597 -3.7; 3957 -3.3; 4353 -3.5; 4788 -3.6; 5267 -5.2; 5793 -7.8; 6373 -14.0; 7010 -11.0; 7711 -5.4; 8482 -5.2; 9330 -7.3; 10263 -10.1; 11289 -6.1; 12418 -5.3; 13660 -5.3; 15026 -6.4; 16529 -5.5; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.97 | 3.8 dB   |
| Peaking | 753 Hz   | 1.76 | 5.2 dB   |
| Peaking | 2309 Hz  | 3.11 | -3.1 dB  |
| Peaking | 6551 Hz  | 6.77 | -10.1 dB |
| Peaking | 20812 Hz | 2.19 | -1.5 dB  |
| Peaking | 88 Hz    | 1.06 | 2.3 dB   |
| Peaking | 157 Hz   | 0.85 | -3.4 dB  |
| Peaking | 454 Hz   | 2.06 | 1.3 dB   |
| Peaking | 4202 Hz  | 3.04 | 2.7 dB   |
| Peaking | 10196 Hz | 6.5  | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Tarah/Jaybird%20Tarah.png)