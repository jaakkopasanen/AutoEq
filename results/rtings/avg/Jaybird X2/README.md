# Jaybird X2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.7; 25 -0.7; 28 -0.7; 31 -0.7; 34 -0.7; 37 -0.7; 41 -0.8; 45 -0.8; 49 -0.9; 54 -1.1; 60 -1.5; 66 -1.9; 72 -2.2; 79 -2.6; 87 -3.1; 96 -3.6; 106 -4.2; 116 -4.7; 128 -5.1; 141 -5.5; 155 -5.8; 170 -6.1; 187 -6.2; 206 -6.1; 227 -6.0; 249 -5.8; 274 -5.5; 302 -5.0; 332 -4.5; 365 -4.0; 402 -3.6; 442 -3.1; 486 -2.6; 535 -2.0; 588 -1.4; 647 -0.8; 712 -0.5; 783 -0.5; 861 -1.1; 947 -2.0; 1042 -2.8; 1146 -3.4; 1261 -3.7; 1387 -3.9; 1526 -4.0; 1678 -4.1; 1846 -4.1; 2031 -3.8; 2234 -3.3; 2457 -2.9; 2703 -2.9; 2973 -3.0; 3270 -2.9; 3597 -2.8; 3957 -2.8; 4353 -2.8; 4788 -2.0; 5267 -1.5; 5793 -0.7; 6373 -1.1; 7010 -1.8; 7711 -5.2; 8482 -7.8; 9330 -8.1; 10263 -9.4; 11289 -12.0; 12418 -11.7; 13660 -7.4; 15026 -5.2; 16529 -8.6; 18182 -13.3; 20000 -13.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.14 | 3.6 dB   |
| Peaking | 725 Hz   | 2.61 | 3.6 dB   |
| Peaking | 5930 Hz  | 2.1  | 4.1 dB   |
| Peaking | 11198 Hz | 1.64 | -8.0 dB  |
| Peaking | 19154 Hz | 0.98 | -11.6 dB |
| Peaking | 62 Hz    | 1.92 | 1.4 dB   |
| Peaking | 186 Hz   | 1.18 | -2.9 dB  |
| Peaking | 12549 Hz | 5.43 | -2.0 dB  |
| Peaking | 14899 Hz | 2.5  | 2.8 dB   |
| Peaking | 17486 Hz | 3.06 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -8.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X2/Jaybird%20X2.png)