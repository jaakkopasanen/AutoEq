# Sennheiser EH250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -1.0; 49 -1.7; 54 -2.8; 60 -4.0; 66 -4.6; 72 -5.1; 79 -6.0; 87 -6.6; 96 -7.1; 106 -7.5; 116 -7.7; 128 -7.4; 141 -5.7; 155 -5.3; 170 -5.2; 187 -5.0; 206 -4.5; 227 -4.0; 249 -3.8; 274 -4.1; 302 -6.7; 332 -7.6; 365 -6.9; 402 -6.5; 442 -6.8; 486 -7.5; 535 -8.2; 588 -8.4; 647 -8.5; 712 -8.5; 783 -8.3; 861 -8.5; 947 -8.9; 1042 -8.9; 1146 -8.7; 1261 -8.7; 1387 -9.0; 1526 -9.2; 1678 -9.3; 1846 -8.9; 2031 -8.4; 2234 -7.7; 2457 -7.4; 2703 -6.5; 2973 -4.8; 3270 -0.7; 3597 -1.2; 3957 -10.0; 4353 -10.3; 4788 -6.4; 5267 -5.8; 5793 -1.3; 6373 -5.3; 7010 -9.9; 7711 -9.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.9; 13660 -12.8; 15026 -12.8; 16529 -11.7; 18182 -10.7; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser EH250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.93 | 6.9 dB  |
| Peaking | 1272 Hz  | 0.7  | -2.7 dB |
| Peaking | 3337 Hz  | 7.2  | 8.0 dB  |
| Peaking | 11371 Hz | 1.63 | 5.3 dB  |
| Peaking | 14643 Hz | 0.74 | -8.1 dB |
| Peaking | 106 Hz   | 2.83 | -2.2 dB |
| Peaking | 229 Hz   | 2.59 | 2.9 dB  |
| Peaking | 4183 Hz  | 8.91 | -5.6 dB |
| Peaking | 5933 Hz  | 5.6  | 6.7 dB  |
| Peaking | 7187 Hz  | 5.82 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | 2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -7.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH250/Sennheiser%20EH250.png)