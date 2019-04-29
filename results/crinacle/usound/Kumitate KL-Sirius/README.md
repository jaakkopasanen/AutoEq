# Kumitate KL-Sirius
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.4; 31 -1.9; 34 -2.3; 37 -2.7; 41 -3.1; 45 -3.4; 49 -3.6; 54 -3.8; 60 -4.1; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.9; 106 -6.2; 116 -6.4; 128 -6.7; 141 -7.0; 155 -7.2; 170 -7.4; 187 -7.5; 206 -7.5; 227 -7.6; 249 -7.6; 274 -7.5; 302 -7.5; 332 -7.4; 365 -7.3; 402 -7.3; 442 -7.2; 486 -7.1; 535 -7.0; 588 -6.8; 647 -6.7; 712 -6.5; 783 -6.4; 861 -6.4; 947 -6.6; 1042 -7.3; 1146 -8.3; 1261 -9.3; 1387 -9.7; 1526 -9.2; 1678 -8.0; 1846 -6.5; 2031 -5.4; 2234 -4.6; 2457 -4.2; 2703 -4.3; 2973 -4.8; 3270 -5.2; 3597 -5.1; 3957 -5.0; 4353 -5.0; 4788 -4.6; 5267 -3.8; 5793 -3.5; 6373 -6.8; 7010 -11.6; 7711 -10.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sirius GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sirius ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.13 | 6.0 dB  |
| Peaking | 54 Hz    | 1.93 | 1.8 dB  |
| Peaking | 1389 Hz  | 2.53 | -4.4 dB |
| Peaking | 3933 Hz  | 0.52 | 2.4 dB  |
| Peaking | 7276 Hz  | 5.57 | -7.6 dB |
| Peaking | 247 Hz   | 0.97 | -1.3 dB |
| Peaking | 2465 Hz  | 2.78 | 1.5 dB  |
| Peaking | 3415 Hz  | 1.39 | -1.1 dB |
| Peaking | 5643 Hz  | 5.94 | 2.5 dB  |
| Peaking | 10213 Hz | 0.44 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Sirius/Kumitate%20KL-Sirius.png)