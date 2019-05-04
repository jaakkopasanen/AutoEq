# Corsair HS70 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.4; 28 -3.9; 31 -4.4; 34 -4.8; 37 -5.0; 41 -5.3; 45 -5.5; 49 -5.6; 54 -5.8; 60 -6.2; 66 -6.6; 72 -7.1; 79 -7.6; 87 -8.0; 96 -8.3; 106 -8.3; 116 -8.2; 128 -7.9; 141 -7.4; 155 -6.9; 170 -6.3; 187 -5.6; 206 -4.9; 227 -4.3; 249 -3.9; 274 -4.1; 302 -4.1; 332 -4.1; 365 -4.1; 402 -4.3; 442 -4.4; 486 -4.4; 535 -4.2; 588 -4.1; 647 -3.7; 712 -2.6; 783 -2.2; 861 -3.3; 947 -2.2; 1042 -1.6; 1146 -1.4; 1261 -1.2; 1387 -1.4; 1526 -1.9; 1678 -2.9; 1846 -3.9; 2031 -4.6; 2234 -4.7; 2457 -4.6; 2703 -4.5; 2973 -4.5; 3270 -4.2; 3597 -3.8; 3957 -3.3; 4353 -3.5; 4788 -6.0; 5267 -5.0; 5793 -2.5; 6373 -0.5; 7010 -1.9; 7711 -6.5; 8482 -11.2; 9330 -9.9; 10263 -8.8; 11289 -11.9; 12418 -13.4; 13660 -9.5; 15026 -4.6; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS70 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS70 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 102 Hz   | 1.2  | -4.2 dB |
| Peaking | 1162 Hz  | 1.52 | 3.3 dB  |
| Peaking | 6668 Hz  | 4.27 | 6.1 dB  |
| Peaking | 8576 Hz  | 3.43 | -6.7 dB |
| Peaking | 12210 Hz | 2.62 | -9.4 dB |
| Peaking | 20 Hz    | 2.56 | 2.1 dB  |
| Peaking | 254 Hz   | 3.54 | 1.1 dB  |
| Peaking | 2309 Hz  | 2.69 | -1.0 dB |
| Peaking | 4539 Hz  | 2.37 | 2.2 dB  |
| Peaking | 4911 Hz  | 5.86 | -4.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Corsair%20HS70%20Wireless/Corsair%20HS70%20Wireless.png)