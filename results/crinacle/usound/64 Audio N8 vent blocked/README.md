# 64 Audio N8 vent blocked
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.6; 106 -1.5; 116 -2.4; 128 -3.2; 141 -4.0; 155 -4.6; 170 -5.3; 187 -5.9; 206 -6.6; 227 -7.0; 249 -7.4; 274 -7.8; 302 -8.1; 332 -8.3; 365 -8.5; 402 -8.6; 442 -8.7; 486 -8.7; 535 -8.6; 588 -8.5; 647 -8.3; 712 -7.9; 783 -7.6; 861 -7.3; 947 -7.2; 1042 -7.5; 1146 -8.2; 1261 -9.3; 1387 -10.1; 1526 -10.5; 1678 -10.4; 1846 -10.1; 2031 -9.6; 2234 -8.9; 2457 -7.8; 2703 -6.6; 2973 -5.5; 3270 -4.8; 3597 -4.6; 3957 -4.9; 4353 -5.2; 4788 -6.0; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -8.4; 10263 -6.7; 11289 -6.5; 12418 -6.8; 13660 -8.4; 15026 -6.6; 16529 -6.6; 18182 -11.0; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 vent blocked GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 vent blocked ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 58 Hz    | 0.23 | 7.0 dB  |
| Peaking | 278 Hz   | 0.58 | -4.9 dB |
| Peaking | 1704 Hz  | 1.6  | -4.1 dB |
| Peaking | 3371 Hz  | 2.88 | 2.5 dB  |
| Peaking | 5980 Hz  | 4.26 | 6.8 dB  |
| Peaking | 94 Hz    | 6.14 | 1.0 dB  |
| Peaking | 953 Hz   | 5.72 | 0.9 dB  |
| Peaking | 19285 Hz | 1.4  | -5.9 dB |
| Peaking | 20131 Hz | 0.08 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20N8%20vent%20blocked/64%20Audio%20N8%20vent%20blocked.png)