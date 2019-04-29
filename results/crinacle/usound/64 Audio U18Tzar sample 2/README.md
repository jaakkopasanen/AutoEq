# 64 Audio U18Tzar sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.8; 25 -5.3; 28 -5.9; 31 -6.4; 34 -6.8; 37 -7.2; 41 -7.6; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.7; 87 -9.9; 96 -10.2; 106 -10.5; 116 -10.6; 128 -10.7; 141 -10.7; 155 -10.7; 170 -10.6; 187 -10.5; 206 -10.3; 227 -10.0; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.9; 365 -8.6; 402 -8.2; 442 -8.0; 486 -7.6; 535 -7.3; 588 -6.9; 647 -6.6; 712 -6.1; 783 -5.7; 861 -5.3; 947 -5.1; 1042 -5.3; 1146 -5.9; 1261 -6.5; 1387 -6.8; 1526 -6.7; 1678 -6.3; 1846 -6.0; 2031 -6.2; 2234 -6.5; 2457 -4.7; 2703 -3.7; 2973 -4.1; 3270 -4.7; 3597 -4.1; 3957 -2.0; 4353 -0.5; 4788 -2.3; 5267 -3.9; 5793 -3.1; 6373 -4.8; 7010 -6.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.9; 15026 -10.8; 16529 -16.0; 18182 -18.7; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.4  | 2.9 dB   |
| Peaking | 153 Hz   | 0.43 | -4.4 dB  |
| Peaking | 3653 Hz  | 0.08 | 1.1 dB   |
| Peaking | 4370 Hz  | 2.87 | 4.9 dB   |
| Peaking | 18013 Hz | 1.08 | -14.0 dB |
| Peaking | 942 Hz   | 1.47 | 2.4 dB   |
| Peaking | 1252 Hz  | 0.63 | -1.6 dB  |
| Peaking | 1332 Hz  | 3.85 | -0.7 dB  |
| Peaking | 2716 Hz  | 6.01 | 2.2 dB   |
| Peaking | 13272 Hz | 4.27 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20U18Tzar%20sample%202/64%20Audio%20U18Tzar%20sample%202.png)