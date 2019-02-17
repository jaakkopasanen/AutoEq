# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.1; 23 -11.2; 25 -11.2; 28 -11.1; 31 -11.0; 34 -10.9; 37 -10.8; 41 -10.5; 45 -10.2; 49 -9.8; 54 -9.3; 60 -9.2; 66 -9.6; 72 -10.1; 79 -10.5; 87 -11.1; 96 -11.9; 106 -12.2; 116 -12.0; 128 -12.0; 141 -11.8; 155 -11.2; 170 -10.0; 187 -9.8; 206 -8.3; 227 -6.1; 249 -3.8; 274 -1.2; 302 -0.5; 332 -0.5; 365 -0.6; 402 -1.2; 442 -1.7; 486 -2.4; 535 -3.0; 588 -3.3; 647 -4.2; 712 -5.0; 783 -5.4; 861 -5.9; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.4; 1387 -8.2; 1526 -9.4; 1678 -10.2; 1846 -10.1; 2031 -9.5; 2234 -8.0; 2457 -4.9; 2703 -4.3; 2973 -4.6; 3270 -3.8; 3597 -1.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -7.8; 9330 -10.6; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.1; 18182 -12.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.94 | -4.5 dB |
| Peaking | 141 Hz   | 0.69 | -7.0 dB |
| Peaking | 323 Hz   | 1.2  | 9.4 dB  |
| Peaking | 4526 Hz  | 2.04 | 7.1 dB  |
| Peaking | 17994 Hz | 1.91 | -6.3 dB |
| Peaking | 578 Hz   | 2.82 | 1.3 dB  |
| Peaking | 1912 Hz  | 1.64 | -6.7 dB |
| Peaking | 2484 Hz  | 1.54 | 4.0 dB  |
| Peaking | 6713 Hz  | 8.39 | 2.4 dB  |
| Peaking | 9140 Hz  | 6.58 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.5 dB |
| Peaking | 250 Hz   | 1.41 | 3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)