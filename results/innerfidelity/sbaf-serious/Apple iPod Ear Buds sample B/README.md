# Apple iPod Ear Buds sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.8; 170 -2.2; 187 -3.5; 206 -4.6; 227 -5.6; 249 -6.4; 274 -7.0; 302 -7.3; 332 -7.4; 365 -7.2; 402 -6.9; 442 -6.5; 486 -6.4; 535 -6.4; 588 -6.2; 647 -6.4; 712 -6.6; 783 -6.4; 861 -6.5; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.5; 1387 -7.0; 1526 -7.5; 1678 -7.8; 1846 -7.7; 2031 -6.9; 2234 -5.8; 2457 -6.2; 2703 -8.7; 2973 -11.6; 3270 -10.9; 3597 -8.0; 3957 -7.0; 4353 -8.1; 4788 -8.4; 5267 -8.0; 5793 -9.1; 6373 -11.0; 7010 -9.3; 7711 -8.5; 8482 -8.7; 9330 -6.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.19 | 6.6 dB  |
| Peaking | 251 Hz  | 2.42 | -2.6 dB |
| Peaking | 354 Hz  | 1.06 | -3.2 dB |
| Peaking | 3050 Hz | 5.45 | -5.6 dB |
| Peaking | 6474 Hz | 2.29 | -3.9 dB |
| Peaking | 19 Hz   | 1.27 | 1.3 dB  |
| Peaking | 45 Hz   | 0.29 | -0.5 dB |
| Peaking | 142 Hz  | 3.37 | 1.4 dB  |
| Peaking | 1722 Hz | 2.69 | -1.4 dB |
| Peaking | 2330 Hz | 6.36 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -2.2 dB |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds%20sample%20B/Apple%20iPod%20Ear%20Buds%20sample%20B.png)