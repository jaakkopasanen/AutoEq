# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.1; 25 -1.4; 28 -1.8; 31 -2.1; 34 -2.4; 37 -2.6; 41 -2.9; 45 -3.2; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.6; 72 -4.8; 79 -5.3; 87 -5.7; 96 -6.0; 106 -6.2; 116 -6.5; 128 -6.8; 141 -7.1; 155 -7.3; 170 -7.5; 187 -7.6; 206 -7.7; 227 -7.7; 249 -7.8; 274 -7.7; 302 -7.7; 332 -7.5; 365 -7.3; 402 -7.0; 442 -6.9; 486 -6.8; 535 -6.9; 588 -6.9; 647 -6.7; 712 -6.7; 783 -6.8; 861 -7.1; 947 -7.5; 1042 -8.2; 1146 -8.8; 1261 -9.5; 1387 -10.2; 1526 -11.0; 1678 -11.5; 1846 -11.5; 2031 -11.4; 2234 -11.0; 2457 -10.1; 2703 -8.6; 2973 -6.6; 3270 -4.3; 3597 -2.5; 3957 -2.6; 4353 -3.7; 4788 -3.3; 5267 -1.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.19 | 5.4 dB  |
| Peaking | 48 Hz   | 1.75 | 2.2 dB  |
| Peaking | 1963 Hz | 1.03 | -5.8 dB |
| Peaking | 3621 Hz | 2.52 | 5.6 dB  |
| Peaking | 5831 Hz | 3.07 | 6.6 dB  |
| Peaking | 72 Hz   | 1.66 | 0.6 dB  |
| Peaking | 218 Hz  | 0.95 | -1.4 dB |
| Peaking | 759 Hz  | 2.31 | 0.8 dB  |
| Peaking | 8115 Hz | 5.34 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf5/Etymotic%20hf5.png)