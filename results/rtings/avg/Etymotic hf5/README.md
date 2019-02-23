# Etymotic hf5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.7; 106 -1.6; 116 -2.5; 128 -3.4; 141 -4.2; 155 -4.9; 170 -5.4; 187 -5.9; 206 -6.3; 227 -6.6; 249 -6.6; 274 -6.7; 302 -6.8; 332 -6.8; 365 -6.9; 402 -6.9; 442 -6.8; 486 -6.8; 535 -6.6; 588 -6.4; 647 -6.1; 712 -5.8; 783 -5.7; 861 -5.8; 947 -6.1; 1042 -6.8; 1146 -7.6; 1261 -8.4; 1387 -9.0; 1526 -9.4; 1678 -9.9; 1846 -10.3; 2031 -10.5; 2234 -9.9; 2457 -8.8; 2703 -8.2; 2973 -8.1; 3270 -8.2; 3597 -8.7; 3957 -9.4; 4353 -9.5; 4788 -8.6; 5267 -6.6; 5793 -3.9; 6373 -2.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -8.9; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.46 | 6.9 dB  |
| Peaking | 1873 Hz  | 1.7  | -4.0 dB |
| Peaking | 4303 Hz  | 2.42 | -3.2 dB |
| Peaking | 6301 Hz  | 3.84 | 5.2 dB  |
| Peaking | 14947 Hz | 5.23 | -2.7 dB |
| Peaking | 18 Hz    | 1.16 | 2.3 dB  |
| Peaking | 43 Hz    | 1.01 | -1.3 dB |
| Peaking | 95 Hz    | 1.59 | 2.6 dB  |
| Peaking | 193 Hz   | 0.45 | -1.4 dB |
| Peaking | 780 Hz   | 2.47 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Etymotic%20hf5/Etymotic%20hf5.png)