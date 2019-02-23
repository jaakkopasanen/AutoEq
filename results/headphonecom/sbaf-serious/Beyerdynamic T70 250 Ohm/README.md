# Beyerdynamic T70 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.4; 25 -5.5; 28 -5.7; 31 -5.8; 34 -6.0; 37 -6.1; 41 -6.2; 45 -6.3; 49 -6.4; 54 -6.5; 60 -6.6; 66 -6.6; 72 -6.7; 79 -6.6; 87 -6.5; 96 -6.9; 106 -7.7; 116 -8.4; 128 -9.0; 141 -9.4; 155 -9.2; 170 -8.2; 187 -8.8; 206 -8.4; 227 -7.7; 249 -7.3; 274 -7.2; 302 -7.1; 332 -7.3; 365 -7.6; 402 -7.9; 442 -8.2; 486 -8.1; 535 -6.6; 588 -6.7; 647 -6.8; 712 -6.8; 783 -6.8; 861 -6.9; 947 -6.8; 1042 -6.7; 1146 -6.6; 1261 -6.6; 1387 -7.0; 1526 -7.4; 1678 -7.3; 1846 -6.4; 2031 -5.6; 2234 -4.0; 2457 -3.5; 2703 -4.2; 2973 -4.1; 3270 -4.4; 3597 -4.6; 3957 -0.5; 4353 -2.4; 4788 -3.5; 5267 -0.7; 5793 -0.5; 6373 -1.3; 7010 -8.6; 7711 -12.9; 8482 -14.8; 9330 -14.0; 10263 -8.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 160 Hz   | 1.17 | -2.6 dB  |
| Peaking | 4021 Hz  | 1.35 | 4.2 dB   |
| Peaking | 5538 Hz  | 5.14 | 4.2 dB   |
| Peaking | 6219 Hz  | 6.88 | 5.2 dB   |
| Peaking | 8393 Hz  | 2.67 | -10.1 dB |
| Peaking | 10 Hz    | 0.34 | 1.4 dB   |
| Peaking | 444 Hz   | 4.99 | -1.7 dB  |
| Peaking | 2150 Hz  | 1.27 | -2.5 dB  |
| Peaking | 2284 Hz  | 2.93 | 4.3 dB   |
| Peaking | 11219 Hz | 6.05 | 2.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70%20250%20Ohm/Beyerdynamic%20T70%20250%20Ohm.png)