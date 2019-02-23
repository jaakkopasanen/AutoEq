# Apple iPod Ear Buds sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -1.1; 170 -2.5; 187 -3.8; 206 -5.0; 227 -6.0; 249 -6.8; 274 -7.3; 302 -7.7; 332 -7.8; 365 -7.5; 402 -7.3; 442 -6.8; 486 -6.8; 535 -6.8; 588 -6.5; 647 -6.8; 712 -6.9; 783 -6.8; 861 -6.9; 947 -6.9; 1042 -6.9; 1146 -6.8; 1261 -6.9; 1387 -7.3; 1526 -7.8; 1678 -8.2; 1846 -8.1; 2031 -7.3; 2234 -6.2; 2457 -6.5; 2703 -9.1; 2973 -12.0; 3270 -11.2; 3597 -8.4; 3957 -7.4; 4353 -8.4; 4788 -8.8; 5267 -8.3; 5793 -9.5; 6373 -11.3; 7010 -9.6; 7711 -8.9; 8482 -9.1; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple iPod Ear Buds sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.14 | 6.8 dB  |
| Peaking | 290 Hz  | 1.22 | -5.7 dB |
| Peaking | 663 Hz  | 0.48 | -2.7 dB |
| Peaking | 3060 Hz | 5.51 | -5.7 dB |
| Peaking | 6485 Hz | 2.08 | -4.1 dB |
| Peaking | 18 Hz   | 2.53 | 0.7 dB  |
| Peaking | 146 Hz  | 4.41 | 1.3 dB  |
| Peaking | 204 Hz  | 4.62 | -0.9 dB |
| Peaking | 1745 Hz | 5.14 | -1.2 dB |
| Peaking | 2342 Hz | 7.65 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds%20sample%20B/Apple%20iPod%20Ear%20Buds%20sample%20B.png)