# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.8; 60 -1.2; 66 -1.6; 72 -2.1; 79 -2.5; 87 -3.0; 96 -3.6; 106 -4.0; 116 -4.5; 128 -4.9; 141 -5.3; 155 -5.5; 170 -5.8; 187 -6.0; 206 -6.2; 227 -6.3; 249 -6.4; 274 -6.5; 302 -6.5; 332 -6.5; 365 -6.6; 402 -6.6; 442 -6.6; 486 -6.6; 535 -6.4; 588 -6.2; 647 -5.9; 712 -5.7; 783 -5.5; 861 -5.6; 947 -6.0; 1042 -6.7; 1146 -7.5; 1261 -8.3; 1387 -8.9; 1526 -9.4; 1678 -9.9; 1846 -10.5; 2031 -10.7; 2234 -10.5; 2457 -9.5; 2703 -8.4; 2973 -7.7; 3270 -7.7; 3597 -8.1; 3957 -8.8; 4353 -9.3; 4788 -9.0; 5267 -6.7; 5793 -3.5; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.5  | 6.6 dB  |
| Peaking | 830 Hz   | 2.61 | 1.6 dB  |
| Peaking | 1901 Hz  | 1.38 | -4.3 dB |
| Peaking | 4533 Hz  | 3.36 | -3.1 dB |
| Peaking | 6290 Hz  | 4.43 | 6.1 dB  |
| Peaking | 21 Hz    | 0.28 | 1.9 dB  |
| Peaking | 34 Hz    | 1.17 | -2.3 dB |
| Peaking | 183 Hz   | 0.7  | -0.6 dB |
| Peaking | 3003 Hz  | 8.06 | 0.7 dB  |
| Peaking | 14907 Hz | 5.74 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20hf5/Etymotic%20hf5.png)