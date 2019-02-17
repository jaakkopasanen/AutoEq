# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.5; 23 -14.0; 25 -14.4; 28 -14.9; 31 -15.4; 34 -15.7; 37 -16.0; 41 -16.3; 45 -16.6; 49 -16.9; 54 -17.2; 60 -17.5; 66 -17.8; 72 -17.9; 79 -18.1; 87 -18.1; 96 -17.9; 106 -17.5; 116 -17.6; 128 -18.6; 141 -19.6; 155 -18.8; 170 -17.6; 187 -18.6; 206 -18.4; 227 -17.7; 249 -16.3; 274 -14.7; 302 -12.5; 332 -10.2; 365 -7.6; 402 -5.1; 442 -3.4; 486 -3.1; 535 -3.9; 588 -5.0; 647 -6.0; 712 -6.7; 783 -7.1; 861 -7.0; 947 -6.7; 1042 -6.2; 1146 -6.0; 1261 -6.0; 1387 -6.3; 1526 -7.4; 1678 -8.4; 1846 -9.5; 2031 -9.6; 2234 -8.4; 2457 -6.1; 2703 -3.7; 2973 -1.6; 3270 -4.3; 3597 -3.0; 3957 -0.5; 4353 -2.9; 4788 -7.2; 5267 -5.6; 5793 -4.0; 6373 -3.2; 7010 -4.4; 7711 -6.2; 8482 -7.0; 9330 -9.6; 10263 -10.4; 11289 -8.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 3 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.88 | -7.5 dB |
| Peaking | 147 Hz   | 1.85 | -7.8 dB |
| Peaking | 226 Hz   | 2.7  | -8.3 dB |
| Peaking | 23 Hz    | 0.33 | -6.5 dB |
| Peaking | 473 Hz   | 3.57 | 5.3 dB  |
| Peaking | 3884 Hz  | 4.46 | 6.3 dB  |
| Peaking | 6246 Hz  | 5.74 | 4.2 dB  |
| Peaking | 10029 Hz | 3.8  | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.2 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB |
| Peaking | 125 Hz   | 1.41 | -9.9 dB |
| Peaking | 250 Hz   | 1.41 | -9.2 dB |
| Peaking | 500 Hz   | 1.41 | 5.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)