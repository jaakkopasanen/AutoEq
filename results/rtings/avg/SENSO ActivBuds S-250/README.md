# SENSO ActivBuds S-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.2; 25 -6.5; 28 -6.9; 31 -7.3; 34 -7.7; 37 -8.0; 41 -8.4; 45 -8.8; 49 -9.1; 54 -9.7; 60 -10.6; 66 -11.4; 72 -12.1; 79 -13.0; 87 -14.0; 96 -15.0; 106 -16.2; 116 -17.3; 128 -18.4; 141 -19.4; 155 -20.3; 170 -21.0; 187 -21.7; 206 -22.1; 227 -22.3; 249 -22.3; 274 -22.1; 302 -21.8; 332 -21.4; 365 -20.8; 402 -20.0; 442 -19.1; 486 -17.9; 535 -16.5; 588 -15.0; 647 -13.2; 712 -11.4; 783 -9.7; 861 -8.2; 947 -7.0; 1042 -6.1; 1146 -4.9; 1261 -3.2; 1387 -1.2; 1526 -0.5; 1678 -1.1; 1846 -4.3; 2031 -6.0; 2234 -4.3; 2457 -1.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SENSO ActivBuds S-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SENSO ActivBuds S-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 1.2  | 1.8 dB   |
| Peaking | 146 Hz  | 0.75 | -5.0 dB  |
| Peaking | 302 Hz  | 0.49 | -13.9 dB |
| Peaking | 1325 Hz | 1.29 | 7.0 dB   |
| Peaking | 4071 Hz | 0.96 | 6.7 dB   |
| Peaking | 1622 Hz | 5.26 | 3.0 dB   |
| Peaking | 2057 Hz | 3    | -4.5 dB  |
| Peaking | 2538 Hz | 3.04 | 3.8 dB   |
| Peaking | 6152 Hz | 2.66 | 6.2 dB   |
| Peaking | 6625 Hz | 1.08 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -9.0 dB  |
| Peaking | 250 Hz   | 1.41 | -14.6 dB |
| Peaking | 500 Hz   | 1.41 | -9.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SENSO%20ActivBuds%20S-250/SENSO%20ActivBuds%20S-250.png)