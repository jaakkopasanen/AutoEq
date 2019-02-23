# Etymotic ER-4P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.9; 28 -1.2; 31 -1.5; 34 -1.7; 37 -2.0; 41 -2.2; 45 -2.5; 49 -2.8; 54 -3.1; 60 -3.5; 66 -3.9; 72 -4.2; 79 -4.5; 87 -5.1; 96 -5.3; 106 -5.6; 116 -5.8; 128 -6.1; 141 -6.4; 155 -6.7; 170 -6.8; 187 -7.0; 206 -7.1; 227 -7.1; 249 -7.1; 274 -7.1; 302 -7.0; 332 -6.9; 365 -6.7; 402 -6.6; 442 -6.7; 486 -6.6; 535 -6.7; 588 -6.5; 647 -6.4; 712 -6.4; 783 -6.6; 861 -6.9; 947 -7.6; 1042 -8.2; 1146 -9.0; 1261 -9.8; 1387 -10.8; 1526 -11.9; 1678 -12.5; 1846 -12.8; 2031 -12.8; 2234 -12.5; 2457 -11.6; 2703 -10.0; 2973 -7.5; 3270 -4.6; 3597 -2.8; 3957 -3.0; 4353 -4.3; 4788 -4.3; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.9; 15026 -11.2; 16529 -6.5; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4P GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4P ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.9  | 5.6 dB  |
| Peaking | 52 Hz    | 1.35 | 2.2 dB  |
| Peaking | 2014 Hz  | 1.15 | -7.4 dB |
| Peaking | 3615 Hz  | 2.85 | 5.9 dB  |
| Peaking | 5929 Hz  | 3.38 | 6.7 dB  |
| Peaking | 224 Hz   | 1.53 | -0.9 dB |
| Peaking | 748 Hz   | 1.94 | 1.0 dB  |
| Peaking | 1403 Hz  | 3.99 | -0.7 dB |
| Peaking | 15056 Hz | 4.96 | -5.4 dB |
| Peaking | 20889 Hz | 0.89 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -8.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4P/Etymotic%20ER-4P.png)