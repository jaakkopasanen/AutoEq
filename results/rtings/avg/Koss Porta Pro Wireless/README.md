# Koss Porta Pro Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.1; 25 -2.8; 28 -3.7; 31 -4.6; 34 -5.3; 37 -5.9; 41 -6.5; 45 -7.1; 49 -7.5; 54 -8.0; 60 -8.6; 66 -9.1; 72 -9.4; 79 -9.8; 87 -10.2; 96 -10.6; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.4; 170 -11.3; 187 -11.0; 206 -10.6; 227 -10.2; 249 -9.9; 274 -9.6; 302 -9.4; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.3; 486 -8.1; 535 -7.7; 588 -7.4; 647 -7.0; 712 -6.6; 783 -6.2; 861 -5.9; 947 -5.7; 1042 -5.6; 1146 -5.6; 1261 -5.7; 1387 -6.1; 1526 -6.6; 1678 -7.4; 1846 -8.1; 2031 -8.2; 2234 -6.9; 2457 -4.9; 2703 -3.2; 2973 -3.0; 3270 -3.9; 3597 -3.7; 3957 -1.8; 4353 -0.5; 4788 -0.6; 5267 -6.9; 5793 -5.5; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 0.87 | 6.1 dB  |
| Peaking | 139 Hz   | 0.45 | -4.9 dB |
| Peaking | 949 Hz   | 2.44 | 1.4 dB  |
| Peaking | 4229 Hz  | 1.96 | 5.6 dB  |
| Peaking | 22050 Hz | 2.21 | 1.5 dB  |
| Peaking | 2040 Hz  | 2.46 | -4.7 dB |
| Peaking | 2870 Hz  | 1.17 | 4.5 dB  |
| Peaking | 3512 Hz  | 3.54 | -4.2 dB |
| Peaking | 5433 Hz  | 9.53 | -5.3 dB |
| Peaking | 6493 Hz  | 8.93 | 3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro%20Wireless/Koss%20Porta%20Pro%20Wireless.png)