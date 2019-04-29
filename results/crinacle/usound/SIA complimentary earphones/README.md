# SIA complimentary earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.3; 25 -8.4; 28 -8.6; 31 -8.7; 34 -8.8; 37 -9.0; 41 -9.1; 45 -9.3; 49 -9.5; 54 -9.8; 60 -10.1; 66 -10.5; 72 -10.9; 79 -11.4; 87 -11.9; 96 -12.5; 106 -13.0; 116 -13.6; 128 -14.2; 141 -14.8; 155 -15.3; 170 -15.9; 187 -16.5; 206 -17.0; 227 -17.6; 249 -18.2; 274 -18.8; 302 -19.3; 332 -19.1; 365 -18.1; 402 -16.4; 442 -13.3; 486 -10.4; 535 -7.8; 588 -5.6; 647 -3.5; 712 -1.3; 783 -0.7; 861 -2.6; 947 -5.0; 1042 -7.1; 1146 -10.1; 1261 -14.9; 1387 -18.6; 1526 -15.7; 1678 -9.9; 1846 -5.0; 2031 -1.2; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -4.8; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SIA complimentary earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SIA complimentary earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 335 Hz  | 0.44 | -22.0 dB |
| Peaking | 724 Hz  | 1.04 | 14.1 dB  |
| Peaking | 783 Hz  | 0.2  | 7.3 dB   |
| Peaking | 1407 Hz | 1.85 | -23.9 dB |
| Peaking | 2181 Hz | 0.71 | 9.5 dB   |
| Peaking | 2057 Hz | 4.83 | 3.3 dB   |
| Peaking | 2081 Hz | 2.24 | -1.4 dB  |
| Peaking | 4676 Hz | 2.31 | 7.6 dB   |
| Peaking | 5590 Hz | 1.52 | -10.7 dB |
| Peaking | 6216 Hz | 3.81 | 10.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB  |
| Peaking | 250 Hz   | 1.41 | -13.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/SIA%20complimentary%20earphones/SIA%20complimentary%20earphones.png)