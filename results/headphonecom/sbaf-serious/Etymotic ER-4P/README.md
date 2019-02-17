# Etymotic ER-4P
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -0.8; 45 -1.1; 49 -1.4; 54 -1.7; 60 -2.1; 66 -2.5; 72 -2.8; 79 -3.1; 87 -3.6; 96 -3.9; 106 -4.2; 116 -4.4; 128 -4.7; 141 -5.0; 155 -5.2; 170 -5.4; 187 -5.5; 206 -5.6; 227 -5.7; 249 -5.7; 274 -5.7; 302 -5.6; 332 -5.4; 365 -5.3; 402 -5.2; 442 -5.2; 486 -5.2; 535 -5.3; 588 -5.0; 647 -5.0; 712 -5.0; 783 -5.1; 861 -5.5; 947 -6.1; 1042 -6.8; 1146 -7.6; 1261 -8.4; 1387 -9.4; 1526 -10.4; 1678 -11.1; 1846 -11.3; 2031 -11.4; 2234 -11.1; 2457 -10.2; 2703 -8.5; 2973 -6.0; 3270 -3.2; 3597 -1.3; 3957 -1.6; 4353 -2.9; 4788 -2.9; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB   |
| Peaking | 889 Hz   | 0.64 | 5.6 dB   |
| Peaking | 2280 Hz  | 0.44 | -10.2 dB |
| Peaking | 3568 Hz  | 1.67 | 11.5 dB  |
| Peaking | 5852 Hz  | 2.18 | 8.3 dB   |
| Peaking | 7693 Hz  | 7.63 | -1.0 dB  |
| Peaking | 13936 Hz | 0.96 | 1.0 dB   |
| Peaking | 14897 Hz | 4.53 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.2 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4P/Etymotic%20ER-4P.png)