# Ortofon 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.2; 60 -1.1; 66 -1.8; 72 -2.5; 79 -3.1; 87 -3.5; 96 -3.7; 106 -3.7; 116 -3.9; 128 -3.9; 141 -3.9; 155 -3.7; 170 -2.9; 187 -2.5; 206 -1.3; 227 -0.5; 249 -0.5; 274 -0.5; 302 -1.3; 332 -4.3; 365 -7.9; 402 -10.6; 442 -12.0; 486 -12.5; 535 -12.3; 588 -11.6; 647 -9.2; 712 -9.5; 783 -9.8; 861 -10.1; 947 -10.1; 1042 -10.6; 1146 -9.9; 1261 -9.5; 1387 -9.9; 1526 -11.1; 1678 -10.8; 1846 -7.9; 2031 -4.1; 2234 -0.6; 2457 -2.7; 2703 -3.0; 2973 -0.5; 3270 -0.5; 3597 -4.1; 3957 -8.4; 4353 -8.6; 4788 -10.0; 5267 -11.5; 5793 -4.1; 6373 -1.2; 7010 -6.3; 7711 -9.9; 8482 -12.2; 9330 -12.5; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.3; 16529 -11.5; 18182 -12.1; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.55 | 5.9 dB   |
| Peaking | 281 Hz   | 0.18 | 46.1 dB  |
| Peaking | 392 Hz   | 0.12 | -43.3 dB |
| Peaking | 3482 Hz  | 0.92 | 15.0 dB  |
| Peaking | 4183 Hz  | 2.64 | -11.2 dB |
| Peaking | 1648 Hz  | 4.24 | -4.5 dB  |
| Peaking | 2206 Hz  | 4.02 | 4.4 dB   |
| Peaking | 6328 Hz  | 6.5  | 8.6 dB   |
| Peaking | 12981 Hz | 1.37 | 9.5 dB   |
| Peaking | 20689 Hz | 0.06 | -6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 7.6 dB  |
| Peaking | 500 Hz   | 1.41 | -6.6 dB |
| Peaking | 1000 Hz  | 1.41 | -4.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%201/Ortofon%201.png)