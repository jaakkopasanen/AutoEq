# Sennheiser IE 8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -7.1; 25 -7.6; 28 -8.3; 31 -8.9; 34 -9.4; 37 -9.9; 41 -10.4; 45 -10.9; 49 -11.4; 54 -11.9; 60 -12.4; 66 -12.9; 72 -13.4; 79 -13.7; 87 -14.1; 96 -14.5; 106 -14.6; 116 -14.8; 128 -15.0; 141 -15.1; 155 -15.1; 170 -15.0; 187 -14.8; 206 -14.5; 227 -14.2; 249 -13.7; 274 -13.1; 302 -12.4; 332 -11.7; 365 -10.8; 402 -10.1; 442 -9.5; 486 -8.8; 535 -7.9; 588 -7.0; 647 -6.2; 712 -5.4; 783 -4.9; 861 -4.5; 947 -4.4; 1042 -4.1; 1146 -4.4; 1261 -5.0; 1387 -6.1; 1526 -7.2; 1678 -7.8; 1846 -7.9; 2031 -7.7; 2234 -7.3; 2457 -6.6; 2703 -5.6; 2973 -4.4; 3270 -3.1; 3597 -2.8; 3957 -4.5; 4353 -5.5; 4788 -2.9; 5267 -0.5; 5793 -1.2; 6373 -2.9; 7010 -2.4; 7711 -3.9; 8482 -4.1; 9330 -4.8; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -5.5; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.45 | -7.9 dB |
| Peaking | 179 Hz  | 0.86 | -5.4 dB |
| Peaking | 333 Hz  | 1.24 | -3.5 dB |
| Peaking | 1907 Hz | 2.35 | -4.0 dB |
| Peaking | 5515 Hz | 4.4  | 4.1 dB  |
| Peaking | 507 Hz  | 3.9  | -0.9 dB |
| Peaking | 990 Hz  | 1.62 | 1.3 dB  |
| Peaking | 1492 Hz | 4.4  | -1.3 dB |
| Peaking | 3453 Hz | 6.2  | 2.1 dB  |
| Peaking | 4270 Hz | 8.35 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20IE%208/Sennheiser%20IE%208.png)