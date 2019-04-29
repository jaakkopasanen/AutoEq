# 64 Audio N8 vent blocked
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.9; 96 -1.8; 106 -2.7; 116 -3.5; 128 -4.3; 141 -5.1; 155 -5.7; 170 -6.4; 187 -7.1; 206 -7.7; 227 -8.2; 249 -8.5; 274 -8.9; 302 -9.2; 332 -9.3; 365 -9.3; 402 -9.4; 442 -9.5; 486 -9.4; 535 -9.3; 588 -9.1; 647 -8.9; 712 -8.6; 783 -8.3; 861 -8.0; 947 -8.0; 1042 -8.3; 1146 -9.0; 1261 -9.8; 1387 -10.3; 1526 -10.4; 1678 -10.3; 1846 -9.9; 2031 -9.0; 2234 -7.7; 2457 -6.1; 2703 -4.5; 2973 -3.2; 3270 -2.5; 3597 -2.6; 3957 -3.3; 4353 -4.1; 4788 -5.1; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.4; 10263 -8.9; 11289 -6.6; 12418 -9.2; 13660 -17.3; 15026 -22.5; 16529 -24.9; 18182 -27.4; 20000 -23.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`64 Audio N8 vent blocked GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `64 Audio N8 vent blocked ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 51 Hz    | 0.38 | 7.5 dB   |
| Peaking | 743 Hz   | 0.14 | -3.8 dB  |
| Peaking | 3223 Hz  | 3.06 | 4.0 dB   |
| Peaking | 7444 Hz  | 0.48 | 10.0 dB  |
| Peaking | 17981 Hz | 0.37 | -23.3 dB |
| Peaking | 19 Hz    | 2.36 | 1.6 dB   |
| Peaking | 1701 Hz  | 4.21 | -2.0 dB  |
| Peaking | 6018 Hz  | 4    | 4.7 dB   |
| Peaking | 11232 Hz | 0.83 | -5.9 dB  |
| Peaking | 11760 Hz | 2.75 | 11.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB   |
| Peaking | 62 Hz    | 1.41 | 5.7 dB   |
| Peaking | 125 Hz   | 1.41 | 2.1 dB   |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 16000 Hz | 1.41 | -25.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/64%20Audio%20N8%20vent%20blocked/64%20Audio%20N8%20vent%20blocked.png)