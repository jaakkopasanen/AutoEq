# Etymotic hf3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -0.8; 41 -1.1; 45 -1.4; 49 -1.7; 54 -2.0; 60 -2.4; 66 -2.7; 72 -3.1; 79 -3.6; 87 -3.9; 96 -4.2; 106 -4.4; 116 -4.7; 128 -5.0; 141 -5.5; 155 -5.7; 170 -5.9; 187 -6.0; 206 -6.1; 227 -6.1; 249 -6.2; 274 -6.1; 302 -6.1; 332 -5.9; 365 -5.7; 402 -5.5; 442 -5.6; 486 -5.5; 535 -5.3; 588 -5.1; 647 -4.9; 712 -4.9; 783 -5.1; 861 -5.5; 947 -6.1; 1042 -6.7; 1146 -7.4; 1261 -8.1; 1387 -9.0; 1526 -9.8; 1678 -10.3; 1846 -10.5; 2031 -10.3; 2234 -9.9; 2457 -8.9; 2703 -7.5; 2973 -5.3; 3270 -2.8; 3597 -1.1; 3957 -1.2; 4353 -2.3; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 28 Hz   | 0.43 | 6.1 dB  |
| Peaking | 790 Hz  | 0.96 | 2.9 dB  |
| Peaking | 2035 Hz | 0.71 | -5.7 dB |
| Peaking | 3604 Hz | 1.92 | 7.8 dB  |
| Peaking | 5736 Hz | 2.73 | 6.3 dB  |
| Peaking | 195 Hz  | 2.39 | -0.4 dB |
| Peaking | 6624 Hz | 8.11 | 1.9 dB  |
| Peaking | 7694 Hz | 2.62 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf3/Etymotic%20hf3.png)