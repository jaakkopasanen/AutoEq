# Sennheiser Momentum On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.5; 25 -8.6; 28 -8.8; 31 -9.0; 34 -9.1; 37 -9.2; 41 -9.3; 45 -9.3; 49 -9.4; 54 -9.5; 60 -9.7; 66 -9.8; 72 -9.7; 79 -9.4; 87 -9.5; 96 -10.0; 106 -10.2; 116 -10.1; 128 -10.1; 141 -10.0; 155 -9.7; 170 -9.3; 187 -9.0; 206 -8.3; 227 -7.6; 249 -6.6; 274 -5.5; 302 -5.0; 332 -4.4; 365 -4.0; 402 -3.8; 442 -3.8; 486 -4.0; 535 -4.3; 588 -4.7; 647 -5.1; 712 -5.4; 783 -5.5; 861 -5.6; 947 -5.6; 1042 -6.1; 1146 -6.8; 1261 -7.9; 1387 -9.2; 1526 -10.4; 1678 -11.4; 1846 -11.3; 2031 -10.6; 2234 -9.5; 2457 -7.7; 2703 -5.7; 2973 -4.2; 3270 -2.8; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -5.0; 5267 -4.6; 5793 -3.1; 6373 -5.1; 7010 -9.0; 7711 -9.3; 8482 -8.5; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 126 Hz  |  0.29 | -4.4 dB |
| Peaking | 397 Hz  |  0.75 | 5.4 dB  |
| Peaking | 1841 Hz |  1.74 | -6.3 dB |
| Peaking | 3875 Hz |  1.58 | 6.7 dB  |
| Peaking | 7774 Hz |  3.15 | -4.0 dB |
| Peaking | 23 Hz   |  1.16 | -0.6 dB |
| Peaking | 81 Hz   |  4.62 | 0.8 dB  |
| Peaking | 986 Hz  |  5.64 | 0.9 dB  |
| Peaking | 4977 Hz | 12.01 | -3.0 dB |
| Peaking | 5893 Hz |  7.92 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)