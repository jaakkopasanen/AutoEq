# Plantronics Backbeat Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -23.0; 23 -21.0; 25 -19.2; 28 -16.8; 31 -14.8; 34 -13.6; 37 -13.3; 41 -13.3; 45 -13.0; 49 -12.5; 54 -11.8; 60 -11.0; 66 -10.1; 72 -9.1; 79 -7.6; 87 -5.4; 96 -3.1; 106 -2.7; 116 -3.8; 128 -4.5; 141 -4.2; 155 -3.2; 170 -1.7; 187 -0.5; 206 -0.5; 227 -1.3; 249 -2.1; 274 -2.6; 302 -2.8; 332 -2.7; 365 -2.6; 402 -2.6; 442 -2.4; 486 -2.7; 535 -3.2; 588 -3.4; 647 -3.5; 712 -3.8; 783 -3.9; 861 -3.4; 947 -3.6; 1042 -3.9; 1146 -4.0; 1261 -4.0; 1387 -4.2; 1526 -4.2; 1678 -4.1; 1846 -6.0; 2031 -7.2; 2234 -7.3; 2457 -6.8; 2703 -6.3; 2973 -5.8; 3270 -5.6; 3597 -7.1; 3957 -9.3; 4353 -10.0; 4788 -8.9; 5267 -6.5; 5793 -3.8; 6373 -4.3; 7010 -6.9; 7711 -10.1; 8482 -9.7; 9330 -7.4; 10263 -8.6; 11289 -12.0; 12418 -13.6; 13660 -14.8; 15026 -14.6; 16529 -10.5; 18182 -6.4; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.61 | -18.1 dB |
| Peaking | 49 Hz    | 2.19 | -6.1 dB  |
| Peaking | 4219 Hz  | 3.56 | -5.2 dB  |
| Peaking | 12464 Hz | 0.87 | -4.2 dB  |
| Peaking | 14572 Hz | 1.24 | -7.5 dB  |
| Peaking | 102 Hz   | 3.64 | 4.9 dB   |
| Peaking | 148 Hz   | 0.5  | -19.2 dB |
| Peaking | 174 Hz   | 0.56 | 21.5 dB  |
| Peaking | 2204 Hz  | 3.65 | -3.0 dB  |
| Peaking | 5995 Hz  | 8.77 | 3.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.3 dB   |
| Peaking | 250 Hz   | 1.41 | 2.8 dB   |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 16000 Hz | 1.41 | -11.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20Backbeat%20Pro/Plantronics%20Backbeat%20Pro.png)