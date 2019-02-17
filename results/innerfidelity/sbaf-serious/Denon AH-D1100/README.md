# Denon AH-D1100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -11.3; 25 -11.9; 28 -12.6; 31 -13.2; 34 -13.7; 37 -14.2; 41 -14.8; 45 -15.3; 49 -15.7; 54 -16.1; 60 -16.5; 66 -16.9; 72 -17.1; 79 -17.4; 87 -17.7; 96 -17.8; 106 -17.5; 116 -17.2; 128 -17.6; 141 -17.8; 155 -18.3; 170 -16.7; 187 -17.2; 206 -17.8; 227 -17.5; 249 -16.6; 274 -15.3; 302 -13.4; 332 -11.1; 365 -8.6; 402 -5.8; 442 -3.8; 486 -3.6; 535 -4.3; 588 -5.3; 647 -6.3; 712 -7.2; 783 -7.2; 861 -7.2; 947 -6.7; 1042 -6.1; 1146 -5.5; 1261 -5.1; 1387 -5.3; 1526 -5.9; 1678 -6.2; 1846 -6.1; 2031 -6.6; 2234 -9.2; 2457 -8.3; 2703 -6.3; 2973 -3.8; 3270 -4.9; 3597 -4.7; 3957 -0.5; 4353 -2.1; 4788 -4.5; 5267 -3.1; 5793 -4.1; 6373 -4.4; 7010 -4.4; 7711 -6.3; 8482 -8.4; 9330 -9.7; 10263 -9.9; 11289 -8.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D1100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.14 | -5.7 dB |
| Peaking | 101 Hz  | 0.75 | -8.4 dB |
| Peaking | 223 Hz  | 2.11 | -7.9 dB |
| Peaking | 4139 Hz | 3.48 | 5.6 dB  |
| Peaking | 21 Hz   | 2.97 | 2.6 dB  |
| Peaking | 472 Hz  | 3.72 | 5.2 dB  |
| Peaking | 2284 Hz | 7.14 | -3.3 dB |
| Peaking | 6384 Hz | 2.53 | 2.5 dB  |
| Peaking | 9683 Hz | 2.55 | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB |
| Peaking | 125 Hz   | 1.41 | -9.0 dB |
| Peaking | 250 Hz   | 1.41 | -9.6 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1100/Denon%20AH-D1100.png)