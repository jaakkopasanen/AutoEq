# Sennheiser PMX 100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.3; 25 -4.9; 28 -5.7; 31 -6.3; 34 -6.8; 37 -7.2; 41 -7.7; 45 -8.1; 49 -8.4; 54 -8.8; 60 -9.2; 66 -9.6; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.7; 106 -10.8; 116 -10.8; 128 -11.0; 141 -11.1; 155 -11.0; 170 -10.9; 187 -10.5; 206 -10.4; 227 -10.1; 249 -9.5; 274 -9.0; 302 -8.6; 332 -8.1; 365 -7.8; 402 -7.5; 442 -7.2; 486 -6.9; 535 -6.6; 588 -6.3; 647 -6.1; 712 -5.9; 783 -5.7; 861 -5.8; 947 -5.8; 1042 -6.0; 1146 -6.1; 1261 -6.5; 1387 -7.2; 1526 -8.2; 1678 -8.9; 1846 -9.3; 2031 -9.1; 2234 -7.4; 2457 -5.7; 2703 -4.0; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -5.7; 4353 -13.1; 4788 -8.6; 5267 -2.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PMX 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.94 | 3.3 dB   |
| Peaking | 124 Hz  | 0.58 | -4.8 dB  |
| Peaking | 3463 Hz | 3.34 | 8.5 dB   |
| Peaking | 4395 Hz | 4.67 | -10.8 dB |
| Peaking | 5781 Hz | 3.21 | 7.5 dB   |
| Peaking | 226 Hz  | 3.1  | -0.6 dB  |
| Peaking | 844 Hz  | 0.96 | 1.3 dB   |
| Peaking | 1842 Hz | 2.27 | -3.7 dB  |
| Peaking | 2888 Hz | 6.69 | 2.5 dB   |
| Peaking | 8207 Hz | 5.27 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX%20100/Sennheiser%20PMX%20100.png)