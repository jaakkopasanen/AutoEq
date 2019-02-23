# Razer Kraken USB
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.5; 34 -2.5; 37 -3.3; 41 -4.4; 45 -5.4; 49 -6.4; 54 -7.6; 60 -8.9; 66 -10.2; 72 -11.2; 79 -12.1; 87 -12.8; 96 -13.2; 106 -13.4; 116 -13.4; 128 -13.4; 141 -13.1; 155 -12.7; 170 -12.1; 187 -11.3; 206 -10.3; 227 -9.6; 249 -9.8; 274 -10.8; 302 -11.9; 332 -12.8; 365 -13.4; 402 -13.5; 442 -13.2; 486 -13.8; 535 -13.8; 588 -12.2; 647 -10.6; 712 -9.6; 783 -8.1; 861 -6.6; 947 -5.6; 1042 -5.1; 1146 -4.4; 1261 -3.5; 1387 -2.5; 1526 -1.5; 1678 -0.8; 1846 -0.9; 2031 -0.7; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.6; 6373 -7.7; 7010 -8.8; 7711 -9.2; 8482 -11.8; 9330 -12.0; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
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

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.82 | 7.0 dB   |
| Peaking | 102 Hz  | 0.8  | -7.6 dB  |
| Peaking | 487 Hz  | 1.03 | -8.4 dB  |
| Peaking | 3409 Hz | 0.3  | 7.5 dB   |
| Peaking | 8400 Hz | 1.61 | -10.3 dB |
| Peaking | 170 Hz  | 2.23 | -2.0 dB  |
| Peaking | 226 Hz  | 1.21 | 2.1 dB   |
| Peaking | 322 Hz  | 3.06 | -2.0 dB  |
| Peaking | 5570 Hz | 4.86 | 3.0 dB   |
| Peaking | 6457 Hz | 7.67 | -4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | -8.1 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Razer%20Kraken%20USB/Razer%20Kraken%20USB.png)