# Eskuche 33 1 3 B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -1.0; 34 -2.0; 37 -3.1; 41 -4.3; 45 -5.2; 49 -5.8; 54 -6.3; 60 -6.6; 66 -6.7; 72 -6.9; 79 -7.1; 87 -7.2; 96 -7.4; 106 -7.3; 116 -7.1; 128 -7.2; 141 -7.5; 155 -7.8; 170 -7.9; 187 -8.0; 206 -8.2; 227 -8.3; 249 -8.5; 274 -8.6; 302 -8.6; 332 -8.4; 365 -8.4; 402 -8.5; 442 -8.8; 486 -9.2; 535 -9.5; 588 -9.2; 647 -9.1; 712 -9.0; 783 -8.7; 861 -8.3; 947 -7.0; 1042 -6.1; 1146 -5.3; 1261 -5.0; 1387 -3.6; 1526 -3.3; 1678 -2.8; 1846 -2.4; 2031 -2.2; 2234 -2.0; 2457 -2.3; 2703 -2.3; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eskuche 33 1 3 B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eskuche 33 1 3 B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.53 | 6.9 dB  |
| Peaking | 1433 Hz | 0.16 | -4.0 dB |
| Peaking | 1703 Hz | 0.92 | 6.3 dB  |
| Peaking | 3946 Hz | 1.04 | 8.0 dB  |
| Peaking | 6080 Hz | 3.62 | 4.5 dB  |
| Peaking | 12 Hz   | 1.36 | 2.1 dB  |
| Peaking | 72 Hz   | 1.41 | -0.7 dB |
| Peaking | 370 Hz  | 4.17 | 0.8 dB  |
| Peaking | 731 Hz  | 3.84 | -0.7 dB |
| Peaking | 7778 Hz | 6.96 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Eskuche%2033%201%203%20B/Eskuche%2033%201%203%20B.png)