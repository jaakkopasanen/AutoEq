# Woodees iESW101V Vintage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.7; 23 -12.7; 25 -12.6; 28 -12.5; 31 -12.3; 34 -12.2; 37 -12.1; 41 -11.9; 45 -11.8; 49 -11.7; 54 -11.7; 60 -11.6; 66 -11.6; 72 -11.5; 79 -11.5; 87 -11.5; 96 -11.4; 106 -11.3; 116 -11.1; 128 -11.1; 141 -11.1; 155 -11.0; 170 -10.8; 187 -10.6; 206 -10.4; 227 -10.2; 249 -9.9; 274 -9.6; 302 -9.2; 332 -8.7; 365 -8.3; 402 -7.8; 442 -7.5; 486 -7.0; 535 -6.6; 588 -6.1; 647 -5.6; 712 -5.3; 783 -4.9; 861 -5.0; 947 -5.3; 1042 -4.5; 1146 -4.1; 1261 -4.9; 1387 -5.6; 1526 -6.3; 1678 -6.8; 1846 -7.0; 2031 -7.2; 2234 -7.4; 2457 -7.4; 2703 -6.9; 2973 -5.1; 3270 -2.3; 3597 -0.5; 3957 -0.8; 4353 -3.1; 4788 -5.3; 5267 -8.4; 5793 -12.4; 6373 -5.4; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW101V Vintage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101V Vintage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.2  | -6.0 dB |
| Peaking | 171 Hz  | 0.53 | -3.4 dB |
| Peaking | 850 Hz  | 1.35 | 2.3 dB  |
| Peaking | 3766 Hz | 3.67 | 6.8 dB  |
| Peaking | 5664 Hz | 9.86 | -7.4 dB |
| Peaking | 274 Hz  | 3.71 | -0.2 dB |
| Peaking | 1145 Hz | 6.27 | 1.7 dB  |
| Peaking | 2485 Hz | 1.48 | -1.9 dB |
| Peaking | 3257 Hz | 5.32 | 2.2 dB  |
| Peaking | 6740 Hz | 9.96 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101V%20Vintage/Woodees%20iESW101V%20Vintage.png)