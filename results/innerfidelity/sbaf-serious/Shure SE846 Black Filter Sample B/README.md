# Shure SE846 Black Filter Sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -12.9; 25 -12.9; 28 -12.9; 31 -12.8; 34 -12.8; 37 -12.7; 41 -12.7; 45 -12.7; 49 -12.6; 54 -12.6; 60 -12.6; 66 -12.6; 72 -12.6; 79 -12.6; 87 -12.7; 96 -12.7; 106 -12.5; 116 -12.4; 128 -12.3; 141 -12.2; 155 -11.9; 170 -11.7; 187 -11.4; 206 -11.2; 227 -10.8; 249 -10.6; 274 -10.4; 302 -10.1; 332 -9.8; 365 -9.5; 402 -9.3; 442 -9.0; 486 -8.9; 535 -8.6; 588 -8.1; 647 -7.8; 712 -7.7; 783 -7.4; 861 -7.5; 947 -7.7; 1042 -7.9; 1146 -8.0; 1261 -8.1; 1387 -8.4; 1526 -8.6; 1678 -8.5; 1846 -8.1; 2031 -7.4; 2234 -6.5; 2457 -4.6; 2703 -2.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Black Filter Sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter Sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.45 | -5.2 dB |
| Peaking | 113 Hz  | 0.32 | -5.4 dB |
| Peaking | 1861 Hz | 1.15 | -3.8 dB |
| Peaking | 3250 Hz | 1.33 | 7.3 dB  |
| Peaking | 5586 Hz | 2.55 | 4.9 dB  |
| Peaking | 4481 Hz | 4.66 | 1.4 dB  |
| Peaking | 6560 Hz | 4.87 | 3.7 dB  |
| Peaking | 6823 Hz | 1.52 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Black%20Filter%20Sample%20B/Shure%20SE846%20Black%20Filter%20Sample%20B.png)