# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.0; 37 -1.2; 41 -1.5; 45 -1.8; 49 -2.1; 54 -2.4; 60 -2.8; 66 -3.2; 72 -3.4; 79 -3.9; 87 -4.3; 96 -4.6; 106 -4.9; 116 -5.1; 128 -5.4; 141 -5.7; 155 -5.9; 170 -6.1; 187 -6.2; 206 -6.3; 227 -6.3; 249 -6.4; 274 -6.4; 302 -6.3; 332 -6.1; 365 -5.9; 402 -5.6; 442 -5.5; 486 -5.4; 535 -5.5; 588 -5.5; 647 -5.3; 712 -5.3; 783 -5.4; 861 -5.7; 947 -6.1; 1042 -6.8; 1146 -7.4; 1261 -8.1; 1387 -8.8; 1526 -9.6; 1678 -10.1; 1846 -10.1; 2031 -10.0; 2234 -9.6; 2457 -8.7; 2703 -7.2; 2973 -5.2; 3270 -2.9; 3597 -1.1; 3957 -1.2; 4353 -2.3; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.55 | 4.4 dB  |
| Peaking | 41 Hz   | 0.55 | 3.1 dB  |
| Peaking | 1956 Hz | 1.66 | -4.6 dB |
| Peaking | 3685 Hz | 2.64 | 5.7 dB  |
| Peaking | 5715 Hz | 2.81 | 6.1 dB  |
| Peaking | 633 Hz  | 3.31 | -1.2 dB |
| Peaking | 657 Hz  | 1.58 | 2.4 dB  |
| Peaking | 1400 Hz | 3.47 | -1.0 dB |
| Peaking | 6591 Hz | 7.82 | 2.1 dB  |
| Peaking | 7721 Hz | 2.32 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf5/Etymotic%20hf5.png)