# Sennheiser Momentum Wireless Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.6; 25 -6.9; 28 -7.4; 31 -7.7; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.0; 60 -9.2; 66 -9.4; 72 -9.7; 79 -9.9; 87 -10.3; 96 -10.6; 106 -10.7; 116 -10.7; 128 -10.6; 141 -10.3; 155 -10.6; 170 -10.1; 187 -9.6; 206 -9.3; 227 -8.8; 249 -8.2; 274 -7.7; 302 -6.9; 332 -6.3; 365 -6.3; 402 -6.9; 442 -7.2; 486 -7.7; 535 -7.9; 588 -7.9; 647 -7.9; 712 -8.2; 783 -7.9; 861 -8.1; 947 -8.4; 1042 -8.5; 1146 -8.7; 1261 -9.0; 1387 -9.6; 1526 -10.3; 1678 -10.3; 1846 -10.5; 2031 -10.1; 2234 -9.0; 2457 -7.4; 2703 -6.0; 2973 -4.0; 3270 -2.2; 3597 -0.7; 3957 -0.5; 4353 -0.5; 4788 -5.7; 5267 -4.9; 5793 -1.3; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum Wireless Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 86 Hz   |  0.71 | -3.4 dB |
| Peaking | 158 Hz  |  1.59 | -2.1 dB |
| Peaking | 1810 Hz |  0.84 | -4.5 dB |
| Peaking | 3669 Hz |  1.98 | 8.0 dB  |
| Peaking | 6221 Hz |  5.71 | 5.6 dB  |
| Peaking | 345 Hz  |  4.58 | 1.4 dB  |
| Peaking | 570 Hz  |  2.49 | -0.7 dB |
| Peaking | 4539 Hz |  8.23 | 3.3 dB  |
| Peaking | 4922 Hz | 11.27 | -4.9 dB |
| Peaking | 8254 Hz |  5.68 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Passive/Sennheiser%20Momentum%20Wireless%20Wired%20Passive.png)