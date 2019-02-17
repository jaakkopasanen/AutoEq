# Woodees iESW101V Vintage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -12.9; 25 -12.9; 28 -12.7; 31 -12.6; 34 -12.5; 37 -12.3; 41 -12.2; 45 -12.1; 49 -12.0; 54 -11.9; 60 -11.9; 66 -11.9; 72 -11.8; 79 -11.8; 87 -11.8; 96 -11.7; 106 -11.6; 116 -11.4; 128 -11.4; 141 -11.4; 155 -11.2; 170 -11.1; 187 -10.9; 206 -10.7; 227 -10.4; 249 -10.1; 274 -9.8; 302 -9.5; 332 -9.0; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.4; 647 -5.9; 712 -5.6; 783 -5.2; 861 -5.3; 947 -5.6; 1042 -4.8; 1146 -4.3; 1261 -5.2; 1387 -5.8; 1526 -6.6; 1678 -7.1; 1846 -7.3; 2031 -7.5; 2234 -7.7; 2457 -7.7; 2703 -7.2; 2973 -5.3; 3270 -2.5; 3597 -0.5; 3957 -1.0; 4353 -3.4; 4788 -5.6; 5267 -8.7; 5793 -12.7; 6373 -5.7; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW101V Vintage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101V Vintage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.14 | -6.7 dB |
| Peaking | 209 Hz  | 0.9  | -2.7 dB |
| Peaking | 2546 Hz | 2.11 | -3.7 dB |
| Peaking | 3635 Hz | 2.26 | 6.6 dB  |
| Peaking | 5652 Hz | 7.75 | -8.5 dB |
| Peaking | 383 Hz  | 2.16 | -0.6 dB |
| Peaking | 1246 Hz | 1.03 | 2.4 dB  |
| Peaking | 1625 Hz | 1.88 | -2.5 dB |
| Peaking | 6307 Hz | 2.93 | -2.1 dB |
| Peaking | 6743 Hz | 6.47 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101V%20Vintage/Woodees%20iESW101V%20Vintage.png)