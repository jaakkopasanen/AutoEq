# Sennheiser MX 560
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.9; 106 -1.5; 116 -1.9; 128 -2.3; 141 -2.7; 155 -2.8; 170 -3.0; 187 -3.3; 206 -3.6; 227 -3.5; 249 -3.5; 274 -3.7; 302 -3.9; 332 -4.1; 365 -4.6; 402 -4.9; 442 -4.7; 486 -3.7; 535 -4.2; 588 -4.5; 647 -4.9; 712 -5.2; 783 -5.5; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.6; 1387 -8.7; 1526 -10.2; 1678 -11.7; 1846 -13.7; 2031 -15.9; 2234 -17.9; 2457 -19.1; 2703 -18.5; 2973 -15.9; 3270 -12.0; 3597 -9.9; 3957 -9.7; 4353 -11.4; 4788 -12.5; 5267 -12.8; 5793 -13.0; 6373 -12.0; 7010 -10.5; 7711 -9.4; 8482 -11.4; 9330 -13.0; 10263 -10.5; 11289 -6.6; 12418 -6.5; 13660 -6.9; 15026 -8.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.23 | 6.3 dB   |
| Peaking | 581 Hz   | 0.85 | 1.8 dB   |
| Peaking | 2385 Hz  | 1.85 | -12.5 dB |
| Peaking | 6831 Hz  | 0.84 | -4.8 dB  |
| Peaking | 22050 Hz | 2.14 | -3.9 dB  |
| Peaking | 3766 Hz  | 3.74 | 4.4 dB   |
| Peaking | 4652 Hz  | 0.99 | -2.3 dB  |
| Peaking | 7613 Hz  | 3.02 | 4.2 dB   |
| Peaking | 9438 Hz  | 2.73 | -4.5 dB  |
| Peaking | 11414 Hz | 3.07 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 5.0 dB   |
| Peaking | 125 Hz   | 1.41 | 3.3 dB   |
| Peaking | 250 Hz   | 1.41 | 1.9 dB   |
| Peaking | 500 Hz   | 1.41 | 1.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -10.4 dB |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)