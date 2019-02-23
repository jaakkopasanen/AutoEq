# AKG K3003 Bass Boost Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -6.0; 25 -6.5; 28 -7.1; 31 -7.6; 34 -8.0; 37 -8.4; 41 -8.8; 45 -9.2; 49 -9.6; 54 -10.0; 60 -10.5; 66 -10.9; 72 -11.3; 79 -11.7; 87 -12.0; 96 -12.3; 106 -12.6; 116 -12.7; 128 -12.9; 141 -13.0; 155 -13.1; 170 -13.1; 187 -12.9; 206 -12.7; 227 -12.4; 249 -12.1; 274 -11.6; 302 -11.0; 332 -10.4; 365 -9.7; 402 -9.0; 442 -8.3; 486 -7.7; 535 -6.9; 588 -6.1; 647 -5.3; 712 -4.7; 783 -4.2; 861 -3.9; 947 -3.8; 1042 -3.9; 1146 -4.2; 1261 -4.4; 1387 -4.3; 1526 -3.8; 1678 -4.7; 1846 -5.4; 2031 -5.8; 2234 -5.9; 2457 -5.5; 2703 -4.0; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.1; 4788 -6.4; 5267 -7.9; 5793 -3.9; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.9; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Bass Boost Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 0.84 | -2.3 dB |
| Peaking | 189 Hz   | 0.52 | -6.1 dB |
| Peaking | 873 Hz   | 0.91 | 3.7 dB  |
| Peaking | 3529 Hz  | 2.45 | 6.5 dB  |
| Peaking | 21844 Hz | 2.33 | 2.2 dB  |
| Peaking | 19 Hz    | 2.27 | 1.8 dB  |
| Peaking | 1529 Hz  | 7.71 | 1.3 dB  |
| Peaking | 2222 Hz  | 4.76 | -1.2 dB |
| Peaking | 5178 Hz  | 6.68 | -3.9 dB |
| Peaking | 6323 Hz  | 5.67 | 5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)