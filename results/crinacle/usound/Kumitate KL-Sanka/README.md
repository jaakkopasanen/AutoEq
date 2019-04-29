# Kumitate KL-Sanka
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.5; 25 -5.8; 28 -6.1; 31 -6.3; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.8; 106 -10.2; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.4; 170 -11.5; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.5; 274 -11.4; 302 -11.2; 332 -11.0; 365 -10.7; 402 -10.5; 442 -10.1; 486 -9.8; 535 -9.4; 588 -9.0; 647 -8.4; 712 -7.8; 783 -7.2; 861 -6.5; 947 -6.0; 1042 -5.8; 1146 -5.8; 1261 -5.8; 1387 -5.3; 1526 -4.3; 1678 -3.0; 1846 -1.9; 2031 -1.5; 2234 -1.9; 2457 -1.9; 2703 -1.7; 2973 -2.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -1.6; 5267 -1.4; 5793 -2.4; 6373 -7.2; 7010 -9.5; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Sanka GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Sanka ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 133 Hz  | 0.81 | -2.9 dB |
| Peaking | 307 Hz  | 0.65 | -4.0 dB |
| Peaking | 2037 Hz | 1.39 | 3.8 dB  |
| Peaking | 4328 Hz | 1.13 | 5.9 dB  |
| Peaking | 6837 Hz | 5.59 | -6.3 dB |
| Peaking | 20 Hz   | 1.66 | 1.4 dB  |
| Peaking | 939 Hz  | 2.38 | 2.1 dB  |
| Peaking | 944 Hz  | 1.31 | -1.3 dB |
| Peaking | 5701 Hz | 9.04 | 1.6 dB  |
| Peaking | 9782 Hz | 1.41 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kumitate%20KL-Sanka/Kumitate%20KL-Sanka.png)