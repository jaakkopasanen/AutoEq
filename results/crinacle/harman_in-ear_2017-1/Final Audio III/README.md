# Final Audio III
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.9; 23 -13.1; 25 -13.3; 28 -13.5; 31 -13.7; 34 -13.9; 37 -14.0; 41 -14.2; 45 -14.3; 49 -14.4; 54 -14.6; 60 -14.7; 66 -14.9; 72 -15.1; 79 -15.3; 87 -15.4; 96 -15.6; 106 -15.6; 116 -15.7; 128 -15.7; 141 -15.6; 155 -15.4; 170 -15.1; 187 -14.7; 206 -14.2; 227 -13.6; 249 -13.1; 274 -12.3; 302 -11.4; 332 -10.4; 365 -9.4; 402 -8.4; 442 -7.4; 486 -6.1; 535 -4.8; 588 -3.5; 647 -2.2; 712 -0.9; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.7; 1261 -0.5; 1387 -0.5; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.9; 3597 -6.5; 3957 -9.7; 4353 -9.0; 4788 -7.7; 5267 -8.0; 5793 -10.8; 6373 -16.5; 7010 -13.8; 7711 -10.5; 8482 -10.6; 9330 -9.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -20.8; 16529 -25.2; 18182 -19.1; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio III GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio III ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.47 | -7.7 dB  |
| Peaking | 126 Hz   | 1.23 | -6.4 dB  |
| Peaking | 228 Hz   | 2.2  | -4.9 dB  |
| Peaking | 6563 Hz  | 5.03 | -10.3 dB |
| Peaking | 16731 Hz | 1.73 | -21.0 dB |
| Peaking | 1896 Hz  | 0.42 | 7.4 dB   |
| Peaking | 3842 Hz  | 8.06 | -4.3 dB  |
| Peaking | 4237 Hz  | 4.91 | -4.2 dB  |
| Peaking | 12119 Hz | 1.52 | 11.3 dB  |
| Peaking | 12165 Hz | 0.47 | -7.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB  |
| Peaking | 62 Hz    | 1.41 | -6.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.8 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 16000 Hz | 1.41 | -16.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Final%20Audio%20III/Final%20Audio%20III.png)