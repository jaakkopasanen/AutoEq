# Jaybird X3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.0; 25 -4.0; 28 -3.9; 31 -3.9; 34 -3.9; 37 -3.9; 41 -3.8; 45 -3.8; 49 -3.8; 54 -3.9; 60 -4.2; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.5; 206 -7.8; 227 -7.6; 249 -7.2; 274 -6.6; 302 -6.0; 332 -5.5; 365 -5.0; 402 -4.4; 442 -3.8; 486 -3.1; 535 -2.4; 588 -1.8; 647 -1.2; 712 -1.0; 783 -1.1; 861 -1.5; 947 -2.4; 1042 -3.2; 1146 -3.8; 1261 -4.2; 1387 -4.3; 1526 -4.5; 1678 -4.8; 1846 -5.4; 2031 -5.9; 2234 -6.0; 2457 -5.9; 2703 -5.7; 2973 -4.6; 3270 -3.2; 3597 -2.1; 3957 -1.4; 4353 -1.2; 4788 -0.6; 5267 -0.5; 5793 -1.3; 6373 -4.8; 7010 -9.8; 7711 -9.4; 8482 -5.1; 9330 -4.7; 10263 -8.0; 11289 -7.4; 12418 -4.6; 13660 -4.6; 15026 -4.6; 16529 -4.6; 18182 -4.6; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 188 Hz   | 0.98 | -3.4 dB |
| Peaking | 687 Hz   | 1.68 | 4.2 dB  |
| Peaking | 5096 Hz  | 2.04 | 5.1 dB  |
| Peaking | 7237 Hz  | 4.91 | -7.8 dB |
| Peaking | 10722 Hz | 6.31 | -4.6 dB |
| Peaking | 47 Hz    | 0.45 | 1.0 dB  |
| Peaking | 107 Hz   | 1.63 | -1.0 dB |
| Peaking | 900 Hz   | 5.35 | 0.8 dB  |
| Peaking | 2397 Hz  | 1.72 | -2.2 dB |
| Peaking | 3631 Hz  | 3.79 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X3/Jaybird%20X3.png)