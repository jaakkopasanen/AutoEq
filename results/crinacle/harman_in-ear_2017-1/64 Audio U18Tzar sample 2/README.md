# 64 Audio U18Tzar sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.9; 25 -6.4; 28 -7.0; 31 -7.5; 34 -7.9; 37 -8.3; 41 -8.7; 45 -9.0; 49 -9.3; 54 -9.5; 60 -9.8; 66 -10.2; 72 -10.5; 79 -10.8; 87 -11.0; 96 -11.3; 106 -11.5; 116 -11.6; 128 -11.7; 141 -11.8; 155 -11.8; 170 -11.7; 187 -11.5; 206 -11.3; 227 -11.1; 249 -10.9; 274 -10.6; 302 -10.2; 332 -9.8; 365 -9.3; 402 -9.0; 442 -8.7; 486 -8.3; 535 -7.9; 588 -7.5; 647 -7.2; 712 -6.7; 783 -6.3; 861 -5.9; 947 -5.9; 1042 -6.1; 1146 -6.6; 1261 -6.9; 1387 -6.9; 1526 -6.6; 1678 -6.1; 1846 -5.7; 2031 -5.6; 2234 -5.2; 2457 -2.9; 2703 -1.5; 2973 -1.7; 3270 -2.3; 3597 -2.1; 3957 -0.6; 4353 -0.5; 4788 -1.4; 5267 -3.0; 5793 -1.9; 6373 -3.2; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.3; 15026 -27.0; 16529 -34.8; 18182 -35.1; 20000 -22.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio U18Tzar sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio U18Tzar sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 74 Hz    | 0.78 | -2.1 dB  |
| Peaking | 179 Hz   | 0.55 | -4.6 dB  |
| Peaking | 4766 Hz  | 0.53 | 15.2 dB  |
| Peaking | 12119 Hz | 1    | 20.4 dB  |
| Peaking | 16681 Hz | 0.3  | -38.1 dB |
| Peaking | 20 Hz    | 2.49 | 1.8 dB   |
| Peaking | 902 Hz   | 1.65 | 2.2 dB   |
| Peaking | 1264 Hz  | 0.75 | -1.8 dB  |
| Peaking | 2709 Hz  | 5.18 | 2.7 dB   |
| Peaking | 14968 Hz | 7.65 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 16000 Hz | 1.41 | -32.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20U18Tzar%20sample%202/64%20Audio%20U18Tzar%20sample%202.png)