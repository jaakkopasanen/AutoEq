# Noontec Zoro II Wireless Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.7; 37 -8.7; 41 -8.8; 45 -8.8; 49 -8.9; 54 -8.9; 60 -9.0; 66 -9.1; 72 -9.2; 79 -9.5; 87 -10.0; 96 -10.6; 106 -11.1; 116 -11.3; 128 -11.6; 141 -11.9; 155 -12.0; 170 -11.9; 187 -12.0; 206 -11.9; 227 -11.6; 249 -11.4; 274 -10.9; 302 -10.6; 332 -10.0; 365 -9.7; 402 -9.5; 442 -9.2; 486 -8.9; 535 -8.6; 588 -7.7; 647 -7.1; 712 -6.8; 783 -6.2; 861 -6.2; 947 -6.0; 1042 -6.0; 1146 -6.0; 1261 -6.6; 1387 -7.2; 1526 -7.7; 1678 -8.0; 1846 -7.7; 2031 -6.8; 2234 -6.0; 2457 -5.2; 2703 -4.7; 2973 -4.0; 3270 -4.3; 3597 -3.3; 3957 -0.5; 4353 -1.9; 4788 -4.3; 5267 -4.8; 5793 -1.7; 6373 -0.6; 7010 -3.5; 7711 -5.8; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro II Wireless Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro II Wireless Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.51 | -2.2 dB |
| Peaking | 122 Hz  | 1.05 | -2.2 dB |
| Peaking | 224 Hz  | 0.63 | -4.7 dB |
| Peaking | 3982 Hz | 3.81 | 5.3 dB  |
| Peaking | 6248 Hz | 5.36 | 5.9 dB  |
| Peaking | 506 Hz  | 2.3  | -1.1 dB |
| Peaking | 953 Hz  | 0.72 | 1.4 dB  |
| Peaking | 1645 Hz | 2.03 | -2.5 dB |
| Peaking | 2728 Hz | 3.28 | 1.5 dB  |
| Peaking | 3392 Hz | 0.23 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro%20II%20Wireless%20Passive/Noontec%20Zoro%20II%20Wireless%20Passive.png)