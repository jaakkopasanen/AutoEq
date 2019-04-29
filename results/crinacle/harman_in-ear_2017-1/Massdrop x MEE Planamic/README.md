# Massdrop x MEE Planamic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.7; 31 -9.1; 34 -9.3; 37 -9.6; 41 -9.9; 45 -10.1; 49 -10.4; 54 -10.6; 60 -10.9; 66 -11.2; 72 -11.5; 79 -11.7; 87 -12.0; 96 -12.3; 106 -12.6; 116 -12.7; 128 -12.8; 141 -12.9; 155 -12.9; 170 -12.8; 187 -12.6; 206 -12.3; 227 -11.9; 249 -11.5; 274 -11.1; 302 -10.5; 332 -9.9; 365 -9.2; 402 -8.6; 442 -8.1; 486 -7.4; 535 -6.8; 588 -6.1; 647 -5.5; 712 -4.8; 783 -4.1; 861 -3.6; 947 -3.4; 1042 -3.5; 1146 -4.1; 1261 -4.8; 1387 -5.3; 1526 -5.7; 1678 -6.1; 1846 -6.3; 2031 -6.3; 2234 -5.8; 2457 -6.0; 2703 -6.0; 2973 -5.7; 3270 -5.5; 3597 -6.3; 3957 -8.3; 4353 -9.4; 4788 -5.6; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.5; 15026 -25.3; 16529 -28.8; 18182 -29.9; 20000 -26.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x MEE Planamic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x MEE Planamic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 81 Hz    | 0.39 | -3.8 dB  |
| Peaking | 190 Hz   | 0.63 | -3.8 dB  |
| Peaking | 886 Hz   | 1.49 | 3.7 dB   |
| Peaking | 10216 Hz | 0.33 | 22.9 dB  |
| Peaking | 17000 Hz | 0.26 | -37.2 dB |
| Peaking | 4302 Hz  | 4.06 | -6.6 dB  |
| Peaking | 5768 Hz  | 1.91 | 7.8 dB   |
| Peaking | 8159 Hz  | 1.48 | -4.6 dB  |
| Peaking | 12720 Hz | 3.47 | 6.5 dB   |
| Peaking | 14739 Hz | 3.48 | -5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 8.3 dB   |
| Peaking | 16000 Hz | 1.41 | -28.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Massdrop%20x%20MEE%20Planamic/Massdrop%20x%20MEE%20Planamic.png)