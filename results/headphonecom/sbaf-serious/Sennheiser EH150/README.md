# Sennheiser EH150
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.4; 79 -2.3; 87 -3.2; 96 -3.8; 106 -3.8; 116 -3.3; 128 -3.3; 141 -2.5; 155 -2.0; 170 -1.5; 187 -0.7; 206 -0.5; 227 -0.5; 249 -0.5; 274 -0.5; 302 -0.5; 332 -0.9; 365 -4.2; 402 -5.0; 442 -6.7; 486 -9.0; 535 -11.0; 588 -12.0; 647 -12.6; 712 -12.5; 783 -12.9; 861 -13.1; 947 -13.2; 1042 -13.1; 1146 -12.9; 1261 -13.0; 1387 -13.1; 1526 -13.1; 1678 -12.8; 1846 -11.8; 2031 -11.0; 2234 -9.8; 2457 -8.4; 2703 -7.4; 2973 -6.9; 3270 -5.4; 3597 -1.3; 3957 -0.6; 4353 -11.7; 4788 -10.6; 5267 -7.3; 5793 -4.6; 6373 -3.1; 7010 -9.8; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.7; 18182 -9.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH150 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.52 | 6.4 dB  |
| Peaking | 293 Hz   | 0.81 | 11.0 dB |
| Peaking | 651 Hz   | 0.54 | -9.7 dB |
| Peaking | 1604 Hz  | 2.07 | -3.0 dB |
| Peaking | 3725 Hz  | 7.84 | 8.2 dB  |
| Peaking | 4063 Hz  | 5.87 | 5.9 dB  |
| Peaking | 4442 Hz  | 5.86 | -9.6 dB |
| Peaking | 6166 Hz  | 7.18 | 6.4 dB  |
| Peaking | 7127 Hz  | 7.45 | -4.6 dB |
| Peaking | 17619 Hz | 2.93 | -3.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | 8.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -7.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH150/Sennheiser%20EH150.png)