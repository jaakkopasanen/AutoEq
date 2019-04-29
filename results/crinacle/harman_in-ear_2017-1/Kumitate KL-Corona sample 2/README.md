# Kumitate KL-Corona sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.8; 25 -2.5; 28 -3.4; 31 -4.0; 34 -4.5; 37 -5.0; 41 -5.4; 45 -5.9; 49 -6.4; 54 -6.8; 60 -7.1; 66 -7.5; 72 -7.9; 79 -8.2; 87 -8.6; 96 -8.9; 106 -9.3; 116 -9.4; 128 -9.6; 141 -9.7; 155 -9.6; 170 -9.6; 187 -9.5; 206 -9.5; 227 -9.2; 249 -9.0; 274 -8.7; 302 -8.5; 332 -8.0; 365 -7.6; 402 -7.3; 442 -7.0; 486 -6.6; 535 -6.2; 588 -5.8; 647 -5.4; 712 -4.9; 783 -4.4; 861 -4.0; 947 -3.9; 1042 -4.1; 1146 -4.7; 1261 -5.2; 1387 -5.3; 1526 -5.2; 1678 -5.0; 1846 -5.0; 2031 -5.0; 2234 -4.7; 2457 -4.3; 2703 -3.6; 2973 -2.8; 3270 -2.0; 3597 -1.3; 3957 -0.8; 4353 -0.5; 4788 -0.6; 5267 -1.3; 5793 -2.8; 6373 -5.3; 7010 -5.5; 7711 -5.4; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -11.0; 18182 -12.3; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.38 | 5.0 dB  |
| Peaking | 118 Hz   | 0.72 | -3.9 dB |
| Peaking | 254 Hz   | 1.35 | -2.2 dB |
| Peaking | 4177 Hz  | 1.54 | 5.3 dB  |
| Peaking | 17861 Hz | 1.64 | -8.1 dB |
| Peaking | 900 Hz   | 2.85 | 1.9 dB  |
| Peaking | 5484 Hz  | 3.8  | 2.7 dB  |
| Peaking | 6191 Hz  | 1.99 | -2.3 dB |
| Peaking | 15198 Hz | 1.83 | 2.1 dB  |
| Peaking | 16460 Hz | 3.76 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Corona%20sample%202/Kumitate%20KL-Corona%20sample%202.png)