# Sennheiser RS 195
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.6; 23 -15.6; 25 -15.4; 28 -15.2; 31 -14.9; 34 -14.6; 37 -14.3; 41 -13.9; 45 -13.7; 49 -13.9; 54 -14.4; 60 -14.9; 66 -15.0; 72 -14.1; 79 -11.9; 87 -9.3; 96 -7.2; 106 -5.8; 116 -4.8; 128 -4.1; 141 -4.3; 155 -4.8; 170 -5.2; 187 -5.3; 206 -4.9; 227 -4.1; 249 -3.6; 274 -3.6; 302 -4.0; 332 -4.6; 365 -5.0; 402 -5.4; 442 -5.9; 486 -6.4; 535 -6.7; 588 -6.7; 647 -6.6; 712 -6.4; 783 -6.1; 861 -6.2; 947 -6.2; 1042 -6.4; 1146 -7.0; 1261 -8.0; 1387 -9.2; 1526 -10.0; 1678 -9.1; 1846 -4.1; 2031 -0.5; 2234 -9.1; 2457 -13.5; 2703 -14.8; 2973 -14.9; 3270 -14.0; 3597 -11.8; 3957 -10.4; 4353 -7.9; 4788 -4.9; 5267 -3.6; 5793 -3.7; 6373 -0.8; 7010 -3.7; 7711 -6.0; 8482 -6.2; 9330 -8.2; 10263 -10.9; 11289 -10.5; 12418 -8.9; 13660 -9.6; 15026 -12.1; 16529 -10.4; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 195 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 195 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.11 | -9.9 dB |
| Peaking | 63 Hz    | 2.88 | -7.8 dB |
| Peaking | 3013 Hz  | 2.52 | -9.8 dB |
| Peaking | 6290 Hz  | 2.21 | 6.9 dB  |
| Peaking | 13326 Hz | 0.58 | -4.7 dB |
| Peaking | 128 Hz   | 3.07 | 3.0 dB  |
| Peaking | 266 Hz   | 2.02 | 2.9 dB  |
| Peaking | 1596 Hz  | 2.99 | -4.8 dB |
| Peaking | 1993 Hz  | 5.06 | 11.0 dB |
| Peaking | 2394 Hz  | 5.37 | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | 2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20RS%20195/Sennheiser%20RS%20195.png)