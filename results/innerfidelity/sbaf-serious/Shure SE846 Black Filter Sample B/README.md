# Shure SE846 Black Filter Sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.6; 28 -11.6; 31 -11.5; 34 -11.5; 37 -11.4; 41 -11.4; 45 -11.4; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.3; 72 -11.3; 79 -11.3; 87 -11.4; 96 -11.4; 106 -11.2; 116 -11.1; 128 -11.0; 141 -10.9; 155 -10.6; 170 -10.4; 187 -10.1; 206 -9.9; 227 -9.6; 249 -9.3; 274 -9.1; 302 -8.8; 332 -8.5; 365 -8.2; 402 -8.0; 442 -7.7; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.5; 712 -6.4; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.1; 1526 -7.3; 1678 -7.2; 1846 -6.8; 2031 -6.1; 2234 -5.2; 2457 -3.3; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter Sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter Sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.35 | -4.6 dB |
| Peaking | 124 Hz  | 0.46 | -3.8 dB |
| Peaking | 3130 Hz | 2.52 | 5.0 dB  |
| Peaking | 5517 Hz | 1.31 | 6.8 dB  |
| Peaking | 8223 Hz | 1.88 | -2.8 dB |
| Peaking | 804 Hz  | 1.74 | 1.1 dB  |
| Peaking | 1850 Hz | 0.83 | -1.5 dB |
| Peaking | 2622 Hz | 5.18 | 2.1 dB  |
| Peaking | 4055 Hz | 4.52 | 1.2 dB  |
| Peaking | 5225 Hz | 7.27 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Black%20Filter%20Sample%20B/Shure%20SE846%20Black%20Filter%20Sample%20B.png)