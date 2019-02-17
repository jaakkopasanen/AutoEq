# AKG K701
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -2.2; 54 -2.9; 60 -2.8; 66 -2.0; 72 -3.7; 79 -4.7; 87 -5.4; 96 -5.8; 106 -6.1; 116 -6.6; 128 -7.1; 141 -7.3; 155 -7.5; 170 -7.6; 187 -7.9; 206 -7.7; 227 -7.9; 249 -7.9; 274 -7.6; 302 -7.5; 332 -7.3; 365 -7.2; 402 -7.0; 442 -6.7; 486 -6.6; 535 -6.2; 588 -4.7; 647 -5.5; 712 -5.4; 783 -5.8; 861 -6.1; 947 -6.5; 1042 -6.6; 1146 -6.9; 1261 -7.2; 1387 -7.4; 1526 -8.1; 1678 -8.6; 1846 -9.7; 2031 -10.8; 2234 -11.2; 2457 -10.5; 2703 -9.4; 2973 -9.1; 3270 -8.6; 3597 -8.5; 3957 -8.9; 4353 -9.5; 4788 -8.5; 5267 -9.0; 5793 -11.8; 6373 -11.6; 7010 -10.4; 7711 -10.9; 8482 -10.3; 9330 -9.1; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.46 | 6.3 dB  |
| Peaking | 163 Hz   | 0.92 | -2.2 dB |
| Peaking | 2236 Hz  | 1.95 | -4.6 dB |
| Peaking | 6100 Hz  | 2.18 | -4.6 dB |
| Peaking | 8264 Hz  | 3.55 | -2.9 dB |
| Peaking | 478 Hz   | 1.11 | -1.3 dB |
| Peaking | 611 Hz   | 1.67 | 2.5 dB  |
| Peaking | 4543 Hz  | 2.88 | -1.8 dB |
| Peaking | 5025 Hz  | 6.65 | 2.7 dB  |
| Peaking | 11043 Hz | 4.35 | 0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K701/AKG%20K701.png)