# Razer Kraken USB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.3; 34 -2.2; 37 -3.1; 41 -4.2; 45 -5.2; 49 -6.2; 54 -7.4; 60 -8.8; 66 -10.0; 72 -11.0; 79 -11.9; 87 -12.6; 96 -13.0; 106 -13.1; 116 -13.2; 128 -13.1; 141 -12.9; 155 -12.5; 170 -11.9; 187 -11.1; 206 -10.2; 227 -9.5; 249 -9.7; 274 -10.7; 302 -11.8; 332 -12.8; 365 -13.3; 402 -13.5; 442 -13.2; 486 -13.7; 535 -13.8; 588 -12.3; 647 -10.7; 712 -9.7; 783 -8.3; 861 -6.7; 947 -5.7; 1042 -5.2; 1146 -4.5; 1261 -3.7; 1387 -2.7; 1526 -1.7; 1678 -1.0; 1846 -1.2; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.5; 6373 -6.8; 7010 -8.9; 7711 -10.0; 8482 -11.4; 9330 -10.3; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Razer Kraken USB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Razer Kraken USB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.81 | 7.1 dB  |
| Peaking | 102 Hz   | 0.8  | -7.4 dB |
| Peaking | 486 Hz   | 1.06 | -8.2 dB |
| Peaking | 3410 Hz  | 0.34 | 7.4 dB  |
| Peaking | 8183 Hz  | 1.76 | -9.8 dB |
| Peaking | 236 Hz   | 5.76 | 1.4 dB  |
| Peaking | 334 Hz   | 5.54 | -1.1 dB |
| Peaking | 5564 Hz  | 5.17 | 2.8 dB  |
| Peaking | 6495 Hz  | 7.01 | -2.8 dB |
| Peaking | 14848 Hz | 1.66 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -8.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)