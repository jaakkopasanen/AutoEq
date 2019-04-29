# Stax SR-L700 #2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -3.0; 66 -4.5; 72 -4.6; 79 -4.9; 87 -5.4; 96 -5.7; 106 -5.8; 116 -6.3; 128 -6.4; 141 -6.7; 155 -6.8; 170 -6.9; 187 -7.1; 206 -7.1; 227 -7.2; 249 -7.4; 274 -7.5; 302 -7.6; 332 -7.6; 365 -7.7; 402 -7.8; 442 -8.1; 486 -8.2; 535 -8.2; 588 -8.6; 647 -8.8; 712 -9.1; 783 -9.4; 861 -9.4; 947 -10.3; 1042 -10.6; 1146 -10.8; 1261 -10.2; 1387 -9.2; 1526 -7.7; 1678 -6.6; 1846 -5.0; 2031 -4.4; 2234 -3.0; 2457 -3.2; 2703 -2.8; 2973 -2.1; 3270 -1.1; 3597 -1.6; 3957 -1.2; 4353 -0.8; 4788 -1.4; 5267 -4.5; 5793 -7.5; 6373 -6.4; 7010 -4.8; 7711 -6.2; 8482 -7.1; 9330 -9.6; 10263 -7.2; 11289 -6.5; 12418 -9.2; 13660 -21.5; 15026 -28.2; 16529 -28.3; 18182 -27.9; 20000 -28.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L700 #2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L700 #2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.83 | 6.9 dB   |
| Peaking | 1111 Hz  | 0.54 | -10.7 dB |
| Peaking | 6045 Hz  | 2.18 | -8.0 dB  |
| Peaking | 6489 Hz  | 0.21 | 23.6 dB  |
| Peaking | 16587 Hz | 0.27 | -35.6 dB |
| Peaking | 17 Hz    | 2.99 | 2.4 dB   |
| Peaking | 9256 Hz  | 2.78 | -6.1 dB  |
| Peaking | 11995 Hz | 0.84 | 23.5 dB  |
| Peaking | 14323 Hz | 0.62 | -24.0 dB |
| Peaking | 16763 Hz | 1.41 | 10.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -30.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Stax%20SR-L700%20#2/Stax%20SR-L700%20#2.png)