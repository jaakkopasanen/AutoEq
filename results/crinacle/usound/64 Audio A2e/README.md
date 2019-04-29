# 64 Audio A2e
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.3; 25 -3.7; 28 -4.2; 31 -4.6; 34 -5.0; 37 -5.2; 41 -5.6; 45 -5.9; 49 -6.2; 54 -6.5; 60 -6.8; 66 -7.2; 72 -7.5; 79 -7.9; 87 -8.3; 96 -8.7; 106 -9.0; 116 -9.4; 128 -9.6; 141 -9.9; 155 -10.0; 170 -10.1; 187 -10.1; 206 -10.1; 227 -10.0; 249 -10.0; 274 -9.9; 302 -9.7; 332 -9.4; 365 -9.2; 402 -8.9; 442 -8.6; 486 -8.3; 535 -7.9; 588 -7.7; 647 -7.2; 712 -6.7; 783 -6.2; 861 -5.8; 947 -5.5; 1042 -5.6; 1146 -6.0; 1261 -6.3; 1387 -6.2; 1526 -5.7; 1678 -5.1; 1846 -4.8; 2031 -5.0; 2234 -4.9; 2457 -4.2; 2703 -3.3; 2973 -2.9; 3270 -3.1; 3597 -4.0; 3957 -5.6; 4353 -6.6; 4788 -2.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -9.3; 8482 -10.9; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A2e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A2e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.61 | 4.5 dB  |
| Peaking | 185 Hz  | 0.57 | -3.9 dB |
| Peaking | 2686 Hz | 1.4  | 2.8 dB  |
| Peaking | 5907 Hz | 2.55 | 6.7 dB  |
| Peaking | 8205 Hz | 5.34 | -6.8 dB |
| Peaking | 419 Hz  | 1.92 | -0.5 dB |
| Peaking | 913 Hz  | 2.93 | 1.4 dB  |
| Peaking | 3347 Hz | 4.52 | 1.4 dB  |
| Peaking | 4376 Hz | 3.85 | -3.5 dB |
| Peaking | 4938 Hz | 7.32 | 3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A2e/64%20Audio%20A2e.png)