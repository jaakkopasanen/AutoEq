# Stax SR-002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.2; 25 -3.3; 28 -3.4; 31 -3.5; 34 -3.6; 37 -3.7; 41 -3.8; 45 -4.0; 49 -4.1; 54 -4.4; 60 -4.6; 66 -5.0; 72 -5.3; 79 -5.7; 87 -6.2; 96 -6.7; 106 -7.1; 116 -7.6; 128 -8.0; 141 -8.4; 155 -8.8; 170 -9.0; 187 -9.3; 206 -9.5; 227 -9.8; 249 -10.1; 274 -10.3; 302 -10.3; 332 -10.4; 365 -10.6; 402 -10.9; 442 -11.2; 486 -11.6; 535 -12.0; 588 -12.5; 647 -12.8; 712 -12.4; 783 -10.5; 861 -7.5; 947 -5.5; 1042 -5.6; 1146 -7.0; 1261 -8.5; 1387 -9.9; 1526 -11.5; 1678 -11.9; 1846 -9.3; 2031 -7.1; 2234 -6.8; 2457 -4.3; 2703 -1.8; 2973 -0.7; 3270 -0.5; 3597 -0.6; 3957 -3.5; 4353 -5.0; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.0; 13660 -18.4; 15026 -30.6; 16529 -34.0; 18182 -30.8; 20000 -28.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 515 Hz   | 0.66 | -8.1 dB  |
| Peaking | 1659 Hz  | 2.57 | -8.9 dB  |
| Peaking | 5676 Hz  | 0.24 | 23.4 dB  |
| Peaking | 12177 Hz | 1.7  | 15.5 dB  |
| Peaking | 15774 Hz | 0.26 | -42.3 dB |
| Peaking | 24 Hz    | 1.16 | 3.5 dB   |
| Peaking | 52 Hz    | 1.96 | 1.9 dB   |
| Peaking | 729 Hz   | 2.9  | -5.5 dB  |
| Peaking | 927 Hz   | 1.38 | 5.2 dB   |
| Peaking | 1272 Hz  | 2.32 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.6 dB   |
| Peaking | 125 Hz   | 1.41 | -1.3 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -5.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 16000 Hz | 1.41 | -34.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-002/Stax%20SR-002.png)