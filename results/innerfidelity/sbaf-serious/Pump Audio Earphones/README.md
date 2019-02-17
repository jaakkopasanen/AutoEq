# Pump Audio Earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.9; 23 -18.0; 25 -18.0; 28 -17.9; 31 -17.8; 34 -17.7; 37 -17.7; 41 -17.6; 45 -17.5; 49 -17.4; 54 -17.3; 60 -17.2; 66 -17.2; 72 -17.1; 79 -17.0; 87 -17.0; 96 -16.9; 106 -16.6; 116 -16.3; 128 -16.1; 141 -15.7; 155 -15.3; 170 -14.9; 187 -14.3; 206 -13.8; 227 -13.1; 249 -12.5; 274 -11.8; 302 -11.1; 332 -10.4; 365 -9.6; 402 -8.9; 442 -8.1; 486 -7.5; 535 -6.8; 588 -5.4; 647 -4.9; 712 -4.5; 783 -3.9; 861 -3.8; 947 -3.9; 1042 -3.9; 1146 -4.0; 1261 -4.0; 1387 -4.6; 1526 -5.1; 1678 -5.9; 1846 -6.8; 2031 -6.8; 2234 -7.1; 2457 -6.3; 2703 -5.6; 2973 -3.7; 3270 -1.9; 3597 -1.6; 3957 -2.9; 4353 -6.7; 4788 -11.1; 5267 -13.0; 5793 -5.3; 6373 -0.5; 7010 -1.5; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pump Audio Earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pump Audio Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.31 | -12.2 dB |
| Peaking | 140 Hz  | 0.36 | -9.6 dB  |
| Peaking | 2078 Hz | 1.14 | -9.8 dB  |
| Peaking | 2342 Hz | 0.4  | 7.0 dB   |
| Peaking | 5044 Hz | 5.03 | -13.5 dB |
| Peaking | 3549 Hz | 3.96 | 3.7 dB   |
| Peaking | 3701 Hz | 1.77 | -1.8 dB  |
| Peaking | 6540 Hz | 5    | 5.8 dB   |
| Peaking | 6922 Hz | 1.63 | -1.1 dB  |
| Peaking | 8147 Hz | 0.8  | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.5 dB |
| Peaking | 62 Hz    | 1.41 | -9.1 dB  |
| Peaking | 125 Hz   | 1.41 | -9.7 dB  |
| Peaking | 250 Hz   | 1.41 | -6.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pump%20Audio%20Earphones/Pump%20Audio%20Earphones.png)