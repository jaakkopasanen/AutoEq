# Etymotic hf3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.4; 28 -1.7; 31 -2.0; 34 -2.3; 37 -2.5; 41 -2.8; 45 -3.1; 49 -3.3; 54 -3.6; 60 -4.1; 66 -4.4; 72 -4.8; 79 -5.2; 87 -5.5; 96 -5.8; 106 -6.1; 116 -6.3; 128 -6.6; 141 -7.1; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.8; 227 -7.8; 249 -7.8; 274 -7.8; 302 -7.7; 332 -7.6; 365 -7.4; 402 -7.1; 442 -7.2; 486 -7.1; 535 -7.0; 588 -6.7; 647 -6.6; 712 -6.6; 783 -6.7; 861 -7.2; 947 -7.7; 1042 -8.4; 1146 -9.1; 1261 -9.8; 1387 -10.6; 1526 -11.5; 1678 -12.0; 1846 -12.1; 2031 -12.0; 2234 -11.5; 2457 -10.6; 2703 -9.1; 2973 -6.9; 3270 -4.5; 3597 -2.8; 3957 -2.9; 4353 -3.9; 4788 -3.6; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.17 | 5.5 dB  |
| Peaking | 48 Hz   | 1.68 | 2.3 dB  |
| Peaking | 1961 Hz | 1.04 | -6.4 dB |
| Peaking | 3602 Hz | 2.62 | 5.5 dB  |
| Peaking | 5832 Hz | 3.03 | 6.7 dB  |
| Peaking | 92 Hz   | 0.88 | 0.9 dB  |
| Peaking | 199 Hz  | 0.68 | -1.7 dB |
| Peaking | 724 Hz  | 2.24 | 1.1 dB  |
| Peaking | 8049 Hz | 5.4  | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -7.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf3/Etymotic%20hf3.png)