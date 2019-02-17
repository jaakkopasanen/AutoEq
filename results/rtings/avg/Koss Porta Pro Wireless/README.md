# Koss Porta Pro Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.0; 25 -3.7; 28 -4.6; 31 -5.5; 34 -6.2; 37 -6.8; 41 -7.4; 45 -8.0; 49 -8.5; 54 -8.9; 60 -9.5; 66 -10.0; 72 -10.3; 79 -10.7; 87 -11.1; 96 -11.5; 106 -11.8; 116 -12.0; 128 -12.2; 141 -12.3; 155 -12.3; 170 -12.2; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.8; 274 -10.5; 302 -10.3; 332 -10.1; 365 -9.8; 402 -9.6; 442 -9.2; 486 -9.0; 535 -8.6; 588 -8.3; 647 -7.9; 712 -7.5; 783 -7.1; 861 -6.8; 947 -6.6; 1042 -6.5; 1146 -6.5; 1261 -6.6; 1387 -7.0; 1526 -7.5; 1678 -8.3; 1846 -9.0; 2031 -9.1; 2234 -7.8; 2457 -5.8; 2703 -4.1; 2973 -3.9; 3270 -4.9; 3597 -4.6; 3957 -2.7; 4353 -0.5; 4788 -0.8; 5267 -7.8; 5793 -6.4; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  0.93 | 5.3 dB  |
| Peaking | 137 Hz   |  0.35 | -5.0 dB |
| Peaking | 140 Hz   |  1.16 | -0.9 dB |
| Peaking | 4338 Hz  |  3.53 | 6.4 dB  |
| Peaking | 21520 Hz |  2.27 | 1.0 dB  |
| Peaking | 1042 Hz  |  2.09 | 1.0 dB  |
| Peaking | 1961 Hz  |  2.65 | -3.1 dB |
| Peaking | 2774 Hz  |  4.48 | 3.1 dB  |
| Peaking | 5452 Hz  | 10.51 | -4.7 dB |
| Peaking | 6566 Hz  |  7.09 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20Porta%20Pro%20Wireless/Koss%20Porta%20Pro%20Wireless.png)