# Kumitate KL-Corona sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.1; 28 -1.6; 31 -2.2; 34 -2.7; 37 -3.2; 41 -3.7; 45 -4.0; 49 -4.3; 54 -4.7; 60 -5.2; 66 -5.7; 72 -6.1; 79 -6.5; 87 -6.9; 96 -7.4; 106 -7.7; 116 -7.9; 128 -8.2; 141 -8.4; 155 -8.4; 170 -8.5; 187 -8.5; 206 -8.3; 227 -8.2; 249 -8.1; 274 -7.9; 302 -7.7; 332 -7.4; 365 -7.1; 402 -6.9; 442 -6.7; 486 -6.4; 535 -6.1; 588 -5.8; 647 -5.6; 712 -5.2; 783 -4.9; 861 -4.7; 947 -4.7; 1042 -5.0; 1146 -5.7; 1261 -6.2; 1387 -6.4; 1526 -6.3; 1678 -6.0; 1846 -5.8; 2031 -5.4; 2234 -4.7; 2457 -3.8; 2703 -2.8; 2973 -2.0; 3270 -1.4; 3597 -1.1; 3957 -0.8; 4353 -0.6; 4788 -0.7; 5267 -1.4; 5793 -2.7; 6373 -4.7; 7010 -4.8; 7711 -5.4; 8482 -5.3; 9330 -5.3; 10263 -5.3; 11289 -5.3; 12418 -5.3; 13660 -5.3; 15026 -6.9; 16529 -13.5; 18182 -15.4; 20000 -15.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Corona sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Corona sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.67 | 5.0 dB   |
| Peaking | 164 Hz   | 0.6  | -3.5 dB  |
| Peaking | 1647 Hz  | 2.28 | -1.7 dB  |
| Peaking | 4022 Hz  | 1.19 | 5.1 dB   |
| Peaking | 18787 Hz | 0.9  | -11.8 dB |
| Peaking | 884 Hz   | 2.72 | 1.1 dB   |
| Peaking | 1267 Hz  | 4.84 | -0.8 dB  |
| Peaking | 5466 Hz  | 3.81 | 1.7 dB   |
| Peaking | 6360 Hz  | 2.22 | -1.6 dB  |
| Peaking | 13708 Hz | 3.07 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Corona%20sample%201/Kumitate%20KL-Corona%20sample%201.png)