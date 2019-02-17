# AKG K3003 Reference Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.1; 25 -4.5; 28 -5.1; 31 -5.6; 34 -6.0; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.5; 54 -7.9; 60 -8.4; 66 -8.9; 72 -9.2; 79 -9.7; 87 -10.0; 96 -10.3; 106 -10.6; 116 -10.8; 128 -11.1; 141 -11.1; 155 -11.4; 170 -11.3; 187 -11.3; 206 -11.2; 227 -11.1; 249 -10.8; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.2; 402 -8.7; 442 -8.3; 486 -8.0; 535 -7.6; 588 -7.1; 647 -6.7; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.8; 1146 -7.1; 1261 -7.4; 1387 -7.5; 1526 -8.1; 1678 -8.7; 1846 -8.9; 2031 -8.7; 2234 -8.3; 2457 -7.2; 2703 -5.4; 2973 -3.6; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -4.9; 4788 -9.5; 5267 -8.6; 5793 -4.5; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -10.7; 9330 -15.2; 10263 -12.8; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 Reference Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.14 | 3.3 dB   |
| Peaking | 158 Hz  | 0.53 | -5.0 dB  |
| Peaking | 3583 Hz | 4.58 | 7.3 dB   |
| Peaking | 6539 Hz | 6.45 | 5.9 dB   |
| Peaking | 9482 Hz | 4.32 | -10.0 dB |
| Peaking | 819 Hz  | 1.73 | 1.7 dB   |
| Peaking | 2564 Hz | 0.84 | -4.1 dB  |
| Peaking | 2842 Hz | 3.38 | 3.7 dB   |
| Peaking | 4532 Hz | 1.59 | 5.9 dB   |
| Peaking | 4876 Hz | 4.47 | -8.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)