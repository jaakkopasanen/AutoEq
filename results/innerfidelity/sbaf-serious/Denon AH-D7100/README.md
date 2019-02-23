# Denon AH-D7100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.6; 25 -12.6; 28 -12.5; 31 -12.5; 34 -12.4; 37 -12.2; 41 -11.9; 45 -11.6; 49 -11.2; 54 -10.7; 60 -10.6; 66 -11.0; 72 -11.5; 79 -11.9; 87 -12.5; 96 -13.4; 106 -13.6; 116 -13.4; 128 -13.4; 141 -13.2; 155 -12.6; 170 -11.4; 187 -11.2; 206 -9.7; 227 -7.5; 249 -5.2; 274 -2.6; 302 -1.2; 332 -1.2; 365 -1.9; 402 -2.6; 442 -3.1; 486 -3.8; 535 -4.4; 588 -4.7; 647 -5.6; 712 -6.4; 783 -6.8; 861 -7.3; 947 -7.7; 1042 -8.1; 1146 -8.4; 1261 -8.8; 1387 -9.7; 1526 -10.8; 1678 -11.6; 1846 -11.6; 2031 -10.9; 2234 -9.4; 2457 -6.3; 2703 -5.7; 2973 -6.1; 3270 -5.2; 3597 -2.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.7; 5793 -4.3; 6373 -5.0; 7010 -4.0; 7711 -6.2; 8482 -8.9; 9330 -12.0; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -10.5; 18182 -13.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D7100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.94 | -3.9 dB  |
| Peaking | 294 Hz   | 0.17 | -14.2 dB |
| Peaking | 380 Hz   | 0.59 | 19.5 dB  |
| Peaking | 4335 Hz  | 1.85 | 8.5 dB   |
| Peaking | 17952 Hz | 1.73 | -7.9 dB  |
| Peaking | 63 Hz    | 2.47 | 2.3 dB   |
| Peaking | 142 Hz   | 1.61 | -2.1 dB  |
| Peaking | 1813 Hz  | 3.36 | -3.7 dB  |
| Peaking | 2305 Hz  | 0.05 | 0.7 dB   |
| Peaking | 9114 Hz  | 5.76 | -7.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -8.7 dB |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)