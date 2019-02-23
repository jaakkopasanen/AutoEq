# Sennheiser IE 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.4; 28 -7.0; 31 -7.6; 34 -8.2; 37 -8.6; 41 -9.2; 45 -9.7; 49 -10.1; 54 -10.6; 60 -11.2; 66 -11.6; 72 -12.1; 79 -12.4; 87 -12.8; 96 -13.3; 106 -13.3; 116 -13.5; 128 -13.7; 141 -13.9; 155 -13.9; 170 -13.8; 187 -13.5; 206 -13.2; 227 -12.9; 249 -12.4; 274 -11.9; 302 -11.2; 332 -10.4; 365 -9.5; 402 -8.8; 442 -8.2; 486 -7.5; 535 -6.7; 588 -5.7; 647 -4.9; 712 -4.2; 783 -3.6; 861 -3.2; 947 -3.2; 1042 -2.8; 1146 -3.2; 1261 -3.8; 1387 -4.8; 1526 -5.9; 1678 -6.5; 1846 -6.6; 2031 -6.4; 2234 -6.0; 2457 -5.3; 2703 -4.3; 2973 -3.1; 3270 -1.9; 3597 -1.6; 3957 -3.2; 4353 -4.2; 4788 -1.6; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.79 | -3.7 dB |
| Peaking | 188 Hz  | 0.64 | -6.2 dB |
| Peaking | 879 Hz  | 1.32 | 4.4 dB  |
| Peaking | 3377 Hz | 3.58 | 4.5 dB  |
| Peaking | 5580 Hz | 2.73 | 6.4 dB  |
| Peaking | 21 Hz   | 2.22 | 2.1 dB  |
| Peaking | 880 Hz  | 3.25 | -1.4 dB |
| Peaking | 1405 Hz | 0.96 | 2.4 dB  |
| Peaking | 1705 Hz | 1.86 | -3.2 dB |
| Peaking | 8245 Hz | 4.42 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20IE%208/Sennheiser%20IE%208.png)