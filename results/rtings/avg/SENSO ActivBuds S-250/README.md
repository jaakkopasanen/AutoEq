# SENSO ActivBuds S-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.6; 28 -9.0; 31 -9.4; 34 -9.8; 37 -10.1; 41 -10.5; 45 -10.9; 49 -11.2; 54 -11.7; 60 -12.2; 66 -12.8; 72 -13.4; 79 -14.0; 87 -14.7; 96 -15.5; 106 -16.1; 116 -16.8; 128 -17.4; 141 -17.9; 155 -18.4; 170 -18.9; 187 -19.2; 206 -19.5; 227 -19.5; 249 -19.5; 274 -19.3; 302 -19.0; 332 -18.5; 365 -17.9; 402 -17.2; 442 -16.3; 486 -15.2; 535 -13.8; 588 -12.3; 647 -10.5; 712 -8.7; 783 -7.0; 861 -5.6; 947 -4.4; 1042 -3.4; 1146 -2.3; 1261 -0.7; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.8; 2031 -3.6; 2234 -2.3; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SENSO ActivBuds S-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SENSO ActivBuds S-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 60 Hz   | 0.43 | -2.4 dB  |
| Peaking | 158 Hz  | 0.57 | -4.9 dB  |
| Peaking | 377 Hz  | 0.43 | -11.3 dB |
| Peaking | 1191 Hz | 0.62 | 9.5 dB   |
| Peaking | 4472 Hz | 1.14 | 5.5 dB   |
| Peaking | 2083 Hz | 4.95 | -4.5 dB  |
| Peaking | 2261 Hz | 1.66 | 2.4 dB   |
| Peaking | 4264 Hz | 3.2  | -1.0 dB  |
| Peaking | 6352 Hz | 2.9  | 4.6 dB   |
| Peaking | 7325 Hz | 1.54 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -8.4 dB  |
| Peaking | 250 Hz   | 1.41 | -11.7 dB |
| Peaking | 500 Hz   | 1.41 | -7.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SENSO%20ActivBuds%20S-250/SENSO%20ActivBuds%20S-250.png)