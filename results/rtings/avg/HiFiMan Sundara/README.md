# HiFiMan Sundara
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.7; 34 -3.1; 37 -3.3; 41 -3.7; 45 -3.9; 49 -4.2; 54 -4.4; 60 -4.7; 66 -4.9; 72 -5.1; 79 -5.3; 87 -5.7; 96 -5.9; 106 -6.3; 116 -6.5; 128 -6.8; 141 -7.0; 155 -7.2; 170 -7.3; 187 -7.5; 206 -7.5; 227 -7.5; 249 -7.6; 274 -7.7; 302 -7.8; 332 -8.0; 365 -8.2; 402 -8.2; 442 -7.6; 486 -7.1; 535 -7.7; 588 -7.9; 647 -7.9; 712 -7.8; 783 -7.7; 861 -7.6; 947 -6.5; 1042 -5.9; 1146 -5.9; 1261 -5.8; 1387 -5.6; 1526 -5.3; 1678 -5.3; 1846 -4.9; 2031 -4.8; 2234 -3.3; 2457 -4.6; 2703 -5.3; 2973 -8.0; 3270 -9.0; 3597 -9.7; 3957 -10.0; 4353 -9.4; 4788 -11.6; 5267 -9.2; 5793 -3.7; 6373 -8.3; 7010 -10.7; 7711 -10.6; 8482 -11.1; 9330 -9.3; 10263 -6.0; 11289 -6.0; 12418 -8.8; 13660 -11.1; 15026 -11.0; 16529 -10.4; 18182 -10.7; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Sundara GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.43 | 6.6 dB  |
| Peaking | 313 Hz   | 0.6  | -2.1 dB |
| Peaking | 4283 Hz  | 2.62 | -4.0 dB |
| Peaking | 17999 Hz | 0.21 | -4.1 dB |
| Peaking | 20602 Hz | 0.92 | -4.9 dB |
| Peaking | 2709 Hz  | 1.31 | 4.7 dB  |
| Peaking | 3106 Hz  | 3.24 | -4.8 dB |
| Peaking | 5855 Hz  | 7.74 | 7.3 dB  |
| Peaking | 9024 Hz  | 0.73 | -5.8 dB |
| Peaking | 10720 Hz | 2.14 | 8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | -2.8 dB |
| Peaking | 16000 Hz | 1.41 | -6.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HiFiMan%20Sundara/HiFiMan%20Sundara.png)