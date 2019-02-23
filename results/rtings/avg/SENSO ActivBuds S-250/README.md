# SENSO ActivBuds S-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.6; 25 -4.0; 28 -4.4; 31 -4.8; 34 -5.1; 37 -5.4; 41 -5.8; 45 -6.2; 49 -6.6; 54 -7.2; 60 -8.0; 66 -8.9; 72 -9.6; 79 -10.5; 87 -11.4; 96 -12.5; 106 -13.6; 116 -14.8; 128 -15.9; 141 -16.9; 155 -17.7; 170 -18.5; 187 -19.1; 206 -19.6; 227 -19.8; 249 -19.7; 274 -19.6; 302 -19.2; 332 -18.8; 365 -18.2; 402 -17.4; 442 -16.5; 486 -15.3; 535 -13.9; 588 -12.4; 647 -10.6; 712 -8.8; 783 -7.2; 861 -5.7; 947 -4.5; 1042 -3.5; 1146 -2.4; 1261 -0.8; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -1.7; 2031 -3.4; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SENSO ActivBuds S-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SENSO ActivBuds S-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.27 | 4.4 dB   |
| Peaking | 213 Hz  | 0.4  | -14.4 dB |
| Peaking | 452 Hz  | 1.05 | -3.0 dB  |
| Peaking | 1264 Hz | 0.65 | 8.0 dB   |
| Peaking | 4466 Hz | 1.13 | 5.5 dB   |
| Peaking | 2047 Hz | 5.29 | -4.2 dB  |
| Peaking | 2281 Hz | 1.7  | 2.2 dB   |
| Peaking | 4266 Hz | 3.29 | -1.0 dB  |
| Peaking | 6329 Hz | 2.92 | 4.6 dB   |
| Peaking | 7361 Hz | 1.55 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.8 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -7.3 dB  |
| Peaking | 250 Hz   | 1.41 | -12.6 dB |
| Peaking | 500 Hz   | 1.41 | -7.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SENSO%20ActivBuds%20S-250/SENSO%20ActivBuds%20S-250.png)