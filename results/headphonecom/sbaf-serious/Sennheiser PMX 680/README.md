# Sennheiser PMX 680
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.2; 28 -8.7; 31 -9.0; 34 -9.3; 37 -9.5; 41 -9.8; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.5; 66 -10.7; 72 -10.8; 79 -10.8; 87 -10.9; 96 -10.9; 106 -10.8; 116 -10.8; 128 -10.8; 141 -11.0; 155 -10.9; 170 -11.1; 187 -11.1; 206 -11.0; 227 -10.9; 249 -10.8; 274 -10.5; 302 -10.1; 332 -9.6; 365 -9.0; 402 -8.4; 442 -7.8; 486 -7.2; 535 -6.4; 588 -5.8; 647 -4.9; 712 -3.7; 783 -3.4; 861 -3.4; 947 -3.7; 1042 -4.1; 1146 -4.5; 1261 -5.1; 1387 -5.8; 1526 -6.7; 1678 -7.4; 1846 -7.8; 2031 -8.2; 2234 -8.3; 2457 -8.0; 2703 -6.9; 2973 -4.8; 3270 -2.3; 3597 -0.8; 3957 -2.0; 4353 -5.3; 4788 -8.8; 5267 -9.8; 5793 -4.6; 6373 -0.5; 7010 -1.3; 7711 -3.6; 8482 -3.8; 9330 -4.9; 10263 -4.5; 11289 -3.8; 12418 -3.8; 13660 -3.8; 15026 -3.8; 16529 -3.8; 18182 -3.8; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PMX 680 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.33 | -6.7 dB  |
| Peaking | 260 Hz  | 0.98 | -4.2 dB  |
| Peaking | 2318 Hz | 1.45 | -8.2 dB  |
| Peaking | 3836 Hz | 0.85 | 6.7 dB   |
| Peaking | 4969 Hz | 4.03 | -11.2 dB |
| Peaking | 493 Hz  | 1.93 | -1.1 dB  |
| Peaking | 790 Hz  | 1.78 | 2.0 dB   |
| Peaking | 1559 Hz | 4.3  | -1.2 dB  |
| Peaking | 6653 Hz | 6.28 | 4.5 dB   |
| Peaking | 8524 Hz | 1.14 | -1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX%20680/Sennheiser%20PMX%20680.png)