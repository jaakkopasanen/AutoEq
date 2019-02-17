# Sennheiser EH250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.6; 60 -1.6; 66 -2.2; 72 -2.7; 79 -3.6; 87 -4.2; 96 -4.7; 106 -5.1; 116 -5.2; 128 -4.9; 141 -3.3; 155 -2.9; 170 -2.8; 187 -2.6; 206 -2.1; 227 -1.6; 249 -1.4; 274 -1.7; 302 -4.2; 332 -5.2; 365 -4.4; 402 -4.1; 442 -4.3; 486 -5.1; 535 -5.8; 588 -6.0; 647 -6.1; 712 -6.0; 783 -5.8; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -6.2; 1261 -6.3; 1387 -6.5; 1526 -6.7; 1678 -6.8; 1846 -6.4; 2031 -6.0; 2234 -5.2; 2457 -4.9; 2703 -4.1; 2973 -2.4; 3270 -0.5; 3597 -0.5; 3957 -7.6; 4353 -7.8; 4788 -4.0; 5267 -3.4; 5793 -0.6; 6373 -2.9; 7010 -7.4; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.6; 13660 -10.4; 15026 -10.4; 16529 -9.3; 18182 -8.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.62 | 6.6 dB  |
| Peaking | 232 Hz   | 1.43 | 4.7 dB  |
| Peaking | 4852 Hz  | 0.65 | 3.7 dB  |
| Peaking | 11860 Hz | 2.01 | 5.5 dB  |
| Peaking | 13124 Hz | 0.73 | -6.5 dB |
| Peaking | 1736 Hz  | 1.85 | -1.3 dB |
| Peaking | 3494 Hz  | 3.36 | 6.2 dB  |
| Peaking | 4107 Hz  | 4.75 | -8.4 dB |
| Peaking | 5983 Hz  | 4.66 | 4.6 dB  |
| Peaking | 7107 Hz  | 5.63 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 4.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH250/Sennheiser%20EH250.png)