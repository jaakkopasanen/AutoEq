# Jaybird X3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.5; 25 -8.5; 28 -8.4; 31 -8.4; 34 -8.4; 37 -8.4; 41 -8.4; 45 -8.4; 49 -8.4; 54 -8.3; 60 -8.4; 66 -8.4; 72 -8.5; 79 -8.5; 87 -8.6; 96 -8.7; 106 -8.7; 116 -8.6; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.7; 187 -7.6; 206 -7.6; 227 -7.3; 249 -6.8; 274 -6.2; 302 -5.7; 332 -5.1; 365 -4.6; 402 -4.0; 442 -3.4; 486 -2.8; 535 -2.1; 588 -1.6; 647 -1.0; 712 -0.7; 783 -0.9; 861 -1.3; 947 -2.1; 1042 -2.9; 1146 -3.6; 1261 -3.9; 1387 -4.2; 1526 -4.3; 1678 -4.7; 1846 -5.4; 2031 -6.0; 2234 -6.5; 2457 -6.5; 2703 -5.9; 2973 -4.3; 3270 -2.6; 3597 -1.4; 3957 -0.8; 4353 -0.5; 4788 -0.6; 5267 -0.5; 5793 -1.0; 6373 -3.5; 7010 -9.6; 7711 -9.9; 8482 -4.9; 9330 -4.5; 10263 -7.4; 11289 -7.7; 12418 -4.5; 13660 -4.5; 15026 -4.5; 16529 -4.5; 18182 -4.5; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 59 Hz    | 0.2  | -4.2 dB |
| Peaking | 655 Hz   | 1.38 | 4.7 dB  |
| Peaking | 5038 Hz  | 1.86 | 5.1 dB  |
| Peaking | 7328 Hz  | 5.49 | -8.4 dB |
| Peaking | 10816 Hz | 6.9  | -4.8 dB |
| Peaking | 374 Hz   | 3.97 | 0.6 dB  |
| Peaking | 885 Hz   | 5    | 0.9 dB  |
| Peaking | 2413 Hz  | 1.98 | -3.0 dB |
| Peaking | 3561 Hz  | 3.37 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X3/Jaybird%20X3.png)