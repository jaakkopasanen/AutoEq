# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.5; 25 -8.9; 28 -9.5; 31 -10.0; 34 -10.5; 37 -10.8; 41 -11.3; 45 -11.7; 49 -12.1; 54 -12.5; 60 -13.0; 66 -13.4; 72 -13.7; 79 -14.2; 87 -14.5; 96 -14.8; 106 -15.1; 116 -15.1; 128 -15.4; 141 -15.5; 155 -15.6; 170 -15.5; 187 -15.4; 206 -15.2; 227 -14.9; 249 -14.5; 274 -14.1; 302 -13.5; 332 -12.9; 365 -12.1; 402 -11.4; 442 -10.8; 486 -10.1; 535 -9.4; 588 -8.6; 647 -7.8; 712 -7.2; 783 -6.7; 861 -6.3; 947 -6.3; 1042 -6.4; 1146 -6.7; 1261 -6.9; 1387 -6.7; 1526 -6.2; 1678 -7.2; 1846 -7.9; 2031 -8.3; 2234 -8.4; 2457 -8.0; 2703 -6.5; 2973 -4.0; 3270 -1.6; 3597 -0.5; 3957 -2.2; 4353 -5.6; 4788 -8.8; 5267 -10.4; 5793 -6.4; 6373 -3.1; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -9.2; 10263 -7.9; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 95 Hz    | 0.42 | -7.6 dB |
| Peaking | 248 Hz   | 0.85 | -4.6 dB |
| Peaking | 3689 Hz  | 2.5  | 12.6 dB |
| Peaking | 4881 Hz  | 0.86 | -8.8 dB |
| Peaking | 6562 Hz  | 2.99 | 9.0 dB  |
| Peaking | 910 Hz   | 2.19 | 1.3 dB  |
| Peaking | 2258 Hz  | 3.22 | -1.7 dB |
| Peaking | 3070 Hz  | 7.21 | 1.7 dB  |
| Peaking | 9757 Hz  | 6.62 | -3.9 dB |
| Peaking | 10568 Hz | 1.68 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)