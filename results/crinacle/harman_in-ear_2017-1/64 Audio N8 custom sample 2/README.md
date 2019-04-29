# 64 Audio N8 custom sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -2.9; 28 -3.6; 31 -4.3; 34 -4.8; 37 -5.3; 41 -5.8; 45 -6.3; 49 -6.6; 54 -7.0; 60 -7.7; 66 -8.2; 72 -8.6; 79 -9.1; 87 -9.7; 96 -10.1; 106 -10.3; 116 -10.8; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.7; 187 -11.9; 206 -11.7; 227 -11.7; 249 -11.6; 274 -11.5; 302 -11.1; 332 -10.8; 365 -10.4; 402 -10.1; 442 -9.7; 486 -9.3; 535 -8.8; 588 -8.4; 647 -7.9; 712 -7.3; 783 -6.8; 861 -6.4; 947 -6.3; 1042 -6.5; 1146 -7.1; 1261 -7.7; 1387 -8.1; 1526 -8.1; 1678 -7.9; 1846 -7.4; 2031 -6.6; 2234 -5.4; 2457 -3.9; 2703 -2.5; 2973 -1.3; 3270 -0.6; 3597 -0.5; 3957 -1.4; 4353 -2.4; 4788 -3.3; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.1; 15026 -26.2; 16529 -34.0; 18182 -32.6; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 custom sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 custom sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.58 | 6.9 dB   |
| Peaking | 188 Hz   | 0.42 | -5.5 dB  |
| Peaking | 5489 Hz  | 0.61 | 13.3 dB  |
| Peaking | 12461 Hz | 1.35 | 17.7 dB  |
| Peaking | 16633 Hz | 0.44 | -35.1 dB |
| Peaking | 1782 Hz  | 1.14 | -7.4 dB  |
| Peaking | 2480 Hz  | 0.49 | 5.6 dB   |
| Peaking | 4698 Hz  | 3.48 | -5.2 dB  |
| Peaking | 7653 Hz  | 5.05 | -2.5 dB  |
| Peaking | 9824 Hz  | 6.45 | 0.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB   |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 16000 Hz | 1.41 | -30.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20custom%20sample%202/64%20Audio%20N8%20custom%20sample%202.png)