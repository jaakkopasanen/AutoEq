# Jaybird Tarah
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -6.8; 25 -6.9; 28 -6.9; 31 -6.9; 34 -6.9; 37 -6.9; 41 -6.9; 45 -7.0; 49 -7.0; 54 -7.0; 60 -7.0; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.4; 106 -7.5; 116 -7.8; 128 -8.1; 141 -8.3; 155 -8.3; 170 -8.1; 187 -7.7; 206 -7.3; 227 -6.8; 249 -6.4; 274 -5.9; 302 -5.5; 332 -5.0; 365 -4.5; 402 -4.0; 442 -3.5; 486 -3.0; 535 -2.4; 588 -1.8; 647 -1.3; 712 -0.8; 783 -0.5; 861 -0.6; 947 -1.6; 1042 -3.1; 1146 -4.3; 1261 -4.8; 1387 -5.2; 1526 -5.6; 1678 -6.0; 1846 -6.5; 2031 -7.4; 2234 -8.3; 2457 -8.7; 2703 -8.2; 2973 -6.3; 3270 -4.4; 3597 -3.3; 3957 -2.8; 4353 -3.0; 4788 -3.9; 5267 -5.0; 5793 -7.7; 6373 -12.9; 7010 -11.4; 7711 -6.0; 8482 -5.4; 9330 -5.9; 10263 -9.5; 11289 -6.8; 12418 -5.4; 13660 -5.4; 15026 -6.1; 16529 -5.5; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 123 Hz   | 0.43 | -2.7 dB |
| Peaking | 720 Hz   | 0.97 | 5.4 dB  |
| Peaking | 2654 Hz  | 1.08 | -6.0 dB |
| Peaking | 3758 Hz  | 1.45 | 6.4 dB  |
| Peaking | 6556 Hz  | 4.8  | -9.2 dB |
| Peaking | 22 Hz    | 1.59 | -1.0 dB |
| Peaking | 887 Hz   | 6.45 | 0.9 dB  |
| Peaking | 1161 Hz  | 5.17 | -0.9 dB |
| Peaking | 8398 Hz  | 4.12 | 1.5 dB  |
| Peaking | 10361 Hz | 5.68 | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Tarah/Jaybird%20Tarah.png)