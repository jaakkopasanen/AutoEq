# Etymotic ER-4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.1; 72 -1.4; 79 -1.8; 87 -2.3; 96 -2.5; 106 -2.8; 116 -3.0; 128 -3.3; 141 -3.6; 155 -4.1; 170 -4.3; 187 -4.4; 206 -4.5; 227 -4.5; 249 -4.5; 274 -4.5; 302 -4.4; 332 -4.3; 365 -4.3; 402 -4.3; 442 -4.4; 486 -4.3; 535 -4.4; 588 -4.2; 647 -4.2; 712 -4.4; 783 -4.7; 861 -5.2; 947 -6.0; 1042 -6.9; 1146 -7.9; 1261 -8.9; 1387 -10.2; 1526 -11.5; 1678 -12.7; 1846 -14.1; 2031 -15.2; 2234 -15.5; 2457 -14.9; 2703 -12.9; 2973 -10.6; 3270 -8.4; 3597 -7.4; 3957 -8.2; 4353 -9.7; 4788 -9.1; 5267 -6.7; 5793 -4.7; 6373 -5.0; 7010 -7.5; 7711 -10.7; 8482 -10.5; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.1; 16529 -14.0; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.05 | 5.2 dB  |
| Peaking | 1678 Hz  | 2.86 | -3.6 dB |
| Peaking | 2287 Hz  | 2.1  | -8.7 dB |
| Peaking | 16159 Hz | 3.73 | -5.5 dB |
| Peaking | 16160 Hz | 2.93 | -3.3 dB |
| Peaking | 170 Hz   | 1.47 | -1.6 dB |
| Peaking | 639 Hz   | 1.74 | 2.0 dB  |
| Peaking | 4598 Hz  | 4.02 | -4.6 dB |
| Peaking | 6852 Hz  | 1.1  | 5.6 dB  |
| Peaking | 7924 Hz  | 2.67 | -9.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -9.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -4.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20ER-4S/Etymotic%20ER-4S.png)