# AKG K3003 High Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.2; 28 -2.8; 31 -3.3; 34 -3.7; 37 -4.1; 41 -4.5; 45 -4.9; 49 -5.3; 54 -5.7; 60 -6.2; 66 -6.6; 72 -7.0; 79 -7.4; 87 -7.7; 96 -8.0; 106 -8.3; 116 -8.5; 128 -8.8; 141 -8.9; 155 -9.1; 170 -9.0; 187 -9.1; 206 -8.9; 227 -8.8; 249 -8.5; 274 -8.3; 302 -7.9; 332 -7.4; 365 -7.0; 402 -6.5; 442 -6.2; 486 -5.8; 535 -5.4; 588 -4.9; 647 -4.4; 712 -4.2; 783 -3.8; 861 -3.9; 947 -3.9; 1042 -4.4; 1146 -4.6; 1261 -4.8; 1387 -5.0; 1526 -5.4; 1678 -5.9; 1846 -6.0; 2031 -5.9; 2234 -5.7; 2457 -5.6; 2703 -5.6; 2973 -5.7; 3270 -3.9; 3597 -0.5; 3957 -0.6; 4353 -5.5; 4788 -10.4; 5267 -9.9; 5793 -8.6; 6373 -3.8; 7010 -3.9; 7711 -6.1; 8482 -8.7; 9330 -14.4; 10263 -14.1; 11289 -7.3; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 High Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.9  | 5.0 dB   |
| Peaking | 154 Hz   | 0.97 | -3.1 dB  |
| Peaking | 4955 Hz  | 0.94 | 8.4 dB   |
| Peaking | 5097 Hz  | 3.21 | -13.2 dB |
| Peaking | 9691 Hz  | 3.72 | -11.6 dB |
| Peaking | 821 Hz   | 1.46 | 2.7 dB   |
| Peaking | 3193 Hz  | 1.65 | -4.8 dB  |
| Peaking | 3719 Hz  | 2.73 | 6.8 dB   |
| Peaking | 4540 Hz  | 9.88 | -3.5 dB  |
| Peaking | 11771 Hz | 9.55 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)