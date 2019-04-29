# 64 Audio A6t
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.4; 23 -10.6; 25 -10.8; 28 -10.9; 31 -11.0; 34 -11.1; 37 -11.1; 41 -11.1; 45 -11.1; 49 -11.0; 54 -10.9; 60 -10.8; 66 -10.8; 72 -10.8; 79 -10.8; 87 -10.8; 96 -10.8; 106 -10.8; 116 -10.7; 128 -10.6; 141 -10.5; 155 -10.3; 170 -10.1; 187 -9.9; 206 -9.7; 227 -9.4; 249 -9.2; 274 -9.0; 302 -8.8; 332 -8.7; 365 -8.6; 402 -8.5; 442 -8.4; 486 -8.3; 535 -8.1; 588 -7.8; 647 -7.4; 712 -6.9; 783 -6.3; 861 -5.6; 947 -5.2; 1042 -5.1; 1146 -5.4; 1261 -5.8; 1387 -6.0; 1526 -5.8; 1678 -5.5; 1846 -5.3; 2031 -5.4; 2234 -5.4; 2457 -5.0; 2703 -4.5; 2973 -4.0; 3270 -3.0; 3597 -2.5; 3957 -2.6; 4353 -3.4; 4788 -4.0; 5267 -2.4; 5793 -0.5; 6373 -1.2; 7010 -4.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.7; 16529 -15.3; 18182 -17.7; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio A6t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio A6t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.12 | -4.4 dB  |
| Peaking | 996 Hz   | 2.35 | 1.8 dB   |
| Peaking | 3576 Hz  | 1.53 | 3.6 dB   |
| Peaking | 5938 Hz  | 4.05 | 5.8 dB   |
| Peaking | 17770 Hz | 1.46 | -12.9 dB |
| Peaking | 543 Hz   | 3.86 | -0.5 dB  |
| Peaking | 1780 Hz  | 5.88 | 0.6 dB   |
| Peaking | 7892 Hz  | 4.77 | -0.7 dB  |
| Peaking | 13658 Hz | 1.91 | 2.3 dB   |
| Peaking | 15950 Hz | 3.08 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -8.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/64%20Audio%20A6t/64%20Audio%20A6t.png)