# Yamaha YH100 Sn130216
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -0.7; 37 -0.9; 41 -1.1; 45 -1.2; 49 -1.3; 54 -1.4; 60 -1.5; 66 -1.6; 72 -1.8; 79 -2.0; 87 -2.3; 96 -2.7; 106 -2.9; 116 -3.1; 128 -3.4; 141 -3.7; 155 -3.9; 170 -4.0; 187 -4.1; 206 -4.3; 227 -4.3; 249 -4.3; 274 -4.3; 302 -4.2; 332 -4.4; 365 -4.5; 402 -4.6; 442 -4.6; 486 -5.0; 535 -5.2; 588 -5.3; 647 -5.7; 712 -6.3; 783 -6.6; 861 -7.1; 947 -6.6; 1042 -5.9; 1146 -4.3; 1261 -1.4; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.6; 2031 -3.0; 2234 -5.3; 2457 -2.4; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha YH100 Sn130216 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH100 Sn130216 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.68 | 4.0 dB  |
| Peaking | 60 Hz   | 0.4  | 4.0 dB  |
| Peaking | 339 Hz  | 1.57 | 1.4 dB  |
| Peaking | 1525 Hz | 2.64 | 5.8 dB  |
| Peaking | 4156 Hz | 1.01 | 6.7 dB  |
| Peaking | 919 Hz  | 3.24 | -1.9 dB |
| Peaking | 1283 Hz | 8.15 | 1.9 dB  |
| Peaking | 4282 Hz | 5.51 | -1.2 dB |
| Peaking | 6384 Hz | 2.42 | 4.7 dB  |
| Peaking | 7471 Hz | 1.75 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 2.1 dB  |
| Peaking | 250 Hz   | 1.41 | 1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH100%20Sn130216/Yamaha%20YH100%20Sn130216.png)