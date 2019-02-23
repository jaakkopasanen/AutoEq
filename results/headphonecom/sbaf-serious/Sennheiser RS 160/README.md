# Sennheiser RS 160
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.7; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.1; 45 -8.2; 49 -8.2; 54 -8.0; 60 -8.0; 66 -8.1; 72 -8.1; 79 -7.9; 87 -7.6; 96 -7.7; 106 -8.8; 116 -9.5; 128 -8.8; 141 -9.7; 155 -9.6; 170 -8.5; 187 -8.5; 206 -8.6; 227 -8.0; 249 -7.5; 274 -6.9; 302 -6.5; 332 -6.6; 365 -6.9; 402 -7.2; 442 -7.1; 486 -6.5; 535 -5.8; 588 -5.1; 647 -5.0; 712 -4.9; 783 -4.7; 861 -4.8; 947 -5.5; 1042 -7.1; 1146 -7.3; 1261 -7.4; 1387 -8.5; 1526 -9.3; 1678 -10.7; 1846 -6.9; 2031 -8.6; 2234 -9.7; 2457 -9.2; 2703 -8.3; 2973 -8.4; 3270 -7.3; 3597 -6.2; 3957 -5.2; 4353 -6.3; 4788 -4.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.8; 9330 -12.9; 10263 -10.7; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 160 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 160 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 129 Hz  | 0.96 | -2.8 dB |
| Peaking | 1618 Hz | 5.16 | -3.4 dB |
| Peaking | 2476 Hz | 2.33 | -3.0 dB |
| Peaking | 5859 Hz | 2.44 | 7.2 dB  |
| Peaking | 9338 Hz | 3.72 | -7.8 dB |
| Peaking | 37 Hz   | 1.1  | -0.7 dB |
| Peaking | 41 Hz   | 0.33 | -0.7 dB |
| Peaking | 91 Hz   | 3.57 | 1.5 dB  |
| Peaking | 828 Hz  | 1.57 | 2.9 dB  |
| Peaking | 1088 Hz | 2.09 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20160/Sennheiser%20RS%20160.png)