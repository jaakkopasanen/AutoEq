# JAYS q-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.2; 25 -5.2; 28 -5.3; 31 -5.4; 34 -5.6; 37 -5.6; 41 -5.7; 45 -5.8; 49 -6.0; 54 -6.2; 60 -6.5; 66 -6.7; 72 -6.8; 79 -7.2; 87 -7.5; 96 -7.8; 106 -8.0; 116 -8.3; 128 -8.3; 141 -8.6; 155 -8.9; 170 -9.1; 187 -9.2; 206 -9.1; 227 -9.1; 249 -8.9; 274 -8.9; 302 -8.5; 332 -8.2; 365 -8.3; 402 -8.4; 442 -8.1; 486 -7.7; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.9; 1526 -7.7; 1678 -8.5; 1846 -8.5; 2031 -8.1; 2234 -7.3; 2457 -5.9; 2703 -3.4; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -9.3; 9330 -12.2; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS q-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS q-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 192 Hz  | 0.87 | -2.7 dB |
| Peaking | 423 Hz  | 1.91 | -1.1 dB |
| Peaking | 1953 Hz | 1.31 | -7.7 dB |
| Peaking | 3633 Hz | 0.52 | 8.5 dB  |
| Peaking | 9130 Hz | 3.21 | -8.9 dB |
| Peaking | 26 Hz   | 1.02 | 1.4 dB  |
| Peaking | 2499 Hz | 4.06 | -3.0 dB |
| Peaking | 2878 Hz | 1.88 | 3.6 dB  |
| Peaking | 3578 Hz | 1.44 | -2.1 dB |
| Peaking | 6068 Hz | 6.21 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 9.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20q-Jays/JAYS%20q-Jays.png)