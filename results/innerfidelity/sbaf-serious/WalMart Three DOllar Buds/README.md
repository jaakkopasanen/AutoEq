# WalMart Three DOllar Buds
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.6; 170 -2.0; 187 -3.5; 206 -5.2; 227 -6.9; 249 -8.4; 274 -9.7; 302 -11.1; 332 -12.3; 365 -13.1; 402 -13.5; 442 -13.0; 486 -12.4; 535 -11.6; 588 -9.5; 647 -9.2; 712 -9.3; 783 -9.2; 861 -8.9; 947 -8.5; 1042 -8.9; 1146 -8.7; 1261 -8.7; 1387 -8.6; 1526 -8.7; 1678 -8.7; 1846 -7.6; 2031 -5.8; 2234 -3.5; 2457 -2.7; 2703 -4.1; 2973 -5.5; 3270 -5.6; 3597 -4.3; 3957 -4.2; 4353 -5.6; 4788 -5.7; 5267 -5.8; 5793 -5.7; 6373 -8.1; 7010 -7.8; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`WalMart Three DOllar Buds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `WalMart Three DOllar Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 79 Hz   | 0.17 | 6.9 dB   |
| Peaking | 276 Hz  | 1.99 | -4.1 dB  |
| Peaking | 413 Hz  | 1.22 | -9.6 dB  |
| Peaking | 1898 Hz | 0.85 | -10.6 dB |
| Peaking | 2263 Hz | 1.12 | 12.3 dB  |
| Peaking | 16 Hz   | 2.26 | 0.8 dB   |
| Peaking | 151 Hz  | 5.92 | 1.4 dB   |
| Peaking | 3149 Hz | 4.56 | -3.3 dB  |
| Peaking | 3477 Hz | 2.35 | 2.4 dB   |
| Peaking | 6644 Hz | 6.53 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 3.9 dB  |
| Peaking | 125 Hz   | 1.41 | 7.1 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -5.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/WalMart%20Three%20DOllar%20Buds/WalMart%20Three%20DOllar%20Buds.png)