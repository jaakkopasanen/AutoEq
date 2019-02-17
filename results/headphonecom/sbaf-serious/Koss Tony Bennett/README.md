# Koss Tony Bennett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -2.6; 25 -3.2; 28 -3.9; 31 -4.4; 34 -4.9; 37 -5.3; 41 -5.9; 45 -6.3; 49 -6.7; 54 -7.2; 60 -7.6; 66 -7.6; 72 -6.6; 79 -4.4; 87 -4.3; 96 -7.1; 106 -8.6; 116 -9.5; 128 -10.2; 141 -10.8; 155 -11.2; 170 -10.7; 187 -11.5; 206 -11.4; 227 -11.0; 249 -10.6; 274 -9.5; 302 -7.5; 332 -5.9; 365 -5.2; 402 -5.8; 442 -6.7; 486 -6.9; 535 -6.9; 588 -6.3; 647 -6.8; 712 -6.4; 783 -5.6; 861 -4.9; 947 -6.7; 1042 -6.0; 1146 -5.2; 1261 -4.4; 1387 -4.1; 1526 -4.2; 1678 -4.1; 1846 -3.8; 2031 -3.5; 2234 -3.7; 2457 -3.4; 2703 -2.9; 2973 -3.4; 3270 -3.4; 3597 -2.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Tony Bennett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Tony Bennett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.7  | 4.6 dB  |
| Peaking | 83 Hz   | 6.97 | 4.4 dB  |
| Peaking | 170 Hz  | 1.17 | -5.4 dB |
| Peaking | 2041 Hz | 0.7  | 2.5 dB  |
| Peaking | 4947 Hz | 1.64 | 6.1 dB  |
| Peaking | 62 Hz   | 4.74 | -1.1 dB |
| Peaking | 251 Hz  | 4.18 | -1.7 dB |
| Peaking | 351 Hz  | 4.14 | 2.6 dB  |
| Peaking | 6386 Hz | 5.25 | 3.0 dB  |
| Peaking | 8184 Hz | 1.55 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Tony%20Bennett/Koss%20Tony%20Bennett.png)