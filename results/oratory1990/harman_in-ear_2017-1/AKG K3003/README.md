# AKG K3003
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.5; 25 -9.5; 28 -9.6; 31 -9.5; 34 -9.5; 37 -9.5; 41 -9.6; 45 -9.7; 49 -9.9; 54 -10.1; 60 -10.2; 66 -10.4; 72 -10.7; 79 -11.1; 87 -11.4; 96 -11.6; 106 -11.9; 116 -12.2; 128 -12.4; 141 -12.5; 155 -12.6; 170 -12.6; 187 -12.5; 206 -12.4; 227 -12.2; 249 -11.9; 274 -11.6; 302 -11.2; 332 -10.7; 365 -10.2; 402 -9.7; 442 -9.2; 486 -8.7; 535 -8.1; 588 -7.6; 647 -7.1; 712 -6.6; 783 -6.1; 861 -5.7; 947 -5.6; 1042 -5.7; 1146 -5.7; 1261 -5.4; 1387 -5.1; 1526 -4.7; 1678 -4.1; 1846 -3.5; 2031 -2.8; 2234 -1.9; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.7; 5267 -5.7; 5793 -6.7; 6373 -5.8; 7010 -6.8; 7711 -7.9; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -16.1; 15026 -25.8; 16529 -23.5; 18182 -16.8; 20000 -15.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K3003 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.16 | -2.6 dB  |
| Peaking | 147 Hz   | 0.7  | -4.2 dB  |
| Peaking | 295 Hz   | 1.08 | -2.5 dB  |
| Peaking | 3121 Hz  | 0.9  | 6.7 dB   |
| Peaking | 16071 Hz | 1.56 | -21.3 dB |
| Peaking | 840 Hz   | 4.33 | 0.8 dB   |
| Peaking | 4383 Hz  | 4.62 | 3.8 dB   |
| Peaking | 5082 Hz  | 2.26 | -3.0 dB  |
| Peaking | 11796 Hz | 2.96 | 6.0 dB   |
| Peaking | 20475 Hz | 0.5  | -6.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 16000 Hz | 1.41 | -20.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/AKG%20K3003/AKG%20K3003.png)