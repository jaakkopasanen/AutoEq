# Sennheiser Momentum On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.3; 28 -9.5; 31 -9.6; 34 -9.7; 37 -9.8; 41 -9.9; 45 -10.0; 49 -10.0; 54 -10.1; 60 -10.3; 66 -10.4; 72 -10.3; 79 -10.1; 87 -10.1; 96 -10.6; 106 -10.8; 116 -10.8; 128 -10.8; 141 -10.6; 155 -10.3; 170 -10.0; 187 -9.6; 206 -9.0; 227 -8.2; 249 -7.3; 274 -6.1; 302 -5.7; 332 -5.1; 365 -4.6; 402 -4.4; 442 -4.5; 486 -4.7; 535 -5.0; 588 -5.3; 647 -5.8; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.2; 1042 -6.7; 1146 -7.5; 1261 -8.6; 1387 -9.8; 1526 -11.0; 1678 -12.0; 1846 -12.0; 2031 -11.3; 2234 -10.2; 2457 -8.4; 2703 -6.3; 2973 -4.8; 3270 -3.5; 3597 -1.8; 3957 -0.5; 4353 -0.5; 4788 -5.6; 5267 -5.2; 5793 -3.8; 6373 -5.7; 7010 -9.6; 7711 -9.9; 8482 -9.2; 9330 -9.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.61 | -3.7 dB |
| Peaking | 132 Hz  |  1.64 | -3.6 dB |
| Peaking | 1829 Hz |  2.11 | -6.6 dB |
| Peaking | 3937 Hz |  2.11 | 6.7 dB  |
| Peaking | 7843 Hz |  2.98 | -4.3 dB |
| Peaking | 202 Hz  |  2.69 | -1.7 dB |
| Peaking | 402 Hz  |  1.18 | 2.6 dB  |
| Peaking | 975 Hz  |  3.48 | 0.6 dB  |
| Peaking | 1384 Hz |  3.97 | -1.1 dB |
| Peaking | 5964 Hz | 11.09 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)