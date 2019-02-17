# Sennheiser EH350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.5; 96 -2.5; 106 -3.4; 116 -3.8; 128 -4.4; 141 -3.9; 155 -4.0; 170 -4.4; 187 -4.7; 206 -4.8; 227 -5.0; 249 -5.1; 274 -5.3; 302 -5.4; 332 -5.6; 365 -5.7; 402 -5.7; 442 -6.0; 486 -5.9; 535 -5.6; 588 -5.6; 647 -5.3; 712 -5.5; 783 -6.3; 861 -6.4; 947 -6.6; 1042 -6.4; 1146 -6.2; 1261 -7.0; 1387 -7.5; 1526 -8.0; 1678 -8.0; 1846 -6.5; 2031 -5.9; 2234 -5.3; 2457 -5.0; 2703 -5.2; 2973 -5.2; 3270 -5.6; 3597 -3.8; 3957 -0.5; 4353 -5.8; 4788 -7.3; 5267 -4.5; 5793 -2.5; 6373 -1.1; 7010 -5.9; 7711 -9.4; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -14.3; 15026 -14.6; 16529 -12.0; 18182 -10.9; 20000 -9.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.23 | 6.1 dB   |
| Peaking | 73 Hz    | 3.06 | 1.6 dB   |
| Peaking | 5775 Hz  | 0.86 | 6.0 dB   |
| Peaking | 11542 Hz | 1.83 | 11.1 dB  |
| Peaking | 12916 Hz | 0.57 | -12.8 dB |
| Peaking | 1557 Hz  | 4.95 | -2.2 dB  |
| Peaking | 4076 Hz  | 5.92 | 7.2 dB   |
| Peaking | 4525 Hz  | 6.06 | -8.2 dB  |
| Peaking | 6277 Hz  | 5.92 | 4.3 dB   |
| Peaking | 7592 Hz  | 6.72 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH350/Sennheiser%20EH350.png)